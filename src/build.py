"""Build dist/index.html (standalone) and dist/embed.html (Prismic frame) from src/template.html.

    .venv/bin/python src/build.py

Checks before writing: every marker appears once, the page script parses (macOS
JavaScriptCore), and in headless Chrome the page runs without errors and its
numbers match src/model.py for every profile at three prices.
"""
import base64, json, os, re, subprocess, sys, tempfile
from datetime import date
import tax, model
from common import ROOT, SRC, DIST, PROCESSED

JSC = '/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
CHECK_PRICES = [3.0, None, 6.25]   # None = today's price
MONTHS = 'January February March April May June July August September October November December'.split()


def long_date(d):
    return f'{MONTHS[d.month - 1]} {d.day}, {d.year}'


def data():
    m = json.loads((PROCESSED / 'model.json').read_text())
    wm = m['weight_model']
    y, mo = wm['latest_cpi_month'].split('-')
    tax_params = {k: getattr(tax, k) for k in dir(tax) if k.isupper()}
    profiles = [dict(id=p['id'], name=p['name'], blurb=p['blurb'], income=p['income'],
                     tax=dict(status=p['tax']['status'], kids=p['tax']['kids'], seniors=p['tax'].get('seniors', 0),
                              social_security=p['tax'].get('social_security', 0)),
                     cars=[dict(miles=c['miles'], mpg=c['mpg'], label=c['label']) for c in p['cars']])
                for p in m['profiles']]
    ids = [p['id'] for p in profiles]
    assert len(ids) == len(set(ids)), 'duplicate profile id'
    return m, dict(price=m['price'], price_date=m['price_date'], ri=dict(gas=m['ri']['Gasoline (all types)'], motor=m['ri']['Motor fuel']),
                   wm=dict(w0=wm['w0'], r=wm['r'], p_dec=wm['p_dec'], latestLabel=f'{MONTHS[int(mo) - 1]} {y}'),
                   tax=tax_params, profiles=profiles, pctl=model.INC_PCTL, built=long_date(date.today()))


def page_js(html):
    i = html.index('<script>') + 8
    return html[i:html.index('</script>', i)]


def check_parse(html):
    if not os.path.exists(JSC):
        print('jsc not found; parse check skipped'); return
    with tempfile.TemporaryDirectory() as d:
        open(f'{d}/page.js', 'w').write(page_js(html))
        open(f'{d}/chk.js', 'w').write('try{ new Function(read("%s/page.js")); print("ok") }catch(e){ print("PARSE ERROR: "+e) }' % d)
        out = subprocess.run([JSC, f'{d}/chk.js'], capture_output=True, text=True).stdout.strip()
    assert out == 'ok', out


def check_in_chrome(html, m, name):
    if not os.path.exists(CHROME):
        print('Chrome not found; runtime check skipped'); return
    prices = [p if p is not None else m['price'] for p in CHECK_PRICES]
    probe = html.replace('<script>', '<script>window.onerror=function(msg,u,l,c){document.body.setAttribute("data-err",msg+" @"+l+":"+c)};', 1)
    probe = probe.replace('</body>', '<script>try{document.body.setAttribute("data-check",JSON.stringify(window.__gcCheck(%s)))}catch(e){document.body.setAttribute("data-err",String(e))}</script></body>' % json.dumps(prices))
    with tempfile.TemporaryDirectory() as d:
        open(f'{d}/probe.html', 'w').write(probe)
        dom = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--virtual-time-budget=3000', '--window-size=1200,900',
                              '--dump-dom', f'file://{d}/probe.html'], capture_output=True, text=True, timeout=120).stdout
    err = re.search(r'data-err="([^"]*)"', dom)
    assert dom and not err, f'{name}: page JavaScript error: {err.group(1) if err else "no output from Chrome"}'
    got = json.loads(re.search(r'data-check="([^"]*)"', dom).group(1).replace('&quot;', '"'))
    worst = 0.0
    for g in got:
        wm = m['weight_model']
        assert abs(g['cpi'] - model.cpi_weight_at(g['price'], wm)) < 1e-9, 'CPI weight mismatch'
        for pj, pp in zip(g['profiles'], m['profiles']):
            assert pj['id'] == pp['id']
            share_py = 100 * model.gas_cost(pp['cars'], g['price']) / pp['after_tax']
            worst = max(worst, abs(pj['afterTax'] - pp['after_tax']), abs(pj['share'] - share_py))
    assert worst < 1e-6, f'{name}: page and model disagree by {worst}'
    print(f'{name}: runs in Chrome without errors; matches model.py for {len(m["profiles"])} profiles at {prices}')


def main():
    m, d = data()
    tpl = (SRC / 'template.html').read_text()
    logos = {}
    for key, fn in (('__LOGO_ON_LIGHT__', 'd4tp-text-dark.svg'), ('__LOGO_ON_DARK__', 'd4tp-text-light.svg')):
        logos[key] = 'data:image/svg+xml;base64,' + base64.b64encode((ROOT / 'assets' / fn).read_bytes()).decode()
    for marker in ['__DATA__', '__FORCE_FRAMED__', *logos]:
        assert tpl.count(marker) == 1, f'marker {marker} appears {tpl.count(marker)} times'
    DIST.mkdir(exist_ok=True)
    for fname, framed in (('index.html', 'false'), ('embed.html', 'true')):
        html = tpl.replace('__DATA__', json.dumps(d, separators=(',', ':'))).replace('__FORCE_FRAMED__', framed)
        for k, v in logos.items():
            html = html.replace(k, v)
        check_parse(html)
        check_in_chrome(html, m, fname)
        (DIST / fname).write_text(html)
        print(f'wrote dist/{fname}  {len(html) / 1024:.0f} KB')


if __name__ == '__main__':
    sys.exit(main())
