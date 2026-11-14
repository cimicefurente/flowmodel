# P. Principles

They hold for product and method alike.

| ID | Principle | Serves |
| --- | --- | --- |
| P1 | One source of truth for every fact; other documents cite it | Structure |
| P2 | Explicit contracts on every edge, so a node can be replaced without touching the others | Malleability |
| P3 | Every non-deterministic node (AI, person) has an independent verifier downstream; the verification chain ends in a deterministic check or in a person | Reliability |
| P4 | Constraints are enforced mechanically whenever possible; no node changes its own constraints | Security |
| P5 | Least privilege and least context: each node receives only the permissions, inputs and rules it needs | Security, AI attention |
| P6 | Every change, to the product or to the method, goes through the same pipeline: propose → verify → apply → version → roll back | Safe malleability |
| P7 | Every cycle has an exit condition and a budget; beyond it, a person decides | Control |
| P8 | Grow by zooming: large nodes at first, detail only where needed | Scalability of the model |
| P9 | Every decision has a status and evidence; it is never rewritten, only superseded by a new one | Structure |
| P10 | Every flow has at least one measure; only what is measured can be improved | Improvement |
| P11 | Every boundary crossing goes through an explicit contract; no node skips a layer | Security, malleability |
| P12 | Identity and permissions are checked at the trust boundary, on the side you control; never only on the caller's side | Security |
| P13 | Every state has exactly one state owner, accountable for it; more than one writer is allowed only with a declared concurrency rule | Robustness, scalability |
| P14 | What you do not control (external nodes) has a contract, a maximum wait time and a fallback | Reliability |
| P15 | Every dependency on a shared component (this standard, a template, the engine, a tool) goes through a stable identifier and a pinned version recorded in one lock file; never through a location such as a repo, a path or a file URL | Malleability, evolution |

`P11`–`P13` hold for any software, including software that does not have the user → UI → API → data shape (a CLI, a batch pipeline, a library). That chain proper is an architecture template (`TA-1`).

## Short form

The short form that agents load (`PA-4`) is the table above without the "Serves" column. It is derived from this file, never written separately.
