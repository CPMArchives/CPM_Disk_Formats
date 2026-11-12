# Montezuma Micro versus cpmtools diskdefs — preliminary cross-reference

Comparison date: 2026-11-12. This is a **source-field screening audit**, not a claim of disk interchangeability or historical identity.

## Sources

- BetterCPM external catalogue: [DISK.FDF](https://github.com/CPMArchives/BetterCPM/blob/main/third_party/montezuma/DISK.FDF) (96 definitions; blob `9b520eb0f165affe519d22be6a926dd7204e6959`)
- BetterCPM internal catalogue: [DISK-INT.FDF](https://github.com/CPMArchives/BetterCPM/blob/main/third_party/montezuma/DISK-INT.FDF) (16 definitions; blob `9cde9144de5cc11e3f3a2f6cf07e9d0db1e43f19`)
- BetterCPM decoded migration: [metadata/DISK.FDF](https://github.com/CPMArchives/BetterCPM/blob/main/metadata/DISK.FDF) (107 admitted definitions; five external records excluded)
- cpmtools: [pinned diskdefs snapshot](../sources/cpmtools-diskdefs-e534e20.txt) (131 named definitions; upstream commit `e534e20c15973a9559e981efb498a102020e5db7`)

## Results

- **112** Montezuma source definitions examined.
- **43** have at least one cpmtools entry matching the compared logical geometry and allocation fields.
- **69** have no such candidate.
- **0 confirmed physically identical formats**: cpmtools alone generally does not establish the physical sector-ID order, and matching the tested fields is not sufficient.
- Of the 96 external Montezuma records, **five** are absent from BetterCPM's admitted decoded metadata: `MMF003`, `MMF031`, `MMF064`, `MMF071`, `MMF087`. They remain in the original external source and in this audit.

### Matching method and limits

For each Montezuma record, compare `SPT` (in 128-byte records), allocation block size derived from `BSH`, `DRM+1`, `OFF`, physical-sector size derived from its size code, sectors per track, and logical track count estimated as cylinders × sides. Against cpmtools compare `sectrk * seclen / 128`, `blocksize`, `maxdir`, `boottrk`, `seclen`, `sectrk`, and `tracks`. Montezuma's final machine-specific geometry byte is interpreted as single-sided for values below 192 and double-sided for 192 and above, following BetterCPM's decoded migration.

**This comparison does not test** explicit sector-ID order, track traversal, physical recording mode, all DPB parameters (including DSM), boot-sector contents, or hardware behavior. A matching row is a *candidate*, never an automatic merge or an `equivalent` relationship. A row with no match is *not demonstrated absent* from cpmtools under another layout representation; it lacks a match under these criteria.

## Full 112-entry cross-reference

| MM ID | Historical format | Result | cpmtools candidates |
|---|---|---|---|
| MMF001 | Access Matrix (40T, SS, DD, 171K) | Parameter-compatible candidate | `cpcsys`, `vt180` |
| MMF002 | Access Matrix (40T, DS, DD, 350K) | No matching parameter set | — |
| MMF003 | Acorn (80T, SS, SD, 392K) | No matching parameter set | — |
| MMF004 | Adler Textriter Series III (40T, SS, DD, 160K) | No matching parameter set | — |
| MMF005 | Altertext Diskreader (40T, SS, DD, 144K) | No matching parameter set | — |
| MMF006 | Ampro Little Board (40T, SS, DD, 190K) | Parameter-compatible candidate | `amp1` |
| MMF007 | Ampro Little Board (40T, DS, DD, 390K) | Parameter-compatible candidate | `v1050`, `microbee40`, `dreamdisk40`, `dec_pro`, `trsp`, `trsq`, `amp2`, `ampro400d` |
| MMF008 | AOS/VT Basic 4 S-10 (80T, DS, DD, 626K) | No matching parameter set | — |
| MMF009 | Archives Model III (80T, DS, DD, 790K) | No matching parameter set | — |
| MMF010 | ATR-8000 512 byte sector (40T, SS, DD, 190K) | Parameter-compatible candidate | `icl-comet-525ss` |
| MMF011 | ATR-8000 1024 byte sector (40T, SS, DD, 190K) | No matching parameter set | — |
| MMF012 | Aust. Comp. & Telecomm. (40T, SS, DD, 171K) | No matching parameter set | — |
| MMF013 | AVATAR TC1 Terminal Converter (40T, SS, DD, 184K) | No matching parameter set | — |
| MMF014 | AVATAR TC1 Terminal Converter (40T, DS, DD, 384K) | No matching parameter set | — |
| MMF015 | BMC if800/20 (40T, DS, DD, 384K) | No matching parameter set | — |
| MMF016 | Bondwell Model 12 (40T, SS, DD, 170K) | Parameter-compatible candidate | `trsg` |
| MMF017 | California Computer Systems (40T, DS, DD, 332K) | No matching parameter set | — |
| MMF018 | Cifer 2683 (40T, DS, DD, 384K) | No matching parameter set | — |
| MMF019 | Columbia 964 (40T, SS, DD, 190K) | No matching parameter set | — |
| MMF020 | Compustar Model 30 (35T, DS, DD, 340K, *) | Parameter-compatible candidate | `nsfd`, `mdsad350` |
| MMF021 | Computer Operation NCHQ (40T, SS, SD, 82K) | No matching parameter set | — |
| MMF022 | Cromemco Z-2 (40T, SS, SD, 82K) | No matching parameter set | — |
| MMF023 | Cromemco Z-2 (40T, SS, DD, 190K) | No matching parameter set | — |
| MMF024 | DEC Rainbow 100+ (80T, SS, DD, 390K) | Parameter-compatible candidate | `v1050`, `microbee40`, `dreamdisk40`, `dec_pro`, `trsp`, `trsq`, `amp2`, `ampro400d` |
| MMF025 | DEC RX50K (80T, SS, DD, 390K) | Parameter-compatible candidate | `v1050`, `microbee40`, `dreamdisk40`, `dec_pro`, `trsp`, `trsq`, `amp2`, `ampro400d` |
| MMF026 | DEC VT-180 (40T, SS, DD, 171K) | Parameter-compatible candidate | `cpcsys`, `vt180` |
| MMF027 | Dictaphone 6000 CP/M Rev. A (80T, DS, DD, 692K) | No matching parameter set | — |
| MMF028 | Dictaphone 6000 CP/M v. 2.26 (80T, DS, DD, 706K) | No matching parameter set | — |
| MMF029 | Digital Research 8" CP/M Standard (77T, SS, SD, 243K) | Parameter-compatible candidate | `ibm-3740`, `zen9`, `mds-sd` |
| MMF030 | Digital Research 8" CP/M Standard (77T, DS, DD, 988K) | No matching parameter set | — |
| MMF031 | Eagle (80T, SS, DD, 390K) | No matching parameter set | — |
| MMF032 | Eagle (80T, DS, DD, 790K, *) | No matching parameter set | — |
| MMF033 | ECB Bus (80T, DS, DD, 760K, *) | No matching parameter set | — |
| MMF034 | Epson QX-10 (40T, DS, DD, 380K) | No matching parameter set | — |
| MMF035 | Epson QX-10 MF (40T, DS, DD, 280K) | No matching parameter set | — |
| MMF036 | Heath H8 with Trionyx H-C8 controller (40T, DS, DD, 390K) | No matching parameter set | — |
| MMF037 | Hewlett-Packard HP-125 (40T, DS, DD, 252K) | No matching parameter set | — |
| MMF038 | Hewlett-Packard HP-87XM (35T, DS, DD, 244K) | No matching parameter set | — |
| MMF039 | Holmes Engineering VID80 (40T, SS, DD, 195K) | Parameter-compatible candidate | `kpii` |
| MMF040 | Hurricane Labs Inc. Compactor I & II (40T, SS, DD, 190K) | Parameter-compatible candidate | `morsddd` |
| MMF041 | IBM PC using CP/M 86 (40T, SS, DD, 156K) | Parameter-compatible candidate | `ibm-8ss`, `ibm-8ds`, `ibmpc-514ss` |
| MMF042 | IBM PC using CP/M 86 (40T, DS, DD, 316K, *) | No matching parameter set | — |
| MMF043 | Intertec Superbrain (35T, SS, DD, 164K) | No matching parameter set | — |
| MMF044 | Intertec Superbrain (35T, DS, DD, 340K, *) | Parameter-compatible candidate | `nsfd`, `mdsad350` |
| MMF045 | Kaypro 2 (40T, SS, DD, 195K) | Parameter-compatible candidate | `kpii` |
| MMF046 | Kaypro 2X, 4, & 10 (40T, DS, DD, 392K) | Parameter-compatible candidate | `kpiv` |
| MMF047 | Lifeboat TRS-80 Mod 1 (40T, SS, SD, 72K) | Parameter-compatible candidate | `trsomsssd` |
| MMF048 | LNW Research LNW80 (40T, SS, DD, 166K) | No matching parameter set | — |
| MMF049 | Lobo MAX-80 (40T, SS, DD, 166K) | No matching parameter set | — |
| MMF050 | Lobo MAX-80 (40T, DS, DD, 346K) | No matching parameter set | — |
| MMF051 | Lobo MAX-80 CP/M 3.0 (40T, SS, DD, 185K) | No matching parameter set | — |
| MMF052 | Lobo MAX-80 CP/M 3.0 (40T, DS, DD, 384K) | No matching parameter set | — |
| MMF053 | Memory Merchant Shuffle Board (40T, SS, DD, 190K) | Parameter-compatible candidate | `trso` |
| MMF054 | Micro-Abacus (80T, DS, DD, 624K) | No matching parameter set | — |
| MMF055 | Monroe OC 8820 (40T, DS, DD, 308K) | No matching parameter set | — |
| MMF056 | Monroe OC 8820 (80T, SS, DD, 308K) | No matching parameter set | — |
| MMF057 | Morrow Micro Decision (40T, SS, DD, 190K) | Parameter-compatible candidate | `morsddd` |
| MMF058 | Morrow Micro Decision MD3 (40T, DS, DD, 390K) | No matching parameter set | — |
| MMF059 | NCR Decision Mate V (40T, DS, DD, 308K, *) | No matching parameter set | — |
| MMF060 | NEC PC-8001A (40T, SS, DD, 148K) | No matching parameter set | — |
| MMF061 | Octagon 8/16 CP/M-86 (40T, SS, DD, 156K) | No matching parameter set | — |
| MMF062 | Octagon 8/16 CP/M-86 (40T, DS, DD, 316K) | No matching parameter set | — |
| MMF063 | Omikron Mapper I, Model 1 & 3 (40T, SS, SD, 83K) | No matching parameter set | — |
| MMF064 | Omikron Mapper II (40T, SS, DD, 134K) | No matching parameter set | — |
| MMF065 | Omikron Mapper III (40T, SS, DD, 190K) | Parameter-compatible candidate | `morsddd` |
| MMF066 | Osborne 1 (40T, SS, SD, 90K) | Parameter-compatible candidate | `osb1sssd` |
| MMF067 | Osborne 1 with 2x2 upgrade (40T, DS, DD, 390K) | Parameter-compatible candidate | `osborne4`, `pmc101`, `mordsdd`, `amp3`, `amp5` |
| MMF068 | Osborne Executive (40T, SS, DD, 185K) | Parameter-compatible candidate | `1715`, `osborne1` |
| MMF069 | Otrona 816A (40T, DS, DD, 364K, *) | No matching parameter set | — |
| MMF070 | Otrona 816A (80T, DS, DD, 774K, *) | No matching parameter set | — |
| MMF071 | Pied Piper Executive (80T, DS, DD, 784K) | No matching parameter set | — |
| MMF072 | Radio Shack TRS-80 Model 4 CP/M Plus (40T, SS, DD, 156K) | Parameter-compatible candidate | `ibm-8ss`, `ibm-8ds`, `ibmpc-514ss` |
| MMF073 | Sanyo (40T, DS, DD, 312K) | No matching parameter set | — |
| MMF074 | Sanyo MBC-1200/1250 (80T, DS, DD, 624K) | No matching parameter set | — |
| MMF075 | Sperry UTS-30 (80T, DS, DD, 710K) | No matching parameter set | — |
| MMF076 | Tecron TEF System 10 (80T, DS, DD, 790K) | No matching parameter set | — |
| MMF077 | Tektronics 4170 CP/M 86 (40T, DS, DD, 316K, *) | No matching parameter set | — |
| MMF078 | Teletek Systemaster (80T, SS, SD, 72K) | No matching parameter set | — |
| MMF079 | Teletek Systemaster (40T, SS, DD, 144K) | No matching parameter set | — |
| MMF080 | Televideo 802 (40T, DS, DD, 342K) | No matching parameter set | — |
| MMF081 | Toshiba T-100 (40T, DS, DD, 256K) | No matching parameter set | — |
| MMF082 | Video Genie III (80T, DS, DD, 692K) | No matching parameter set | — |
| MMF083 | Visual 1050 (80T, SS, DD, 390K) | Parameter-compatible candidate | `v1050`, `microbee40`, `dreamdisk40`, `dec_pro`, `trsp`, `trsq`, `amp2`, `ampro400d` |
| MMF084 | Xerox 820-1 (40T, SS, SD, 82K) | No matching parameter set | — |
| MMF085 | Xerox 820-2 (40T, SS, DD, 157K) | No matching parameter set | — |
| MMF086 | XOR S100-4 (40T, SS, DD, 185K) | No matching parameter set | — |
| MMF087 | Zenith H89 (40T, SS, SD, 94K) | No matching parameter set | — |
| MMF088 | Zenith H89/H90 (40T, SS, DD, 152K) | Parameter-compatible candidate | `fdd3000_2` |
| MMF089 | Zenith H90 (80T, DS, DD, 632K) | No matching parameter set | — |
| MMF090 | Zenith Z100 (40T, SS, DD, 152K) | Parameter-compatible candidate | `zen7` |
| MMF091 | Zenith Z100 (40T, DS, DD, 312K) | Parameter-compatible candidate | `zen8` |
| MMF092 | Zorba GC200 (40T, DS, DD, 390K) | No matching parameter set | — |
| MMF093 | Montezuma Micro CP/M v 1.26 & 1.30 (40T, SS, DD, 170K) | Parameter-compatible candidate | `trsg` |
| MMF094 | Montezuma Micro CP/M v 1.26 & 1.30 (40T, DS, DD, 350K, *) | Parameter-compatible candidate | `trsi`, `trsk` |
| MMF095 | Montezuma Micro CP/M v 1.32 (40T/256S, DS, DD, 350K, *) | Parameter-compatible candidate | `trsi`, `trsk` |
| MMF096 | Montezuma Micro CP/M v 1.42 & 1.44 (40T, DS, DD, 342K) | No matching parameter set | — |
| MMI001 | Montezuma Micro Standard SYSTEM (40T, SS, DD, 170K) | Parameter-compatible candidate | `trsg` |
| MMI002 | Montezuma Micro Standard DATA (40T, SS, DD, 200K) | Parameter-compatible candidate | `trsh` |
| MMI003 | Montezuma Micro Standard DS SYSTEM (40T, DS, DD, 350K) | Parameter-compatible candidate | `trsi`, `trsk` |
| MMI004 | Montezuma Micro Standard DS DATA (40T, DS, DD, 400K) | Parameter-compatible candidate | `trsj`, `trsl`, `trsw` |
| MMI005 | Montezuma Micro 80T SYSTEM (80T, SS, DD, 350K) | Parameter-compatible candidate | `trsi`, `trsk` |
| MMI006 | Montezuma Micro 80T DATA (80T, SS, DD, 400K) | Parameter-compatible candidate | `trsj`, `trsl`, `trsw` |
| MMI007 | Montezuma Micro 80T DS SYSTEM (80T, DS, DD, 710K) | Parameter-compatible candidate | `trsm` |
| MMI008 | Montezuma Micro 80T DS DATA (80T, DS, DD, 800K) | Parameter-compatible candidate | `trsn` |
| MMI009 | Montezuma Micro Extended SYSTEM (40T, SS, DD, 190K) | Parameter-compatible candidate | `trso` |
| MMI010 | Montezuma Micro Extended DS SYSTEM (40T, DS, DD, 390K) | Parameter-compatible candidate | `v1050`, `microbee40`, `dreamdisk40`, `dec_pro`, `trsp`, `trsq`, `amp2`, `ampro400d` |
| MMI011 | Montezuma Micro Extended 80T SYSTEM (80T, SS, DD, 390K) | Parameter-compatible candidate | `v1050`, `microbee40`, `dreamdisk40`, `dec_pro`, `trsp`, `trsq`, `amp2`, `ampro400d` |
| MMI012 | Montezuma Micro Extended 80T DS SYSTEM (80T, DS, DD, 790K) | Parameter-compatible candidate | `trsr` |
| MMI013 | Montezuma Micro SUPER DATA (40T, SS, DD, 220K) | No matching parameter set | — |
| MMI014 | Montezuma Micro SUPER DS DATA (40T, DS, DD, 440K) | No matching parameter set | — |
| MMI015 | Montezuma Micro 80T SUPER DATA (80T, SS, DD, 440K) | No matching parameter set | — |
| MMI016 | Montezuma Micro 80T SUPER DS DATA (80T, DS, DD, 880K) | No matching parameter set | — |

## Next verification steps

1. For each of the 43 candidate records, compare the complete DPB, sector-ID order and head/track traversal before declaring equivalence.
2. Prioritize the 69 no-match records as **potential additional historical definitions**, not 69 proven new formats.
3. Preserve MMF/MMI source IDs as provenance identifiers; assign permanent database IDs only after deciding whether each is a new historical identity, an alias, or a variant.
4. Do not automatically ingest the five excluded external records into an accepted catalogue. Investigate their exclusion reasons.
5. Track historical format identity separately from geometry equivalence, per the database's design rules.
