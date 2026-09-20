# Devil’s Advocate — internal editorial review

**Recommendation: Minor Revision.** Strongest counterargument: this could be classical finite-atomic identification repackaged as a broad resolution of unlinked-regression identifiability, with a reflected-pair lower bound mistakenly advertised as a coefficient-identification lower bound. The frozen manuscript largely defeats this objection: it explicitly credits Thorin/Prony/Lagrange foundations, limits the conjecture contradiction to the literal signed-permutation conclusion, and restricts sharpness to law recovery from a consecutive cumulant segment over all signed-coefficient dictionaries. These qualifications must survive release summaries and metadata.

## Submission and scope

Reviewed frozen ZIP SHA256 `d916b6842c1b51b2f7b54ea686b5c8735497ae3929429c6aae6afe19a1a7584e`; contained PDF SHA256 `f78c40e91a26e46ae5f15d2b10ccd53c86bdf78e3391925559479f1c20e71461`. Both matched. Extracted separately and did not edit the submission. Read manuscript Markdown and relevant TeX (including abstract), claims, prior-art, provenance, assurance, and checker source. No other editorial-role reports were consulted. Ran the normal standard-library replay and complete-manifest verifier; both passed. This is a producer-coordinated model review, not unaffiliated peer review, formal verification, or independent external reproduction.

## Critical findings

None found within this review’s scope.

## Major findings

None found. In particular, the following attempted objections did not expose a proof gap:

- **Minimality/convolution:** Theorem 2.2 fixes the dictionary and excludes proper subvectors, rather than permitting replacement by newly merged Gamma variables. Full support yields aggregate mass equal to the sum of all positive shapes; every proper subvector has strictly less available mass. Thus the example cannot be dismissed by merging its first two variables. The target source’s Discussion defines minimality by a subvector of the original predictor vector, supporting this interpretation: [BSS v1, Section 5](https://arxiv.org/html/2507.14986v1#S5).
- **Necessity of SR:** Theorem 4.1 removes shared labels from a violating subset pair; equal positive total mass makes both remaining sets nonempty. For shape range [m,Mm], q²>M and h²>q²M separate the squared-coefficient intervals. A mismatch in the lowest interval cannot be repaired by coefficients from either higher interval. This establishes failure even modulo arbitrary signs and permutations, not merely failure of labeled uniqueness.
- **Signed coefficients:** Theorem 2.1 uses the rational logarithmic derivative, not a meromorphic claim about a noninteger Gamma transform. Negative scales produce negative real poles but retain strictly negative residues. Centering adds constants and cannot erase poles. The positive weighted measure used in Theorem 5.1 remains positive for negative nodes.
- **Sharpness quantifiers:** Theorem 5.2 fixes one dictionary on both sides of each dimension-specific reflected pair. Even cumulants agree, the Lagrange identity cancels the required odd orders, and the next odd cumulant differs. The d=1 boundary also works. Reflection is itself a sign transformation, so the construction says nothing about optimal identification modulo signs; Remark 5.3 expressly excludes that interpretation. No per-dictionary, nonnegative-coefficient, or nonconsecutive-order optimality is claimed.
- **Extensions:** The convolution-family argument includes the variance factor and assumes the required finite sequence of nonzero derivatives. It does not silently infer a Gamma pole argument for Poisson or a worst-case cutoff for each family. The one-Gaussian result is correctly separated from the continuous ambiguity with multiple Gaussian coordinates.

## Minor findings

1. **Broken evidence pointer in the public prior-art record.** `PRIOR_ART.md:3` says the original detailed report is preserved at `provenance/original-note/PRIOR_ART.md`; later text relies on that report for additional fingerprints. That path is absent from the complete 25-file ZIP inventory. This makes the public record appear more self-contained than it is. Either include the intended redistributable original report or identify it explicitly as private retained material and remove public-path implications. Bounded historical uncertainty is otherwise disclosed appropriately.

2. **Describe formula spot checks more precisely than implementation mutation testing.** `reproduce.py:19` tests the literal false equality `1*1**2 == 4`, while line 20 checks a fixed normalized seventh cumulant against a raw-cumulant constant. `checks/identities.py:39–49` does provide meaningful companion checks of the intended formulas, so this is not missing mathematical validation. However, these controls do not demonstrate that mutating an implemented normalization routine would be caught: no such routine is exercised. The manuscript (`paper.tex:382`) and assurance wording should call these fixed formula negative controls, or route deliberately altered normalization through an actual checked reconstruction function before claiming implementation-mutation coverage.

## Provenance and assurance assessment

The supplied-review origin of the sharpness construction is acknowledged rather than attributed to an authenticated external expert. The package disclaims verified historical priority, external independence, formal proof, and statistical stability. These boundaries are appropriate. Neither replay nor this review authenticates the supplied reviews or establishes rights to redistribute them; the package excludes their raw contents. No new rights or priority conclusion is drawn here.

## Confidence and disposition

High confidence in the local mathematical reasoning audited above; moderate confidence in the broader literature framing because this was not a comprehensive historical search. The target conjecture wording was checked against the primary v1 source. The all-dimensional mathematics rests on the written arguments, not the finite replay. Acceptable as an explicitly unrefereed candidate after the two small documentation corrections; this recommendation does not authorize claims of independent peer review or novelty certification.
