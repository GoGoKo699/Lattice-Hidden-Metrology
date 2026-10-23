# Thirty understanding milestones

This map describes the project, not a particular learner. Its single educational anchor is Chris Peikert's *A Decade of Lattice Cryptography*, in the revised version identified by the [Peikert bridge](PEIKERT_BRIDGE.md). The bridge supplies the optical foundations and later continuous-LWE connection absent from that source; primary papers remain research dependencies rather than additional educational anchors.

**M01–M15: background/preliminaries.** The fifteen targets connect lattice objects, probability conventions and computational experiments to coherent light, readout and calibrated estimation. This phase ends with the complete equal-access experiment.

**M16–M30: narrative/innovation.** The fifteen targets move from the source and operator identities through global recovery, quantum hardness and local information to the complete resource-qualified conclusion. This allocation reflects the project's connection between cryptography and optical statistics; it is not a judgment of a learner's background.

Each milestone records a central question, understanding target, dependencies and story role, conceptual connection, and source pointers. Dependencies refer only to earlier milestones. Together the targets provide global understanding, not mastery of every lemma or every neighboring subject. The authoritative proofs remain under `science/`.

## Phase I — Background and preliminaries

### M01 — Lattice points and coordinates

**Phase:** Background/preliminaries.

**Central question:** What does a lattice specify, and what must an algorithm still find?

**Understanding target:** Distinguish a lattice, its basis and a computational task on that lattice.

**Dependencies and story role:** None; introduces the geometric objects without equating a concise description with an efficient solution.

**Conceptual connection:** Integer coordinates make the Gaussian and modular constructions concrete.

**Source pointers:** Peikert 2.1–2.2; [bridge B1](PEIKERT_BRIDGE.md#b1-lattice-language).

### M02 — Noisy modular observations

**Phase:** Background/preliminaries.

**Central question:** How can noisy equations carry a common hidden quantity?

**Understanding target:** Identify the shared secret and fresh sample randomness in an LWE observation.

**Dependencies and story role:** M01; moves from point geometry to a statistical experiment.

**Conceptual connection:** A common latent parameter is also what links this project’s independent optical pulses.

**Source pointers:** Peikert 4.2.1; [bridge B1](PEIKERT_BRIDGE.md#b1-lattice-language); [model M4](../science/model.md).

### M03 — Gaussian conventions

**Phase:** Background/preliminaries.

**Central question:** Why is a Gaussian width not its standard deviation?

**Understanding target:** Convert the project’s width into variance and combine independent Gaussian noises correctly.

**Dependencies and story role:** M01; fixes the normalization before physical noise is introduced.

**Conceptual connection:** The factor of pi links lattice Gaussian notation to vacuum measurement variance.

**Source pointers:** Peikert 2.3; [bridge B2](PEIKERT_BRIDGE.md#b2-gaussian-width-is-not-standard-deviation); [model M1](../science/model.md).

### M04 — Discrete structure and smoothing

**Phase:** Background/preliminaries.

**Central question:** What is retained when Gaussian randomness is supported on integers?

**Understanding target:** Distinguish discrete Gaussian mass from continuous density and understand the role of peak spacing and broadening.

**Dependencies and story role:** M03; introduces the periodic structure that later becomes optically unresolved.

**Conceptual connection:** Classical smoothing motivates, but does not itself prove, the operator-level optical bound.

**Source pointers:** Peikert 2.3; [bridge B2](PEIKERT_BRIDGE.md#b2-gaussian-width-is-not-standard-deviation); [model M2](../science/model.md).

### M05 — Search and decision experiments

**Phase:** Background/preliminaries.

**Central question:** Must an estimator recover a cryptographic secret to contradict hardness?

**Understanding target:** Separate secret recovery from distinguishing a specified structured distribution from its null.

**Dependencies and story role:** M02; makes the computational task precise before importing an assumption.

**Conceptual connection:** A useful angle estimator will become a decision test, not a secret-recovery algorithm.

**Source pointers:** Peikert 4.2.1; [bridge B7](PEIKERT_BRIDGE.md#b7-why-efficient-quantum-inference-is-covered); [hardness H1](../science/quantum-hardness.md).

### M06 — Conditional reductions

**Phase:** Background/preliminaries.

**Central question:** Which direction does the hardness implication run?

**Understanding target:** Explain why an efficient solver for the target would give a solver for the assumed-hard source, without claiming unconditional hardness.

**Dependencies and story role:** M05; relates experiments through a charged algorithm.

**Conceptual connection:** A quantum reduction and a quantum adversary are distinct notions; the observer model must be specified.

**Source pointers:** Peikert 4.2.2; [bridge B7](PEIKERT_BRIDGE.md#b7-why-efficient-quantum-inference-is-covered); [hardness H1–H3](../science/quantum-hardness.md).

### M07 — The continuous hidden-axis source

**Phase:** Background/preliminaries.

**Central question:** What replaces the modular secret in homogeneous continuous LWE?

**Understanding target:** Identify the unit axis, Gaussian envelope and periodic weighting, and distinguish this source from ordinary LWE.

**Dependencies and story role:** M02, M03, M04, M06; introduces the actual imported source.

**Conceptual connection:** The later continuous-LWE theorem, not the educational survey, supplies its precise computational assumption.

**Source pointers:** [Bridge B3](PEIKERT_BRIDGE.md#b3-from-noisy-equations-to-a-hidden-axis); [model M1](../science/model.md); [related work](../references/RELATED_WORK.md).

### M08 — An axis rather than an arrow

**Phase:** Background/preliminaries.

**Central question:** Why do opposite hidden directions describe the same source?

**Understanding target:** Interpret the integer-Gaussian mixture and the sign symmetry of its normal.

**Dependencies and story role:** M07; identifies what statistical recovery can meaningfully return.

**Conceptual connection:** The eventual angle formula must work with two unoriented axes.

**Source pointers:** [Bridge B3](PEIKERT_BRIDGE.md#b3-from-noisy-equations-to-a-hidden-axis); [model M2](../science/model.md).

### M09 — Coherent displacements

**Phase:** Background/preliminaries.

**Central question:** How is a real label represented by an optical pulse?

**Understanding target:** Relate mean quadrature, coherent amplitude, vacuum variance and photon number in the stated units.

**Dependencies and story role:** M03; supplies the physical carrier and its cost.

**Conceptual connection:** Increasing the displacement scale reduces label-referred readout noise while increasing probe energy.

**Source pointers:** [Bridge B4](PEIKERT_BRIDGE.md#b4-turning-labels-into-light); [model M3](../science/model.md); [resources P1](../science/resources.md).

### M10 — Mixtures and inaccessible labels

**Phase:** Background/preliminaries.

**Central question:** Which information is actually given to the observer?

**Understanding target:** Distinguish a classical mixture from a label-revealed ensemble, purification or coherent sampling oracle.

**Dependencies and story role:** M07, M09; fixes the quantum input interface.

**Conceptual connection:** Discarding the label is why pure-state conditional sensitivity cannot be used as mixed-state information.

**Source pointers:** [Bridge B4](PEIKERT_BRIDGE.md#b4-turning-labels-into-light); [model M3–M4](../science/model.md).

### M11 — Passive mixing and null symmetry

**Phase:** Background/preliminaries.

**Central question:** Why is the encoding a real mode rotation rather than an arbitrary phase shift?

**Understanding target:** Identify the transformations of both quadrature vectors and explain which leave the Gaussian null invariant.

**Dependencies and story role:** M09, M10; fixes the actual parameter-encoding operation.

**Conceptual connection:** Null invariance is the physical premise that allows prior-risk hardness.

**Source pointers:** [Bridge B4](PEIKERT_BRIDGE.md#b4-turning-labels-into-light); [model M3](../science/model.md).

### M12 — Homodyne as noisy classical data

**Phase:** Background/preliminaries.

**Central question:** What distribution does a fixed laboratory readout produce?

**Understanding target:** Derive the rescaled Gaussian readout noise and distinguish axial from transverse widths.

**Dependencies and story role:** M03, M08, M09; connects the optical source to a classical statistical model.

**Conceptual connection:** The same measured data can support unrestricted estimation without making inference efficient.

**Source pointers:** [Bridge B5](PEIKERT_BRIDGE.md#b5-readout-fourier-contrast-and-global-recovery); [resolution R3](../science/resolution.md).

### M13 — Risk and information distance

**Phase:** Background/preliminaries.

**Central question:** What does it mean to improve an estimate over prior knowledge?

**Understanding target:** Explain bounded squared loss, prior-only Bayes risk, trace-distance control and computational indistinguishability without conflating them.

**Dependencies and story role:** M05, M06, M10; introduces operational comparison criteria.

**Conceptual connection:** A state can be statistically distinguishable yet computationally indistinguishable for the allowed observer.

**Source pointers:** [Bridge B7–B8](PEIKERT_BRIDGE.md#b7-why-efficient-quantum-inference-is-covered); [model M4](../science/model.md); [hardness H4](../science/quantum-hardness.md).

### M14 — Local sensitivity and nuisance parameters

**Phase:** Background/preliminaries.

**Central question:** What can Fisher information say when the source axis is unknown?

**Understanding target:** Separate local fixed-source sensitivity, unknown-source nuisance information and global estimation risk.

**Dependencies and story role:** M10, M12, M13; introduces the information comparison without granting the axis.

**Conceptual connection:** Calibration changes identifiability and must also enter the local information matrix.

**Source pointers:** [Bridge B8](PEIKERT_BRIDGE.md#b8-three-boundaries-and-two-kinds-of-information); [information F1–F4](../science/fisher-information.md).

### M15 — The complete equal-access experiment

**Phase:** Background/preliminaries.

**Central question:** What exactly is held equal between the two observers?

**Understanding target:** Assemble source, encoding, prior, independent calibration and sensing batches, permitted processing and charged resources into one experiment.

**Dependencies and story role:** M01–M14; background synthesis, not one more isolated ingredient.

**Conceptual connection:** The comparison changes computation, not the hidden knowledge or data supplied to each observer.

**Source pointers:** [Model M1–M5](../science/model.md); [bridge B4–B8](PEIKERT_BRIDGE.md#b4-turning-labels-into-light); [resources P5](../science/resources.md).

## Phase II — Narrative and innovation

### M16 — Source algebra and tails

**Phase:** Narrative/innovation.

**Central question:** How does the exact source decomposition support resource accounting?

**Understanding target:** Connect completing the square, integer-Gaussian moments and subgaussian tails to preparation and energy bounds.

**Dependencies and story role:** M04, M07, M08, M15; begins the contribution with a local algebraic mechanism.

**Conceptual connection:** The same controlled tails support both finite optical simulation and finite data storage.

**Source pointers:** [Model M2](../science/model.md); [resources P1–P2](../science/resources.md); Peikert 2.3 for notation.

### M17 — Fourier components of an optical mixture

**Phase:** Narrative/innovation.

**Central question:** How does light damp each periodic component of the source?

**Understanding target:** Follow the Gaussian kernel identity and explain why the two unitary factors have the same sign, with trace norm still preserved.

**Dependencies and story role:** M10, M16; upgrades a classical source expansion to an operator statement.

**Conceptual connection:** A nonpositive Fourier component can have a calculable trace norm even though it is not a density operator.

**Source pointers:** [Resolution R1](../science/resolution.md); [bridge B8](PEIKERT_BRIDGE.md#b8-three-boundaries-and-two-kinds-of-information).

### M18 — An obstruction for every measurement

**Phase:** Narrative/innovation.

**Central question:** How does one-pulse damping limit a full calibrated experiment?

**Understanding target:** Combine normalization, triangle inequality and tensor telescoping into a finite prior-risk bound.

**Dependencies and story role:** M13, M17; promotes the local operator identity to an operational impossibility regime.

**Conceptual connection:** This is an unconditional quantum-state bound, stronger than failure of one chosen readout.

**Source pointers:** [Resolution R2](../science/resolution.md); [model M4](../science/model.md).

### M19 — A contrast that finds an axis

**Phase:** Narrative/innovation.

**Central question:** Why does a bounded cosine statistic expose the hidden normal?

**Understanding target:** Explain integer-phase cancellation at the true axis and the population gap away from its two signs.

**Dependencies and story role:** M08, M12, M16; constructs the statistical recovery mechanism.

**Conceptual connection:** The peak-spacing model becomes an explicit objective with a provable gap.

**Source pointers:** [Estimation E1](../science/estimation.md); [bridge B5–B6](PEIKERT_BRIDGE.md#b5-readout-fourier-contrast-and-global-recovery).

### M20 — Finite observations and exhaustive search

**Phase:** Narrative/innovation.

**Central question:** How can polynomially many data points support an exponential search?

**Understanding target:** Relate a finite net, a uniform concentration bound, data truncation and numerical precision to a finite-copy guarantee.

**Dependencies and story role:** M13, M19; turns the population contrast into a data-based procedure.

**Conceptual connection:** The logarithm of the net size enters sample complexity; the net size itself enters computation.

**Source pointers:** [Estimation E2, E4](../science/estimation.md); [resources P4](../science/resources.md).

### M21 — Two axes determine one angle

**Phase:** Narrative/innovation.

**Central question:** How can calibration and sensing be combined without choosing their signs?

**Understanding target:** Recover the angle from the invariant inner-product ratio and propagate axis error into probability and squared-risk bounds.

**Dependencies and story role:** M11, M15, M20; completes the global estimator.

**Conceptual connection:** Independent calibrated axes replace free knowledge of the source and avoid a local-to-global inference.

**Source pointers:** [Estimation E3](../science/estimation.md); [bridge B6](PEIKERT_BRIDGE.md#b6-worked-two-mode-example).

### M22 — The polynomial-copy resolution scale

**Phase:** Narrative/innovation.

**Central question:** Where do the optical impossibility and statistical achievability results meet?

**Understanding target:** Compare the low-energy trace bound with inverse-polynomial contrast strength and identify the matching asymptotic scale.

**Dependencies and story role:** M18, M21; combines both sides of the resolution question.

**Conceptual connection:** A polynomial-copy boundary is not an optimal finite threshold or a fixed universal sample exponent.

**Source pointers:** [Resolution R3–R4](../science/resolution.md); [resources P1](../science/resources.md).

### M23 — Preparing the quantum challenge efficiently

**Phase:** Narrative/innovation.

**Central question:** Why can a reduction supply the entire optical input?

**Understanding target:** Account for classical truncation, rounding, photon cutoff and coherent-state synthesis with polynomial resources.

**Dependencies and story role:** M06, M09, M10, M16; closes the input-access step needed for a quantum lower bound.

**Conceptual connection:** Classical challenge samples suffice because the reduction prepares a mixture, not a secret-dependent coherent oracle.

**Source pointers:** [Resources P2–P3](../science/resources.md); [hardness H3](../science/quantum-hardness.md).

### M24 — From angle risk to a decision test

**Phase:** Narrative/innovation.

**Central question:** Why would a useful efficient collective estimator contradict the assumption?

**Understanding target:** Construct the loss-based test, use the angle-independent null, and retain calibration and simulation errors.

**Dependencies and story role:** M05, M11, M13, M23; completes the computational separation.

**Conceptual connection:** The reduction contains the observer’s entire quantum processing, rather than assuming classical hardness survives it.

**Source pointers:** [Hardness H1–H5](../science/quantum-hardness.md); [bridge B7](PEIKERT_BRIDGE.md#b7-why-efficient-quantum-inference-is-covered).

### M25 — A mixed-data Fisher witness

**Phase:** Narrative/innovation.

**Central question:** How can one prove substantial sensitivity after the label has been discarded?

**Understanding target:** Use the statistic derivative and its variance to lower-bound Fisher information of the actual homodyne distribution.

**Dependencies and story role:** M12, M14, M19; begins the independent local-information argument.

**Conceptual connection:** The axis-dependent witness is for analysis; the optical measurement remains laboratory-fixed.

**Source pointers:** [Information F1](../science/fisher-information.md); [bridge B8](PEIKERT_BRIDGE.md#b8-three-boundaries-and-two-kinds-of-information).

### M26 — Bounding quantum information without revealing labels

**Phase:** Narrative/innovation.

**Central question:** How is the true mixed-state QFI bounded and compared with homodyne information?

**Understanding target:** Use the active two-mode plane, mixture convexity and the deep-resolution limit to obtain the constant fraction.

**Dependencies and story role:** M10, M11, M25; completes the fixed-source comparison.

**Conceptual connection:** Conditional pure-state information enters only as an upper bound, not as the mixed-state value.

**Source pointers:** [Information F2–F3](../science/fisher-information.md); [resources P1](../science/resources.md).

### M27 — Paying for calibration locally

**Phase:** Narrative/innovation.

**Central question:** How much local information remains when the source is a nuisance?

**Understanding target:** Interpret the joint source-angle information matrix and its Schur complement, including the equal-batch cost.

**Dependencies and story role:** M14, M15, M26; transfers the information fraction to the calibrated local model.

**Conceptual connection:** Local nuisance elimination is not prior averaging, and an SLD bound is not a universal attainability theorem.

**Source pointers:** [Information F4](../science/fisher-information.md); [model M5](../science/model.md).

### M28 — The complete resource and robustness statement

**Phase:** Narrative/innovation.

**Central question:** Which physical imperfections and costs are actually included?

**Understanding target:** Combine photons, pulses, bits, computation and workspace; distinguish uniform pure loss and bounded-risk stability from uncontrolled FI perturbations.

**Dependencies and story role:** M21, M22, M23, M24, M27; closes the operational account.

**Conceptual connection:** Polynomial energy can be large, and trace-distance continuity does not automatically control derivatives.

**Source pointers:** [Resources P1–P5](../science/resources.md); [verification guide](../verification/README.md).

### M29 — Attribution and evidential boundaries

**Phase:** Narrative/innovation.

**Central question:** Which parts come from earlier work, and what do finite checks establish?

**Understanding target:** Separate the imported hCLWE assumption and classical learning gap from the optical results, local derivations and finite tests.

**Dependencies and story role:** M22, M24, M27, M28; places the contribution against its actual dependencies.

**Conceptual connection:** A single teaching anchor does not replace research citations or an independent proof review.

**Source pointers:** [Related work](../references/RELATED_WORK.md); [bibliography](../references/references.bib); [verification guide](../verification/README.md).

### M30 — The full information-to-inference separation

**Phase:** Narrative/innovation.

**Central question:** What survives when all assumptions and costs are stated together?

**Understanding target:** Explain the three regimes, the independent global and local arguments, the conditional quantum lower bound, and the access changes that invalidate it.

**Dependencies and story role:** M15, M22, M24, M27, M28, M29; final synthesis of the project rather than an extra technical topic.

**Conceptual connection:** The outcome is a supplied-source inference separation, not a quantum speedup, standardized-scheme attack or unrestricted metrological impossibility.

**Source pointers:** [Scientific map](../science/README.md); [bridge B8](PEIKERT_BRIDGE.md#b8-three-boundaries-and-two-kinds-of-information); [model M4–M5](../science/model.md).

[Learning guide](README.md) · [Peikert bridge](PEIKERT_BRIDGE.md) · [Scientific map](../science/README.md)
