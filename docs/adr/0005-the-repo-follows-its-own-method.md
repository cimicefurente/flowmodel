---
status: superseded by ADR-0010
---

# The repo follows its own method, in a minimal form

This repo is built with the method it describes. For now that means: rules for agents in `AGENTS.md`; a protected area (`MB-6`) made of `standard/`, `prompts/`, `docs/adr/` and the agent and CI configuration, enforced by `.github/CODEOWNERS` and branch protection on `main`; decisions recorded as ADRs in `docs/adr/`. The toolkit for its own development is `TK-1`, installed as development tooling, separate from the standard.

## Consequences

- The first commit goes straight to `main`, because the repo is empty; after it the maintainer turns on branch protection, and every later change goes through a PR.
- Other parts of the method (engine, interruption budget, measures) are added when the engine exists.
