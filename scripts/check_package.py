"""Portable structure and provenance checks; Python standard library only."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
assert (root / 'SKILL.md').read_text(encoding='utf-8').startswith('---\nname: idea-to-demo\n')
manifest = json.loads((root / 'references/snapshot-manifest.json').read_text(encoding='utf-8'))
assert len(manifest['files']) == 14
for name, digest in manifest['files'].items():
    data = (root / 'references/sop' / Path(name).name).read_bytes()
    assert hashlib.sha256(data).hexdigest() == digest, name
    assert len(re.findall(rb'(?m)^## M\d\d\.\d\d ', data)) == 4, name
for file in root.rglob('*.md'):
    if '.git' in file.parts:
        continue
    for link in re.findall(r'\]\(([^)]+)\)', file.read_text(encoding='utf-8')):
        if link.startswith(('http:', 'https:', '#')):
            continue
        target = (file.parent / link.split('#')[0]).resolve()
        assert target.is_relative_to(root) and target.exists(), (file.relative_to(root), link)
print('PASS: Skill entry, 14 SOP hashes / 56 steps, local Markdown links')
