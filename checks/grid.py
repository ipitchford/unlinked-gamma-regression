"""Exact bounded checks. These checks are not proofs of the universal claims."""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict, Counter
import json, platform, sys
from pathlib import Path

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def measure(alpha, scales):
    out = defaultdict(Q)
    for w, s in zip(alpha, scales):
        if s:
            out[s] += w
    return tuple(sorted(out.items()))

def cumulants(alpha, scales):
    return tuple((sum((w * s ** n for w, s in zip(alpha, scales))) for n in range(2, 2 * len(alpha) + 2)))

def fiber(alpha, scales):
    target = measure(alpha, scales)
    choices = (Q(0),) + tuple((s for s, _ in target))
    return [b for b in product(choices, repeat=len(alpha)) if measure(alpha, b) == target]

def shape_condition(alpha):
    seen = {}
    for bits in product((0, 1), repeat=len(alpha)):
        subset = tuple(sorted((w for w, b in zip(alpha, bits) if b)))
        total = sum(subset, Q(0))
        if total in seen and seen[total] != subset:
            return False
        seen[total] = subset
    return True

def orbit_key(alpha, scales):
    return tuple(sorted(((w, s) for w, s in zip(alpha, scales))))

def full_support(a):
    return all((s != 0 for s in a))

def run():
    alpha = tuple(map(Q, (1, 1, 2)))
    a = tuple(map(Q, (1, 1, 2)))
    b = tuple(map(Q, (2, 2, 1)))
    require(measure(alpha, a) == measure(alpha, b) == ((Q(1), Q(2)), (Q(2), Q(2))), 'Exact check failed at original line 54')
    require(cumulants(alpha, a) == cumulants(alpha, b), 'Exact check failed at original line 55')
    require(sorted((w * s * s for w, s in zip(alpha, a))) == [1, 1, 8], 'Exact check failed at original line 56')
    require(sorted((w * s * s for w, s in zip(alpha, b))) == [2, 4, 4], 'Exact check failed at original line 57')
    require(set(fiber(alpha, a)) == {a, b}, 'Exact check failed at original line 58')

    def mgf_parts(scales):
        poly = [Q(1)]
        for w, s in zip(alpha, scales):
            for _ in range(int(w)):
                nxt = [Q(0)] * (len(poly) + 1)
                for j, c in enumerate(poly):
                    nxt[j] += c
                    nxt[j + 1] -= s * c
                poly = nxt
        return (sum((w * s for w, s in zip(alpha, scales))), poly)
    require(mgf_parts(a) == mgf_parts(b) == (Q(6), [1, -6, 13, -12, 4]), 'Exact check failed at original line 71')
    m0, m1, m2, m3 = cumulants(alpha, a)[:4]
    det = m0 * m2 - m1 * m1
    q0 = (-m2 * m2 + m1 * m3) / det
    q1 = (-m0 * m3 + m1 * m2) / det
    require((det, q0, q1) == (16, 2, -3), 'Exact check failed at original line 77')
    require(all((s * s + q1 * s + q0 == 0 for s in (1, 2))), 'Exact check failed at original line 78')
    w2 = m1 - m0
    w1 = m0 - w2
    require((w1, w2) == (2, 8), 'Exact check failed at original line 81')
    profiles = [(1,), (1, 1), (1, 2), (1, 1, 2), (1, 1, 3), (1, 2, 3), (1, 2, 4), (1, 1, 1, 1), (Q(1, 2), Q(1, 3), Q(5, 6)), (Q(1, 2), Q(1, 2), Q(3, 2)), (1, 2, 3, 4)]
    grid = tuple(map(Q, (-2, -1, 0, 1, 2)))
    reports = []
    for raw in profiles:
        alpha = tuple(map(Q, raw))
        by_m, by_c = ({}, {})
        support = {}
        orbit = {}
        sr = shape_condition(alpha)
        count = 0
        for scales in product(grid, repeat=len(alpha)):
            mk, ck = (measure(alpha, scales), cumulants(alpha, scales))
            require(by_m.setdefault(mk, ck) == ck, 'Exact check failed at original line 96')
            require(by_c.setdefault(ck, mk) == mk, 'Exact check failed at original line 97')
            require(support.setdefault(mk, full_support(scales)) == full_support(scales), 'Exact check failed at original line 98')
            if sr or (full_support(scales) and len(set(scales)) == len(scales)):
                candidates = fiber(alpha, scales)
                require(all((orbit_key(alpha, z) == orbit_key(alpha, scales) for z in candidates)), 'Exact check failed at original line 102')
            count += 1
        reports.append(dict(shapes=list(map(str, alpha)), vectors=count, distinct_laws=len(by_m), shape_condition=sr))
    return dict(status='passed', python=sys.version, platform=platform.platform(), example_fiber=[[1, 1, '2*sqrt(2)'], [2, 2, 'sqrt(2)']], original_example_mgf_identity='exact matching exponent and denominator', prony=dict(determinant=16, annihilator=[2, -3, 1], atoms=[1, 2], shape_masses=[2, 2]), profiles=reports, total_grid_vectors=sum((r['vectors'] for r in reports)), limits='Bounded exact tests; no universal proof, formal verification, statistical stability or novelty certification.')

