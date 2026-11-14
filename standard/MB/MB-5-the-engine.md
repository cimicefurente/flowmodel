---
id: MB-5
name: The engine
module: MB
owner: The maintainer (protected area, MB-6)
status: decided
---

## MB-5 The engine

The engine is the node that runs the method: it calls the tools, starts the agents, stops at the decision points and delivers questions to the person. It has a card like any other node, with these parts:

| Part | What it declares |
| --- | --- |
| Controller | Where it runs; how it reads the state and chooses the next step; with which permissions |
| Method state | Where tasks, cards and decisions live; who writes it (`P13`) |
| Compute resources | N resources, N to be decided. For each: type (local, online), environment, capabilities (models, tools), permissions, cost, availability |
| Channel to the person | How questions and reports arrive; how decisions come back (`MB-4`) |
| Stopping | How you stop it, who can, what happens to work in progress (`CC-18`) |
| Measures | Duration, cost, attempts, interruptions (`P10`) |

Each part is decided per project, from the questions in `PA-3` or starting from a `TM` template. The same schema covers an engine running entirely on one computer, entirely on one server, or spread over several servers and computers.
