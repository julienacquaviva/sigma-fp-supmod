"""Writes the mode tables of the README from tools/modes_v45.json (the table the build follows)."""
import json, pathlib
H = pathlib.Path(__file__).resolve().parent
D = json.loads((H / 'modes_v45.json').read_text())
GROUPS = [('23.976 / 24 / 25', (23.976, 24, 25)), ('29.97', (29.97,)), ('48', (48,)), ('50', (50,)), ('59.94', (59.94,)), ('100', (100,)), ('119.88', (119.88,))]


def table(media, ratio):
    r = next(x for x in D[media]['ratios'] if x['ratio'] == ratio)
    out = ['| Crop | Sensor area | ' + ' | '.join(g for g, _ in GROUPS) + ' |', '|---|---|' + '---|' * len(GROUPS)]
    for c in r['crops']:
        st = {s['fps']: s for s in c['states']}
        cells = []
        for _, fs in GROUPS:
            ss = [st[f] for f in fs if f in st]
            if not ss:
                cells.append('')
                continue
            assert len({tuple(s['out']) for s in ss}) == 1, (media, ratio, c['crop'], fs)
            s = ss[0]
            t = '%dx%d' % tuple(s['out'])
            if s['one']:
                t = '**' + t + '**'
            if s.get('window', c['window']) != c['window']:
                t += ' ¹'
            cells.append(t)
        out.append('| %.1fx | %dx%d | ' % (c['crop'], *c['window']) + ' | '.join(cells) + ' |')
    return '\n'.join(out)


def all_tables():
    parts = []
    for media, label in (('SSD', 'FAST (SSD, up to 370 MB/s)'), ('v90', 'REGULAR (v90 card, up to 195 MB/s)'), ('v60', 'MEDIUM (v60 card, up to 125 MB/s)'), ('v30', 'SLOW (v30 card, up to 85 MB/s)')):
        body = '\n\n'.join('**%s**\n\n%s' % (r, table(media, r)) for r in ('3:2', '16:9', '2:1'))
        n = sum(len(c['states']) for r in D[media]['ratios'] for c in r['crops'])
        if media == 'SSD':
            parts.append('### DATA = %s\n\n%s' % (label, body))
        else:
            parts.append('<details>\n<summary><b>DATA = %s</b></summary>\n\n%s\n\n</details>' % (label, body))
    return '\n\n'.join(parts)


if __name__ == '__main__':
    print(all_tables())
