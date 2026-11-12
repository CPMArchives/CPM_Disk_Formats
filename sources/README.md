# Initial source inventory

## cpmtools diskdefs

- Repository: https://github.com/lipro-cpm4l/cpmtools
- Branch: `cpm4l/cpmtools-2.21`
- Commit: `e534e20c15973a9559e981efb498a102020e5db7`
- File: `diskdefs`
- Blob SHA: `68cb8f111733674310654a3f19adbdfce9f8fdaa`
- Observed definitions: 131

## LibDsk

- Release: 1.5.22
- Primary built-in geometry table: `lib/dsksgeom.c` (`stdg[]`)
- Sample: `doc/libdskrc.sample`
- Prior inspection: 36 source-table entries, 35 distinct names; 25 sample sections.
- The table includes a duplicate `c64cpm` name with differing parameters, requiring investigation.

Import source text and preserve provenance. Do not treat all LibDsk geometries as CP/M historical formats.
