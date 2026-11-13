# TK-1 Engineering skills for coding agents

When to use it: the method's agents are coding agents that support skills (slash commands loaded from `SKILL.md` files), and the project wants a ready-made set of skills for the judgement steps of `MB-2`.

Which skill carries out each step:

| Step (`MB-2`) | Skill |
| --- | --- |
| 1. Idea | — (the person) |
| 2. Clarification | `/grill-with-docs` |
| 3. Decision | — (the person) |
| 4. Specification | `/to-spec` |
| 5. Breakdown | `/to-tickets` |
| 6. Execution | `/implement` with `/tdd` |
| 7. Verification | `/code-review`, plus the pipeline |
| 8. Integration | — (mechanical gate) |
| 9. Retrospective | `/retro` |

Triage of incoming tickets: `/triage`.

Rules when adopting it:

- The skills are pinned to one version (`P15`) and copied into the project with their own installer, so every executor runs the same version.
- Names and file formats the skills define (glossary file, ADR folder, tracker configuration) belong to the skills: the project's documents point to them instead of restating them (`P1`).

## Sources

- Matt Pocock, [mattpocock/skills](https://github.com/mattpocock/skills)
