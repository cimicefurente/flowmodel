# flowmodel

One schema to describe a software product and the method that builds it, and an engine that runs that method.

| Folder | Content |
| --- | --- |
| [`standard/`](standard/README.md) | The model: modules `MM`, `P`, `T`, `MB`, `PA`. Start here. |
| [`prompts/`](prompts/) | System prompts for each role (`PA-4`) |
| [`method/`](method/) | This repo's own method cards (ADR-0010), e.g. the companion |
| [`engine/`](engine/README.md) | The reference engine (`MB-5`). Not written yet |
| [`docs/adr/`](docs/adr/) | Decisions about this repo |

## Adopting it

A project keeps its own cards in its own repo and refers to the standard and the engine by stable identifier and pinned version, never by path or URL (`P15`, `CC-19`). Start with the project-setup prompt (`prompts/project-setup.md`) and procedure `PA-1`.

No licence yet: all rights reserved.
