# T. Templates

## Sub-modules

| ID | Name |
| --- | --- |
| [`T-0`](T-0-how-a-template-is-used.md) | How a template is used |
| [`TA-1`](TA-1-client-server.md) | Multi-user client-server application |
| [`TK-1`](TK-1-engineering-skills.md) | Engineering skills for coding agents |

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
