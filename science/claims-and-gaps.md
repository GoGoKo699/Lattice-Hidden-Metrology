# Candidate claims and proof obligations

These are **research targets, not certified theorems**.

1. **Optical resolution:** derive a trace-distance or statistical-distance upper bound between relevant phase hypotheses in the low-energy regime, including calibration copies. This would prove information-theoretic indistinguishability independently of computational assumptions.
2. **Unbounded recovery:** specify a homodyne protocol and unrestricted estimator with polynomial sample complexity and bounded risk in a high-energy regime. Include the cost of learning nuisance parameters from the same calibration data available to every observer.
3. **Efficient quantum hardness:** reduce any efficient quantum estimator improving on the prior-only benchmark to a quantum algorithm contradicting a precisely parameterized continuous-LWE assumption. Account for coherent measurements, sample generation, discretization and approximation error.
4. **Fisher information:** compute quantum and homodyne classical Fisher information for the *marginal mixed state*, not merely for coherent states conditioned on an inaccessible classical label. Show any claimed constant fraction uniformly in the stated parameter range.
5. **Novelty and physics:** separate known hard learning of Gaussian-pancake/continuous-LWE distributions from any genuinely new optical resolution or estimation theorem.

**Critical caution:** a large Fisher information alone does not establish globally small estimation risk; a local information calculation cannot replace a constructive estimator. Also, a classical LWE reduction does not automatically establish hardness against collective quantum measurements on the optical mixture. These are the first two potentially fatal inference gaps.
