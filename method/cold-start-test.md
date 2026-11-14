# Cold-start test

ID: `cold-start-test`. The verifier of the edge `companion-to-companion` (`P3`): a fresh companion session must rebuild the working state from the declared inputs of the `companion` node (N6) alone. The rubric below is fixed; a change to it is a change to the protected area (`MB-6`).

## When it runs

- Once when it is introduced (#34).
- At the test threshold in the companion's Errors and limits (N12).
- Whenever the parts of `companion-handoff` or this rubric change.

## How it runs

1. The running companion writes the handoff (`companion-handoff`) and, apart from it, the answer key: its own answer to each item below.
2. It starts a fresh session on the fixed model: no earlier conversation and no memory, with the prompt `prompts/companion.md` and only the declared inputs: `AGENTS.md`, the tracker and the handoff. The fresh session does not see the answer key, does not list worktrees or agents itself, asks the maintainer nothing and changes nothing.
3. The fresh session answers every item, citing for each answer the input it comes from and the issue or PR numbers.
4. The running companion scores each answer against the key, appends one line to the log (`method/cold-start-log.md`) and posts the handoff, the key, the answers and the line as one comment on the issue or PR named in the line.

The model is fixed: every run uses the same model, recorded in the log. Changing it is the maintainer's decision.

## Items

| ID | What the fresh session must state | Comes from |
| --- | --- | --- |
| CS-1 | The running executors: for each, the ticket number, the agent's ID, the worktree, the branch and what it is doing or waiting for | Handoff |
| CS-2 | The local worktrees: for each, the path, the branch, the ticket or PR number and whether it can be removed | Handoff |
| CS-3 | The open tickets being worked on, each with its state: not started, executor running, PR open, waiting for the maintainer | Tracker, handoff |
| CS-4 | The open PRs waiting for the maintainer, each with its ticket | Tracker |
| CS-5 | The open questions to the maintainer, each with its ticket, and which one to ask next | Tracker |
| CS-6 | The decisions recorded on the open tickets, each cited by issue or PR number | Tracker |
| CS-7 | The next action, and whether a new executor may start now (at most three at once) | All |
| CS-8 | Nothing invented: no ticket, PR, executor, worktree, question or decision that the key does not hold | All |

## Scoring

- Each item is pass or fail; there is no partial credit.
- CS-1 to CS-6 pass when the answer names exactly the elements of the key, with the same numbers and identifiers and the same state; the wording may differ. A missing or extra element fails the item. When the key is empty, "none" passes.
- CS-7 passes when the action is one of the actions the key accepts.
- CS-8 passes when no answer holds an element absent from the key.
- An answer that cites no input fails.
- The score is the number of items passed out of 8. The result is `pass` only at 8/8; otherwise `fail`, and the failed items go back to the handoff or to this rubric, as the edge's failure path says.

## Log format

One line per run, appended at the end of `method/cold-start-log.md` and never edited (`P9`). The line is a row of the table in that file:

| Column | Content |
| --- | --- |
| Date | When the run ended, ISO 8601 in UTC, e.g. `2026-11-14T16:05Z` |
| Model | The exact model ID of the fresh session |
| Rubric | The short commit of the last change to this file |
| Main | The short commit of main the inputs were read at |
| Score | Items passed out of 8, e.g. `7/8` |
| Result | `pass` or `fail` |
| Failed | The failed item IDs, comma-separated, or `-` |
| Ref | The issue or PR where the run's comment is posted, e.g. `#34` |
