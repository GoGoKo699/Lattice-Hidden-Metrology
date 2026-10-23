# Information surviving homodyne readout

The local information result complements, but does not replace, the [global recovery theorem](estimation.md). Here $`w`$ is a fixed source parameter. The classical Fisher information is that of the full homodyne law after averaging over the inaccessible displacement label. The quantum Fisher information is that of the corresponding mixed optical state.

For a differentiable outcome density, $`I_{\rm hom}=\mathbb E(\partial_\theta\log p_\theta)^2`$. For a differentiable state, define the symmetric logarithmic derivative $`\mathcal L`$ by $`\partial_\theta\rho=(\rho\mathcal L+\mathcal L\rho)/2`$ and $`F_Q=\operatorname{Tr}(\rho\mathcal L^2)`$. These are information measures, not claims that their optimal estimators or measurements are computationally accessible.

## F1. A mixed-distribution Fisher witness

In the plane spanned by $`w,Jw`$, homodyne outcomes at zero angle have independent coordinates

```math
T=aK+G_c,\qquad Z\sim G_h,
```

with the notation of R3. Set $`k_0=2\pi/a`$, $`A=e^{-\pi r^2}`$, and consider the real statistic $`g(T,Z)=Z\sin(k_0T)`$.

Under angle encoding, these two coordinates become $`(T\cos\theta-Z\sin\theta,T\sin\theta+Z\cos\theta)`$. Direct differentiation gives

```math
\left.\frac{d}{d\theta}\mathbb E_\theta g\right|_{\theta=0}
=\mathbb E[T\sin(k_0T)]-k_0\mathbb E Z^2\mathbb E\cos(k_0T)
=-\gamma A.
```

Indeed, integer $`K`$ makes the sine insensitive to its shift, $`\mathbb E[T\sin(k_0T)]=c^2A/a`$, and $`(h^2-c^2)/a=\gamma`$. Also

```math
\operatorname{Var}(g)=\frac{h^2}{4\pi}(1-e^{-4\pi r^2}).
```

The score identity $`\partial_\theta\mathbb E g=\mathbb E[(g-\mathbb E g)\partial_\theta\log p_\theta]`$ and Cauchy–Schwarz therefore prove

```math
I_{\rm hom}\ge
\frac{2\pi\gamma^2}{h^2\sinh(2\pi r^2)}.
```

The witness is a tool for bounding information; it is not an estimator given the secret axis. Homodyne measures all laboratory $`Q`$ quadratures without knowing $`w`$. Rotating the recorded coordinates for this calculation does not require a hidden-axis-dependent optical operation.

## F2. Quantum upper bound for the actual mixed state

For a fixed axis, the state factors into its special one-mode mixture and identical Gaussian perpendicular modes. Since $`J^2=-I`$, the axis orbit lies entirely in the two-dimensional plane $`\operatorname{span}\{w,Jw\}`$. A rotation restricted to this plane generates exactly the same state family as the physical parallel rotation: the difference acts within an invariant perpendicular Gaussian sector.

Use that plane-restricted representation, with independent input labels $`T_0,G_1`$. The pure coherent pair has quantum Fisher information $`2R^2(T_0^2+G_1^2)`$. Convexity of quantum Fisher information for a parameter-independent mixture and M2 give

```math
I_{\rm hom}\le F_Q(\sigma_{O_\theta w})
\le2R^2\left(\mathbb E T_0^2+\frac1{2\pi}\right)
\le\frac{2R^2}{\pi}.
```

The first inequality is measurement monotonicity. The pure-state quantity appears only as an **upper bound** on the mixed-state information, not as a replacement for it. Rotational covariance makes these bounds independent of $`w`$ and $`\theta`$.

## F3. Constant-fraction regime

For $`R=\gamma/\beta`$, $`\beta\to0`$, and $`\gamma\ge2\sqrt n`$,

```math
h^2\to1,\qquad r^2=(1+\pi+o(1))\beta^2,
```

and hence

```math
I_{\rm hom}\ge\left(\frac1{1+\pi}+o(1)\right)R^2,
\qquad
\liminf\frac{I_{\rm hom}}{F_Q}\ge\frac{\pi}{2(1+\pi)}.
```

The lower-bound fraction is approximately $`0.379`$. Thus both informations scale as $`\Theta(R^2)`$. This deep-resolution regime is stronger than the lower-energy condition needed merely for polynomial-copy global recovery. Neither an exact optimal fraction nor a super-shot-noise advantage is asserted.

## F4. Charging the unknown source in the local comparison

The source axis is a nuisance parameter. Choose orthonormal local tangent coordinates for the sphere at $`w`$ with the first tangent $`Jw`$. By invariance under orthogonal rotations fixing $`w`$, the per-copy homodyne axis-information matrix is $`I_{\rm hom}I_{n-1}`$, and the corresponding quantum matrix is $`F_QI_{n-1}`$. These scalars equal the information along the unit-speed angle orbit.

For independent calibration and sensing batches the joint matrix is, for $`f=I_{\rm hom}`$ or $`f=F_Q`$,

```math
\mathcal I_f=f
\begin{pmatrix}
(N_c+N_s)I_{n-1}&N_s e_1\\
N_s e_1^T&N_s
\end{pmatrix}.
```

The upper-left block describes source-axis variation. The off-diagonal block follows because a change of the first source tangent and a change of the signal angle induce the same infinitesimal signal-axis motion. The Schur complement eliminating the nuisance coordinates is

```math
I_{\rm eff}=\frac{N_cN_s}{N_c+N_s}I_{\rm hom},
\qquad
F_{\rm eff}=\frac{N_cN_s}{N_c+N_s}F_Q.
```

Thus the same constant-fraction comparison survives local nuisance elimination, with the full calibration cost retained. $`F_{\rm eff}`$ is a quantum-information bound, not a claim that every multiparameter quantum Cramér–Rao bound is attainable.

These are local frequentist matrices at fixed $`w`$, not the Fisher information of a state obtained by averaging the unknown axis first. M5 shows why that distinction matters. E2–E3, separately, establish global operational recovery for the same-data experiment. No efficiency or global-risk conclusion is deduced from Fisher information alone.

[Scientific map](README.md) · [Related work and foundations](../references/RELATED_WORK.md)
