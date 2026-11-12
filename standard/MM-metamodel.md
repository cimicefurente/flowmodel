# MM. Metamodel

## MM-1 Purpose and use

One schema describes both the software and the method that produces it. Both are networks of nodes that transform artifacts, connected by edges, under constraints. The method is a program run by people and AI, whose output is changes to the product.

The schema itself is a node: it takes a project description and the person's answers, and produces the project's cards. Templates (`T`) are its ready-made configurations.

At the start of a project:

1. Give an AI the modules listed in `PA-4`, its system prompt and a description of the project.
2. The AI follows procedure `PA-1`: it asks questions, proposes suitable templates, fills in the cards and marks as hypotheses whatever the person has not decided.
3. The result is a set of cards and five views, kept in the project's repo and updated with the same method they describe.

The schema describes; it does not choose technologies. Any field may stay "to be decided"; no field is invented. Start with a few large nodes and add detail only where it is needed.

## MM-2 Sources

| Source | Idea | What the model takes from it |
| --- | --- | --- |
| Leon J. Osterweil, ["Software Processes Are Software Too"](https://www.ics.uci.edu/~taylor/ICS221/papers/p2-osterweil.pdf), ICSE 1987, pp. 2–13 | A development process can be described and programmed like software | The method uses the same primitives as the product |
| NIST, [FIPS PUB 183, IDEF0](https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub183.pdf), 21 December 1993 (withdrawn as a federal standard in 2008) | Every function has Inputs, Controls, Outputs, Mechanisms | The basic fields of the node card |
| Philippe Kruchten, ["The 4+1 View Model of Architecture"](https://doi.org/10.1109/52.469759), IEEE Software 12(6), November 1995, pp. 42–50 | An architecture is described with several views, tied together by scenarios | The views; flows as scenarios |
| Simon Brown, [C4 model](https://c4model.com/) | Zoom levels: context, containers, components, code | A node can contain a flow |
| OMG, [SPEM 2.0](https://www.omg.org/spec/SPEM/2.0), April 2008 | Process metamodel: roles, activities, work products | Roles = executors; work products = artifacts |
| Bertrand Meyer, ["Applying 'Design by Contract'"](https://doi.org/10.1109/2.161279), IEEE Computer 25(10), October 1992, pp. 40–51 | Preconditions, postconditions, invariants | Contracts on nodes and edges |
| Brendan Fong and David I. Spivak, [*Seven Sketches in Compositionality*](https://arxiv.org/abs/1803.05316), 2018 | Processes as morphisms that compose | Edges compatible by type; composable flows |
| Rick Kazman, Mark Klein, Paul Clements, [ATAM: Method for Architecture Evaluation](https://apps.dtic.mil/sti/html/tr/ADA382629/index.html), CMU/SEI-2000-TR-004, August 2000 | Quality requirements are written as concrete, measurable scenarios | Quality constraints (`MM-5`) |
| Microsoft, [secure design review and threat modeling](https://www.microsoft.com/en-us/securityengineering/sdl/practices/secure-by-design); [STRIDE](https://learn.microsoft.com/en-us/training/modules/design-solutions-secure-applications/4-evaluate-application-threats-threat-modeling) | Threats are sought along trust boundaries; every flow that crosses one needs authentication, authorisation and validation | The security view (`V5`), `P12` |

No source is a prerequisite for using the model.

## MM-3 Primitives

Eight concepts are enough to describe any project, product and method. If something fits none of them, either a concept is missing or it is being described badly. Templates (`T`) are not primitives: they are sets of cards written with these.

| Primitive | What it is | Product example | Method example |
| --- | --- | --- | --- |
| Node | A unit that transforms inputs into outputs. Types in `MM-4` | Order service | Executor agent, reviewer, the person |
| Artifact | What travels on edges: data, document, event | Order, HTTP request | Spec, task, proposed change (PR), decision (ADR) |
| Edge | A typed connection between two nodes | API call, queued event | Task assigned, PR opened |
| State | What persists and is shared between nodes | Database, file | Git repo, task tracker |
| Flow | A graph of nodes started by a trigger, with a goal and an end | "The user places an order" | "From idea to released feature" |
| Constraint | A rule that limits nodes or flows without being an input | Rate limit, security rule | Decisions, policies, rules for agents |
| Boundary | A grouping with rules on what enters, leaves and depends; a trust boundary separates parties with different permissions | Module, service, network | Protected area, role |
| Environment | Where a node runs, with which resources | Server, browser, cloud | Laptop, cloud, home server |

## MM-4 Node card

Node types:

| Type | Deterministic | Examples |
| --- | --- | --- |
| Component | Yes | Service, module, function |
| Tool | Yes | Script, CLI, compiler, pipeline |
| Verifier | Yes if automatic; no if a person or an AI | Test, linter, reviewer |
| AI agent | No | A coding agent, a model launched by a script |
| Person | No | The developer, the client, a colleague |
| External | Outside your control | A management system, a Git platform, a third-party API |

Every node is described with 18 fields. The first five are enough for a draft; the others are filled in when the node becomes important or risky.

| # | Field | Question it answers |
| --- | --- | --- |
| N1 | ID | What is its stable key? It never changes, even if the name does |
| N2 | Name | What do people call it? It may change, and each project may replace it with its own term |
| N3 | Type | One of the types above |
| N4 | Purpose | What does it do, in one sentence? |
| N5 | Input | From whom, which artifact, with which trigger, with which preconditions? |
| N6 | Controls | Which constraints limit it without being inputs? |
| N7 | Executor and permissions | Who or what runs it, with which capabilities and which context? |
| N8 | Determinism | Same input, same output? |
| N9 | Transformation | What does it do to the input; which side effects does it have? |
| N10 | State | What does it read and write besides messages? |
| N11 | Output | To whom, which artifact, with which postconditions? |
| N12 | Verification | How do we know the output is correct, and who checks it? |
| N13 | Errors and limits | Which error outputs, which budget, after how many attempts does it pass to whom? |
| N14 | Measures | What is measured to know it works and to improve it? |
| N15 | Zoom | Does it contain a sub-flow? Which one? |
| N16 | Owner | Who may change this card? |
| N17 | Card status | Hypothesis, decided or superseded, with the reference to the decision? |
| N18 | Contract version | Which version of its inputs and outputs (N5, N11) do others depend on? Major when a change breaks them, minor when it only adds |

Field N8 decides a lot: a non-deterministic node (AI, person) always needs a verifier downstream (N12, `P3`).

N18 versions the node's contract, not the card: the card's own history is in version control (`P1`). A whole project used by another project is, from outside, a node with its own contract version and, inside, a sub-flow (N15).

An external node has a reduced card: N1–N5, N11, N13, N18, plus two fields of its own: maximum wait time and fallback when it does not answer (`P14`). Example: a pipeline that downloads a tool from an external site fails if the site answers with an error; the card says how many attempts to make and what happens next.

## MM-5 Other cards

Each also has an ID, an owner and a card status, like the node.

| Card | Fields |
| --- | --- |
| Artifact | Type and schema (fields, format); source of truth (where the original lives); who creates and who changes it; life cycle (e.g. draft → approved → superseded); versioning and backward compatibility; sensitivity (personal data, secrets) |
| Edge | From → to; artifact; mode (synchronous call, event, schedule, shared state); guarantees (ordering, delivery, idempotency); security if it crosses a boundary (channel, caller identity, permissions checked, validation); contract evolution (how it changes without breaking its users); what happens if it fails |
| State | Content; owner (the only writer, `P13`); readers; concurrency rule if there is more than one writer; persistence and backup; how to roll back |
| Flow | Goal; trigger; nodes and edges (diagram); success condition; error paths; cycles with exit condition and budget; measures (duration, cost, outcome) |
| Constraint | Type (structure, security, quality, process); rule; what it applies to; why, with the evidence; who can change it; how it is enforced (mechanically or only by instruction) |
| Boundary | What it contains; whether it is a trust boundary; what may enter and leave; which dependencies are allowed |
| Environment | Resources and limits; who manages it; which nodes it hosts; where configuration and secrets live |

For a constraint, "how it is enforced" matters more than the rule itself: a rule written only in a prompt is a suggestion; a rule enforced by CI or permissions is a constraint.

A quality constraint is written as a measurable scenario; otherwise "secure" and "scalable" cannot be verified:

| Part | Example |
| --- | --- |
| Quality | Scalability |
| Stimulus | 200 users of the same customer open the order list in the same minute |
| Environment | Production, normal load |
| Expected response | The list opens without errors |
| Measure | 95% of responses under 1 s |
| Verification | Load test in the pipeline, before release |

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

## MM-7 Knowledge hierarchy

vision → adopted standards and templates → decisions (ADR) → specifications → tasks → code

A level wins over those below it. The only exception: an ADR may depart from an adopted standard or template only if it cites it and explains why; without the citation, the standard wins.

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
| CC-13 | Every state with more than one writer has a concurrency rule | Yes |
| CC-14 | Every success condition and every acceptance criterion has at least one verifier that names it | Yes |
| CC-15 | Every external node has a maximum wait time and a fallback | Yes |
| CC-16 | Every verification chain ends in a deterministic check or in a person | Yes |
| CC-17 | Every adopted template is declared; every deviation cites an ADR | Yes |
| CC-18 | The engine declares how it stops, and each of its compute resources has an environment | Yes |
| CC-19 | Every reference to a shared component (standard, template, engine, tool) uses a stable identifier and a pinned version, never a location (`P15`) | Yes |

## MM-9 Example: same card, two levels

A product node and a method node filled in with the same card; the values are illustrative.

| Field | Product: order service | Method: executor |
| --- | --- | --- |
| N1 ID | `orders-service` | `executor` |
| N2 Name | Order service | Executor |
| N3 Type | Component | AI agent |
| N4 Purpose | Records an order and starts the payment | Implements a task and proposes a change |
| N5 Input | `CreateOrder` from the public API, synchronous call; authenticated user | Task from the engine, event; acceptance criteria present |
| N6 Controls | Validation rules; rate limit | Rules for agents; perimeter of allowed files |
| N7 Executor and permissions | The service process; writes only the orders table | A coding agent; writes only on its own branch |
| N8 Determinism | Yes | No |
| N9 Transformation | Validates, saves, emits an event | Writes tests and code |
| N10 State | Writes the orders database | Reads the repo, writes the branch |
| N11 Output | `OrderCreated` to the payment service, event | Proposed change (PR) to the reviewer |
| N12 Verification | Contract tests; error monitoring | Automated tests + independent reviewer + person |
| N13 Errors and limits | `InvalidOrder` to the caller; 3 attempts on the event | After 3 attempts the person decides |
| N14 Measures | Latency, error rate | Duration, cost, attempts |
| N15 Zoom | — | Test-first cycle |
| N16 Owner | Product team | The person (protected area, `MB-6`) |
| N17 Card status | Decided | Hypothesis |
| N18 Contract version | `2.1` | `1.0` |
