---
id: MB-1
name: Three execution levels
module: MB
owner: The maintainer (protected area, MB-6)
status: decided
---

## MB-1 Three execution levels

Each step of the method is assigned to the lowest level that is enough: what a script can do is not done by an AI; what an AI with a verifier can do is not done by a person.

| Level | Node type (N3) | Determinism (N10) | Examples | Verification |
| --- | --- | --- | --- | --- |
| Mechanical | Tool, automatic verifier | Yes | Create a branch or a working folder, run the checks, push, open a PR, read the outcome of a run, the Integration gate, clean-up | The script's own tests |
| Judgement | AI agent, AI reviewer | No | Specify, break down, implement, review, propose the retrospective | A verifier downstream (`P3`) |
| Decision | Person | No | Choose, approve a constraint or a protected file, decide beyond the attempt budget | The end of the chain (`P3`, `CC-16`) |
