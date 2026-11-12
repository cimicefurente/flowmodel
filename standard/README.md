# The flow model

One schema to describe a piece of software and the method that produces it.

## How the standard is organised

The standard is split into modules. A module cites another only by ID (e.g. `P3`, `CC-12`, `TA-1`), so modules can be moved or split mechanically.

Split rule: each module has one kind of reader that loads it, one rate of change and one owner.

| Module | File | Content | Loaded by | Changes |
| --- | --- | --- | --- | --- |
| `MM` Metamodel | [`MM-metamodel.md`](MM-metamodel.md) | Primitives, cards, views, hierarchy, consistency checks | The AI that fills in or checks the cards | Rarely |
| `P` Principles | [`P-principles.md`](P-principles.md) | Rules that hold for product and method alike | Every agent, in short form | Rarely |
| `T` Templates | [`templates/`](templates/README.md) | Pre-filled cards for each part of the schema: architectures, engines, people, nodes, toolkits | The AI when a project starts | When a new case is needed |
| `MB` Base method | [`MB-base-method.md`](MB-base-method.md) | Steps, execution levels, cycles, the person as a node, the engine | The engine and the method's agents | At every retrospective |
| `PA` AI procedure | [`PA-ai-procedure.md`](PA-ai-procedure.md) | Starting a project, questions, what gets loaded | The AI at project start; the system prompts | When the method changes |

System prompts for each role are in [`../prompts/`](../prompts/).

The cards compiled for a project do not live here: they live in the project's own repo, and refer to this standard by identifier and version, never by path (`P15`).
