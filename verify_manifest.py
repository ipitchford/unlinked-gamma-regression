from pathlib import Path
import hashlib
root=Path(__file__).resolve().parent
listed=set()
for line in (root/'MANIFEST.sha256').read_text().splitlines():
    expected,name=line.split('  ',1)
    path=(root/name).resolve()
    if not path.is_relative_to(root) or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
        raise RuntimeError('Hash mismatch: '+name)
    listed.add(name)
actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts and '__pycache__' not in p.parts and p.name!='MANIFEST.sha256'}
if actual!=listed:
    raise RuntimeError('Manifest coverage mismatch: '+str(actual ^ listed))
print('PASS: complete manifest and hashes')
