# RockyBorg — Interdisciplinary Project

Collaborative repository for the RockyBorg Raspberry Pi robotics project.

## Project status

**Architecture decision pending:** the team is evaluating ROS 2, ROS 1, and a standalone Python implementation. No framework is assumed by the folder layout.

## Repository layout

- `docs/` — requirements, architecture, decisions, and setup guides
- `research/` — technology comparisons, benchmarks, references
- `hardware/` — parts inventory, wiring, sensor and Raspberry Pi documentation
- `src/` — implementation code (structure to be decided)
- `tests/` — experiments and tests
- `dashboard/` — dashboard prototypes and Node-RED flows, if selected
- `meetings/` — meeting notes and action items
- `reports/` — presentations, milestones, final report

## Collaboration


## Next decisions

1. Confirm Raspberry Pi model and memory capacity.
2. Inventory sensors and hardware interfaces.
3. Compare ROS 2 vs ROS 1 vs classical Python, including maintainability, CPU/RAM overhead, and project fit.
4. Record the chosen stack in `docs/architecture-decision.md` before reorganizing `src/`.
