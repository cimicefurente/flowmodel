---
id: MB-3
name: Cycles
module: MB
owner: The maintainer (protected area, MB-6)
status: decided
---

## MB-3 Cycles

Return edges are what make a method different from a pipeline:

- verification sends the work back to execution at most N times; beyond N the person decides (`P7`) between three paths: retry (back to Execution with more attempts), rewrite the task (back to Breakdown) or revisit the decision (back to Decision);
- the retrospective opens a new cycle from Decision: it changes decisions, rules and checks, going through `P6`;
- a contradiction found at any step goes back to Decision.
