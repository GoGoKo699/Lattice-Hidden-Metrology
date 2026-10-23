# Scientific account

A measurement can retain sensitivity without making a useful estimate computationally accessible. This project makes that distinction in a supplied-source optical experiment. The probes are separable coherent-state mixtures with an unknown axis drawn from homogeneous continuous LWE. A public, passive mode mixer encodes one angle. Calibration and sensing pulses come from the same source; neither observer receives its axis.

There are three regimes to distinguish. At inadequate energy the quantum states themselves lose the useful structure. Above a matching polynomial-copy resolution scale, homodyne data and unrestricted classical computation recover the angle. Under the specified quantum hCLWE assumption, efficient quantum computation still cannot improve appreciably on the prior, even with collective measurements. In a higher-energy regime, homodyne also retains a constant fraction of local quantum Fisher information after charging calibration.

## Exact result map

| Statement | Assumptions and result | Proof |
|---|---|---|
| M1–M5: experiment | Fixed unknown source axis, independent calibration/sensing labels, public real passive mixer; no calibration means exact Bayesian nonidentifiability | [Model](model.md) |
| R1–R2: quantum smoothing | Explicit optical Fourier identity and measurement-independent trace-distance bound, including all copies | [Resolution](resolution.md) |
| R3–R4: resolution scale | Below $`R^2=o(\gamma^2/\log n)`$, polynomially many copies contain negligible angle information; at $`R^2\ge c_0\gamma^2/\log n`$, polynomial-copy recovery is possible | [Resolution](resolution.md), [E2–E3](estimation.md) |
| E1–E4: global estimator | Explicit finite Fourier-net search learns both axes, handles their sign ambiguity and gives a finite squared-risk bound | [Estimation](estimation.md) |
| H1–H5: quantum computation | Under quantum decisional hCLWE hardness, every uniform efficient collective estimator has prior-only Bayes risk up to negligible improvement | [Hardness](quantum-hardness.md) |
| F1–F4: information readout | Mixed-state QFI and homodyne FI are both of order $`R^2`$ when $`R=\gamma/\beta`$, $`\beta\to0`$; a constant fraction survives nuisance elimination | [Fisher information](fisher-information.md) |
| P1–P5: resource closure | Photon count, finite classical precision, polynomial coherent-state simulation, operational perturbation control and uniform pure loss | [Resources](resources.md) |

The quantum-resolution and recovery theorems are unconditional. The efficient-estimation obstruction is computational and explicitly conditional. The numerical checks establish only their listed finite identities and examples.

## Proof dependencies

Start with M1–M3 for the Gaussian conventions and coherent source. M2 supplies the mixture, moment and tail formulas used throughout. R1 is an operator calculation, not a classical-data bound; it yields R2 and the low-energy half of R4. E1 constructs a population contrast, E2 makes it a finite-data estimator, and E3 converts two unoriented axes into the angle. This supplies the high-energy half of R4 independently of Fisher information.

H3 maps classical hCLWE samples into the full quantum experiment. P2–P3 close its finite-precision simulation cost. This is the step needed to cover efficient collective quantum measurements rather than merely classical postprocessing. F1 bounds information in the already mixed homodyne distribution, F2 bounds the actual mixed-state QFI, and F4 removes the source nuisance parameter while retaining calibration cost.

## Interpretation and boundaries

The separation is not a quantum speedup, a new encryption scheme, or an attack on a standardized lattice cryptosystem. It identifies a computational obstruction *after* simple measurement preserves substantial local sensitivity, while supplying a separate operational proof that the angle can be estimated from the same finite data.

The source is engineered and supplied. Chosen replacement probes, secret-dependent advice, a source program, or a purification would change access. The encoding is real mode mixing, not a generic optical phase shift. The energy is polynomial but can be large. Local information matrices are not global risk guarantees; the latter have their own proof. Neither the study nor its finite tests establish the hCLWE assumption or an exhaustive priority claim.

For attribution, read [Related work](../references/RELATED_WORK.md). For reproduction and its limits, read [Verification](../verification/README.md).
