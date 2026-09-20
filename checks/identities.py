#!/usr/bin/env python3
"""Exact checks of revision-specific identities, using rational polynomials."""
from fractions import Fraction as F
from math import factorial
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def mul(p, q):
    r = [F(0)] * (len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return r


def run():
    dimensions = []
    # An alternative encoding of the interpolation cancellation:
    # sum_i alpha_i*a_i^3/(1-i^2*u) = u^(d-1)/prod_i(1-i^2*u).
    # Compare exact polynomial numerators, without evaluating power sums.
    for d in range(1, 21):
        alpha = [F(2, i*factorial(d-i)*factorial(d+i)) for i in range(1, d+1)]
        scales = [(-1)**(d-i)*i for i in range(1, d+1)]
        numerator = [F(0)] * d
        for i in range(1, d+1):
            basis = [F(1)]
            for j in range(1, d+1):
                if i != j:
                    basis = mul(basis, [1, -j*j])
            weight = alpha[i-1]*scales[i-1]**3
            numerator = [x+weight*y for x,y in zip(numerator,basis)]
        require(numerator == [F(0)]*(d-1)+[F(1)], 'rational numerator d='+str(d))
        dimensions.append(d)
    # Scaled Poisson Z_alpha=2*P_alpha: v=4, and the allocation map must
    # include sqrt(v). Squared reconstruction avoids approximate roots.
    alpha, variance, beta = F(1), F(4), F(2)
    scale = F(1)
    require(alpha*variance*scale**2 == beta**2, 'convolution normalization')
    require(alpha*scale**2 != beta**2, 'normalization mutation not detected')
    # For a3=(1,-2,3) with integer shapes (45,9,1), the normalization
    # of the first distinguishing raw cumulant is factorial(6).
    value = sum(w*s**7 for w,s in zip((45,9,1),(1,-2,3)))
    require(factorial(6)*value == 777600, 'seventh cumulant')
    require(sum(w*s*s for w,s in zip((45,9,1),(1,-2,3))) == 90, 'variance')
    return {'status':'PASS', 'rational_numerator_dimensions':dimensions,
            'scaled_poisson_normalization':'PASS',
            'missing_variance_factor_mutation_rejected':True,
            'integer_example_seventh_cumulant':777600,
            'scope':'Finite exact revision checks, not a formal or universal proof.'}

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
