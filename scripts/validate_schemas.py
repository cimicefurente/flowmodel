"""Check the standard's card schemas and their fixtures.

Usage: validate_schemas.py <schemas folder>

Development tooling; its pinned dependencies are in requirements-schemas.txt.

The folder holds one `<name>.schema.json` per kind and, for each of them,
`fixtures/<name>/valid/*.yaml` and `fixtures/<name>/invalid/*.yaml`.
A schema made only of `$defs` is a library and has no fixtures.

The check fails if a schema is not valid against the 2020-12 metaschema,
if a kind has no valid or no invalid fixture, if a valid fixture fails its
schema or if an invalid fixture passes it.

YAML is read with the YAML 1.2 core rules the standard requires (`PA-5`):
only `true` and `false` are booleans, dates stay strings and duplicate keys
are an error.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import best_match
from referencing import Registry, Resource

METASCHEMA = "https://json-schema.org/draft/2020-12/schema"
LIBRARY_KEYS = {"$schema", "$id", "title", "description", "$comment", "$defs"}


class StrictLoader(yaml.SafeLoader):
    """SafeLoader with YAML 1.2 core booleans, no timestamps, unique keys."""


_DROPPED = {"tag:yaml.org,2002:bool", "tag:yaml.org,2002:timestamp"}
StrictLoader.yaml_implicit_resolvers = {
    first: [(tag, rx) for tag, rx in resolvers if tag not in _DROPPED]
    for first, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
StrictLoader.add_implicit_resolver(
    "tag:yaml.org,2002:bool",
    re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$"),
    list("tTfF"),
)


def _construct_mapping(loader, node, deep=False):
    keys = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in keys:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        keys.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.load(handle, Loader=StrictLoader)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    folder = Path(argv[1])
    failures: list[str] = []
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

    if not schemas:
        failures.append(f"{folder}: no *.schema.json found")

    ids = [schema.get("$id") for schema in schemas.values()]
    if None in ids or len(set(ids)) != len(ids):
        failures.append("every schema needs a unique $id")
    registry = Registry().with_resources(
        (schema["$id"], Resource.from_contents(schema))
        for schema in schemas.values()
        if "$id" in schema
    )

    fixtures = folder / "fixtures"
    kinds = {name for name, schema in schemas.items() if set(schema) - LIBRARY_KEYS}
    if fixtures.is_dir():
        for extra in sorted(p.name for p in fixtures.iterdir() if p.name not in names):
            failures.append(f"{fixtures / extra}: no schema named {extra}")

    for name in sorted(kinds):
        validator = Draft202012Validator(schemas[name], registry=registry)
        for expected in ("valid", "invalid"):
            files = sorted((fixtures / name / expected).glob("*.yaml"))
            if not files:
                failures.append(f"{name}: no {expected} fixture")
            for path in files:
                try:
                    instance = load_yaml(path)
                except yaml.YAMLError as error:
                    failures.append(f"{path}: not readable YAML: {error}")
                    continue
                error = best_match(validator.iter_errors(instance))
                if expected == "valid" and error is None:
                    print(f"valid   pass  {path}")
                elif expected == "invalid" and error is not None:
                    where = "/".join(str(p) for p in error.absolute_path) or "(root)"
                    print(f"invalid fail  {path}\n              at {where}: {error.message}")
                elif expected == "valid":
                    where = "/".join(str(p) for p in error.absolute_path) or "(root)"
                    failures.append(f"{path}: should pass, fails at {where}: {error.message}")
                else:
                    failures.append(f"{path}: should fail, passes")

    if failures:
        print(f"\n{len(failures)} problem(s):", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1
    print("\nall schemas valid; every valid fixture passes and every invalid fixture fails")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
