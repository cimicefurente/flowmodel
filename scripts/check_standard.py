"""Check the layout of the standard, the IDs cited in it and the prompts' loads.

Usage: check_standard.py [repo root]

Development tooling; its pinned dependencies are in requirements-schemas.txt.

Layout of `standard/`:

- each module is a folder named by its ID (`MM`, `P`, ...), holding a
  `README.md` and one Markdown file per sub-module, `<ID>-<slug>.md`;
- every sub-module file starts with a YAML header between `---` lines with
  exactly the keys `id`, `name`, `module`, `owner` and `status`; `id` matches
  the file name and is unique, `module` is the folder, `status` is
  `hypothesis`, `decided` or `superseded`; when the text opens with a heading
  that starts with the ID, the rest of the heading is the `name`;
- a sub-module's ID equals its module's only when it is the module's only file;
- the module's `README.md` has a `## Sub-modules` section whose table lists
  exactly its sub-module files, one row each: | [`ID`](file) | name |;
- the only other Markdown files directly in `standard/` are `README.md` and
  `GLOSSARY.md`.

IDs: an ID is defined by a module folder, by a sub-module header, or by a cell
of a sub-module's table in a column headed `ID` or `#` holding only the ID
(e.g. `P3`, `CC-12`, `N4`). A citation is inline code holding only an ID
(e.g. `MM-4`, `TA`), outside fenced code blocks. Every ID cited in
`standard/`, `prompts/`, the glossaries and the root `README.md` must resolve to
exactly one file or module.

Prompts: every `prompts/*.md` has a header whose `id` is its file name; each
entry of `loads:` is a module or sub-module ID, optionally followed by
`short form` when its files have a `## Short form` section, and resolves to
a set of files.

Links: every relative Markdown link in the files above points to an existing
path.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ID = r"[A-Z]{1,3}(?:-?\d+)?"
ID_RE = re.compile(rf"^{ID}$")
MODULE_RE = re.compile(r"^[A-Z]{1,3}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CODE_RE = re.compile(r"`([^`\n]+)`")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
HEADING_RE = re.compile(r"^#+\s+(\S+)\s+(.*?)\s*$")
INDEX_HEADING = "## Sub-modules"
INDEX_ROW_RE = re.compile(r"^\|\s*\[`([^`]+)`\]\(([^)]+)\)\s*\|\s*(.*?)\s*\|\s*$")
HEADER_KEYS = {"id", "name", "module", "owner", "status"}
STATUSES = {"hypothesis", "decided", "superseded"}
TOP_LEVEL = {"README.md", "GLOSSARY.md"}
SHORT_FORM = " short form"


def split_header(text: str) -> tuple[dict | None, str, int]:
    """Return the YAML header, the text after it and the line the text starts on."""
    if not text.startswith("---\n"):
        return None, text, 1
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text, 1
    header = yaml.safe_load(text[4:end])
    body = text[end + 5 :]
    return header, body, text[: end + 5].count("\n") + 1


def strip_fences(text: str) -> list[tuple[int, str]]:
    """Lines outside fenced code blocks, with their 1-based numbers."""
    lines, fenced = [], False
    for number, line in enumerate(text.split("\n"), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            lines.append((number, line))
    return lines


def table_definitions(body: str) -> list[str]:
    """IDs defined by the cells of columns headed `ID` or `#`."""
    found, columns = [], None
    for _, line in strip_fences(body):
        if not line.startswith("|"):
            columns = None
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if columns is None:
            columns = [i for i, cell in enumerate(cells) if cell in ("ID", "#")]
            continue
        if all(set(cell) <= set("-: ") for cell in cells):
            continue
        for i in columns:
            if i < len(cells):
                cell = cells[i].strip("`")
                if ID_RE.match(cell):
                    found.append(cell)
    return found


def first_heading(body: str) -> tuple[str, str] | None:
    for line in body.split("\n"):
        if line.strip():
            match = HEADING_RE.match(line)
            return (match.group(1), match.group(2)) if match else None
    return None


def check(root: Path) -> tuple[list[str], str]:
    errors: list[str] = []
    standard = root / "standard"
    rel = lambda path: path.relative_to(root).as_posix()  # noqa: E731

    # --- modules and sub-modules -----------------------------------------
    targets: dict[str, set[frozenset[str]]] = {}  # ID -> the file sets it names
    loadable: dict[str, frozenset[str]] = {}  # module and sub-module IDs
    submodules: dict[str, Path] = {}

    def define(identifier: str, files: frozenset[str]) -> None:
        targets.setdefault(identifier, set()).add(files)

    modules = [d for d in sorted(standard.iterdir()) if d.is_dir() and MODULE_RE.match(d.name)]
    for path in sorted(standard.rglob("*.md")):
        if not (path.parent in modules or (path.parent == standard and path.name in TOP_LEVEL)):
            errors.append(f"{rel(path)}: not in a module folder")

    for folder in modules:
        module = folder.name
        files = sorted(p for p in folder.glob("*.md") if p.name != "README.md")
        if not (folder / "README.md").is_file():
            errors.append(f"{rel(folder)}: no README.md")
        if not files:
            errors.append(f"{rel(folder)}: no sub-module files")
        names: dict[str, tuple[str, str]] = {}  # file name -> (id, name)
        for path in files:
            text = path.read_text(encoding="utf-8")
            try:
                header, body, _ = split_header(text)
            except yaml.YAMLError as error:
                errors.append(f"{rel(path)}: header is not YAML: {error}")
                continue
            if not isinstance(header, dict):
                errors.append(f"{rel(path)}: no YAML header")
                continue
            keys = set(header)
            if keys != HEADER_KEYS:
                errors.append(
                    f"{rel(path)}: header keys {sorted(keys)}, expected {sorted(HEADER_KEYS)}"
                )
                continue
            if not all(isinstance(value, str) and value.strip() for value in header.values()):
                errors.append(f"{rel(path)}: every header value must be a non-empty string")
                continue
            identifier = header["id"]
            if not ID_RE.match(identifier):
                errors.append(f"{rel(path)}: id {identifier!r} is not an ID")
                continue
            stem = path.stem
            if not (stem.startswith(identifier + "-") and SLUG_RE.match(stem[len(identifier) + 1 :])):
                errors.append(f"{rel(path)}: file name does not match id {identifier!r} (<id>-<slug>.md)")
            if header["module"] != module:
                errors.append(f"{rel(path)}: module {header['module']!r}, but the folder is {module!r}")
            if header["status"] not in STATUSES:
                errors.append(f"{rel(path)}: status {header['status']!r} not in {sorted(STATUSES)}")
            if identifier == module and len(files) > 1:
                errors.append(f"{rel(path)}: id equals the module, but the module has other files")
            if identifier in submodules:
                errors.append(f"{rel(path)}: id {identifier!r} also in {rel(submodules[identifier])}")
                continue
            heading = first_heading(body)
            if heading and heading[0] == identifier and heading[1] != header["name"]:
                errors.append(f"{rel(path)}: name {header['name']!r}, but the heading says {heading[1]!r}")
            submodules[identifier] = path
            names[path.name] = (identifier, header["name"])
            own = frozenset({rel(path)})
            define(identifier, own)
            loadable[identifier] = own
            for row_id in table_definitions(body):
                define(row_id, own)
        module_files = frozenset(rel(p) for p in files)
        define(module, module_files)
        loadable[module] = module_files

        readme = folder / "README.md"
        if readme.is_file():
            errors += check_index(readme, names, rel)

    # --- citations and links ---------------------------------------------
    scanned = sorted(
        {*standard.rglob("*.md"), *(root / "prompts").glob("*.md"), *root.glob("*GLOSSARY*.md"),
         *(root / "engine").glob("GLOSSARY.md"), root / "README.md"}
    )
    citations = 0
    for path in scanned:
        if not path.is_file():
            continue
        for number, line in strip_fences(path.read_text(encoding="utf-8")):
            for token in CODE_RE.findall(line):
                if not ID_RE.match(token):
                    continue
                citations += 1
                found = targets.get(token, set())
                if len(found) != 1:
                    where = "nothing" if not found else ", ".join(sorted(",".join(sorted(t)) for t in found))
                    errors.append(f"{rel(path)}:{number}: `{token}` resolves to {where}")
            for link in LINK_RE.findall(line):
                if re.match(r"^[a-z]+:", link) or link.startswith("#"):
                    continue
                target = (path.parent / link.split("#")[0]).resolve()
                if not target.exists():
                    errors.append(f"{rel(path)}:{number}: link {link!r} points to nothing")

    # --- prompts ----------------------------------------------------------
    prompts = sorted((root / "prompts").glob("*.md"))
    for path in prompts:
        try:
            header, _, _ = split_header(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as error:
            errors.append(f"{rel(path)}: header is not YAML: {error}")
            continue
        if not isinstance(header, dict):
            errors.append(f"{rel(path)}: no YAML header")
            continue
        if header.get("id") != path.stem:
            errors.append(f"{rel(path)}: id {header.get('id')!r} does not match the file name")
        loads = header.get("loads")
        if not isinstance(loads, list) or not loads:
            errors.append(f"{rel(path)}: loads is not a non-empty list")
            continue
        for entry in loads:
            entry = str(entry)
            identifier = entry[: -len(SHORT_FORM)] if entry.endswith(SHORT_FORM) else entry
            files = loadable.get(identifier)
            if files is None:
                errors.append(f"{rel(path)}: loads {entry!r}, which is not a module or sub-module ID")
                continue
            if identifier != entry and not any(
                "\n## Short form\n" in (root / f).read_text(encoding="utf-8") for f in files
            ):
                errors.append(f"{rel(path)}: loads {entry!r}, but {identifier} has no short form")

    summary = (
        f"{len(modules)} modules, {len(submodules)} sub-modules, {citations} citations, "
        f"{len(prompts)} prompts"
    )
    return errors, summary


def check_index(readme: Path, names: dict[str, tuple[str, str]], rel) -> list[str]:
    errors = []
    lines = readme.read_text(encoding="utf-8").split("\n")
    if INDEX_HEADING not in lines:
        return [f"{rel(readme)}: no {INDEX_HEADING!r} section"]
    rows: dict[str, tuple[str, str]] = {}
    for line in lines[lines.index(INDEX_HEADING) + 1 :]:
        if line.startswith("## "):
            break
        match = INDEX_ROW_RE.match(line)
        if match:
            identifier, target, name = match.groups()
            if target in rows:
                errors.append(f"{rel(readme)}: {target} listed twice")
            rows[target] = (identifier, name)
    if rows != names:
        missing = sorted(set(names) - set(rows))
        extra = sorted(set(rows) - set(names))
        wrong = sorted(f for f in set(rows) & set(names) if rows[f] != names[f])
        errors.append(
            f"{rel(readme)}: index does not match the sub-modules "
            f"(missing {missing}, extra {extra}, wrong ID or name {wrong})"
        )
    return errors


def main(argv: list[str]) -> int:
    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    errors, summary = check(root)
    if errors:
        print(f"{len(errors)} problem(s):", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    print(f"standard ok: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
