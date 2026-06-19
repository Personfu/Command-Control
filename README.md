# Command-Control

> FLLC adversary-emulation and command-and-control literacy workspace for scoped labs, detection engineering, and exploit-intelligence education.

## Portfolio role

This repository is no longer positioned as a raw link dump for C2 tooling. It should become a **controlled emulation and detection design notebook** for offensive security learning, bug bounty context, and blue-team validation.

The offensive angle is valid when scoped:

- understand C2 concepts;
- model beacon patterns;
- build toy telemetry;
- write detections;
- validate blue-team controls;
- support authorized red-team planning.

## What belongs here

- C2 concept notes.
- Beacon telemetry models.
- Synthetic NetFlow examples.
- Detection engineering notes.
- Red-team planning templates for authorized work.
- Report templates and evidence handling.

## What does not belong here

- live C2 deployment instructions;
- persistence or stealth recipes;
- evasion chains;
- third-party targeting;
- credential theft workflows;
- operational attack infrastructure.

## Planned structure

```text
docs/
  emulation-concepts.md
  beacon-telemetry-model.md
  detection-engineering.md
  report-template.md
labs/
  toy-beacon-simulator/
  synthetic-netflow/
  sigma-ideas/
data/
  synthetic-events.example.json
```

## FLLC integration

Feature as:

- `C2 Beacon Literacy Lab`.
- `Synthetic NetFlow Detector`.
- `Adversary Emulation Notes`.
- `Detection Engineering Workbook`.

## Bug-hunter / red-team report template

```text
Engagement:
Written authorization:
Emulation objective:
Toy or lab infrastructure:
Telemetry collected:
Detection hypothesis:
Observed result:
Control gap:
Recommended fix:
Cleanup completed:
```

## Public boundary

Public work should use toy telemetry and synthetic event streams. Authorized engagements require written scope. Offensive does not mean sloppy; the value is translating adversary behavior into evidence, detections, and remediation.
