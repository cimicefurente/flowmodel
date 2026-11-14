# The flow model

One schema to describe a piece of software and the method that produces it.

## How the standard is organised

The standard is split into modules. A module cites another only by ID (e.g. `P3`, `CC-12`, `TA-1`), so modules can be moved or split mechanically.

Split rule: each module has one kind of reader that loads it, one rate of change and one owner.

Each module is a folder named by its ID, with a `README.md` (the module's introduction and an index of its sub-modules) and one file per sub-module, `<ID>-<slug>.md`. Each sub-module file starts with a YAML header: `id`, `name`, `module`, `owner`, `status` (`MM-5`). A prompt that loads a module ID loads all its sub-modules (`PA-4`). `P` is one file, because its principles are table rows and its short form is derived from it.

| Module | Folder | Content | Loaded by | Changes |
| --- | --- | --- | --- | --- |
| `MM` Metamodel | [`MM/`](MM/README.md) | Primitives, cards, views, hierarchy, consistency checks | The AI that fills in or checks the cards | Rarely |
| `P` Principles | [`P/`](P/README.md) | Rules that hold for product and method alike | Every agent, in short form | Rarely |
| `T` Templates | [`T/`](T/README.md) | Pre-filled cards for each part of the schema: architectures, engines, people, nodes, toolkits | The AI when a project starts | When a new case is needed |
| `MB` Base method | [`MB/`](MB/README.md) | Steps, execution levels, cycles, the person as a node, the engine | The engine and the method's agents | At every retrospective |
| `PA` AI procedure | [`PA/`](PA/README.md) | Starting a project, questions, what gets loaded | The AI at project start; the system prompts | When the method changes |

The JSON Schemas of the cards, of the lock file and of the executor outcome file are in [`schemas/`](schemas/) (`PA-5`).

System prompts for each role are in [`../prompts/`](../prompts/).

The cards compiled for a project do not live here: they live in the project's own repo, and refer to this standard by identifier and version, never by path (`P15`).
