# T. Templates

## T-0 How a template is used

A template is a set of pre-filled cards for one part of the schema. There are five families:

| Family | What it pre-fills | ID |
| --- | --- | --- |
| Architecture | Nodes, boundaries, edges, constraints and quality goals of the product | `TA` |
| Engine | Controller, method state, compute resources, stopping (`MB-5`) | `TM` |
| Person | Decision points, interruption budget, channel (`MB-4`) | `TP` |
| Node | Full card of a recurring node (e.g. executor, reviewer) | `TN` |
| Toolkit | The tools that carry out the steps of the method (`MB-2`) | `TK` |

When a project starts, it adopts the templates it needs (`PA-1`), then for each one it:

- **narrows**: removes what is not needed, with the reason written down;
- **widens**: adds nodes, boundaries, constraints;
- **departs**: changes a rule of the template only with an ADR that cites it (`MM-7`, `CC-17`).

Adopted cards start as "hypothesis" and become "decided" only when the person confirms them.

Architecture, engine, person and node templates do not choose technologies: they say what must be true, not with which product. A toolkit template is the only place where a tool is named, so that changing tools means switching toolkit, not editing the method.

## Written templates

| ID | Template |
| --- | --- |
| [`TA-1`](TA-1-client-server.md) | Multi-user client-server application |
| [`TK-1`](TK-1-engineering-skills.md) | Engineering skills for coding agents |

## Other templates, to write when needed

| ID | Template | Notes |
| --- | --- | --- |
| TA-2 | Local tool or CLI | One user, no network boundary |
| TA-3 | Batch or data pipeline | Scheduled trigger; idempotency and resumption matter more than latency |
| TA-4 | Library | The contract is the public interface; backward compatibility at the centre |
| TA-5 | Event-driven system | Queues, at-least-once delivery, ordering |
| TA-6 | AI agent or AI flow | Non-deterministic nodes at the centre; verification and budget first |
| TM-1 | Fully local engine | Controller, state and executors on one computer |
| TM-2 | Fully online engine | Controller, state and executors on one server |
| TM-3 | Mixed engine | Several servers and computers; e.g. controller on a personal server, state on a Git platform, executors partly online and partly on a laptop |
| TP-1… | Person profiles | Interruption budget and decision points for different working styles |
| TN-1… | Recurring nodes | Executor, reviewer, coordinator |
| TK-2… | Other toolkits | One per set of tools that carries out the method's steps |
