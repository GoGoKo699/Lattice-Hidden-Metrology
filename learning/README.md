# Learning Lattice Hidden Metrology

The question is not whether the light contains an angle, but when that angle can be recovered from finite observations and with what computation. Calibration, optical noise and inference must be kept in the same experiment.

The single educational anchor is **Chris Peikert, *A Decade of Lattice Cryptography***, [Cryptology ePrint 2015/939](https://eprint.iacr.org/2015/939), using the revised PDF dated 17 February 2016 and recorded by the archive on 18 February 2016. The [Peikert bridge](PEIKERT_BRIDGE.md) selects the relevant sections, translates notation, and supplies the optical and estimation concepts absent from that survey.

## Reading route

Start with [the bridge](PEIKERT_BRIDGE.md), alongside the [30-milestone map](MILESTONES.md). Its first **15 background/preliminaries** targets connect lattice equations and Gaussian widths to a complete optical experiment. Its next **15 narrative/innovation** targets assemble the resolution theorem, global estimator, quantum reduction and information comparison into one account. Both phases proceed from individual ingredients to the complete model or conclusion.

| Goal | Start here |
|---|---|
| Translate lattice notation and locate the selected reading | Bridge B0–B3 |
| Understand the physical source and measurement | Bridge B4–B5 |
| Follow a complete finite example | Bridge B6 and [its checks](../verification/check_learning.py) |
| Separate conditional hardness from unconditional statistics | Bridge B7–B8 |
| Audit the exact statements and proofs | [Scientific map](../science/README.md) |

The map is a common set of understanding targets, not a personalized assessment or a claim to cover every technical lemma. No learner answers or progress records are stored here. Specialist derivations have one authoritative home under `science/`; the bridge explains and links them rather than replacing them.

The decisive distinctions are supplied-source versus chosen-probe access, independent calibration versus revealed source information, local sensitivity versus global risk, and unrestricted inference versus efficient quantum computation. The results preserve all four.
