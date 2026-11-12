# The engine interprets the project's method flow cards with a deterministic controller

Projects adapt the method, so the engine (`MB-5`) does not hard-code the steps of `MB-2`: it reads the project's method flow card and the cards of its nodes and runs them, and adapting the method changes cards, never the engine. Its controller is deterministic: the same cards and the same run log always lead to the same choices. All judgement lives in AI agent and person nodes (`MB-1`); the work of a non-deterministic executor reaches the controller only as an outcome file validated by a schema.

## Consequences

- `MB-2` is published as a method template made of cards (`T-0`), which a project adopts, narrows and widens like any template; that card is the single source of the method graph (`P1`).
- A change to the method, such as one proposed by the retrospective, is a change to cards in the protected area (`MB-6`), never to the engine.

## Considered options

- The `MB-2` cycle hard-coded in the engine: simpler at first, but every adaptation of the method would need a new engine.
- An AI agent as controller: flexible, but its choices cannot be replayed or checked mechanically (`P4`).
