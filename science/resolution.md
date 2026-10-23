# Optical resolution and the polynomial-copy boundary

All notation is defined in the [model](model.md). Let $`D(\rho,\sigma)=\|\rho-\sigma\|_1/2`$. This page concerns the optical states themselves, so its upper bounds apply to every measurement, not only homodyne detection.

## R1. Exact operator Fourier identity

Define

```math
A_\ell=\int_{\mathbb R^n}e^{-\pi\|x\|^2}e^{2\pi i\ell\gamma w\cdot x}
|Rx\rangle_Q\langle Rx|\,dx,
```

Then

```math
\sigma_w=C^{-1}\sum_{\ell\in\mathbb Z}e^{-\pi\beta^2\ell^2}A_\ell,
\qquad A_0=\tau_R.
```

In coordinates with first axis $`w`$, the one-dimensional position kernel of the null is

```math
\tau_R(q,q')=\frac{1}{\sqrt{\pi+R^2}}
\exp\left[-\frac{q^2+q'^2}{2}
+\frac{R^2(q+q')^2}{4(\pi+R^2)}\right].
```

Completing the Gaussian integral with the Fourier factor gives

```math
A_\ell=e^{-\pi^2\ell^2\gamma^2/(\pi+R^2)}U_\ell\tau_R U_\ell,
\qquad
U_\ell=\exp\left[\frac{i\pi\ell\gamma R}{\pi+R^2}Q_w\right].
```

There is intentionally **no adjoint** on the rightmost unitary: a Fourier component is generally not a positive operator. Left and right unitary multiplication nevertheless preserve the trace norm, so

```math
\|A_\ell\|_1=e^{-\pi^2\ell^2\gamma^2/(\pi+R^2)}.
```

The remaining modes factor as normalized Gaussian states. The same identity therefore holds in every dimension. Absolute trace-norm convergence justifies summing the components.

## R2. Measurement-independent upper bound

Set

```math
\zeta^2=\beta^2+\frac{\pi\gamma^2}{\pi+R^2},
\qquad
B_R=\frac{\sum_{\ell\ge1}e^{-\pi\zeta^2\ell^2}
+\sum_{\ell\ge1}e^{-\pi S^2\ell^2}}{C}.
```

Then

```math
D(\sigma_w,\tau_R)\le\min\{1,B_R\},\qquad
B_R\le\frac{2e^{-\pi\zeta^2}}{1-e^{-3\pi\zeta^2}}.
```

**Proof.** Subtract $`\tau_R`$ from R1. The zero Fourier coefficient contributes $`-(C-1)\tau_R/C`$. Apply the triangle inequality to that term and all nonzero components, with the factor $`1/2`$ in trace distance. Pair positive and negative indices to obtain $`B_R`$. Since $`\zeta^2\le S^2`$, bound both positive-index sums by the first one. Finally $`\ell^2\ge1+3(\ell-1)`$ for $`\ell\ge1`$ gives the geometric series.

For $`M=N_c+N_s`$ pulses, tensor telescoping and mixing over $`w`$ give distance at most $`\min\{1,MB_R\}`$ from the angle-independent null experiment. Consequently every estimator, including one with unlimited computation, obeys

```math
\mathbb E(\widehat\theta-\theta)^2
\ge r_0-L_{\max}\min\{1,MB_R\}.
```

This finite statement includes all calibration pulses. It does not assume a specific readout or an unbiased estimator.

## R3. A resolved homodyne witness

Homodyne readout divided by $`R`$ gives $`Y=X+G_s^{\otimes n}`$ with $`s^2=\pi/R^2`$. Define

```math
c^2=b^2+s^2,\quad h^2=1+s^2,\quad r^2=c^2/a^2,\quad A=e^{-\pi r^2}.
```

The bounded function $`\cos(2\pi w\cdot Y/a)`$ has expectation $`A`$ under the source and $`e^{-\pi h^2/a^2}`$ under the null. Since $`(h^2-c^2)/a^2=S^2`$,

```math
D(\sigma_w,\tau_R)\ge\frac{A}{2}(1-e^{-\pi S^2}).
```

The observable here uses the axis only as an information-theoretic witness. The implementable measurement is ordinary homodyne in fixed laboratory quadratures; the [global estimator](estimation.md) learns the axis rather than receiving it.

## R4. Matching polynomial-copy scale

Assume the hard-family parameter range in M1, with $`n\to\infty`$ and all nonprecision parameters polynomially bounded.

If $`R^2=o(\gamma^2/\log n)`$, then $`\zeta^2/\log n\to\infty`$. R2 implies that every polynomial number of pulses is negligibly close to the null. Thus no estimator can achieve a nonnegligible Bayes-risk improvement, independently of any computational assumption.

Conversely, for any fixed $`c_0>0`$, if

```math
R^2\ge c_0\frac{\gamma^2}{\log n},
```

then

```math
r^2=\frac{\beta^2S^2}{\gamma^2}
+\frac{\pi S^4}{R^2\gamma^2}=O(\log n),
```

so $`A`$ is inverse-polynomial. The finite estimator theorem E2 then recovers any inverse-polynomial angle accuracy with polynomially many calibration and sensing pulses. Its computational search remains exponential.

These are matching *polynomial-versus-superpolynomial copy* regimes, not a universal sharp numerical constant or an optimal finite-sample rate. The polynomial degree can depend on $`c_0`$ and the requested accuracy. In total probe photons per pulse, the scale is of order $`n\gamma^2/\log n`$, using the energy formula in [resources](resources.md).

[Scientific map](README.md) · [Global recovery](estimation.md)
