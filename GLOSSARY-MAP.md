# Glossary Map

## Contexts

- [Standard](./standard/GLOSSARY.md): the flow model, which describes a product and the method that builds it; every entry points to the module ID that defines the term
- [Engine](./engine/GLOSSARY.md): the reference engine (`MB-5`), which runs a project's method cards

## Relationships

- **Standard → Engine**: the engine reads the standard only through the card schemas (ADR-0001); engine entries cite standard terms by ID and never redefine them (`P1`)
- **Standard ↔ Engine**: shared terms (engine, controller, executor, decision point) are defined only in the standard; the engine glossary adds only what the engine adds to them
