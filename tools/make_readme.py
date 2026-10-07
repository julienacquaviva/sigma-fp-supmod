"""Rebuilds README.md from tools/README.template.md and the mode tables (tools/modes_v45.json)."""
import pathlib
import make_tables
H = pathlib.Path(__file__).resolve().parent
t = (H / 'README.template.md').read_text(encoding='utf-8')
assert t.count('{{TABLES}}') == 1
(H.parent / 'README.md').write_text(t.replace('{{TABLES}}', make_tables.all_tables()), encoding='utf-8', newline='\n')
print('README.md written')
