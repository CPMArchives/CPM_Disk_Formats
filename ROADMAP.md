# Roadmap / Deferred Work

This document tracks future work without committing to a particular schema or implementation.

## Manufacturer-supported floppy hardware catalogue

**Status:** Deferred — research and design not started.

Investigate how the CP/M Disk Formats Database should record **manufacturer-official floppy hardware configurations** and associate them with historical disk formats. Scope includes factory-shipped equipment and manufacturer-supported drives, controllers, and upgrades; aftermarket and homebrew configurations are out of scope for this catalogue.

The catalogue could span dozens of manufacturers and over a hundred configurations. Treat it as a substantial historical research and verification project, not a small metadata addition.

Before changing the schema:

- Review existing historical-identity, compatibility, and provenance fields to avoid duplicating information.
- Determine how to represent manufacturers, computer models, official hardware configurations, physical disk formats, and the potentially many-to-many relationships among them.
- Require documentary provenance for each hardware association; do not infer a unique drive or controller from a disk definition or capacity alone.
- Preserve the database's application-independent role and its YAML-authoritative / generated-SQLite architecture.

**Potential consumer:** CP/M Image Workbench, for selecting or deriving physical parameters when creating/recreating IMD images and for assessing compatibility with historically supported hardware. Distinguish the intended target hardware from the imaging hardware used to reproduce a disk.

**Deliverable when resumed:** A reviewed data-model proposal and a small source-backed pilot covering a few manufacturer-supported configurations. No schema change, bulk research, or Workbench implementation is authorized by this TODO.
