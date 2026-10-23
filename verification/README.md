# Finite verification

The analytical proofs are in `science/`. The suite independently evaluates finite instances of their formulas and a small estimator demonstration. It does **not** test lattice hardness, prove an asymptotic theorem, certify experimental hardware, or replace independent expert review.

## Run

From the repository root, using Python 3.13:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 .venv/bin/python verification/verify.py
```

The script prints a JSON report and exits unsuccessfully if an assertion fails. Only `--write` replaces `verification/expected_results.json`, and only after all checks pass. Run without that flag to retain the reference report. The tested environment was Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The random seed is 20261023. Small last-bit differences across platforms are expected; compare assertions and tolerances rather than bytewise JSON equality.

## What was checked

The stored run passed **3,748 assertions**. This is an assertion count, not a count of independent theorems.

| Check | Cases and method | Main tolerance or observed quantity |
|---|---|---|
| Source formulas | 27 parameter combinations; mixture/Fourier densities, second moments, and 2,727 contrast-direction checks | Density tolerance $`2\times10^{-11}`$; largest observed error approximately $`1.2\times10^{-15}`$ |
| Optical operator kernel | 12 direct complex Gaussian integrals, explicitly checking the same-sign two-sided unitary factors | Absolute tolerance $`2\times10^{-11}`$ |
| Trace-distance bounds | Four one-mode Fock matrices, cutoff 40, 80-node Gaussian quadrature | Mass deficit below $`2\times10^{-10}`$; bound tolerance $`2\times10^{-9}`$ |
| Actual mixed-state QFI | Three two-mode cases, spectral QFI with cutoffs 28 and 36 and 96 quadrature nodes | Cutoff difference below $`3\times10^{-6}`$; largest observed approximately $`1.8\times10^{-12}`$ |
| Deep-resolution homodyne FI | Three additional quadrature calculations at $`R=\gamma/\beta`$ | Compared with the analytic witness and quantum upper bound |
| Angle and nuisance geometry | Dimensions 2, 4, 10 and 20; 320 sign cases and sample-allocation Schur complements | Angle tolerance $`2\times10^{-14}`$ |
| Null-state symmetry | Three dimensions: real mixing preserves covariance, generic phase rotation changes it | Real-mixing tolerance $`10^{-13}`$ |
| Two-batch estimator | Eight seeded 2D trials; 1,500 copies per batch, 2,048-direction grid | All angle errors below 0.06 radians; maximum observed approximately 0.00895 |

The small Fock examples are chosen for numerical convergence, not as cryptographically hard instances. The estimator demonstration uses a convenient circle grid rather than the conservative general theorem's net and sample count. Its success does not validate the asymptotic guarantee or imply efficient recovery in growing dimension.

## Numerical safeguards and limitations

The discrete Gaussian sums use tails below double precision for the listed cases. Density and characteristic-function calculations are compared in different representations. The Fourier-operator check integrates the original complex kernel directly. The quantum Fisher calculation diagonalizes the actual mixed one-mode factors and uses their product spectrum, rather than substituting a pure coherent-state formula. Increasing two Fock cutoffs tests convergence at those listed parameters only; it is not a uniform truncation proof. The analytical simulation-error argument is P2–P3.

The script's assertions expose every numerical tolerance. The [JSON report](expected_results.json) records actual inputs, outputs, environment and scope. No empirical probability of cryptographic security is reported.

## Learning-route checks

Run the additional suite with the same environment:

```bash
OPENBLAS_NUM_THREADS=1 .venv/bin/python verification/check_learning.py
```

Its **9 tests** check the exact M01–M30 sequence, 15/15 phase allocation, six record fields, backward dependencies, internal learning links and heading fragments, explicit anchor version, Gaussian-noise conversions, the worked contrast and photon values, sign-independent angle readout, and the calibration information factor. The tests do not assess a learner or replace the scientific suite.

The furnishing review reran the unchanged scientific script and reproduced the stored report byte-for-byte in the pinned environment. All nine learning tests passed. The scientific files remain those integrated at `d27588da1c5950d2b9240c2897e0d7ebbc690d86`; the learning route explains rather than strengthens their claims.

Source, numerical and navigation checks do not establish correct display in GitHub's renderer. Hosted mathematical rendering could not be visually inspected in this review: the connected file tools returned Markdown source, and a usable browser connection was unavailable. This remains an unverified presentation check, not a completed release-readiness certification.
