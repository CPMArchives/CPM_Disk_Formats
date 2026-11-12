# Schema v0.1 notes

The only universally required fields are `id`, `name`, and `status`.

Status: `active`, `provisional`, or `retired`. A retired record requires `retirement.reason`. IDs are permanent and never reused.

The schema distinguishes media geometry, recording, logical layout, filesystem/DPB, and reserved system areas. The source term `tracks` in cpmtools is retained as `logical_layout.tracks` until physical interpretation is independently supported.

Unknown values are omitted. Historical evidence and discrepancies belong in `provenance` and `notes`. No field-by-field citation apparatus is required.

Relations must be recorded in both files. `derived_from` reciprocates with `derived_into`; other relationship names reciprocate with themselves. JSON Schema checks individual files; catalogue-wide checks must verify IDs, filenames, reciprocal links, and retirement targets.

`recording.track_overrides` supports exceptions. Additional per-sector attributes should be introduced only when real source examples require them.

This is a pilot schema, not yet fully validated against representative source records.
