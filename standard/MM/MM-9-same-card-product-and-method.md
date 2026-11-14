---
id: MM-9
name: Same card, product and method
module: MM
owner: The maintainer (protected area, MB-6)
status: decided
---

## MM-9 Same card, product and method

A product node and a method node filled in with the same card; the values are illustrative.

| Field | Product: order service | Method: executor |
| --- | --- | --- |
| N1 ID | `orders-service` | `executor` |
| N2 Name | Order service | Executor |
| N3 Type | Component | AI agent |
| N4 Origin | `internal` | `internal` |
| N5 Purpose | Records an order and starts the payment | Implements a task and proposes a change |
| N6 Input | `CreateOrder` from the public API, synchronous call; authenticated user | Task from the engine, event; acceptance criteria present |
| N7 Output | `OrderCreated` to the payment service, event | Proposed change (PR) to the reviewer |
| N8 Card owner | Product team | The person (protected area, `MB-6`) |
| N9 Card status | Decided | Hypothesis |
| N10 Determinism | Yes | No |
| N11 Verification | Contract tests; error monitoring | Automated tests + independent reviewer + person |
| N12 Errors and limits | `InvalidOrder` to the caller; 3 attempts on the event | After 3 attempts the person decides |
| N13 Contract version | `2.1` | `1.0` |
| N14 Controls | Validation rules; rate limit | Rules for agents; perimeter of allowed files |
| N15 Executor and permissions | The service process; writes only the orders table | A coding agent; writes only on its own branch |
| N16 Transformation | Validates, saves, emits an event | Writes tests and code |
| N17 State | Writes the orders database | Reads the repo, writes the branch |
| N18 Measures | Latency, error rate | Duration, cost, attempts |
| N19 Zoom | — | Test-first cycle |
