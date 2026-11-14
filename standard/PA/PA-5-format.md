---
id: PA-5
name: Format
module: PA
owner: The maintainer (protected area, MB-6)
status: decided
---

## PA-5 Format

Cards:

- One card per YAML file (YAML 1.2) in the project's repo, valid against the JSON Schema (2020-12) the standard publishes for its kind in `schemas/`, one schema per card of `MM-4` and `MM-5`.
- A card declares only its kind (`kind: node`), never the version of the standard: the version comes from the lock file.
- Keys are field names in `snake_case` (`card_status`, `errors_and_limits`), never field numbers. Prose, such as rationale and examples, goes in the text fields of the schema.
- Every card has `id`, `owner` and `card_status`. A decided card cites the decision (`CC-10`); a superseded card cites the decision that superseded it (N9 in `MM-4`).
- A node card is one whole tier of `MM-4`: the schema infers the tier from the fields present, and an external node has exactly the external tier.
- A node's inputs and outputs are non-empty lists of entries, each naming its source or destination (`CC-1`).
- An undecided field holds the placeholder of `MM-1`. In inputs and outputs only the fields of an entry may hold it. A cycle's exit condition and budget (`CC-5`) and an external node's maximum wait time and fallback (`CC-15`) may not hold it.
- The consistency checks (`MM-8`) turn every placeholder into a question, so `CC-1` is satisfied only when no placeholder remains in inputs and outputs.
- Only `true` and `false` are booleans; versions are quoted strings; durations are strictly positive ISO 8601 durations (`PT30S`, `PT2H`, `P1D`).

Views are Mermaid diagrams derived from the cards. Illustrations of the model itself (e.g. `MB-2`) may be hand-drawn SVG, with the Mermaid next to them as the textual source.

Pinning (`P15`, `CC-19`):

- The standard has one semantic version for its modules, templates and schemas, released as the git tag `standard/vX.Y.Z`.
- Each project has one lock file (`kind: lock`), valid against its schema in `schemas/`. It records the standard version, the adopted templates by ID (their version is the standard's), the engine version with the checksum of its release's checksums file (which lists the checksum of each platform's executable) and the version of each tool of the toolkit.
- The lock file holds identifiers and exact versions only. An exact version is a full semantic version `MAJOR.MINOR.PATCH`, optionally with a pre-release or build part, or, for a tool, a full 40-character commit hash.
- The lock file never holds a path, a repo, a URL, a range, a partial version or a moving name such as `latest` or `SNAPSHOT`.
- A lock pins exact versions; compatible ranges, if ever needed, are declared in cards or templates, never in the lock (`P15`).

The file an executor writes at the end of a run (`MB-5`) also has a schema in `schemas/` (`kind: outcome`).
