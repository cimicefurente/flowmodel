---
id: PA-4
name: What is loaded, and by whom
module: PA
owner: The maintainer (protected area, MB-6)
status: decided
---

## PA-4 What is loaded, and by whom

Least context (`P5`): each agent receives only the modules it needs. Each role has a system prompt in `prompts/` that lists the IDs to load; the full text is assembled at the time of use, by the engine or by hand, never copied into the prompt (`P1`).

| Who | Loads | Prompt |
| --- | --- | --- |
| AI at project start | `MM`, `P`, `T`, `PA` | `prompts/project-setup.md` |
| AI that checks consistency | `MM-8` and the project's cards | `prompts/consistency-check.md` |
| Executor agent | `P` in short form, the cards of its own node and of the task, the project's standards | `prompts/executor.md` |
| Engine | `MB` and the project's method cards | `prompts/engine.md` |
