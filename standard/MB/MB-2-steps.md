---
id: MB-2
name: Steps
module: MB
owner: The maintainer (protected area, MB-6)
status: decided
---

## MB-2 Steps

No AI output changes the product without going through verification.

![MB-2: the nine steps of the method, in a 3×3 snake grid](diagrams/mb-2.svg)

The drawing above is a hand-made SVG (`diagrams/mb-2.svg`), because Mermaid cannot lay out a snake grid with its return edges. The textual source, which agents read and change, is the Mermaid below: if a step changes, both are updated.

```mermaid
flowchart TD
  A["1. Idea<br/>person<br/>→ project description"] --> B["2. Clarification<br/>AI + person<br/>→ decisions, glossary"]
  B --> C["3. Decision<br/>person<br/>→ decision record (ADR)"]
  C --> D["4. Specification<br/>AI agent<br/>→ spec of one slice"]
  D --> E["5. Breakdown<br/>AI agent<br/>→ tasks with criteria"]
  E --> F["6. Execution<br/>AI agent<br/>→ proposed change (PR)"]
  F -- PR --> G["7. Verification<br/>tests + independent reviewer<br/>→ outcome"]
  G -- "fails: retry (max N)" --> F
  G -- "beyond N attempts" --> P(["The person decides"])
  P -- retry --> F
  P -- "rewrite the task" --> E
  P -- "revisit the decision" --> C
  G -- ok --> H["8. Integration<br/>verifier (gate)<br/>→ new product state"]
  H --> I["9. Retrospective<br/>AI + person<br/>→ changes to method and rules"]
  I -- "new cycle" --> C
```

| # | Step | Executor | Level (`MB-1`) | Output |
| --- | --- | --- | --- | --- |
| 1 | Idea | Person | Decision | Project description |
| 2 | Clarification | AI + person | Judgement + decision | Decisions, glossary |
| 3 | Decision | Person | Decision | Decision record (ADR) |
| 4 | Specification | AI agent | Judgement | Spec of one slice |
| 5 | Breakdown | AI agent | Judgement | Tasks with criteria |
| 6 | Execution | AI agent | Judgement | Proposed change (PR) |
| 7 | Verification | Tests + independent reviewer | Mechanical + judgement | Outcome |
| 8 | Integration | Verifier (gate) | Mechanical | New product state |
| 9 | Retrospective | AI + person | Judgement + decision | Changes to method and rules |

The tools that carry out each step come from the adopted toolkit template (`TK`).
