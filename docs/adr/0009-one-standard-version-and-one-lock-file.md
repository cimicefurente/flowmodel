# One version for the standard and one lock file per project

`PA-5` leaves open how a project pins the standard it follows (`P15`). The standard has one semver version covering its modules, templates and schemas, released as the git tag `standard/vX.Y.Z`, so a project cannot combine incompatible pieces; the engine is versioned separately. Each project has one YAML lock file that pins, with identifiers and versions only, the standard version, the adopted templates by ID, the engine version with its checksum and the versions of the toolkit's tools (`CC-19`). Cards declare only their kind and take the version from the lock file, so upgrading the standard does not touch every card.

## Consequences

- The standard and the engine both start at `0.1.0` and become `1.0.0` when the engine passes the acceptance criterion of its first version, before any production adoption.
- The engine refuses a lock file whose standard major version it does not support.

## Considered options

- A version per module or template: finer upgrades, but every combination would need to be checked for compatibility.
- A version in every card: self-describing, but every upgrade of the standard would rewrite every card.
