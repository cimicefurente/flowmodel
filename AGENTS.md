# AGENTS.md

Rules for every agent working on this repo. This file is protected (`.github/CODEOWNERS`); propose changes in a PR, never edit it inside another task.

## Language

- Talk to the maintainer in Italian.
- Everything in the repo is in English: documents, code, comments, ADRs, issues, PRs, commit messages.

## What this repo is

The flow model standard (`standard/`), the system prompts for its roles (`prompts/`) and its reference engine (`engine/`). Start from `README.md` and `standard/README.md`.

## Knowledge hierarchy

`standard/` → `docs/adr/` → issue → code. A lower level never contradicts a higher one; if your work would, stop and open an issue that quotes both sides.

- One source of truth per fact: cite it by ID (e.g. `P3`, `CC-12`), never copy it (`P1`).
- ADRs are never rewritten; a new ADR says which one it supersedes (`P9`).
- The repo is self-contained (ADR-0002): no references to earlier versions, to other projects or to inspirations, except in "Sources" sections with links.
- No tool is named in `MB`; tools go in toolkit templates (ADR-0003).

## Boundaries

- The engine reads the standard only through the card schemas, never through its files or paths (ADR-0001).
- Prompts list module IDs; they never copy module text (ADR-0004).
- Never edit a path listed in `.github/CODEOWNERS` unless your task is about that path; such PRs wait for the maintainer.
- Never: spend money, create or read secrets, start permanent services, open network ports, act outside this repo, delete or rename data or repos.

## Minimum context

Read only what your task needs: this file, the modules it cites, the relevant ADRs, your issue (`P5`).
