# Updated claim-level prior-art assessment

Search date: 20 September 2026. The original detailed search report is preserved in the earlier private intake record (not redistributed). This update addresses the supplied sharpness addendum and the final manuscript. **Historical priority remains BOUNDED UNCERTAINTY.** Negative searches do not establish novelty.

## Frozen statements

1. Fixed-dictionary centered standardized Gamma laws are classified by aggregate positive shape mass at nonzero signed effective scales; coefficient fibers are finite allocations.
2. Equal shape sums imply equal shape multisets if and only if every minimal representation is signed-permutation identifiable.
3. For d predictors, cumulants through 2d+1 determine the response law; for each d there is one fixed positive-shape dictionary and a reflected full-support pair matching through 2d but differing at 2d+1. The cutoff refers to a consecutive initial cumulant segment and signed coefficients.
4. The stated finite nonvanishing-cumulant hypotheses extend allocation results to analytic convolution families. No unrestricted non-Gaussian theorem is claimed.

## Normalization and fingerprints for the added statement

The lower-bound dictionary is alpha_i=2/[i(d-i)!(d+i)!], a_i=(-1)^(d-i)i. Standardized regression coefficients are sqrt(alpha_i)*a_i. Reflection preserves the dictionary and changes a to -a. For integer-shape examples a common multiplier L changes the coefficients to sqrt(L alpha_i)*a_i.

Small exact dictionaries:
- d=1: alpha=(1), a=(1).
- d=2: alpha=(1/3,1/24), a=(-1,2).
- d=3: alpha=(1/24,1/120,1/1080), a=(1,-2,3), or integer shapes (45,9,1) after multiplication by 1080.

For d=3 integer shapes, raw cumulants of orders 2–7 are 90,0,1620,0,162000,777600. Normalized by (n-1)! they are 90,0,270,0,1350,1080.

The interpolation denominator is Q(z)=product_(j=1)^d(z-j^2). The exact rational fingerprint is

    sum_i alpha_i a_i^3/(1-i^2 u) = u^(d-1)/product_i(1-i^2 u).

Equivalently the derivative of the difference between a response CGF and its reflection is 2t^(2d)/product_i(1-i^2 t^2). Its moment cancellation is a direct instance of classical Lagrange interpolation / barycentric weights; the abstract interpolation identity is not claimed as new.

Aliases examined: finite atomic moment problem, Prony system, signed Gamma convolution, weighted sums of chi-squares, reflection moment matching, cumulant identifiability, barycentric cancellation, bounded subset relations. The original report supplies the aggregate-measure, Thorin, subset-sum, sequence and small-Hankel fingerprints.

## Additional exact query log

Web-indexed searches, 20 September 2026:
- `"gamma" "cumulants" "2d+1" identifiability`
- `"gamma" "cumulants" "sharp" "identifiability"`
- `"moment matching" "reflection" "gamma" cumulants`
- `"2" "i(d-i)" "(d+i)" cumulants`
- `"Gamma" "cumulant" "identifiability" "2d"`
- `"weighted sums" "gamma" "moments" identification`
- `"45,9,1" "cumulants"`
- `"2d+1" "Prony" "sharp"`
- `"gamma" "cumulants" "Lagrange interpolation" identifiability`
- `"cumulants" "45" "9" "777600"`
- `"Gamma" "optimal" "moment" "identification" weighted sums`
- `"unlinked" "subset" "multiset"`
- `"gamma" "45, 9, 1"`
- `"Gamma" "cumulants" "2d+1"`
- `"cumulants" "barycentric" gamma`
- `"1/24" "1/120" "1/1080"`

Most precise queries returned unrelated results. The searches located classical moment/Prony and Gamma approximation literature, not a verified identical fixed-dictionary cutoff theorem. A nearby 2026 paper, *Moments of sums of exponentials, beyond CHS*, arXiv:2602.03058v1, was inspected at its abstract and HTML overview as a lead about moment formulas and inequalities. It was not used as a source of the present identifiability statements. Full citation-graph coverage and a comprehensive search of classical distribution-characterization monographs were not completed. No outbound author enquiry was made.

## Adjudication

| Contribution unit | Outcome | Permitted manuscript language |
|---|---|---|
| Distinct labeled subset sums as sufficient Gamma condition | Prior-art collision in the Gamma part of BSS Theorem 5 | Existing condition; present model and necessity statement distinguished |
| Aggregate uniqueness for positive Gamma convolution | Classical Thorin-measure theory | Classical foundation; signed centered proof given explicitly |
| Finite-atomic moment reconstruction | Classical Prony/Vandermonde method | Application, not a new algorithm |
| Lagrange leading-coefficient identity | Classical interpolation identity | Tool used in the proof, not a novel identity |
| Minimal full-support counterexample, exact allocation classification and (SR) equivalence | BOUNDED UNCERTAINTY on historical priority | Complete local proofs; no first/new claim |
| Uniform optimal consecutive cumulant cutoff respecting a fixed dictionary | BOUNDED UNCERTAINTY on historical priority | Theorem and construction included with proof and exact scope; historical novelty unestablished |
| Analytic convolution-family extension | BOUNDED UNCERTAINTY on priority | Sufficient theorem under displayed hypotheses |

The final paper avoids “first,” “new,” or comprehensive priority clearance. The exact conjecture comparison is version-specific. “Final” describes completion of the requested review manuscript, not publication status or historical novelty.

## Publication update

The JMLR 2024 and 2026 sources were verified and added as statistical context; see SOURCE_VERIFICATION.md. Additional phrase searches for unlinked Gamma subset-sum identification, shape allocation and the 2d+1 cumulant cutoff did not establish an earlier equivalent theorem. Search results were sparse and often irrelevant; no priority clearance follows. The classical invariant and reconstruction tools remain explicitly attributed.
