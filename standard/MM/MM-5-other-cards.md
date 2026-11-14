---
id: MM-5
name: Other cards
module: MM
owner: The maintainer (protected area, MB-6)
status: decided
---

## MM-5 Other cards

Each also has an ID, a card owner and a card status, like the node.

| Card | Fields |
| --- | --- |
| Artifact | Type and schema (fields, format); source of truth (where the original lives); who creates and who changes it; life cycle (e.g. draft → approved → superseded); versioning and backward compatibility; sensitivity (personal data, secrets) |
| Edge | From → to; artifact; mode (synchronous call, event, schedule, shared state); guarantees (ordering, delivery, idempotency); security if it crosses a boundary (channel, caller identity, permissions checked, validation); contract evolution (how it changes without breaking its users); what happens if it fails |
| State | Content; state owner (`P13`); writers; readers; concurrency rule if there is more than one writer (`CC-13`); persistence and backup; how to roll back |
| Flow | Goal; trigger; nodes and edges (diagram); success condition; error paths; cycles with exit condition and budget; measures (duration, cost, outcome) |
| Constraint | Type (structure, security, quality, process); rule; what it applies to; why, with the evidence; who can change it; how it is enforced (mechanically or only by instruction) |
| Boundary | What it contains; whether it is a trust boundary; what may enter and leave; which dependencies are allowed |
| Environment | Resources and limits; who manages it; which nodes it hosts; where configuration and secrets live |

For a constraint, "how it is enforced" matters more than the rule itself: a rule written only in a prompt is a suggestion; a rule enforced by CI or permissions is a constraint.

A quality constraint is written as a measurable scenario; otherwise "secure" and "scalable" cannot be verified:

| Part | Example |
| --- | --- |
| Quality | Scalability |
| Stimulus | 200 users of the same customer open the order list in the same minute |
| Environment | Production, normal load |
| Expected response | The list opens without errors |
| Measure | 95% of responses under 1 s |
| Verification | Load test in the pipeline, before release |
