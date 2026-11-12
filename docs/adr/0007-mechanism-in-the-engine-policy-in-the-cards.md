# Mechanisms live in the engine, policies in the project's cards

One engine serves every adopting project, so it provides only mechanisms; what a project allows is a policy declared in its cards: executors and their permissions, platform capabilities, isolation, concurrency, budgets and limits, verifiers, authentication. Every policy has a safe default, but none is imposed: a weaker choice is allowed and flagged by the validator, for example a capability that would let a node change the protected area or its own constraints (`CC-7`). This applies `P5` without restricting any project.

## Consequences

- The engine names no agent or tool: an executor is a command template from the adopted toolkit (ADR-0003) or from the node card.
- Changing a policy is a change to cards, through the same pipeline as any other change (`P6`); only a missing mechanism needs a new engine version.
