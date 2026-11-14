---
id: MM-6
name: Views
module: MM
owner: The maintainer (protected area, MB-6)
status: decided
---

## MM-6 Views

Cards are the source of truth; views are five ways of looking at them. Views are derived from the cards, never written separately, so they cannot contradict them.

| ID | View | Question | Derived from | Form |
| --- | --- | --- | --- | --- |
| V1 | Flows (dynamics) | What happens when…? | Flow and edge cards | One sequence or flow diagram per scenario |
| V2 | Structure (statics) | What parts is it made of, who may depend on whom? | Nodes and boundaries | Block diagram with the allowed dependencies |
| V3 | Execution | What runs where, with which resources? | Nodes and environments | Map of machines and services |
| V4 | Knowledge | Which document wins if two contradict each other? | Constraints and document artifacts | Hierarchy (`MM-7`) |
| V5 | Security | Where can one get in, who is who at each step, where does sensitive data go? | Trust boundaries, edges that cross them, sensitive artifacts, external nodes | Trust-boundary diagram with the crossing edges and the threats per edge |

The flow view alone is not enough: rules such as "the core does not depend on the interface" are structural constraints and appear in no flow.
