# Domain-specialist internal editorial report

Recommendation: **Accept** for publication as the explicitly unrefereed candidate described in the manuscript.

Status: internal model review; no authenticated external referee status or endorsement. Date: 20 September 2026.

## Reviewed object and scope

Reviewed the separately extracted, unchanged frozen submission, concentrating on mathematical scope, terminology, statistical connections and novelty boundaries. Verified archive SHA256 `d916b6842c1b51b2f7b54ea686b5c8735497ae3929429c6aae6afe19a1a7584e` and PDF SHA256 `f78c40e91a26e46ae5f15d2b10ccd53c86bdf78e3391925559479f1c20e71461`. Read the manuscript source, including title and abstract, and its prior-art statement. Did not consult other editorial reports. This was not a formal-proof audit, comprehensive priority search, or computational replay.

## Assessment

The population target and fixed, labeled, known Gamma dictionary are explicit. The distinction between an aggregate distributional invariant and its allocations to predictors is mathematically appropriate. Calling the aggregate a positive measure even for negative support is correct; the text does not incorrectly identify it as the ordinary positive-support Thorin measure. Rational logarithmic derivatives, rather than Gamma transforms with noninteger powers, are used for the pole argument.

The fiber/minimality reasoning, separated-scale argument for the arithmetic criterion, and generic distinct-scale argument appear sound on substantive reading. Full support is sufficient for dictionary-relative minimality because omitted positive shapes strictly reduce the invariant's total mass. The consecutive cumulant cutoff is carefully limited to signed coefficients, worst-case dictionaries, and response-law reconstruction; the reflected lower-bound pair is not incorrectly offered as a failure of identification modulo sign. The analytic-family extension includes the required variance factor and finite nonvanishing-derivative hypothesis. No unrestricted non-Gaussian conclusion is asserted.

The comparison with [BSS version 1](https://arxiv.org/html/2507.14986v1), especially its Discussion and Theorem 5, is accurate: the displayed full-support example addresses the literal signed-permutation conjecture, while retaining finite ambiguity. The manuscript acknowledges that the underlying convolution obstruction is already present in BSS and distinguishes its centered model from the existing mixed-model theorem. This assessment does not rely on the validity of every auxiliary statement in BSS.

The added statistical connections are supported by the primary sources. [Azadkia–Balabdaoui, JMLR 25(197)](https://jmlr.org/papers/v25/22-0930.html) concerns estimation under identification and an extended-distance treatment in nonidentified settings. [Balabdaoui–Di Noia–Durot, JMLR 27(101)](https://jmlr.org/papers/v27/25-0516.html), including Theorem 3 in its PDF, treats latent-distribution estimation and gives a parametric Wasserstein-1 rate under assumptions. The manuscript explicitly prevents transfer of those rates to arbitrary Gamma configurations or a sample-cumulant estimator. These sources supply statistical context rather than evidence of novelty or proof of the manuscript's theorems.

Classical aggregate-measure and Prony foundations are credited, and historical priority for the allocation criterion and fixed-dictionary optimal cutoff remains explicitly uncertain. This is suitable candidate framing, not evidence of an established original research contribution.

## Objections and confidence

- **Major/blocking objections:** none identified within this role's scope.
- **Minor optional clarification:** the introductory phrase “parametric-rate results” could name Wasserstein-1 and Theorem 3 of BDD for easier verification. The current wording already says “under their assumptions” and is not misleading; this is not a condition of acceptance.
- **Residual limitation:** historical priority has not been independently cleared by this review. Preserve the existing bounded-uncertainty and unrefereed disclosures in release descriptions.

Confidence: high for the stated model/scope distinctions and checked source connections; moderate-to-high for the mathematical reasoning on substantive reading; limited for historical novelty. Acceptance does not certify external peer review, proof-assistant verification, numerical stability, or finite-sample guarantees.
