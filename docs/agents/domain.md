# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- **`GLOSSARY-MAP.md`** at the repo root: it points at one `GLOSSARY.md` per context. Read each one relevant to the topic.
- **`docs/adr/`**: system-wide decisions. Read ADRs that touch the area you're about to work in.
- **`engine/docs/adr/`**: decisions scoped to the engine context. Check it when the topic touches `engine/`.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs`) creates them lazily when terms or decisions actually get resolved.

## File structure

Multi-context repo (`GLOSSARY-MAP.md` at the root), with two contexts:

```
/
├── GLOSSARY-MAP.md
├── docs/adr/                 ← system-wide decisions
├── standard/
│   └── GLOSSARY.md           ← Standard context
└── engine/
    ├── GLOSSARY.md           ← Engine context
    └── docs/adr/             ← engine decisions
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in the relevant `GLOSSARY.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-NNNN (<title>), but worth reopening because…_
