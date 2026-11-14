"""Check the standard's card schemas and their fixtures, and optionally cards.

Usage: validate_schemas.py <schemas folder> [<card file> ...]

Development tooling; its pinned dependencies are in requirements-schemas.txt.

Layout of the folder:

- one `<name>.schema.json` per schema. A schema made only of `$defs` (and
  descriptive keywords) is a library: it is not a kind and has no fixtures;
- for every other schema, `fixtures/<name>/valid/*.yaml` and
  `fixtures/<name>/invalid/*.yaml`, at least one of each. Anything else under
  `fixtures/` (another folder, a `.yml` file, a library's folder) is an error.

Every invalid fixture declares where it must fail, with one or more lines

    # expect: /errors_and_limits/fallback

holding a JSON Pointer (RFC 6901) into the fixture; the root is written `/`.
The set of locations of the validation errors (each narrowed into anyOf
and oneOf branches to its most relevant cause) must equal the set declared,
so an invalid fixture cannot fail for another reason. A valid fixture
declares no location.

The check fails if a schema is not valid against the 2020-12 metaschema,
if a kind lacks valid or invalid fixtures, if a valid fixture fails its
schema, or if an invalid fixture passes it or fails somewhere else.

Each card file given after the folder (e.g. this repo's own `method/*.yaml`)
must be valid against the schema of the kind it declares (`kind: node`).

YAML is read with the YAML 1.2 core schema the standard requires (`PA-5`):
implicit types are only null (`~`, `null`, empty), booleans (`true`,
`false`), integers (decimal, `0o` octal, `0x` hexadecimal) and floats
(including `.inf` and `.nan`); everything else, such as `yes`, `1_000`,
`1:30`, dates and `<<`, is a string, and `017` is 17. Duplicate keys are an
error, and a document that is not plain JSON data (an explicit tag such as
`!!binary` or `!!set`, a non-string key) is rejected.
"""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import best_match
from referencing import Registry, Resource

METASCHEMA = "https://json-schema.org/draft/2020-12/schema"
LIBRARY_KEYS = {"$schema", "$id", "title", "description", "$comment", "$defs"}
EXPECT = re.compile(r"^# expect: (\S+)\s*$", re.MULTILINE)

# --- YAML 1.2 core schema ---------------------------------------------------


class CoreLoader(yaml.SafeLoader):
    """SafeLoader restricted to the YAML 1.2 core schema, with unique keys."""


CoreLoader.yaml_implicit_resolvers = {}
CoreLoader.add_implicit_resolver(
    "tag:yaml.org,2002:null",
    re.compile(r"^(?:~|null|Null|NULL|)$"),
    ["~", "n", "N", ""],
)
CoreLoader.add_implicit_resolver(
    "tag:yaml.org,2002:bool",
    re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$"),
    list("tTfF"),
)
CoreLoader.add_implicit_resolver(
    "tag:yaml.org,2002:int",
    re.compile(r"^(?:[-+]?[0-9]+|0o[0-7]+|0x[0-9a-fA-F]+)$"),
    list("-+0123456789"),
)
CoreLoader.add_implicit_resolver(
    "tag:yaml.org,2002:float",
    re.compile(
        r"^(?:[-+]?(?:\.[0-9]+|[0-9]+(?:\.[0-9]*)?)(?:[eE][-+]?[0-9]+)?"
        r"|[-+]?\.(?:inf|Inf|INF)|\.(?:nan|NaN|NAN))$"
    ),
    list("-+.0123456789"),
)


def _construct_int(loader, node):
    value = loader.construct_scalar(node)
    if value.startswith("0o"):
        return int(value[2:], 8)
    if value.startswith("0x"):
        return int(value[2:], 16)
    return int(value, 10)


def _construct_float(loader, node):
    value = loader.construct_scalar(node)
    lowered = value.lower()
    if lowered.endswith(".inf"):
        return -math.inf if value.startswith("-") else math.inf
    if lowered == ".nan":
        return math.nan
    return float(value)


def _construct_mapping(loader, node, deep=False):
    keys = []
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in keys:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        keys.append(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


CoreLoader.add_constructor("tag:yaml.org,2002:int", _construct_int)
CoreLoader.add_constructor("tag:yaml.org,2002:float", _construct_float)
CoreLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


def is_json(value) -> bool:
    if isinstance(value, dict):
        return all(isinstance(k, str) and is_json(v) for k, v in value.items())
    if isinstance(value, list):
        return all(is_json(item) for item in value)
    return value is None or isinstance(value, (str, bool, int, float))


def load_yaml(text: str):
    data = yaml.load(text, Loader=CoreLoader)
    if not is_json(data):
        raise yaml.YAMLError("not plain JSON data (explicit tag or non-string key)")
    return data


def self_test() -> list[str]:
    """The loader's YAML 1.2 core behaviour, checked on every run."""
    cases = {
        "017": 17, "08": 8, "0o17": 15, "0x1F": 31, "-3": -3, "1_000": "1_000",
        "1:30": "1:30", "2.1": 2.1, "1e3": 1000.0, ".inf": math.inf,
        "yes": "yes", "no": "no", "on": "on", "true": True, "False": False,
        "~": None, "null": None, "2026-01-01": "2026-01-01", "0b11": "0b11",
    }
    failures = []
    for text, expected in cases.items():
        got = load_yaml(f"v: {text}\n")["v"]
        if type(got) is not type(expected) or got != expected:
            failures.append(f"YAML loader: {text!r} read as {got!r}, expected {expected!r}")
    if load_yaml("<<: x\n") != {"<<": "x"}:
        failures.append("YAML loader: '<<' must be a plain key")
    for bad in ("a: 1\na: 2\n", "v: !!binary aGk=\n", "1: x\n"):
        try:
            load_yaml(bad)
            failures.append(f"YAML loader: {bad!r} must be rejected")
        except yaml.YAMLError:
            pass
    return failures


# --- checks -----------------------------------------------------------------


def pointer(path) -> str:
    parts = [str(p).replace("~", "~0").replace("/", "~1") for p in path]
    return "/" + "/".join(parts) if parts else "/"


def check_fixtures(folder: Path, kinds: set[str], libraries: set[str]) -> list[str]:
    """Reject anything under fixtures/ that the checks would otherwise skip."""
    failures = []
    fixtures = folder / "fixtures"
    if not fixtures.is_dir():
        return [f"{fixtures}: missing"]
    for entry in sorted(fixtures.iterdir()):
        if entry.name in libraries:
            failures.append(f"{entry}: {entry.name} is a library schema and has no fixtures")
            continue
        if not entry.is_dir() or entry.name not in kinds:
            failures.append(f"{entry}: no schema named {entry.name}")
            continue
        for sub in sorted(entry.iterdir()):
            if sub.name not in ("valid", "invalid") or not sub.is_dir():
                failures.append(f"{sub}: only valid/ and invalid/ are allowed")
                continue
            for item in sorted(sub.iterdir()):
                if not item.is_file() or item.suffix != ".yaml":
                    failures.append(f"{item}: fixtures are *.yaml files")
    return failures


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: validate_schemas.py <schemas folder> [<card file> ...]", file=sys.stderr)
        return 2
    folder = Path(argv[1])
    failures: list[str] = self_test()
    schemas: dict[str, dict] = {}
    names: set[str] = set()

    for path in sorted(folder.glob("*.schema.json")):
        name = path.name.removesuffix(".schema.json")
        names.add(name)
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            failures.append(f"{path}: not JSON: {error}")
            continue
        if schema.get("$schema") != METASCHEMA:
            failures.append(f"{path}: $schema must be {METASCHEMA}")
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as error:  # SchemaError, or an unresolvable metaschema
            failures.append(f"{path}: not valid against the metaschema: {error}")
            continue
        print(f"schema  ok    {path}")
        schemas[name] = schema

    if not names:
        failures.append(f"{folder}: no *.schema.json found")

    ids = [schema.get("$id") for schema in schemas.values()]
    if None in ids or len(set(ids)) != len(ids):
        failures.append("every schema needs a unique $id")
    registry = Registry().with_resources(
        (schema["$id"], Resource.from_contents(schema))
        for schema in schemas.values()
        if "$id" in schema
    )

    libraries = {name for name, schema in schemas.items() if not set(schema) - LIBRARY_KEYS}
    kinds = names - libraries
    failures += check_fixtures(folder, kinds, libraries)

    for name in sorted(kinds & set(schemas)):
        validator = Draft202012Validator(schemas[name], registry=registry)
        for expected in ("valid", "invalid"):
            files = sorted((folder / "fixtures" / name / expected).glob("*.yaml"))
            if not files:
                failures.append(f"{name}: no {expected} fixture")
            for path in files:
                text = path.read_text(encoding="utf-8")
                declared = set(EXPECT.findall(text))
                try:
                    instance = load_yaml(text)
                except yaml.YAMLError as error:
                    failures.append(f"{path}: not readable YAML: {error}")
                    continue
                # Each error, narrowed into anyOf/oneOf branches to its most relevant cause.
                errors = [best_match([error]) for error in validator.iter_errors(instance)]
                found = {pointer(error.absolute_path) for error in errors}
                if expected == "valid":
                    if declared:
                        failures.append(f"{path}: a valid fixture declares no '# expect:'")
                    elif errors:
                        details = "; ".join(f"{pointer(e.absolute_path)}: {e.message}" for e in errors)
                        failures.append(f"{path}: should pass, fails: {details}")
                    else:
                        print(f"valid   pass  {path}")
                elif not declared:
                    failures.append(f"{path}: an invalid fixture needs '# expect: <pointer>'")
                elif not errors:
                    failures.append(f"{path}: should fail, passes")
                elif found != declared:
                    failures.append(
                        f"{path}: should fail at {sorted(declared)}, fails at {sorted(found)}"
                    )
                else:
                    print(f"invalid fail  {path}")
                    for error in errors:
                        print(f"              at {pointer(error.absolute_path)}: {error.message}")

    for path in map(Path, argv[2:]):
        try:
            card = load_yaml(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as error:
            failures.append(f"{path}: not readable YAML: {error}")
            continue
        kind = card.get("kind") if isinstance(card, dict) else None
        if not isinstance(kind, str) or kind not in kinds & set(schemas):
            failures.append(f"{path}: no schema for kind {kind!r}")
            continue
        validator = Draft202012Validator(schemas[kind], registry=registry)
        errors = [best_match([error]) for error in validator.iter_errors(card)]
        for error in errors:
            failures.append(f"{path}: at {pointer(error.absolute_path)}: {error.message}")
        if not errors:
            print(f"card    pass  {path}")

    if failures:
        print(f"\n{len(failures)} problem(s):", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1
    print("\nall schemas valid; every valid fixture passes and every invalid fixture fails where it declares;"
          " every card given passes its kind's schema")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
