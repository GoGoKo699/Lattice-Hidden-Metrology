# Hardness against efficient collective quantum estimation

## H1. The exact assumption

Use the parameter range and finite-precision model in [M1](model.md) and [resources](resources.md). Assume **quantum decisional hCLWE hardness**: for every polynomial sample count and every uniform quantum polynomial-time distinguisher, the following classical-input experiments have negligibly different acceptance probabilities:

```math
\text{one uniform hidden }w,\quad X_1,\ldots,X_M\overset{\mathrm{iid}\mid w}{\sim}H_w;
\qquad
X_1,\ldots,X_M\overset{\mathrm{iid}}{\sim}G_1^{\otimes n}.
```

Samples are supplied at the polynomial-bit precisions used by the reduction, with negligible sampling/rounding error relative to the corresponding rounded ideal distributions. There is no coherent sample oracle, QRAM, or advice correlated with $`w`$.

This is a stated computational assumption, not a theorem tested numerically. Bruna–Regev–Song–Tang, Definition 2.21 and Corollary 4.2, provide the quantum worst-case-lattice reduction in the specified regime. The present result does not identify these parameters with any deployed LWE scheme. The separate LWE-to-CLWE reductions of Gupte–Vafa–Vaikuntanathan give additional context, not an unperformed parameter transfer.

## H2. Prior-risk theorem

Under H1, for every uniform quantum polynomial-time estimator acting on any polynomial numbers of calibration and sensing pulses,

```math
\mathbb E_{w,\theta,\mathrm{measurement}}
(\widehat\theta-\theta)^2\ge\frac{\theta_0^2}{3}-\operatorname{negl}(n).
```

The expectation includes the random source axis and independent uniform angle prior. Estimates can be clipped without increasing risk. The result is an average-case statement, not hardness for every fixed public axis.

The estimator may perform arbitrary efficient collective measurements on both batches, with polynomial workspace and adaptive quantum/classical processing. It is not restricted to a classical postprocessor or to homodyne detection.

## H3. Reduction

Given the classical hCLWE challenge samples, the reduction draws its own angle from the declared prior, splits the samples into the two promised batches, and performs the efficient classical-to-quantum preparation

```math
X_j\longmapsto|RX_j\rangle_Q\quad\text{(calibration)},
\qquad
X_j\longmapsto|RO_\theta X_j\rangle_Q\quad\text{(sensing)}.
```

It does not know or need the hidden axis. It then runs the candidate estimator, including its entire collective measurement, and records a Bernoulli variable with conditional success probability

```math
(\widehat\theta-\theta)^2/(4\theta_0^2).
```

The angle is known to the reduction, not supplied to the estimator.

In the hCLWE experiment this is the promised optical sensing task. In the Gaussian experiment both batches are copies of $`\tau_R`$, independent of the sampled angle, because $`O_\theta`$ is real orthogonal. Even a randomized estimator then has squared risk at least $`\theta_0^2/3`$. If the two optical risks differed by an inverse-polynomial amount, the Bernoulli test would distinguish the classical challenges by an inverse-polynomial amount, contradicting H1.

All classical preparation arithmetic, coherent-state synthesis and prior sampling can be carried out to negligible total error in polynomial resources, as proved in [resources](resources.md). Trace-distance contraction transfers that error through any subsequent measurement. This proves H2 without assuming that classical hardness automatically survives a stronger input interface: the required input interface is explicitly simulated.

## H4. Finite error and general losses

Let $`\epsilon_P,\epsilon_Q`$ bound the simulator's trace-distance error in the two cases and let $`\epsilon_{\rm test}`$ bound its Bernoulli/angle approximation error. For a loss in $`[0,L_{\max}]`$, an ideal risk improvement $`d`$ gives distinguishing advantage at least

```math
d/L_{\max}-\epsilon_P-\epsilon_Q-\epsilon_{\rm test}.
```

The same argument applies to any bounded, efficiently evaluable loss and efficiently samplable prior, with the corresponding prior-only optimal risk. No claim of exact zero advantage at finite dimension is implied.

Polynomial preprocessing of calibration data is already included. Allowing a separate uncharged preprocessing phase of arbitrary duration, revealing the source axis, or permitting chosen replacement probes changes the experiment and is not covered.

## H5. What is separated

E2–E3 provide inverse-polynomial risk using polynomially many of the same pulses whenever $`R^2\ge c_0\gamma^2/\log n`$. H2 prevents every uniform efficient quantum observer from achieving even a nonnegligible prior-risk improvement under H1. The contrast is **unrestricted inference versus efficient quantum inference**, not quantum versus classical speedup.

[Scientific map](README.md) · [Global estimator](estimation.md) · [Finite resources](resources.md)
