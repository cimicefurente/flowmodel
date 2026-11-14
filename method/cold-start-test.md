# Cold-start test

The rubric of the verifier node `cold-start-test` (its card is `cold-start-test.yaml`): a fresh companion session must rebuild the working state from what the `companion` card declares alone. The rubric is fixed; a change to it is a change to the protected area (ADR-0010).

## How it runs

1. The running companion writes the handoff (`companion-handoff`).
2. It builds the answer key. The key of CS-1 and CS-2 comes from the ground truth read when the handoff is written: the actual list of worktrees with their uncommitted and unpushed work, and the agents and processes actually running. It is fixed then, because running agents keep changing that state while the test runs. It never comes from the handoff. The key of CS-3 to CS-7 comes from the tracker.
3. It starts a fresh session on the fixed model, with no earlier conversation and no memory. The session gets only what the `companion` card declares: its input (N6, the handoff), its constraints (N14, `AGENTS.md`), its context (N15, `prompts/companion.md` and the IDs it loads) and its state (N17, the tracker). It does not see the key, does not list worktrees, agents or processes itself, asks the maintainer nothing and changes nothing.
4. The fresh session answers every item, citing for each answer the input it comes from and the issue or PR numbers.
5. The running companion scores each answer against the key and shows the maintainer the key, the answers and the score.
6. Only after the maintainer confirms the key and the score, the line is appended to `cold-start-log.md`. The log is the only place for the result.

The model is fixed: every run uses the same model, recorded in the log. Changing it is the maintainer's decision.

## Tracker markers

The tracker records decisions and questions with two markers at the start of a comment:

- `**Decided (maintainer, <date>)**`: a decision, with its date in ISO 8601.
- `**Open question for the maintainer**`: one or more questions; each numbered item is one question.

A question is answered when a later comment on the same issue or PR, marked `**Decided (maintainer, <date>)**`, names it (by its number or its words). Every other question under the second marker is open.

## Items

Each element has exactly one state: the first in the listed order that applies.

| ID | What the fresh session must state | States, in order of precedence |
| --- | --- | --- |
| CS-1 | Every running agent or process: its ID, its ticket, its worktree, the branch or PR where its result will land, and its state | `waiting for the maintainer`; `waiting for another agent or process`; `running` |
| CS-2 | Every local worktree other than the main checkout: its path, its branch, its ticket or PR, and its state | `uncommitted work`; `unpushed commits`; `PR open`; `merged` (removable); `clean` (pushed, no open PR, not merged) |
| CS-3 | Every open issue that a running agent, a local worktree, an open PR or an open question refers to, and its state | `waiting for the maintainer` (an open question on it, or a PR of it in that state in CS-4); `PR in progress` (a PR of it in any other state of CS-4); `agent running`; `idle` (only a worktree) |
| CS-4 | Every open PR, with the issue it refers to ("Refs #N") and its state | `draft`; `checks failing`; `checks pending`; `waiting for a reviewer` (a review was requested and not posted); `waiting for the maintainer` |
| CS-5 | Every open question (see the markers above), with its issue or PR, and which one to ask next | - |
| CS-6 | Every decision marked `**Decided (maintainer, <date>)**` on the issues of CS-3 and the PRs of CS-4, cited by issue or PR number | - |
| CS-7 | The next action, and whether a new agent may start now (the limit is in the companion's Output, N7) | - |
| CS-8 | Nothing invented: no issue, PR, agent, process, worktree, question or decision that the key does not hold | - |

## Scoring

- Each item is pass or fail; there is no partial credit.
- CS-1 to CS-6 pass when the answer names exactly the elements of the key, with the same numbers, identifiers and state; the wording may differ. A missing or extra element, or a wrong state, fails the item. When the key is empty, "none" passes.
- The next question of CS-5 and the next action of CS-7 pass when they are in the list the key accepts.
- CS-8 passes when no answer holds an element absent from the key.
- An answer that cites no input fails.
- The score is the number of items passed out of 8. The result is `pass` only at 8/8; otherwise `fail`, and the failed items go back to the handoff or to this rubric, as the edge's failure path says.

## Log format

One line per run, appended at the end of `cold-start-log.md` and never edited (`P9`). The line is a row of the table in that file:

| Column | Content |
| --- | --- |
| Date | When the maintainer confirmed the score, ISO 8601 in UTC, e.g. `2026-11-14T16:05Z` |
| Model | The exact model ID of the fresh session |
| Rubric | The short commit of the last change to this file |
| Main | The short commit of main the inputs were read at |
| Score | Items passed out of 8, e.g. `7/8` |
| Result | `pass` or `fail` |
| Failed | The failed item IDs, comma-separated, or `-` |
| Ref | The issue or PR the run was made for, e.g. `#34` |
