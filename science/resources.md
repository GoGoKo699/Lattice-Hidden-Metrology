# Energy, finite precision and computational access

The analytical states are convenient continuous-variable descriptions. The hardness theorem uses a uniform finite-register circuit model, not an infinite-precision real-number machine. This page connects the two and keeps preparation, calibration and readout costs visible.

## P1. Probe photons and operations

A pulse contains $`n`$ modes. The convention in M3 gives mean photon number $`R^2\|X\|^2/2`$ conditional on the displacement. Thus

```math
\overline N_{\rm pulse}
=\frac{R^2}{2}\left[\frac{n}{2\pi}
-\frac{\gamma^2}{C}\sum_{\ell\in\mathbb Z}\ell^2e^{-\pi S^2\ell^2}\right]
\le\frac{nR^2}{4\pi}.
```

The correction is exponentially small in the hard-family regime. An experiment with $`M=N_c+N_s`$ independent pulses uses $`M\overline N_{\rm pulse}`$ mean probe photons, including calibration. The encoding is a layer of $`n/2`$ public two-mode passive rotations. Homodyne reads all $`n`$ position quadratures per pulse, with finite classical records specified in E2. Both observers require the same laboratory quadrature reference.

The polynomial-copy resolution scale is therefore of order $`n\gamma^2/\log n`$ photons **per pulse**. The stronger constant-information-fraction regime uses $`R=\gamma/\beta`$, or order $`n\gamma^2/\beta^2`$ photons per pulse. For example, $`\gamma=2\sqrt n`$ and $`\beta=1/n`$ give approximately $`n^4/\pi`$ photons per pulse. Polynomial energy is not necessarily experimentally modest.

This accounting concerns transmitted probe excitation, not the energy of local oscillators, control electronics, device work or dissipated heat. No optimality claim for those apparatus resources, or for the estimator's polynomial sample exponent, is made.

## P2. Classical truncation and rounding

Consider $`M`$ pulses and a target total simulation error $`\epsilon`$. M2 gives a coordinate tail bound for both the source labels and their rotated labels. Choosing

```math
B^2\ge\pi^{-1}\log(8nM/\epsilon)
```

makes the probability that any retained coordinate exceeds $`B`$ at most $`\epsilon/4`$. A simulator can return a fixed fallback state on that event. This changes its output by no more than that probability.

Coherent overlaps obey

```math
|\langle Rx|Ry\rangle_Q|^2=e^{-R^2\|x-y\|^2/2},
\qquad
D(|Rx\rangle_Q,|Ry\rangle_Q)\le R\|x-y\|/\sqrt2.
```

Consequently, rounding every label coordinate to a mesh $`\delta`$ costs at most $`MR\sqrt n\,\delta/\sqrt2`$ in total trace distance, using the conservative coordinate error bound $`\delta`$. An angle error $`\delta_\theta`$ costs at most $`MR\sqrt n B|\delta_\theta|/\sqrt2`$, because $`\|O_\theta-O_{\theta'}\|\le|\theta-\theta'|`$. Allocate a fixed fraction of $`\epsilon`$ to each error and choose the meshes accordingly. The required bit count is

```math
O\!\left(\log\frac{Mn(1+R)(1+B)}{\epsilon}\right).
```

Replacing the continuous uniform angle by a fine uniform grid admits this coupling. Squared loss is Lipschitz in the angle on the declared compact interval, so the loss-test error also vanishes with the grid spacing. No exact real input is used.

The source holder can use M2 to prepare classical labels. Truncate the integer Gaussian at $`|K|\le S\sqrt{O(\log(1/\epsilon))}`$, enumerate its polynomially many weights, and sample from their normalized finite-precision cumulative distribution. Gaussian draws, a unit-vector description and arithmetic require polynomial precision. This describes source preparation when its axis is known to the holder; it does not disclose that axis to the observer or to the hardness reduction.

## P3. A polynomial coherent-state simulator

After rounding, each ordinary coherent amplitude has modulus at most $`R(B+1)/\sqrt2`$. Let

```math
\lambda_{\max}=R^2(B+1)^2/2,
\quad
K_{\max}=\left\lceil\max\{2e\lambda_{\max},
2\log_2(8nM/\epsilon)\}\right\rceil.
```

The photon-number distribution of a coherent state is Poisson. For $`k>\lambda`$, its Chernoff bound is $`\Pr(N\ge k)\le(e\lambda/k)^k`$. With $`k=K_{\max}+1`$, the discarded probability is at most $`2^{-k}`$. The trace distance to the normalized truncated pure state is the square root of that probability. Summing over $`nM`$ modes is at most $`\epsilon/8`$ with the displayed cutoff.

The truncated mode has explicitly computable amplitudes proportional to

```math
e^{-|\alpha|^2/2}\frac{\alpha^k}{\sqrt{k!}},
\qquad 0\le k\le K_{\max}.
```

They can be prepared in $`\lceil\log_2(K_{\max}+1)\rceil`$ qubits by a binary tree of conditional rotations: at each node rotate according to the summed probabilities of its two child intervals, then apply the signs/phases at the leaves. There are $`O(K_{\max})`$ nodes; all probabilities and rotations can be evaluated and compiled with polynomially many bits and gates. Near-zero subtrees can be omitted within the assigned synthesis tolerance. Allocate at most $`\epsilon/(8nM)`$ additional trace error per mode.

For polynomial $`R,M,\gamma/\beta`$ and $`\log(1/\epsilon)=\operatorname{poly}(n)`$, every cutoff, bit count and gate count above is polynomial. The reduction simply prepares the **already rotated classical labels** on the sensing half. It need not discover the source axis or implement a secret-dependent optical circuit. There is no QRAM, coherent sampling oracle or uncharged data-loading step.

An efficient collective observer means a uniform polynomial-size quantum circuit on these finite encodings, with its classical processing and all ancillary quantum systems counted. Arbitrary collective measurements of polynomial circuit complexity are included. An idealized analog instrument with infinite precision or computationally unrestricted control is not silently treated as efficient.

## P4. Finite readout and perturbations

E2 supplies a finite range and mesh for every homodyne outcome and a uniform error allowance for every contrast evaluation. A normalized net direction can also be computed to polynomial accuracy: on the retained data range, direction error $`\delta_u`$ changes its cosine by at most $`2\pi\sqrt n B\delta_u/a`$. Assign this error part of the $`\Delta/16`$ evaluation allowance. The exhaustive classical search is still exponential; finite precision does not disguise that cost.

If preparation or readout changes the entire experimental state/distribution by trace/total-variation distance $`\epsilon`$, every bounded-risk assertion changes by at most $`L_{\max}\epsilon`$, and event probabilities by at most $`\epsilon`$. Choose the error budget small compared with the target risk or advantage. These are operational stability statements. Quantum and classical Fisher information involve derivatives and are **not** automatically continuous under arbitrary small trace perturbations; F1–F4 are stated for the smooth ideal family, not for every nearby uncontrolled device.

Uniform pure loss of known transmissivity $`t\in(0,1]`$ maps a coherent state to one with amplitude reduced by $`\sqrt t`$. With the environment inaccessible, it therefore replaces $`R`$ by $`\sqrt t R`$ exactly throughout the model. Both batches must undergo the declared loss. The resolution and recovery conditions use this reduced scale. Unknown mode-dependent loss, access to the lost light, or source drift require different experiments.

## P5. Operational boundary

This is a supplied-source inference separation. An observer allowed to inject chosen coherent probes can characterize the passive mixer directly. A source program or axis-dependent advice similarly removes the hidden-learning bottleneck. The result makes no claim against those stronger access models.

[Scientific map](README.md) · [Quantum reduction](quantum-hardness.md) · [Verification](../verification/README.md)
