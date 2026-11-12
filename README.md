# CP/M Disk Formats Database

An open, application-independent reference of historical CP/M disk formats.

## Scope

The database records physical media and recording characteristics, logical organization, CP/M filesystem parameters, system/boot areas, compatibility, historical identity, and provenance. Disk-image container formats and individual disk damage are outside its primary scope.

## Storage

- `formats/NNNN.yaml`: authoritative YAML 1.2 records, one per permanent numeric ID.
- `schema/format.schema.json`: initial record schema (Draft 2020-12).
- SQLite will be generated from YAML, not edited independently.
- Format ID 0001 is reserved for IBM 3740.
- Missing technical information is permitted; do not invent values.
- Relationships are reciprocal and validated at catalogue level.

## Status

Schema v0.1 pilot on development branch; not yet a complete or historically verified catalogue.

## Sources

Initial sources: cpmtools `diskdefs` and LibDsk 1.5.22 built-in geometry table. Source definitions are evidence, not necessarily complete historical specifications.

See `docs/schema-notes.md` and `sources/README.md`.
