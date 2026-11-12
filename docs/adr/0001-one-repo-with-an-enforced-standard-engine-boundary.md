# One repo for standard and engine, with an enforced boundary

The standard (`standard/`) and the engine (`engine/`) live in one repo, so that a change to a card schema and the engine code that reads it is one PR, checked by one CI run. The engine reads the standard only through the card schemas, never through its files or paths; a CI check enforces this once the engine exists.

## Consequences

- Splitting later is cheap: extract `engine/` with its history (`git filter-repo`) into its own repo. Do it when a second engine or a different owner appears.
- Adopting projects are not affected by a split, because they depend on the standard and the engine by stable identifier and pinned version, never by location (`P15`, `CC-19`).

## Considered options

- Two repos from the start: same guarantee for adopters, but two coordinated PRs for every schema change from day one.
