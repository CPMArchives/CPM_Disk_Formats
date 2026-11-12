# cpmtools import review — 2026-11-12

## Automated validation

GitHub Actions run 43178212549 passed the existing schema and negative tests. This is structural validation only.

## Source inventory

The pinned `diskdefs` snapshot contains 131 distinct `diskdef` headers, but only 130 active `end` directives. The `trsi` definition has `#end` before the next header (`trsj`), so the original source is not a clean sequence of 131 terminated definitions. The importer deliberately split at the next `diskdef` header. Do not claim all 131 are accepted by cpmtools itself without checking its parser.

Four existing pilot records were retained; 127 new provisional records were added.

## Exceptional directives

- Seven records use `skewtab` (apple-do, apple-po, attwp, microbee40, dreamdisk40, dreamdisk80, icl-comet-525ss).
- Three use `logicalextents` (nigdos, attwp, vt180).
- Twelve use `offset` (gide-cfb, trse, trsf, trs5, memotech-type19 through memotech-type1F, com8).
- `trse` and `all1` use `datarate` / `fm` or `FM`; `trsf` and `all1` use `sides`.
- `trsi` has no active terminating `end`.

These values are retained in provenance notes rather than discarded, but are not yet represented as typed fields.

## Semantic issue requiring decision

**cpmtools `seclen` and `sectrk` are parameters of its logical filesystem image access.** The import currently puts them in `recording.bytes_per_sector` and `recording.sectors_per_track`, whose section name implies physical on-disk recording. This is not justified for every entry, especially formats with logical sector transformations. The pilot records already used the same mapping.

Before merging, introduce an explicit logical-sector representation or otherwise correct the field semantics, then regenerate the imported records and rerun CI. Avoid inferring physical sector size or sector count solely from these cpmtools fields.

Likewise, `skew` and `skewtab` must remain identified as cpmtools logical mapping parameters, not presumed physical interleave.

## Recommendation

Keep PR #5 in draft pending the logical-versus-physical sector field correction and a source-mapping audit. Do not merge merely because JSON Schema validation is green.

## Resolution of logical-sector mapping

Schema v0.1 now permits `logical_layout.bytes_per_sector` and `logical_layout.sectors_per_track`. All 131 imported/pilot records now include these source-derived logical values. The 127 new imports and the two pilot records without independent physical evidence omit `recording` geometry. PCW 180K and CP/M-86 144FEAT retain separately verified LibDsk physical geometry. This resolves the logical/physical field conflation; remaining source-exception interpretation is tracked above.
