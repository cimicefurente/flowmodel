---
id: MM-4
name: Node card
module: MM
owner: The maintainer (protected area, MB-6)
status: decided
---

## MM-4 Node card

Node types:

| Type | Deterministic | Examples |
| --- | --- | --- |
| Component | Yes | Service, module, function |
| Tool | Yes | Script, CLI, compiler, pipeline |
| Verifier | Yes if automatic; no if a person or an AI | Test, linter, reviewer |
| AI agent | No | A coding agent, a model launched by a script |
| Person | No | The developer, the client, a colleague |

Every node is described with 19 fields in three nested tiers; each tier is the first part of the next:

| Tier | Fields | When |
| --- | --- | --- |
| Draft | N1–N9 | Enough for a draft: every input already has a source and every output a destination (`CC-1`), and the card has a status (`CC-10`) |
| External | N1–N13 | The whole card of an external node |
| Full | N1–N19 | The other fields are filled in when the node becomes important or risky |

| # | Field | Question it answers |
| --- | --- | --- |
| N1 | ID | What is its stable key? It never changes, even if the name does |
| N2 | Name | What do people call it? It may change, and each project may replace it with its own term |
| N3 | Type | One of the types above |
| N4 | Origin | Is it under your control (`internal`) or not (`external`: a management system, a Git platform, a third-party API)? |
| N5 | Purpose | What does it do, in one sentence? |
| N6 | Input | From whom, which artifact, with which trigger, with which preconditions? |
| N7 | Output | To whom, which artifact, with which postconditions? |
| N8 | Card owner | Who may change this card? |
| N9 | Card status | Hypothesis, decided or superseded, with the reference to the decision? |
| N10 | Determinism | Same input, same output? |
| N11 | Verification | How do we know the output is correct, and who checks it? |
| N12 | Errors and limits | Which error outputs, which budget, after how many attempts does it pass to whom? |
| N13 | Contract version | Which version of its inputs and outputs (N6, N7) do others depend on? Major when a change breaks them, minor when it only adds |
| N14 | Controls | Which constraints limit it without being inputs? |
| N15 | Executor and permissions | Who or what runs it, with which capabilities and which context? |
| N16 | Transformation | What does it do to the input; which side effects does it have? |
| N17 | State | What does it read and write besides messages? |
| N18 | Measures | What is measured to know it works and to improve it? |
| N19 | Zoom | Does it contain a sub-flow? Which one? |

Field N10 decides a lot: a non-deterministic node (AI, person) always needs a verifier downstream (N11, `P3`).

N13 versions the node's contract, not the card: the card's own history is in version control (`P1`). A whole project used by another project is, from outside, a node with its own contract version and, inside, a sub-flow (N19).

Origin is independent of the type: an external AI model is an AI agent with Origin `external`. An external node has a reduced card, N1–N13, and its Errors and limits (N12) must contain a maximum wait time and a fallback when it does not answer (`P14`). Example: a pipeline that downloads a tool from an external site fails if the site answers with an error; the card says how many attempts to make and what happens next.
