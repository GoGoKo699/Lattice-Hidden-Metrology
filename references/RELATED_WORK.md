# Related work and imported ingredients

The source comparison was checked on 23 October 2026. It distinguishes a new optical inference statement from existing cryptographic learning gaps. It is a targeted primary-source comparison, not an exhaustive priority certificate.

## Continuous LWE: the source and computational assumption

Joan Bruna, Oded Regev, Min Jae Song and Yi Tang, **Continuous LWE**, arXiv:2005.09595v2 (24 October 2020; STOC 2021), supplies the homogeneous source in Definition 2.19, its Gaussian-mixture representation in equation (2), the decision experiment in Definition 2.21, and the lattice reduction in Corollary 4.2. The latter applies for $`0<\beta<1`$, $`\gamma\ge2\sqrt n`$, and polynomially bounded $`\gamma/\beta`$.

This project imports that distribution and states quantum decisional hCLWE hardness explicitly. It does not prove cryptographic hardness unconditionally. Its added reduction efficiently prepares the optical experiment from classical challenge samples, including a privately sampled angle and both data batches, so an efficient collective quantum estimator would violate that assumption. See [H1–H4](../science/quantum-hardness.md).

Source: [arXiv version and full paper](https://arxiv.org/abs/2005.09595v2).

## Gaussian-pancake learning: the closest classical antecedent

Min Jae Song, **Cryptographic Hardness of Score Estimation**, NeurIPS 2024, establishes a statistical-to-computational gap for Gaussian-pancake score learning. Section 4 and Theorem 4.2 give polynomial-sample hidden-direction recovery by exhaustive projection pursuit in the stated constant smoothing-spacing regime. The arXiv v1 counterpart is Theorem 4.6. Section 4 also discusses Gaussian indistinguishability beyond a growing smoothing scale.

The distributions are unchanged by reversing their hidden direction. The operational object here is therefore an **unoriented axis**; we do not import a signed-direction recovery claim. Our E1–E3 proof is independent: a bounded cosine contrast gives an explicit noise-dependent gap and finite-copy axis estimates, followed by sign-invariant calibration-to-angle recovery. The optical high-energy theorem includes the larger $`r^2=O(\log n)`$ regime. The original existence of a hard-learning gap and projection-pursuit recovery is not new here.

Sources: [published paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/1d774c112926348c3e25ea47d87c835b-Paper-Conference.pdf), [conference record](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1d774c112926348c3e25ea47d87c835b-Abstract-Conference.html), [arXiv](https://arxiv.org/abs/2404.03272).

## Measurement complexity versus computational inference

Zhenyu Du, Siyuan Cheng, Han Ye, Junjie Chen, Xiao Yuan and Xiongfeng Ma, **Complexity-driven transitions in quantum observation**, arXiv:2606.09765v1 (8 June 2026), studies how quantum circuit depth controls the conversion of quantum to classical Fisher information. Its discussion separates that readout problem from possible computational difficulty in recovering a parameter from the data.

Here the source is a mixed optical state, homodyne is fixed and simple, and computation rather than measurement depth is the eventual obstruction. The comparison includes global estimation with identical calibration access, an operator-level optical resolution bound, and mixed-state information inequalities. This does not replace their depth thresholds or claim that their measurement theorem already proves the present inference separation.

Source: [arXiv version and full paper](https://arxiv.org/abs/2606.09765v1).

## Further cryptographic context

Aparna Gupte, Neekon Vafa and Vinod Vaikuntanathan, **Continuous LWE is as Hard as LWE & Applications to Learning Gaussian Mixtures**, arXiv:2204.02550v3 (2 November 2022), connects LWE and CLWE. Its abstract and version record were checked; its complete parameter transfer is not a dependency reconstructed here. Accordingly this repository does not identify the optical family with a particular deployed LWE parameter set.

Source: [arXiv record](https://arxiv.org/abs/2204.02550v3).

## Standard optical and statistical ingredients

Coherent states, Gaussian quadrature noise, passive linear transformations and homodyne detection use standard continuous-variable quantum information; Weedbrook et al., **Gaussian Quantum Information**, Reviews of Modern Physics 84, 621 (2012), is a suitable foundation. Our quadratures have vacuum variance $`1/2`$, so conventions must be translated rather than copied without rescaling.

Fisher information, symmetric logarithmic derivatives and local quantum estimation are standard; Paris, **Quantum estimation for quantum technology**, International Journal of Quantum Information 7, 125 (2009), supplies a review. The proof uses score Cauchy–Schwarz, QFI monotonicity/convexity, bounded-variable concentration and a nuisance-parameter Schur complement. These ingredients are not claimed as discoveries. Local information does not by itself establish a globally useful or efficient estimator.

Sources: [Weedbrook et al.](https://arxiv.org/abs/1110.3234), [Paris, published-version preprint](https://arxiv.org/abs/0804.2981v3).

## Contribution and comparison limits

The scientific claim is the combined supplied-source optical experiment and its proved resource distinctions: exact Fourier-operator damping; a matching polynomial-copy energy scale; calibration-inclusive finite-data recovery; quantum prior-risk hardness via efficient preparation; and a constant homodyne-information fraction for the actual mixed state, including local source nuisance. See the [result map](../science/README.md).

No claim of being the first statistical/computational gap, first hard Gaussian-mixture learning task, or first cryptographic use of metrology is made. The full parameterized BRST statements and Song's recovery account were compared with the present proofs. Du et al.'s main framing and discussion were checked. Other optical and lattice sources supply foundations or explicitly limited context. The closest-work audit does not substitute for independent expert proof review.
