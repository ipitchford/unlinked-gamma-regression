# Unlinked Gamma regression

Exact identifiability and optimal cumulant order. Anonymous. Version 0.1.0-candidate.

**Unrefereed candidate.** For a fixed known positive Gamma shape dictionary with independent centered unit-variance predictors, the paper characterizes every coefficient fiber, proves an exact subset-sum criterion for uniform identification, and gives the optimal worst-case consecutive cumulant cutoff. Signed and zero coefficients are allowed. Finite ambiguity survives the minimal counterexample.

Read `paper.pdf` or `paper.md`; the full source is `paper.tex`. Run `python3 -S reproduce.py` and `python3 -O -S reproduce.py`; output must equal `evidence/replay.json`. Run `python3 verify_manifest.py` to check the complete inventory. Python 3.10 or later, standard library only. Tested producer runtime: Python 3.14.7 on macOS. CI tests Linux separately.

The checks cover 2,055 vectors and rational lower-bound identities for dimensions 1–20, plus four rejected semantic mutations. They supplement the written general proofs. They do not establish external reproduction, formal verification, numerical stability, statistical rates, or exhaustive novelty.

See STATUS.md, ASSURANCE.md, PROVENANCE.md, RESPONSE_TO_REVIEW.md, CLAIMS.json and LICENSES.md. Rebuild PDF with `latexmk -pdf -interaction=nonstopmode paper.tex`; TeX Live 2026 was used. Layout may vary on other TeX versions.

Version archive: https://doi.org/10.5281/zenodo.22858495 (reserved DOI before publication; canonical published status is recorded in the external release receipt).
