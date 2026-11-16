# 22DISK source integration — initial cross-reference

## Scope and source identity

This is an initial, **non-exhaustive** cross-reference, not a comparison against Sydex's original 187-entry indexed `CPMDISKS.DEF`. The primary Sydex 22DISK 1.44 archive was identified at https://files.mpoli.fi/pub/software/DOS/UTILS/DISKFILE/22DSK144.ZIP but could not be retrieved in the current environment. The 187-entry count is recorded in BetterCPM's historical research; a separate archive description advertises over 400 formats for 1.44, which needs edition/registration reconciliation.

A readable, derivative 22DISK-language file was verified at https://github.com/hww/Aleste520EX/blob/6aac5a781fbe8b17fab9fcd27d2259adc86abf2a/Tools/cpcxfs/cpmdisks.def . It identifies itself as a CPCXFS compilation by Frederic Herlem (24 October 2000), with later ZX Spectrum additions. **It must not be attributed to the original Sydex release.** This derivative contains 44 BEGIN definitions.

The comparison target is the pinned cpmtools `diskdefs` at `sources/cpmtools-diskdefs-e534e20.txt` (131 named entries).

## Initial result

A screening comparison of sector length, sectors/track, allocation block size, directory entries, reserved tracks, and total tracks yielded **8 parameter-compatible source definitions** and **36 without a match** among the 44 CPCXFS entries. These are not confirmed historical equivalences or unique new formats.

| CPCXFS tag | Historical label | cpmtools parameter-compatible candidates |
|---|---|---|
| DA1A | CPC-STD 178K Data | `cpcdata` |
| SY1A | CPC-STD 169K System | `cpcsys`, `vt180` |
| IB1A | CPC-STD 154K IBM CP/M-86 | `ibm-8ss`, `ibm-8ds`, `ibmpc-514ss` |
| PC1A | PCW-STD 173K | `pcw` |
| DXT4 | DiskPara3 796K | `trsn` |
| RD10 | RAMDOS-D10 796K | `trsn` |
| PCW3 | Amstrad PCW DSDD 720K | `cf2dd` |
| ZX0 | ZX Spectrum +3 SSDD 180K | `pcw` |

The remaining 36 CPCXFS definitions lack a match under this narrow parameter comparison, but may be physical-side variants, alternative layout representations, or genuinely additional formats. **Do not infer 36 new formats.** In particular, side-specific CPC entries cannot be collapsed merely because their other parameters resemble a single-sided cpmtools definition.

## Next required steps

1. Acquire and fingerprint the actual Sydex 22DISK 1.44 archive and its indexed `CPMDISKS.DEF`. Use the supplied `STRIPIDX` or a verified parser to recover records, preserving original identifiers, exact parameters, and edition.
2. Resolve the discrepancy between the previously recorded 187-entry count and the archived distribution's over-400-format description.
3. Compare the recovered primary corpus against all cpmtools records, classifying historical physical floppies separately from emulator-only and non-floppy entries.
4. Match complete filesystem/DPB and physical characteristics (including per-side sector ID sequences, traversal, and density), not names or capacities alone.
5. Then cross-reference against Montezuma and the authoritative database YAML; preserve conflicting evidence, do not automatically merge identities or allocate IDs.

No canonical database records have been created or changed by this preliminary survey.
