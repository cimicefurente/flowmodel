---
id: MM-1
name: Purpose and use
module: MM
owner: The maintainer (protected area, MB-6)
status: decided
---

## MM-1 Purpose and use

One schema describes both the software and the method that produces it. Both are networks of nodes that transform artifacts, connected by edges, under constraints. The method is a program run by people and AI, whose output is changes to the product.

The schema itself is a node: it takes a project description and the person's answers, and produces the project's cards. Templates (`T`) are its ready-made configurations.

At the start of a project:

1. Give an AI the modules listed in `PA-4`, its system prompt and a description of the project.
2. The AI follows procedure `PA-1`: it asks questions, proposes suitable templates, fills in the cards and marks as hypotheses whatever the person has not decided.
3. The result is a set of cards and five views, kept in the project's repo and updated with the same method they describe.

The schema describes; it does not choose technologies. Any field may stay "to be decided"; no field is invented. Start with a few large nodes and add detail only where it is needed.
