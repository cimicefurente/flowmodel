# Engine

The reference engine (`MB-5`): the program that runs a project's method cards. Terms of the standard are cited by module ID and never redefined here (`P1`); each entry below defines only what the engine adds.

## Language

### Running the method

**Slice**:
One issue carried through Decision, Specification and Breakdown of `MB-2`, then through Execution, Verification and Integration for each of its tasks, and closed by a Retrospective once all its tasks are integrated. It is the unit of work of one pass through the cycle (`MB-3`).
_Avoid_: Feature, epic, iteration

**Frontier**:
The set of tasks and steps that are ready to start now: their inputs exist and nothing they wait for is still open. The engine runs until the frontier is empty or only decision points (`MB-4`) remain.
_Avoid_: Backlog, ready list

**Executor**:
The executor of a node as declared in its card (`MM-4`), seen from the engine: a process started from a command template, with an assembled prompt, its own working copy and branch, and only the capabilities granted to it. It ends by writing an outcome file.
_Avoid_: Worker, runner

**Capability**:
A named platform permission that a node declares in its card (`MM-4`) and that the engine grants as a credential scoped to one run; a node has none by default (`P5`). It is not a capability of a compute resource (`MB-5`).
_Avoid_: Scope, grant, token

**Outcome file**:
The file an executor writes at the end of a run, validated by a schema: a status (`done`, `blocked` or `question`), a summary, and optionally a question in the form of `MB-4` and a cost. It is the only thing the controller (`MB-5`) reads from a run, which keeps the controller deterministic.
_Avoid_: Result, report, exit status

### State and channel

**Run log**:
The append-only log of events of a project's runs, kept in the working copy and written only by the engine (`P13`). The current state is rebuilt from it and every measure is computed from it.
_Avoid_: Event log, history, journal

**Inbox**:
The queue of open questions to the person, each with options, a recommendation and evidence; it is the engine's channel to the person (`MB-5`), and each answer is recorded in the run log as a decision (`P9`).
_Avoid_: Notifications, question queue

### Platform interfaces

**Tracker**:
The interface through which the engine lists the frontier, changes the state of a task and comments on it. A project chooses its adapter independently of the change host.
_Avoid_: Board, issue system

**Change host**:
The interface through which the engine proposes a change, reads its verification outcome and merges it. A project chooses its adapter independently of the tracker.
_Avoid_: Forge, code host, git platform

**Integration queue**:
The serial queue of verified changes waiting for Integration (`MB-2`): one at a time, each change is rebased on the latest main, verified again, then merged.
_Avoid_: Merge queue, merge train
