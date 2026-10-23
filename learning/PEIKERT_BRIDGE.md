# From Peikert to hidden optical metrology

The single educational anchor is **Chris Peikert, *A Decade of Lattice Cryptography***, using [Cryptology ePrint 2015/939](https://eprint.iacr.org/2015/939). The [90-page revised PDF](https://eprint.iacr.org/2015/939.pdf) is dated **17 February 2016**; the archive records its revision on **18 February 2016**. Section numbers below refer to that version, not to page numbers in the typeset journal edition.

The experiment asks whether data can determine an angle while every efficient quantum computation fails to extract a useful estimate. Peikert supplies the lattice and reduction language. The optical model, continuous-LWE distribution, calibration argument and metrological proofs are supplied here and in the linked scientific account. They are not attributed to the 2016 survey.

## B0. Selected reading and notation

Read these portions alongside the bridge rather than treating the whole survey as a prerequisite.

| Anchor section | Role here | Bridge |
|---|---|---|
| 2.1–2.2: notation, lattices and computational problems | Integer combinations, modular data, and precise problem statements | B1 |
| 2.3: Gaussian and discrete-Gaussian distributions | Width conventions, periodic structure and smoothing | B2–B3 |
| 2.4 opening and 2.4.1: security notions | Security experiments and computational indistinguishability | B7 |
| 4.2.1: LWE definitions | Shared secret, fresh samples, search versus decision | B1, B3 |
| 4.2.2: hardness | The direction and conditional meaning of a reduction | B7 |

The relevant printed page ranges are 6–11 and 22–25. The archive's PDF-page count includes front matter; use section numbers to avoid an offset error. No ring-LWE, encryption-system or homomorphic-encryption chapter is required for this route.

| Notation | Translation or distinction |
|---|---|
| Peikert's continuous Gaussian $`D_s`$ | The project writes a random variable with that law as $`G_s`$; its variance is $`s^2/(2\pi)`$ in one dimension |
| Discrete Gaussian $`D_{\mathbb Z,S}`$ | An integer $`K`$ with mass proportional to $`e^{-\pi k^2/S^2}`$ |
| LWE secret $`s`$ versus project axis $`w`$ | Different objects; the former is modular, the latter a real unit vector |
| Survey approximation factor $`\gamma`$ | Not the project's $`\gamma`$, which sets the periodic source frequency |
| $`\beta, R`$ | Source width and optical displacement scale, respectively; neither is a modulus |
| $`q`$ in LWE versus E2 | LWE's modulus is unrelated to the integer indexing the estimator's finite net |
| $`I_{\rm hom},F_Q`$ | Classical information in homodyne data and quantum information in the mixed optical state |

## B1. Lattice language

A lattice consists of integer combinations of independent basis vectors. For example, the two columns of

```math
B=\begin{pmatrix}2&1\\0&3\end{pmatrix}
```

generate points $`B(z_1,z_2)^T=(2z_1+z_2,3z_2)^T`$ for integer coordinates. A geometric description of these points does not itself supply an efficient algorithm for every associated problem. In bounded-distance decoding, for example, an input is promised to be near a lattice point; the algorithm must still identify that point.

The LWE language in Peikert's Section 4.2.1 replaces exact linear equations by noisy modular observations. One elementary example is a secret $`s=(3,5)`$, a public vector $`a=(2,1)`$, and modulus 17. The noiseless inner product is 11; additive error 1 produces the observation 12. A large collection uses the same secret but fresh public vectors and errors. This two-dimensional arithmetic example is not a hardness instance.

Search asks for the secret. Decision asks whether the observations came from the specified secret-bearing distribution or from the stated null distribution. A sensing lower bound can use a decision assumption even though its output is an angle, not a cryptographic key. The bridge is a reduction, developed in B7.

**Project connection:** [H1](../science/quantum-hardness.md) specifies a different, continuous decision experiment. Ordinary modular LWE samples are not silently substituted for those samples.

## B2. Gaussian width is not standard deviation

In the convention used throughout the project,

```math
G_s:\quad f_s(t)=s^{-1}e^{-\pi t^2/s^2},
\qquad \operatorname{Var}(G_s)=\frac{s^2}{2\pi}.
```

The parameter $`s`$ is a width. It is $`\sqrt{2\pi}`$ times the standard deviation. Independent Gaussian widths therefore add in quadrature: $`G_s+G_t`$ has the same law as $`G_{\sqrt{s^2+t^2}}`$.

The discrete Gaussian replaces continuous support by integer points:

```math
\Pr(K=k)=\frac{e^{-\pi k^2/S^2}}{\sum_{j\in\mathbb Z}e^{-\pi j^2/S^2}}.
```

Its normalization is a sum, not a continuous integral. A scaled discrete Gaussian plus a continuous Gaussian retains a pattern of peaks when the continuous width is sufficiently small relative to their spacing. Peikert's smoothing discussion motivates this comparison, but the optical trace-distance bound below is a separate operator calculation, not an application of a survey theorem without checking its hypotheses.

**Project connection:** [M2](../science/model.md) proves the exact mixture and tail formulas used in preparation, concentration and energy accounting.

## B3. From noisy equations to a hidden axis

The project uses homogeneous continuous LWE, abbreviated hCLWE. Its secret is a unit vector $`w\in\mathbb R^n`$. The density favors parallel layers where $`\gamma w\cdot x`$ is close to an integer:

```math
H_w(x)=\frac{e^{-\pi\|x\|^2}}{\beta C}
\sum_{k\in\mathbb Z}e^{-\pi(k-\gamma w\cdot x)^2/\beta^2},
\quad C=\sum_{\ell\in\mathbb Z}e^{-\pi(\gamma^2+\beta^2)\ell^2}.
```

The first Gaussian controls the overall envelope; the sum creates the fine structure along the unknown normal. This normalized law comes from Bruna–Regev–Song–Tang, not from Peikert's survey. Its exact source and assumption are identified in [related work](../references/RELATED_WORK.md) and [H1](../science/quantum-hardness.md).

Completing the square makes its physical interpretation more concrete. Define

```math
S^2=\gamma^2+\beta^2,\qquad a=\gamma/S^2,\qquad b^2=\beta^2/S^2.
```

Then a sample can be produced as

```math
X=(aK+G_b)w+X_\perp,
\qquad K\sim D_{\mathbb Z,S},
```

where every perpendicular coordinate is an independent $`G_1`$. The integer fixes a layer, $`G_b`$ broadens it, and $`X_\perp`$ fills the transverse directions. The source holder knows the axis; the observer does not. Both $`w`$ and $`-w`$ describe the same law, so the observable object is an unoriented axis.

The average-case hardness experiment chooses the axis once and reuses it for all samples. Choosing a fresh independent axis for every sample would define a different experiment.

## B4. Turning labels into light

Each real label $`X`$ prepares a product coherent state with mean position quadrature $`RX`$ and mean momentum quadrature zero. Here $`[Q_j,P_k]=i\delta_{jk}`$, and vacuum has variance $`1/2`$ in each quadrature. The corresponding usual coherent amplitude is $`RX/\sqrt2`$.

The observer receives the mixture

```math
\sigma_w=\mathbb E_{X\sim H_w}|RX\rangle_Q\langle RX|,
```

not the classical label, a coherent superposition of labels, or a purification of that mixture. This matters: sensitivity available to an observer who knows $`X`$ is not automatically available after $`X`$ is discarded. The state needs neither squeezed inputs nor entanglement between modes.

For even $`n`$, set

```math
J=\bigoplus_{j=1}^{n/2}\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad O_\theta=\cos\theta\,I+\sin\theta\,J.
```

A layer of passive two-mode rotations applies $`O_\theta`$ to both quadrature vectors, changing the source axis to $`O_\theta w`$. A Gaussian-label null source is invariant under this real mode mixing. It is not invariant under an arbitrary rotation of a mode's position into its momentum, since its two quadrature variances differ. That distinction is essential to the lower bound.

Both observers receive independent calibration pulses with axis $`w`$ and sensing pulses with axis $`O_\theta w`$. No pulse's before-and-after label is revealed. Without calibration, averaging over the uniformly random source axis makes the complete sensing-only experiment independent of $`\theta`$. The calibration batch is an information resource, not an optional courtesy.

**Canonical account:** [M3–M5](../science/model.md).

## B5. Readout, Fourier contrast and global recovery

Homodyne detection measures every laboratory $`Q`$ quadrature. Dividing its output by $`R`$ gives

```math
Y=X+G_s^{\otimes n},\qquad s^2=\pi/R^2.
```

This formula follows because a coherent state's measurement noise has variance $`1/2`$ before rescaling. Along the hidden axis, the observed coordinate is $`aK+G_c`$ with $`c^2=b^2+s^2`$; perpendicular coordinates have width $`h`$ with $`h^2=1+s^2`$.

For each trial unit direction $`u`$, compute the empirical average of the bounded statistic

```math
\cos(2\pi u\cdot Y/a).
```

At the true axis, the integer contribution disappears inside the cosine, leaving expected value $`A=e^{-\pi c^2/a^2}`$. Wrong trial axes mix in transverse Gaussian noise. The population contrast obeys

```math
F_w(u)\le A\exp\{-\pi S^2[1-(u\cdot w)^2]\}.
```

This supplies a gap away from the two equivalent true directions. A finite search over a sufficiently fine spherical net, with concentration of these bounded empirical averages, recovers the axis. The number of observations is polynomial in the declared resolved regime, but the number of trial directions grows exponentially with dimension. Data sufficiency and computational efficiency are different statements.

Perform that search separately on calibration and sensing records, yielding axes $`u,v`$. Their relative angle is read through

```math
\widehat\theta=\operatorname{clip}_{[-\pi/8,\pi/8]}
\arctan\frac{(Ju)\cdot v}{u\cdot v}.
```

Changing either axis sign changes both inner products' signs and leaves the ratio unchanged. [E2–E3](../science/estimation.md) prove finite-copy, finite-precision and squared-risk guarantees; no Fisher-information argument is used in that proof.

## B6. Worked two-mode example

Take $`n=2`$, $`\beta=0.2`$, $`\gamma=3`$, $`R=15`$. The scale conversions give

```math
a\approx0.3318584,\quad b^2\approx0.00442478,
\quad s^2\approx0.01396263,\quad c^2\approx0.01838741.
```

Thus $`c^2/a^2\approx0.166961`$, and the expected contrast at the correct axis is about **0.591837**. At a perpendicular direction it is about **$`2.7431\times10^{-13}`$**. These are population expectations, not empirical values guaranteed from a few pulses.

For interpretation, let the actual calibration axis make angle 0.6 radians with the first laboratory mode and let the mixer angle be 0.2 radians. The sensing axis then has angle 0.8. The experiment does not reveal either axis. The estimator scans its trial directions and estimates them from separate batches. With exact axis recovery, its two inner products are $`\cos(0.2)`$ and $`\sin(0.2)`$, producing the answer 0.2 despite either sign ambiguity.

One pulse uses at most $`2(15)^2/(4\pi)\approx35.8099`$ mean probe photons. A demonstration with 1,500 pulses in each batch therefore counts 3,000 pulses and at most about **107,430 mean probe photons**. It does not count calibration as free.

The existing [verification script](../verification/verify.py) performs eight seeded two-batch trials at these optical parameters with a 2,048-direction circle grid. Its [stored report](../verification/expected_results.json) has maximum angle error about 0.008947 radians. This is a low-dimensional illustration, not a hard cryptographic instance or a substitute for E2's deliberately conservative sample theorem. The extra [bridge checks](../verification/check_learning.py) verify the displayed conversions and angle geometry.

## B7. Why efficient quantum inference is covered

Use a uniform angle prior on $`[-\theta_0,\theta_0]`$ with $`\theta_0=\pi/8`$. Without data, the estimate zero has optimal squared risk $`r_0=\theta_0^2/3`$. The computational theorem asks whether an efficient procedure can improve this average risk by a nonnegligible amount.

A reduction receives classical samples from the hCLWE-versus-Gaussian decision experiment. It chooses an angle itself, prepares unrotated coherent states for calibration and rotated states for sensing, then runs the proposed quantum estimator. It knows the chosen angle and can score the answer. A bounded loss can be converted into the probability of a binary test.

If the samples were Gaussian, the optical input is independent of the angle and cannot beat the prior-only optimum. An appreciably smaller risk on the hCLWE source would therefore distinguish the two classical experiments. The preparation uses polynomial energy, bits and gates, so it also simulates the input to an efficient collective quantum measurement. No stronger coherent sample oracle is assumed.

This is the reduction logic familiar from Peikert, with a new preparation map and a separately stated hCLWE assumption. [H1–H4](../science/quantum-hardness.md) and [P2–P3](../science/resources.md) give the complete statement. The conclusion is conditional, averaged over the hidden axis and prior, and restricted to the supplied-source interface. It is not a proof of absolute cryptographic security.

## B8. Three boundaries and two kinds of information

At low optical scale, fine source structure is lost in the quantum state itself. [R1–R2](../science/resolution.md) prove this by an operator Fourier expansion and trace norm, which control every measurement. A bound on homodyne data alone would not justify that conclusion.

At $`R^2\ge c_0\gamma^2/\log n`$ for fixed positive $`c_0`$, the global estimator uses polynomially many pulses. Below $`R^2=o(\gamma^2/\log n)`$, every polynomial-copy experiment is negligibly close to an angle-independent null. These asymptotic regimes identify a polynomial-copy resolution scale, not optimal finite constants.

In the more strongly resolved regime $`R=\gamma/\beta`$, $`\beta\to0`$, homodyne preserves at least a constant fraction of mixed-state quantum Fisher information. Classical Fisher information measures local sensitivity of outcome probabilities; quantum Fisher information bounds what measurements can extract locally. Neither quantity alone constructs a globally accurate or efficient estimator. The exact comparison and its hypotheses are in [F1–F3](../science/fisher-information.md).

Because the source axis is unknown, calibration must also be charged in this local comparison. Removing the source nuisance coordinates multiplies each per-copy information by

```math
\frac{N_cN_s}{N_c+N_s}.
```

For equal batches, this is one quarter of their combined pulse count. The information fraction survives; the cost does not disappear. The quantum matrix supplies a bound, not automatic attainability of a multiparameter Cramér–Rao inequality.

The full conclusion therefore needs three separate proofs: optical structure survives, the same finite data support a global estimate, and efficient quantum computation cannot extract a useful estimate under the stated assumption. Revealing the source axis or allowing chosen replacement probes changes the task. Known uniform pure loss simply replaces $`R`$ by $`\sqrt t R`$; arbitrary imperfections do not automatically preserve derivative-based Fisher information.

Return to the [30-milestone map](MILESTONES.md), the [scientific map](../science/README.md), or the [verification guide](../verification/README.md). The primary literature remains available for attribution and proof dependencies; it is not a second educational-anchor assignment.
