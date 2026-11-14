---
id: MM-3
name: Primitives
module: MM
owner: The maintainer (protected area, MB-6)
status: decided
---

## MM-3 Primitives

Eight concepts are enough to describe any project, product and method. If something fits none of them, either a concept is missing or it is being described badly. Templates (`T`) are not primitives: they are sets of cards written with these.

| Primitive | What it is | Product example | Method example |
| --- | --- | --- | --- |
| Node | A unit that transforms inputs into outputs. Types in `MM-4` | Order service | Executor agent, reviewer, the person |
| Artifact | What travels on edges: data, document, event | Order, HTTP request | Spec, task, proposed change (PR), decision (ADR) |
| Edge | A typed connection between two nodes | API call, queued event | Task assigned, PR opened |
| State | What persists and is shared between nodes | Database, file | Git repo, task tracker |
| Flow | A graph of nodes started by a trigger, with a goal and an end | "The user places an order" | "From idea to released feature" |
| Constraint | A rule that limits nodes or flows without being an input | Rate limit, security rule | Decisions, policies, rules for agents |
| Boundary | A grouping with rules on what enters, leaves and depends; a trust boundary separates parties with different permissions | Module, service, network | Protected area, role |
| Environment | Where a node runs, with which resources | Server, browser, cloud | Laptop, cloud, home server |
