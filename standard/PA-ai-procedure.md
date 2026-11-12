# PA. AI procedure

## PA-1 Steps

The AI that receives this model applies it in nine steps and invents nothing: every missing piece of information becomes a question or a "to be decided" field.

1. **Context**: purpose, users, constraints, resources, starting from the project description.
2. **Templates**: proposes suitable ones for architecture, engine, person and toolkit (`T`), or "none" with the reason; then narrows and widens them with the person (`T-0`).
3. **Product flows**: the 3–7 main scenarios, each with a flow card made of large nodes.
4. **Nodes and artifacts**: minimal cards (N1–N4) for every node; types of the artifacts on the edges; external nodes.
5. **Views**: structure, execution, security.
6. **Method**: starts from `MB` and adapts it; for every step the level, executor and permissions; the engine's card and the person's card.
7. **Constraints**: the rules, each with its type and how it is enforced; quality goals as scenarios.
8. **Consistency checks** (`MM-8`): gaps become questions.
9. **First vertical slice**: proposes the smallest complete flow to build first.

## PA-2 Dialogue rules

One question at a time, each with the AI's recommendation; if the answer is in the documents, it is not asked; every answer updates the cards at once.

## PA-3 Questions to ask

| Area | Questions |
| --- | --- |
| Purpose and users | What must the user be able to do in the end? Who uses it? What will the first version *not* do? |
| Templates | What kind of software is it? Which architecture template is closest, and where does it differ? Which toolkit do the agents use? |
| Flows | What are the main scenarios? What starts them? When has a flow succeeded? |
| Data | What data comes in and goes out? Where does the source of truth live? Is there sensitive data? Must different customers' data be kept apart? |
| Quality | How many users, with which response time, which availability, how fast is a backup restored? |
| Security | Who can do what? Where is identity checked? Where could an attack come in? |
| Externals | Which systems outside your control do you depend on? What happens if they do not answer? |
| Constraints | Time, budget, imposed technologies, company rules? |
| Environments | Where does it run? Which machines and services are available? Where do configuration and secrets live? |
| Engine | Where does the controller run? Where does the method state live? Which compute resources do you have, local and online? How do you want to be able to stop it? |
| Person | Who decides what? What may an agent do on its own? When do you want to be interrupted, how many times a day, on which channel? How is the work verified? |
| Evolution | What will change most often? What must the user or the AI be able to change? |

## PA-4 What is loaded, and by whom

Least context (`P5`): each agent receives only the modules it needs. Each role has a system prompt in `prompts/` that lists the IDs to load; the full text is assembled at the time of use, by the engine or by hand, never copied into the prompt (`P1`).

| Who | Loads | Prompt |
| --- | --- | --- |
| AI at project start | `MM`, `P`, `T`, `PA` | `prompts/project-setup.md` |
| AI that checks consistency | `MM-8` and the project's cards | `prompts/consistency-check.md` |
| Executor agent | `P` in short form, the cards of its own node and of the task, the project's standards | `prompts/executor.md` |
| Engine | `MB` and the project's method cards | `prompts/engine.md` |

## PA-5 Format

One card per Markdown file in the project's repo; views as Mermaid diagrams derived from the cards. Illustrations of the model itself (e.g. `MB-2`) may be hand-drawn SVG, with the Mermaid next to them as the textual source.

How a project pins the version of the standard it follows (`P15`) is defined together with the card schemas: to be decided.
