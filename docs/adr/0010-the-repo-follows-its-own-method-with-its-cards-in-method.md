# The repo follows its own method, with its method cards in `method/`

Supersedes ADR-0005.

This repo is built with the method it describes, in a minimal form: rules for agents in `AGENTS.md`; the cards of this repo's own method (its nodes, edges and artifacts, such as the companion) in `method/`; decisions recorded as ADRs in `docs/adr/`. A protected area (`MB-6`) holds `standard/`, `prompts/`, `method/`, `docs/adr/`, `engine/docs/adr/`, `AGENTS.md` and the agent and CI configuration; it is enforced by `.github/CODEOWNERS` and branch protection on `main`, so every change to it waits for the maintainer's review. The toolkit for the repo's own development is `TK-1`, installed as development tooling, separate from the standard.

## Consequences

- Every change goes through a PR into `main`; only the first commit, made while the repo was empty, went straight to `main`.
- The method cards in `method/` are validated in CI against the standard's card schemas, like the fixtures.
- An agent cannot change the cards that describe its own role: even a result appended to a log in `method/` is a protected-area PR.
- Other parts of the method (engine, interruption budget, measures) are added when the engine exists.
