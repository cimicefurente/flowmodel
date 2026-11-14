---
id: T-0
name: How a template is used
module: T
owner: The maintainer (protected area, MB-6)
status: decided
---

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
