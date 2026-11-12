# System prompts list module IDs; the text is assembled at use

Each role's system prompt in `prompts/` contains only its instructions and the list of module IDs it loads (`PA-4`). The full text is assembled at the time of use, by the engine or by hand, so no module is ever copied into a prompt (`P1`). The short form of `P` is derived from `P-principles.md` in the same way.

## Considered options

- Self-contained prompts with the modules pasted in: easier to use by hand, but they drift from the modules.
