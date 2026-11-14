---
id: MM-8
name: Consistency checks
module: MM
owner: The maintainer (protected area, MB-6)
status: decided
---

## MM-8 Consistency checks

A compiled model is consistent if it passes all these checks. An AI can run them at every change to the cards; every failed check becomes a question or a task. Those marked "Yes" can be written as scripts.

| ID | Check | Mechanical |
| --- | --- | --- |
| CC-1 | Every input has a source and every output a destination, or is declared as a final state | Yes |
| CC-2 | The type of a node's output matches the type of the connected node's input | Yes |
| CC-3 | Every non-deterministic node has a verifier | Yes |
| CC-4 | Every flow has a trigger, a success condition and error paths | Yes |
| CC-5 | Every cycle has an exit condition and a budget | Yes |
| CC-6 | Every artifact has one source of truth and one owner | Yes |
| CC-7 | No node can change the constraints that control it | Yes |
| CC-8 | Every dependency respects the declared boundaries | Yes |
| CC-9 | Every node has an environment it runs in | Yes |
| CC-10 | Every card has a status; every "decided" card cites the decision | Yes |
| CC-11 | No document contradicts a higher level of the hierarchy (`MM-7`) | No: judgement |
| CC-12 | Every edge that crosses a trust boundary has its security declared | Yes |
| CC-13 | Every state has exactly one state owner; every state with more than one writer has a concurrency rule | Yes |
| CC-14 | Every success condition and every acceptance criterion has at least one verifier that names it | Yes |
| CC-15 | Every external node (N4) has a maximum wait time and a fallback in its Errors and limits (N12) | Yes |
| CC-16 | Every verification chain ends in a deterministic check or in a person | Yes |
| CC-17 | Every adopted template is declared; every deviation cites an ADR | Yes |
| CC-18 | The engine declares how it stops, and each of its compute resources has an environment | Yes |
| CC-19 | Every reference to a shared component (standard, template, engine, tool) uses a stable identifier and a pinned version, never a location (`P15`) | Yes |
