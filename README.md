# Lattice Hidden Metrology

**A simple optical measurement can preserve substantial sensitivity while a useful estimate remains computationally inaccessible.**

This project gives a conditional separation for a supplied source of separable coherent light. A passive real mode mixer encodes an angle. Both observers receive identical calibration and sensing pulses from the same unknown source. Ordinary homodyne detection and unrestricted classical inference recover the angle from polynomially many pulses; under quantum homogeneous continuous-LWE hardness, every efficient quantum estimator retains essentially the prior-only risk, even with collective measurements.

The separation does not attack a standardized cryptosystem or compare quantum and classical speedups. It concerns information, optical resolution and the computational cost of inference under a precisely defined access contract.

## Principal results

There are $`n`$ even optical modes. The public source parameters satisfy $`0<\beta<1`$, $`\gamma\ge2\sqrt n`$ and polynomially bounded $`\gamma/\beta`$. The coherent displacement scale $`R`$ is polynomially bounded. Mean probe photons per pulse are asymptotically $`nR^2/(4\pi)`$.

| Regime or question | Result | Proof |
|---|---|---|
| Insufficient resolution | If $`R^2=o(\gamma^2/\log n)`$, no estimator using polynomially many pulses obtains a nonnegligible prior-risk improvement, regardless of computation | [Quantum resolution](science/resolution.md) |
| Polynomial-copy recovery | If $`R^2\ge c_0\gamma^2/\log n`$ for fixed $`c_0>0`$, explicit homodyne plus exhaustive inference gives inverse-polynomial error with polynomially many calibration and sensing pulses | [Global estimator](science/estimation.md) |
| Efficient quantum observer | Under quantum decisional hCLWE hardness, every uniform polynomial-time estimator has Bayes risk at least $`\theta_0^2/3-\operatorname{negl}(n)`$, with $`\theta_0=\pi/8`$ | [Quantum reduction](science/quantum-hardness.md) |
| Information retained by homodyne | At $`R=\gamma/\beta`$, $`\beta\to0`$, both classical and quantum Fisher information scale as $`R^2`$, and their ratio has lower limit at least $`\pi/[2(1+\pi)]\approx0.379`$ | [Mixed-state information](science/fisher-information.md) |
| Calibration and finite resources | The same information fraction survives local nuisance elimination; finite precision, preparation, photons, workspace and uniform pure loss are accounted for | [Information F4](science/fisher-information.md), [resources](science/resources.md) |

The first two rows are unconditional. The third is explicitly computational and conditional. The information row is a local statement for the mixed state, not a substitute for the separate global estimation theorem.

## Read the science

Start with the [scientific map](science/README.md) and [model](science/model.md). For the complete argument, follow [resolution](science/resolution.md) → [global estimation](science/estimation.md) → [quantum hardness](science/quantum-hardness.md) → [Fisher information](science/fisher-information.md) → [finite resources](science/resources.md).

[Related work](references/RELATED_WORK.md) distinguishes the optical results from inherited continuous-LWE hardness and Gaussian-pancake learning gaps. The [bibliography](references/references.bib) gives the primary sources. [llms.txt](llms.txt) maps specific questions to authoritative statements.

## Reproduce the finite checks

Using Python 3.13:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 .venv/bin/python verification/verify.py
```

The suite checks Fourier/mixture identities, the optical kernel, finite Fock trace distances, actual mixed-state quantum Fisher information, source-nuisance algebra, null symmetry and seeded two-batch estimation. The [verification guide](verification/README.md) and [stored report](verification/expected_results.json) give exact cases and tolerances. Finite checks do not prove asymptotic statements or test cryptographic hardness.

## Consequential scope

The encoding is a **real passive mode rotation**, not a generic optical phase shift: the latter can reveal itself through the Gaussian background. The source is supplied; the observer has no secret axis, source program, individual displacement labels, purification, paired input/output data or chosen replacement probes. Calibration is counted, not assumed free.

The hardness theorem averages over the declared hidden-axis and angle priors. The lower-energy threshold distinguishes polynomial from superpolynomial copy requirements, not optimal finite constants. Probe energy can be large. Fisher-information robustness is not inferred from trace-distance robustness. The project makes no unconditional security or exhaustive priority claim.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
