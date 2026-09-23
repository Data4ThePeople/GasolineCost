"""Render POST.md as one standalone HTML page for sharing (not part of the Prismic flow).

    .venv/bin/python src/build_post_html.py

Writes docs/post.html plus docs/images/, so GitHub Pages serves the whole post at
https://data4thepeople.github.io/GasolineCost/post.html. The published page carries an
embargo banner so nobody mistakes it for the live article.
"""
import html as H
import re
import shutil
import sys
from pathlib import Path
from common import ROOT

SRC_POST = ROOT / 'posts' / 'gasoline-share-of-income' / 'POST.md'
DOCS = ROOT / 'docs'
CSS = """
:root{--page:#f9f9f7;--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--muted:#6f6d68;--line:#e1e0d9;
      --border:rgba(11,11,11,.10);--accent:#2a78d6}
@media (prefers-color-scheme:dark){:root{--page:#181A1B;--surface:#1f2223;--ink:#E4E2DC;--ink2:#BBBDC0;
      --muted:#8C9094;--line:#33373A;--border:rgba(255,255,255,.10);--accent:#6da7ec}}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;
     line-height:1.6;font-size:18px;-webkit-font-smoothing:antialiased}
.wrap{max-width:740px;margin:0 auto;padding:24px 16px 80px}
.banner{background:#7a1f1f;color:#fff;font:600 14px/1.4 system-ui,sans-serif;padding:10px 16px;text-align:center}
h1{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;font-size:38px;line-height:1.15;
   margin:28px 0 10px;text-wrap:balance}
h2{font-size:26px;line-height:1.25;margin:40px 0 8px}
h3{font-size:20px;margin:30px 0 6px}
.sub{color:var(--ink2);font-size:20px;margin:0 0 6px}
.meta{color:var(--muted);font-size:14px;margin:0 0 28px;border-bottom:1px solid var(--line);padding-bottom:18px}
p{margin:0 0 18px}
figure{margin:26px 0}
figure img{width:100%;height:auto;display:block;border-radius:10px;border:1px solid var(--border)}
figcaption{color:var(--muted);font-size:14px;font-style:italic;margin-top:8px}
iframe{width:100%;border:1px solid var(--border);border-radius:10px;background:#fff;margin:26px 0;display:block}
hr{border:0;border-top:1px solid var(--line);margin:44px 0}
ul{margin:0 0 18px;padding-left:22px}
li{margin:0 0 10px}
a{color:var(--accent)}
.foot{color:var(--muted);font-size:14px;margin-top:44px;border-top:1px solid var(--line);padding-top:16px}
@media (max-width:600px){body{font-size:17px}h1{font-size:30px}h2{font-size:22px}}
"""


def inline(t):
    t = H.escape(t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    return t


def main():
    raw = SRC_POST.read_text()
    _, fm, body = raw.split('---', 2)
    meta = {}
    for line in fm.strip().splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip()

    out, i = [], 0
    lines = body.strip().splitlines()
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln:
            i += 1; continue
        if ln.startswith('::: divider'):
            out.append('<hr>'); i += 1; continue
        if ln.startswith(':::'):                       # any other fence: skip its marker
            i += 1; continue
        if ln.startswith('<iframe'):
            out.append(ln); i += 1; continue
        m = re.match(r'^(#{1,3})\s+(.*)$', ln)
        if m:
            lvl = len(m.group(1))
            if lvl == 1:
                i += 1; continue                       # the title is rendered from front matter
            out.append(f'<h{lvl}>{inline(m.group(2))}</h{lvl}>'); i += 1; continue
        m = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)$', ln)
        if m:
            cap = ''
            if i + 1 < len(lines) and lines[i + 1].startswith('*') and lines[i + 1].rstrip().endswith('*'):
                cap = f'<figcaption>{inline(lines[i + 1].strip().strip("*"))}</figcaption>'
                i += 1
            out.append(f'<figure><img src="{m.group(2)}" alt="{H.escape(m.group(1))}">{cap}</figure>')
            i += 1; continue
        if ln.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append(f'<li>{inline(lines[i][2:].strip())}</li>')
                i += 1
            out.append('<ul>' + ''.join(items) + '</ul>'); continue
        out.append(f'<p>{inline(ln)}</p>'); i += 1

    DOCS.mkdir(exist_ok=True)
    img_src = SRC_POST.parent / 'images'
    img_out = DOCS / 'images'
    img_out.mkdir(exist_ok=True)
    n = 0
    for p in sorted(img_src.glob('*.png')):
        shutil.copy2(p, img_out / p.name); n += 1

    title = meta.get('title', '')
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{H.escape(title)} | Data 4 The People</title>
<style>{CSS}</style>
</head>
<body>
<div class="banner">EMBARGOED DRAFT &middot; not for publication until Data 4 The People publishes it</div>
<div class="wrap">
<h1>{H.escape(title)}</h1>
<p class="sub">{H.escape(meta.get('subtitle', ''))}</p>
<p class="meta">Data 4 The People &middot; draft of {H.escape(meta.get('date', ''))}</p>
{chr(10).join(out)}
<p class="foot">Built by Data 4 The People. The interactive tool is at
<a href="https://data4thepeople.github.io/GasolineCost/">data4thepeople.github.io/GasolineCost</a>,
and the data and code behind every number are at
<a href="https://github.com/Data4ThePeople/GasolineCost">github.com/Data4ThePeople/GasolineCost</a>.</p>
</div>
</body>
</html>
"""
    (DOCS / 'post.html').write_text(page)
    print(f'wrote docs/post.html ({len(page) / 1024:.0f} KB) and {n} images')


if __name__ == '__main__':
    sys.exit(main())
