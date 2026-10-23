# Global angle recovery with equal calibration access

A Fisher-information bound is local. This page supplies an actual global estimator and a finite error guarantee without knowing the source axis. The two sample batches have the same sizes and distributions as those provided to the efficient quantum observer.

## E1. Exact Fourier contrast and population gap

Use the homodyne notation of [R3](resolution.md). For a trial unit vector $`u`$, define

```math
F_w(u)=\mathbb E\cos(2\pi u\cdot Y/a).
```

Writing $`t=u\cdot w`$ and using M2 gives the exact expression

```math
F_w(u)=e^{-\pi[c^2t^2+h^2(1-t^2)]/a^2}
\mathbb E_K\cos(2\pi Kt).
```

Since $`K`$ is integer-valued, $`F_w(w)=F_w(-w)=A`$. Since a characteristic function is at most one,

```math
F_w(u)\le A e^{-\pi S^2[1-(u\cdot w)^2]}.
```

Thus every direction with projective error $`\sqrt{1-(u\cdot w)^2}\ge\eta`$ lies at least

```math
\Delta=A(1-e^{-\pi S^2\eta^2})
```

below the optimum. This elementary contrast need not be monotone at every intermediate direction; only its exact maxima and this upper envelope are needed.

Also $`\mathbb E\|Y\|^2\le nh^2/(2\pi)`$, so the cosine Lipschitz inequality and Cauchy–Schwarz give

```math
|F_w(u)-F_w(v)|\le L\|u-v\|,
\qquad L=\frac{\sqrt{2\pi n}\,h}{a}.
```

The proof uses the actual noisy data law, not noiseless labels.

## E2. Explicit finite-copy estimator

Choose $`0<\eta\le1/16`$ and $`0<p<1`$. Set

```math
\rho=\min\{1/2,\Delta/(8L)\},\qquad
q=\left\lceil2\sqrt n/\rho\right\rceil,
```

and take the finite set obtained by normalizing every nonzero vector $`k/q`$ with $`k\in\{-q,\ldots,q\}^n`$. It is a $`\rho`$-net of the sphere and has at most $`(2q+1)^n`$ points. Indeed, coordinatewise rounding of any unit vector has Euclidean error at most $`\sqrt n/(2q)`$, and normalization increases that error by at most a factor of two.

For **each** of the calibration and sensing batches use

```math
N=\left\lceil\frac{128}{\Delta^2}
\left[n\log(2q+1)+\log(8/p)\right]\right\rceil
```

independent pulses. Measure every $`Q`$ quadrature and divide the outcomes by $`R`$. For each batch maximize the empirical cosine contrast over the same net. Numerical evaluation and data quantization together may perturb every empirical contrast by at most $`\Delta/16`$.

**Guarantee.** With probability at least $`1-p`$, the two maximizing axes $`u,v`$ satisfy

```math
\sqrt{1-(u\cdot w)^2}<\eta,\qquad
\sqrt{1-(v\cdot O_\theta w)^2}<\eta.
```

**Proof.** For bounded observations in $`[-1,1]`$, Hoeffding's inequality gives probability at most $`2e^{-N\Delta^2/128}`$ for a contrast deviation exceeding $`\Delta/8`$ at one net point. A union bound gives failure at most $`p/4`$ per batch. A net point near the true axis has population value at least $`A-\Delta/8`$. On the concentration event the maximizer's population value is at least

```math
A-\Delta/8-2(\Delta/8)-2(\Delta/16)=A-\Delta/2.
```

E1 excludes projective error at least $`\eta`$.

For finite data storage, set

```math
B=h\sqrt{\pi^{-1}\log(8nN/p)}.
```

The subgaussian bound from M2, after convolution, implies that all $`2nN`$ observed coordinates lie in $`[-B,B]`$ except with probability at most $`p/2`$. Round each retained coordinate on a mesh at most $`a\Delta/(64\pi\sqrt n)`$ and compute each cosine, including finite representation of its normalized net direction, to absolute error at most $`\Delta/64`$. Their total contribution is below the permitted $`\Delta/16`$. Output zero if a coordinate exceeds the declared range. Combining both concentration events and this tail event proves the stated probability. All logarithms are natural.

## E3. Recovering the angle without orienting either axis

Define

```math
\widehat\theta=
\operatorname{clip}_{[-\theta_0,\theta_0]}
\arctan\left(\frac{(Ju)\cdot v}{u\cdot v}\right).
```

Use the principal arctangent; if the denominator is zero, output zero. This fallback is not needed on the success event. Flipping either inferred axis changes the numerator and denominator by the same sign, so the estimator is well defined on unoriented axes.

The exact relation is

```math
w\cdot O_\theta w=\cos\theta,\qquad
(Jw)\cdot O_\theta w=\sin\theta.
```

For analysis only, orient $`u,v`$ to be within $`\sqrt2\eta`$ of the true axes. Each of the two inner products then differs from its ideal value by at most $`2\sqrt2\eta`$. The two-component vector differs from the unit vector $`(\cos\theta,\sin\theta)`$ by at most $`4\eta\le1/4`$. Its angular error is at most $`\arcsin(4\eta)\le8\eta`$. The prior interval stays away from the arctangent branch cut. Clipping cannot increase the error. Therefore

```math
\Pr(|\widehat\theta-\theta|\le8\eta)\ge1-p,
\qquad
\mathbb E(\widehat\theta-\theta)^2\le64\eta^2+4\theta_0^2p.
```

This bound is uniform in the hidden axis and the allowed angle. It counts $`2N`$ pulses, including calibration.

## E4. Complexity and attribution

If $`r^2=O(\log n)`$, public parameters have polynomial size, and the target accuracy and failure probability are inverse-polynomial, then $`\Delta^{-1},L,N,B`$ and the required number of stored bits are polynomially bounded. Exhaustive evaluation over $`(2q+1)^n`$ trial directions is generally exponential. No efficiency advantage is claimed for that search.

Gaussian-pancake parameter recovery by projection pursuit already appears in Song's NeurIPS 2024 Theorem 4.2 (Theorem 4.6 in arXiv v1). E1–E3 provide a self-contained bounded-cosine proof for the optical noise law, with explicit copy and calibration costs, and a sign-invariant angle readout. The existence of a classical statistical-to-computational learning gap is inherited, not claimed as new.

[Scientific map](README.md) · [Quantum hardness](quantum-hardness.md) · [Related work](../references/RELATED_WORK.md)
