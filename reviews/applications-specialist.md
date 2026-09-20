# Internal applications and cross-disciplinary review

Recommendation: **Accept** within this specialist remit, for release as an explicitly unrefereed mathematical candidate. This is internal model-mediated review and does not establish external independence, peer review, novelty, or complete proof validity.

## Frozen target and scope

Reviewed the full manuscript text in a separate extraction (`applications-extract/paper.md`), and the LaTeX abstract/model. Verified archive SHA256 `d916b6842c1b51b2f7b54ea686b5c8735497ae3929429c6aae6afe19a1a7584e` and PDF SHA256 `f78c40e91a26e46ae5f15d2b10ccd53c86bdf78e3391925559479f1c20e71461`. Did not read other reviewer reports or alter the frozen target. Scope: semantic connection to unlinked regression, practical implications, assumptions, estimator misuse, and current statistical framing.

## Findings

1. **The semantic bridge is sound and explicit.** The introductory population target is equality in distribution for a known predictor law. The fixed independent, centered, standardized Gamma dictionary, known positive shapes, signed coefficients, and noiseless linear response are specified before the results. Aggregate distribution recovery, allocation to labeled predictors, and coefficient identification are consistently separated. The two-vector example makes the practical ambiguity concrete even with minimal full-support representations.

2. **No unwarranted estimator claim was found.** Section 1 explicitly says that exact cumulant sufficiency does not validate a sample-cumulant estimator or transfer statistical rates. Exact reconstruction warns about near-colliding nodes, exact real-number equality, and the separate analysis needed for approximate subset sums and estimated cumulants. The scope section excludes finite-sample estimation, unknown shapes, noisy-response deconvolution, conditioning guarantees, and efficient allocation algorithms. Consequently, the finite cumulant cutoff is presented as an information result at the population level, not a sample-size, accuracy, or runtime guarantee.

3. **Statistical context is current and appropriately bounded.** Live primary-source checks on 20 September 2026 confirmed the cited JMLR 2024 and 2026 papers and their stated research targets. The 2024 abstract concerns coefficient estimation under identifiability and extended-distance consistency in some nonidentifiable cases. The 2026 abstract concerns latent-distribution recovery, including a Wasserstein-1 parametric-rate result. The manuscript accurately distinguishes the latter target from coefficient identification and qualifies rates by the source assumptions. Sources: [Azadkia and Balabdaoui (2024)](https://jmlr.org/papers/v25/22-0930.html), [Balabdaoui, Di Noia and Durot (2026)](https://jmlr.org/papers/v27/25-0516.html). This check used article metadata and abstracts, not a new full review of their statistical proofs.

4. **Extensions and limitations are not overgeneralized.** The single-Gaussian extension retains sign ambiguity; multiple standard Gaussian coordinates introduce norm-based continuous ambiguity. The analytic-family extension explicitly requires finitely many nonzero derivatives and does not transfer Gamma optimality to every convolution family. Generic identification is correctly distinguished in the exposition from uniform identification. No empirical application, causal interpretation, record-linkage recovery, or recovery of individual matched observations is claimed.

## Optional improvements, not acceptance conditions

A short sentence explaining that population-generic identification does not imply uniformly stable estimation near coincident scales or near shape subset-sum collisions would help applied readers. The current reconstruction caveat and final exclusions already substantially cover this risk. An equally optional sentence could clarify that these results characterize coefficient compatibility with marginal laws and do not reconstruct missing individual links.

## Confidence and limitations

High confidence in the manuscript's restraint and conceptual distinctions within this remit. Moderate confidence in the breadth of current statistical context: two directly cited primary article abstracts were checked, not an exhaustive literature survey. No empirical estimator evaluation, full theorem audit, PDF visual inspection, code replay, or historical priority determination was undertaken here. No material application-scope objection or required revision identified.
