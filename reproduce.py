#!/usr/bin/env python3
"""Exact producer replay. Standard library only; no assertions used as gates."""
import json
from fractions import Fraction as Q
from checks import grid, identities

def reject_mutation(filename, before, after):
    from pathlib import Path
    source=(Path(__file__).parent/'checks'/filename).read_text()
    if source.count(before)!=1:
        raise RuntimeError('Mutation target must occur exactly once: '+before)
    mutated=source.replace(before,after,1)
    namespace={'__name__':'mutation'}
    exec(compile(mutated, filename, 'exec'),namespace)
    try:
        namespace['run']()
    except RuntimeError:
        return True
    raise RuntimeError('Mutated implementation was accepted: '+filename)

def run():
    controls={
        'changed_sign':reject_mutation('grid.py','    a = tuple(map(Q, (1, 1, 2)))','    a = tuple(map(Q, (1, 1, -2)))'),
        'changed_shape':reject_mutation('grid.py','alpha = tuple(map(Q, (1, 1, 2)))','alpha = tuple(map(Q, (1, 1, 3)))'),
        'missing_variance_factor':reject_mutation('identities.py','alpha*variance*scale**2 == beta**2','alpha*scale**2 == beta**2'),
        'missing_cumulant_factorial':reject_mutation('identities.py','factorial(6)*value == 777600','value == 777600')
    }
    r=grid.run();r.pop('python');r.pop('platform')
    return {'status':'PASS','grid':r,'identities':identities.run(),'negative_controls_rejected':controls,
            'scope':'Finite exact producer checks, not universal proof, formal verification or external reproduction.'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
