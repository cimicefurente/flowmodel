---
id: MM-2
name: Sources
module: MM
owner: The maintainer (protected area, MB-6)
status: decided
---

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
