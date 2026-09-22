"""Static charts for the post (dark palette, house style).

    .venv/bin/python src/charts.py     -> charts/01-*.png ... (moved to posts/<slug>/images at step 2a)
"""
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import cex, model
from common import ROOT, RAW, PROCESSED

OUT = ROOT / 'charts'
BG, INK, INK2, MUTED, GRID = '#181A1B', '#E4E2DC', '#BBBDC0', '#8C9094', '#33373A'
S = ['#3987e5', '#d95926', '#199e70', '#c98500', '#d55181', '#008300']   # dark categorical slots 1-6, fixed order
REF = '#BBBDC0'
plt.rcParams.update({'font.family': ['Helvetica Neue', 'Arial', 'DejaVu Sans'], 'font.size': 12,
                     'text.color': INK2, 'axes.labelcolor': INK2, 'xtick.color': MUTED, 'ytick.color': MUTED})
CREDIT = 'Built by Data 4 The People'


def fig(h=5.4):
    f, ax = plt.subplots(figsize=(8, h), dpi=200)
    f.patch.set_facecolor(BG); ax.set_facecolor(BG)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)
    return f, ax


def title(f, t, sub):
    f.text(0.03, 0.965, t, fontsize=16, fontweight='bold', color=INK, va='top')
    f.text(0.03, 0.905, sub, fontsize=11.5, color=INK2, va='top')


def foot(f, src):
    f.text(0.03, 0.055, src, fontsize=8.5, color=MUTED, va='bottom')
    f.text(0.03, 0.02, CREDIT, fontsize=9, color=INK2, va='bottom', fontweight='bold')


def ri_2023():
    df = pd.read_excel(RAW / 'cpi_relative_importance_2023.xlsx', header=None)
    r = df[df[1].astype(str).str.strip() == 'Gasoline (all types)']
    assert len(r) == 1
    return float(r.iloc[0, 2])


def chart_profiles(m):
    price, wm = m['price'], m['weight_model']
    P = m['profiles']
    cpi0 = m['ri']['Gasoline (all types)']
    f, ax = fig()
    names = [p['name'] for p in P][::-1]; vals = [p['share'] for p in P][::-1]
    ax.barh(names, vals, color=S[0], height=0.55)
    for i, v in enumerate(vals):
        ax.text(v + 0.12, i, f'{v:.1f}%', va='center', color=INK, fontweight='bold', fontsize=11.5)
    ax.axvline(cpi0, color=REF, lw=1.4)
    top = len(P) - 0.45
    ax.text(cpi0 + 0.08, top, f'CPI gasoline weight,\nDec. 2025: {cpi0:.1f}%', ha='left', va='bottom', fontsize=9.5, color=INK2, linespacing=1.15)
    ax.set_xlim(0, max(vals) * 1.15); ax.set_ylim(-0.6, len(P) + 0.35)
    ax.xaxis.set_major_formatter(lambda x, _: f'{x:.0f}%'); ax.grid(axis='x', color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(axis='y', labelcolor=INK, labelsize=11.5)
    f.subplots_adjust(left=0.27, right=0.96, top=0.8, bottom=0.15)
    title(f, 'Gasoline as a share of after-tax income',
          f'Six households at ${price:.2f} a gallon, the U.S. average for regular on {pd.Timestamp(m["price_date"]):%B %-d, %Y}')
    foot(f, 'Sources: EIA, BLS, Census Bureau, FHWA, IRS. After-tax income subtracts federal income and payroll taxes only.')
    f.savefig(OUT / '01-share-by-household.png', facecolor=BG); plt.close(f)


def chart_price(m):
    wm = m['weight_model']
    xs = [2 + i * 0.05 for i in range(101)]
    f, ax = fig(5.8)
    ends = []
    for i, p in enumerate(m['profiles']):
        ys = [100 * model.gas_cost(p['cars'], x) / p['after_tax'] for x in xs]
        ax.plot(xs, ys, color=S[i], lw=2); ends.append((ys[-1], p['name'], S[i]))
    cpi = m['ri']['Gasoline (all types)']
    ax.axhline(cpi, color=REF, lw=1.4); ends.append((cpi, f'CPI weight, {cpi:.1f}%', REF))
    ends.sort()
    placed = []
    for y, n, c in ends:            # spread labels so they do not overlap
        y2 = max([y] + [q + 0.55 for q in placed[-1:]])
        placed.append(y2)
        ax.text(7.08, y2, n, color=c if c != REF else INK2, fontsize=10, va='center', fontweight='bold')
    ax.axvline(m['price'], color=GRID, lw=1)
    ax.text(m['price'], 0.25, f" today ${m['price']:.2f}", color=MUTED, fontsize=9)
    ax.set_xlim(2, 7); ax.set_ylim(0, max(e[0] for e in ends) * 1.08)
    ax.xaxis.set_major_formatter(lambda x, _: f'${x:.0f}'); ax.yaxis.set_major_formatter(lambda x, _: f'{x:.0f}%')
    ax.grid(color=GRID, lw=0.8); ax.set_axisbelow(True); ax.set_xlabel('Price of regular gasoline, dollars per gallon', color=MUTED, fontsize=10)
    f.subplots_adjust(left=0.08, right=0.72, top=0.82, bottom=0.17)
    title(f, 'Share of after-tax income spent on gas, by gas price',
          'Six households, with the CPI gasoline weight (December 2025) for comparison')
    foot(f, 'Sources: EIA, BLS, Census Bureau, FHWA, IRS. Miles and cars held fixed at every price.')
    f.savefig(OUT / '02-share-by-price.png', facecolor=BG); plt.close(f)


def chart_cex():
    q = cex.read('cu-income-quintiles-before-taxes', 2023)
    rows = [(n.replace(' percent', '%'), 100 * d['gas'] / d['income_after']) for n, d in q.items() if n != 'All consumer units']
    ri = ri_2023()
    labels = ['Lowest fifth', 'Second fifth', 'Middle fifth', 'Fourth fifth', 'Highest fifth']
    assert len(rows) == 5
    f, ax = fig()
    vals = [v for _, v in rows][::-1]
    ax.barh(labels[::-1], vals, color=S[0], height=0.55)
    for i, v in enumerate(vals):
        ax.text(v + 0.12, i, f'{v:.1f}%', va='center', color=INK, fontweight='bold', fontsize=11.5)
    ax.axvline(ri, color=REF, lw=1.4)
    ax.text(ri + 0.08, len(rows) - 0.45, f'CPI gasoline weight,\nDec. 2023: {ri:.1f}%', fontsize=9.5, color=INK2, va='bottom', linespacing=1.15)
    ax.set_xlim(0, max(vals) * 1.15); ax.set_ylim(-0.6, len(rows) + 0.35)
    ax.xaxis.set_major_formatter(lambda x, _: f'{x:.0f}%'); ax.grid(axis='x', color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(axis='y', labelcolor=INK, labelsize=11.5)
    f.subplots_adjust(left=0.2, right=0.96, top=0.8, bottom=0.15)
    title(f, 'What households actually spent on gas in 2023',
          'Gasoline and other fuels as a share of after-tax income, by fifth of pretax income')
    foot(f, 'Source: BLS Consumer Expenditure Survey 2023 (the last year BLS published after-tax income). Means per consumer unit.')
    f.savefig(OUT / '03-cex-by-income.png', facecolor=BG); plt.close(f)


def main():
    OUT.mkdir(exist_ok=True)
    m = json.loads((PROCESSED / 'model.json').read_text())
    chart_profiles(m); chart_price(m); chart_cex()
    print('wrote', sorted(p.name for p in OUT.glob('*.png')))


if __name__ == '__main__':
    main()
