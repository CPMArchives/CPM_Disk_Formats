# Historical format validation

Validation is **independent** of a format record's lifecycle `status` (`active`, `provisional`, `retired`). An accepted record may be unvalidated; a provisional record may have passed some tests.

The optional `validation` mapping contains:

- `validation_status`: `unvalidated`, `partially_validated`, `validated`, `failed`, or `blocked`.
- `validation_remaining`: specific outstanding checks.
- `validation_evidence`: references to independent images, documentation, inspection reports, and test results, each with a result and evidence kind.
- `validation_notes`: discrepancies, limitations, and scope.

**Missing `validation` means no validation assessment has been recorded**, not that testing failed or that the definition is historically invalid. Do not automatically mark all imported formats unvalidated; preserve the difference between no assessment and an explicit assessment.

## Evidence standard

An independently sourced authentic historical disk image is a strong practical basis for validation when provenance is credible. Preserve the original image and its SHA-256 in the separate image reference library, when one exists. The format record links to that image or an evidence report rather than duplicating image metadata.

For ordinary CP/M filesystem formats, a typical validation pass checks:

1. Historical identity and image provenance independently of the diskdef being tested.
2. Observable physical geometry, recording and sector IDs, where the image/container permits inspection.
3. Directory interpretation using cpmtools with the candidate definition.
4. Extraction of files, with plausible contents and internal filesystem consistency.
5. Historical documentation or independent evidence where available.
6. Outstanding ambiguities, including parameters that the test image did not exercise.

Successful listing alone is not sufficient. Successful extraction does not prove every DPB parameter, physical track traversal, or historical identity. An image produced with the very definition under test is useful for regression testing but is **not** independent evidence of historical correctness. An image container may omit physical recording details; do not claim geometry was observed when it was only supplied as an access assumption.

Original hardware testing is valuable but not mandatory. Some unusual formats will require a different evidence standard; document the scope and rationale rather than claiming a universal checklist proves all formats.

## Status interpretation

| Status | Meaning |
|---|---|
| `unvalidated` | An assessment explicitly found no substantive validation completed |
| `partially_validated` | Some evidence supports the definition, but material checks remain |
| `validated` | Sufficient independent evidence supports the **specified scope** of the format, with no material unresolved discrepancy |
| `failed` | A recorded validation test failed; this is **not** proof that the definition is incorrect |
| `blocked` | Further validation cannot currently proceed because evidence or tooling is missing |

A failure can result from a damaged image, tool bug, incompatible container interpretation, or an incorrect definition. Record the actual failure and investigate. A later passing test should not erase important contrary evidence.

## Example — hypothetical, not a test result

```yaml
validation:
  validation_status: partially_validated
  validation_remaining:
    - Verify multi-extent extraction against an independent image
  validation_evidence:
    - kind: historical_image
      reference: "example-library:kaypro-ii-system"
      result: informational
      description: "Hypothetical independent Kaypro II image"
    - kind: filesystem_test
      reference: "reports/example-kaypro-extraction.txt"
      result: pass
      tool: cpmtools
      notes: "Illustrative only; no actual test was run"
  validation_notes: "Example only. Do not copy these outcomes into a real record."
```

## Reference-image collection

The proposed separate image library (working name `CPMDiskImages`) has **not** been approved or created. Its eventual image records should own container type, file hash, acquisition source, redistribution status, and image-specific test details. The format database owns the historical validation assessment and links to those evidence records.

The image library should preserve authentic files unchanged and use disposable copies for writes. It may catalogue restricted images by reference and checksum without hosting their bytes. Image containers (RAW, IMD, DMK, CPCEMU DSK) are not disk-format identities in this database.

## First candidate

The Kaypro II `kaypro1.imd` mentioned in the project discussion is a **lead**, not a verified fixture. Do not mark `kpii` validated before obtaining and inspecting the image and recording actual extraction evidence.
