# Cards are YAML files validated by JSON Schema; views are generated

The engine and agents must read cards as data, not parse prose. Each card is one YAML file, validated by the JSON Schema 2020-12 that the standard publishes for its kind; keys are field names, not field numbers, so reordering a card's fields does not break existing cards. Prose such as rationale and examples lives in text fields of the schema, so nothing in a card escapes validation. Views (`MM-6`) are generated from the cards and checked by CI, never written by hand. This departs from `PA-5`, which keeps cards as Markdown files: Markdown tables have no schema and no program can read them reliably; `PA-5` is to be updated to match (`MM-7`).

## Consequences

- The schemas are the whole interface between the standard and the engine (ADR-0001): the engine embeds the schemas of the standard versions it supports, copied from a released tag, and CI checks that the copies match the tag.
- The Mermaid source of `MB-2` becomes a view generated from the method template's cards.

## Considered options

- Markdown cards read by a parser: easier to read by hand, but the format has no schema and every layout change breaks the parser.
