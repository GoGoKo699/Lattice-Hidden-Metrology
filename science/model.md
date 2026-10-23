# Supplied-source optical estimation

The task is to estimate one passive **mode-mixing angle** from a calibratable source of ordinary coherent light. The source has a fixed, unknown axis. Independent calibration and sensing pulses share that axis, but not their individual displacement labels. The statistical and computational observers receive exactly the same pulses.

## M1. Distribution and conventions

There are an even number $`n\ge2`$ of modes. Quadratures satisfy $`[Q_j,P_k]=i\delta_{jk}`$; vacuum has variance $`1/2`$ in each quadrature. Write $`G_s`$ for a real Gaussian with density $`s^{-1}e^{-\pi t^2/s^2}`$, hence variance $`s^2/(2\pi)`$. The normalized $`n`$-dimensional Gaussian in lattice-theory width convention has density $`e^{-\pi\|x\|^2}`$.

Choose a unit vector $`w`$ once, uniformly on the sphere for the hardness experiment. With public $`\beta,\gamma>0`$, let

```math
H_w(x)=\frac{e^{-\pi\|x\|^2}}{\beta C}
\sum_{k\in\mathbb Z}e^{-\pi(k-\gamma w\cdot x)^2/\beta^2},
\qquad
C=\sum_{\ell\in\mathbb Z}e^{-\pi S^2\ell^2},\quad S^2=\gamma^2+\beta^2.
```

This is the homogeneous continuous-LWE distribution of Bruna, Regev, Song and Tang, Definition 2.19. Poisson summation gives the equivalent normalized Fourier expansion

```math
H_w(x)=\frac{e^{-\pi\|x\|^2}}{C}
\sum_{\ell\in\mathbb Z}e^{-\pi\beta^2\ell^2}
e^{2\pi i\ell\gamma w\cdot x}.
```

For the computational theorem use $`0<\beta<1`$, $`\gamma\ge2\sqrt n`$, polynomially bounded $`\gamma/\beta`$, and polynomially bounded optical scale $`R>0`$. The analytical identities need only positive parameters. The exact assumption and its lattice connection are in [quantum hardness](quantum-hardness.md); no standardized cryptosystem is being attacked.

## M2. Sampling representation and moments

Define

```math
a=\frac{\gamma}{S^2},\qquad b^2=\frac{\beta^2}{S^2},\qquad
K\sim D_{\mathbb Z,S},\qquad T_0=aK+G_b.
```

Here $`\Pr(K=k)\propto e^{-\pi k^2/S^2}`$. Completing the square in M1 shows that

```math
X=T_0w+X_\perp,
```

where the perpendicular coordinates are independent $`G_1`$ variables and independent of $`K,G_b`$. This is both an exact description and a finite-precision source-preparation route when the preparer knows $`w`$.

The characteristic-function expansion yields

```math
\mathbb E T_0^2=\frac1{2\pi}
-\frac{\gamma^2}{C}\sum_{\ell\in\mathbb Z}\ell^2e^{-\pi S^2\ell^2}
\le\frac1{2\pi}.
```

A useful stronger fact is $`\mathbb E e^{v\cdot X}\le e^{\|v\|^2/(4\pi)}`$. To prove it, complete the square in the moment-generating function of $`K`$. The remaining shifted Gaussian sum is maximized at an integer shift, by its Poisson expansion with nonnegative Fourier coefficients. Thus $`\mathbb E e^{tK}\le e^{S^2t^2/(4\pi)}`$. Combine the independent terms and use $`a^2S^2+b^2=1`$. In particular, every coordinate satisfies $`\Pr(|X_j|>B)\le2e^{-\pi B^2}`$.

## M3. Optical source and encoding

Let $`|z\rangle_Q`$ denote a product coherent state with mean $`Q=z`$, mean $`P=0`$, and ordinary coherent amplitudes $`z/\sqrt2`$. Prepare

```math
\sigma_w=\mathbb E_{X\sim H_w}|RX\rangle_Q\langle RX|,
\qquad
\tau_R=\mathbb E_{X\sim G_1^{\otimes n}}|RX\rangle_Q\langle RX|.
```

The displacement label is discarded, not supplied to the observer. These are separable positive mixtures of coherent states. No squeezing or entanglement is needed in the source.

Fix the public real matrix

```math
J=\bigoplus_{j=1}^{n/2}\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad O_\theta=e^{\theta J}=\cos\theta\,I+\sin\theta\,J.
```

The passive unitary applies the same $`O_\theta`$ to the $`Q`$ and $`P`$ mode vectors. It consists of parallel two-mode rotations and sends $`\sigma_w`$ to $`\sigma_{O_\theta w}`$. It preserves photon number. The null state $`\tau_R`$ is invariant under every such real orthogonal mode mixing.

**This is not an arbitrary optical phase shift.** The null has $`V_Q=(1/2+R^2/(2\pi))I`$ and $`V_P=I/2`$. Rotating a mode's $`Q`$ into its $`P`$ generally changes that covariance and permits efficient angle estimation. Null invariance, and hence the hardness reduction, requires the specified real mixing action.

## M4. Equal-access experiment

For $`N_c`$ calibration and $`N_s`$ sensing pulses, the conditional state is

```math
\Omega_{w,\theta}
=\sigma_w^{\otimes N_c}\otimes\sigma_{O_\theta w}^{\otimes N_s}.
```

Take $`\theta\in[-\theta_0,\theta_0]`$ with $`\theta_0=\pi/8`$. The squared-loss benchmark uses the uniform prior, independent of $`w`$, and estimates clipped to this interval. Its prior-only Bayes risk is $`r_0=\theta_0^2/3`$ and loss is bounded by $`L_{\max}=4\theta_0^2`$.

Both observers know the public model and receive the same independently emitted batches. Neither receives $`w`$, the source program, the individual labels, a purification, paired input/output pulses, or chosen-probe access to the interferometer. Efficient quantum observers may use collective measurements, polynomial ancillary systems, adaptive processing and polynomial preprocessing of calibration data. Those resources are counted, not excluded.

The [resource account](resources.md) defines finite precision and computation. The [estimator](estimation.md) supplies an unrestricted classical postprocessor for the same homodyne data; it is not a free-secret benchmark.

## M5. Calibration is indispensable

For any number of sensing pulses alone,

```math
\int \sigma_{O_\theta w}^{\otimes N_s}\,dw
=\int \sigma_w^{\otimes N_s}\,dw,
```

by rotational invariance of the hidden-axis prior. Thus the sensing-only Bayesian experiment is exactly independent of the angle. Calibration resolves this identifiability issue. Fixed-source Fisher information must not be confused with Fisher information after averaging out an uncalibrated source.

[Scientific map](README.md) · [Related work](../references/RELATED_WORK.md)
