# One repo for standard and engine; the engine embeds the released schemas and sub-module files

This supersedes ADR-0001.

The standard (`standard/`) and the engine (`engine/`) live in one repo, so that a change to a card schema and the engine code that reads it is one PR, checked by one CI run. The engine reads the standard only through what a standard release publishes: the card schemas and the sub-module files (one file per sub-module, with a YAML header, as `standard/README.md` describes). For each standard version it supports, the engine embeds both, copied from the release's git tag (`standard/vX.Y.Z`, `PA-5`) by one generator, so that it validates cards and assembles each prompt from the IDs it lists (`PA-4`; a module ID stands for all its sub-modules) without reading the standard's folder. It never reads the standard's files or paths in the working tree. CI checks that the copies match the tag and, once the engine exists, that the engine reads nothing else of the standard.

## Consequences

- Splitting later is cheap: extract `engine/` with its history (`git filter-repo`) into its own repo. Do it when a second engine or a different owner appears.
- Adopting projects are not affected by a split, because they depend on the standard and the engine by stable identifier and pinned version, never by location (`P15`, `CC-19`).
- A change to a sub-module reaches the engine only through a new standard release and a regenerated copy, like a change to a schema.

## Considered options

- Two repos from the start: same guarantee for adopters, but two coordinated PRs for every schema change from day one.
- The engine reads the standard's folder at run time: no generator, but the engine would depend on the repo's layout and on unreleased text.
- The engine embeds whole module files: fewer files, but a prompt that cites one sub-module would receive the whole module (`P5`).
