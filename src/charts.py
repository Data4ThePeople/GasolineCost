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
    price = m['price']
    P = m['profiles']
    cpi0 = m['cpi']['now']
    f, ax = fig()
    names = [p['name'] for p in P][::-1]; vals = [p['share'] for p in P][::-1]
    ax.barh(names, vals, color=S[0], height=0.55)
    for i, v in enumerate(vals):
        ax.text(v + 0.12, i, f'{v:.1f}%', va='center', color=INK, fontweight='bold', fontsize=11.5)
    ax.axvline(cpi0, color=REF, lw=1.4)
    top = len(P) - 0.45
    ax.text(cpi0 + 0.08, top, f'CPI gasoline weight at\n${price:.2f} (est.): {cpi0:.1f}%', ha='left', va='bottom', fontsize=9.5, color=INK2, linespacing=1.15)
    ax.set_xlim(0, max(vals) * 1.15); ax.set_ylim(-0.6, len(P) + 0.35)
    ax.xaxis.set_major_formatter(lambda x, _: f'{x:.0f}%'); ax.grid(axis='x', color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(axis='y', labelcolor=INK, labelsize=11.5)
    f.subplots_adjust(left=0.27, right=0.96, top=0.8, bottom=0.19)
    title(f, 'Gasoline as a share of after-tax income',
          f'Six households at ${price:.2f} a gallon, the U.S. average for regular on {pd.Timestamp(m["price_date"]):%B %-d, %Y}')
    foot(f, 'Sources: EIA, BLS, Census Bureau, FHWA, IRS. After-tax income subtracts federal income and payroll taxes only.\n'
             f'CPI weight: BLS July 2026 relative importance (3.8%) moved to the {pd.Timestamp(m["price_date"]):%B %-d, %Y} pump price.')
    f.savefig(OUT / '01-share-by-household.png', facecolor=BG); plt.close(f)


def chart_price(m):
    xs = [2 + i * 0.05 for i in range(101)]
    f, ax = fig(5.8)
    ends = []
    for i, p in enumerate(m['profiles']):
        ys = [100 * model.gas_cost(p['cars'], x) / p['after_tax'] for x in xs]
        ax.plot(xs, ys, color=S[i], lw=2); ends.append((ys[-1], p['name'], S[i]))
    cy = [model.cpi_weight_at(x, m['cpi']) for x in xs]
    ax.plot(xs, cy, color=REF, lw=1.6); ends.append((cy[-1], 'CPI gasoline weight', REF))
    ends.sort()
    placed = []
    for y, n, c in ends:            # spread labels so they do not overlap
        y2 = max([y] + [q + 0.55 for q in placed[-1:]])
        placed.append(y2)
        ax.text(7.08, y2, n, color=c if c != REF else INK2, fontsize=10, va='center', fontweight='bold')
    ax.axvline(m['price'], color=GRID, lw=1)
    ax.text(m['price'], 0.25, f" {pd.Timestamp(m['price_date']):%b. %-d}: ${m['price']:.2f}", color=MUTED, fontsize=9)
    ax.set_xlim(2, 7); ax.set_ylim(0, max(e[0] for e in ends) * 1.08)
    ax.xaxis.set_major_formatter(lambda x, _: f'${x:.0f}'); ax.yaxis.set_major_formatter(lambda x, _: f'{x:.0f}%')
    ax.grid(color=GRID, lw=0.8); ax.set_axisbelow(True); ax.set_xlabel('Price of regular gasoline, dollars per gallon', color=MUTED, fontsize=10)
    f.subplots_adjust(left=0.08, right=0.72, top=0.82, bottom=0.17)
    title(f, 'Share of after-tax income spent on gas, by gas price',
          'Six households, with the CPI gasoline weight at each price (our estimate) for comparison')
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


def mix(a, b, t):
    a, b = [int(a[i:i + 2], 16) for i in (1, 3, 5)], [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02x%02x%02x' % tuple(round(x + (y - x) * t) for x, y in zip(a, b))


def lum(h):
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def cpi_weight(m):
    """The CPI gasoline weight at the price the charts are drawn for."""
    return model.cpi_weight_at(m['price'], m['cpi'])


def colored_line(f, x, y, parts, size=11.5):
    """Draw [(text, color, bold), ...] left to right on one line, measuring each piece."""
    r = f.canvas.get_renderer()
    for text, color, bold in parts:
        t = f.text(x, y, text, fontsize=size, color=color, va='top', fontweight='bold' if bold else 'normal')
        x += t.get_window_extent(renderer=r).width / f.bbox.width


NEU, GREEN, RED = '#383835', '#0ca30c', '#e34948'
MILES = list(range(5_000, 40_001, 5_000))
MPGS = [40, 35, 30, 25, 20, 15]
BAND = 0.15          # within this many points of the CPI weight counts as "about the same"


def cell_color(v, cs, price):
    top = 100 * (MILES[-1] / MPGS[-1]) * price / 35_000   # fixed top of the red ramp, so panels share one scale
    if abs(v - cs) <= BAND:
        return NEU
    if v < cs:
        return mix(NEU, GREEN, 0.35 + 0.65 * min(1, (cs - v) / (cs - 0.1)))
    return mix(NEU, RED, 0.35 + 0.65 * min(1, (v - cs) / (top - cs)))


def draw_matrix(ax, inc, cs, price, fs=11):
    for i, g in enumerate(MPGS):
        for j, mi in enumerate(MILES):
            v = 100 * (mi / g) * price / inc
            col = cell_color(v, cs, price)
            ax.add_patch(plt.Rectangle((j + 0.03, i + 0.03), 0.94, 0.94, color=col, lw=0))
            ax.text(j + 0.5, i + 0.5, f'{v:.1f}%', ha='center', va='center', fontsize=fs, fontweight='bold',
                    color='#0b0b0b' if lum(col) > 0.28 else '#ffffff')
    ax.set_xlim(0, len(MILES)); ax.set_ylim(len(MPGS), 0)
    ax.set_xticks([j + 0.5 for j in range(len(MILES))], [f'{mi // 1000}k' for mi in MILES])
    ax.set_yticks([i + 0.5 for i in range(len(MPGS))], [str(g) for g in MPGS])
    ax.tick_params(axis='both', labelcolor=INK2, labelsize=10.5)


def legend_line(f, y, cs, gap=0.028):
    colored_line(f, 0.03, y, [('Gasoline is ', INK2, False), (f'{cs:.1f}% of consumer spending in the CPI', INK, True),
                              (' at this price.', INK2, False)])
    colored_line(f, 0.03, y - gap, [('Green', GREEN, True), (' is a smaller share of take-home pay than that,   ', INK2, False),
                                    ('gray', '#8C9094', True), (' about the same,   ', INK2, False), ('red', RED, True), (' bigger.', INK2, False)])


def chart_matrix(m):
    """Each $1 a gallon adds miles/mpg/after-tax income to a household's gas share.
    Rows mpg, columns total miles, income fixed at the median household's."""
    med = m['profiles'][0]
    inc, cs = med['after_tax'], cpi_weight(m)
    f, ax = fig(6.2)
    draw_matrix(ax, inc, cs, m['price'])
    ax.set_xlabel('Miles driven a year, all cars', color=MUTED, fontsize=10)
    ax.set_ylabel('Average miles per gallon', color=MUTED, fontsize=10)
    f.subplots_adjust(left=0.1, right=0.97, top=0.76, bottom=0.18)
    title(f, 'Gasoline percent of take-home pay, sensitivity matrix',
          f'At \\${m["price"]:.2f} a gallon, by miles driven and mpg, at the median household\'s take-home pay of \\${inc:,.0f}')
    legend_line(f, 0.855, cs)
    foot(f, 'Sources: BLS (CPI weight, our estimate from the July 2026 figure), Census Bureau, IRS. Married couple, no children.')
    f.savefig(OUT / '04-slope-matrix.png', facecolor=BG); plt.close(f)


def chart_matrix_income(m):
    """The same matrix at three incomes: Census 20th percentile, median, 80th percentile (pretax)."""
    from tax import after_tax
    cs = cpi_weight(m)
    pct = dict(model.INC_PCTL)
    rows = [('20th percentile', pct[20]), ('Median', pct[50]), ('80th percentile', pct[80])]
    f, axes = plt.subplots(3, 1, figsize=(8, 15), dpi=200)
    f.patch.set_facecolor(BG)
    for ax, (lab, pre) in zip(axes, rows):
        ax.set_facecolor(BG)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.tick_params(length=0)
        inc = after_tax('mfj', pre)['after_tax']
        draw_matrix(ax, inc, cs, m['price'], fs=10.5)
        ax.set_title(f'{lab} household income: \\${pre:,} before tax, \\${inc:,.0f} take-home', loc='left', color=INK, fontsize=12.5,
                     fontweight='bold', pad=8)
        ax.set_ylabel('Miles per gallon', color=MUTED, fontsize=9.5)
    axes[-1].set_xlabel('Miles driven a year, all cars', color=MUTED, fontsize=10)
    f.subplots_adjust(left=0.1, right=0.97, top=0.885, bottom=0.075, hspace=0.32)
    f.text(0.03, 0.985, 'Gasoline percent of take-home pay, sensitivity matrix, at three incomes', fontsize=16, fontweight='bold', color=INK, va='top')
    f.text(0.03, 0.962, f'At \\${m["price"]:.2f} a gallon, by miles driven and mpg. The same driving costs the same dollars in every panel, not the same share.', fontsize=11.5, color=INK2, va='top')
    legend_line(f, 0.944, cs, gap=0.013)
    f.text(0.03, 0.03, 'Sources: BLS (CPI weight, our estimate from the July 2026 figure), Census Bureau (2025 income percentiles), IRS.\nMarried couple, no children, federal income and payroll taxes.', fontsize=8.5, color=MUTED, va='bottom')
    f.text(0.03, 0.012, CREDIT, fontsize=9, color=INK2, va='bottom', fontweight='bold')
    f.savefig(OUT / '05-slope-matrix-by-income.png', facecolor=BG); plt.close(f)


def chart_distribution(m):
    """What one CPI number hides: gasoline's share of after-tax income across the income
    distribution, from CEX deciles, moved to the current pump price."""
    d = cex.read('cu-income-deciles-before-taxes', 2023)
    price23 = sum(p for dt, p in model.GAS if dt.startswith('2023')) / len([1 for dt, p in model.GAS if dt.startswith('2023')])
    k = m['price'] / price23
    names = [n for n in d if n != 'All consumer units']
    assert len(names) == 10, names
    shares = [100 * d[n]['gas'] / d[n]['income_after'] * k for n in names]
    cpi = cpi_weight(m)
    f, ax = fig(5.8)
    xs = list(range(1, 11))
    ax.plot(xs, shares, color=S[0], lw=2.5, marker='o', ms=7, mfc=S[0], mec=BG, mew=2)
    ax.axhline(cpi, color=REF, lw=1.6)
    ax.text(10.35, cpi, f'What the CPI\nreports: {cpi:.1f}%', color=INK2, fontsize=10.5, va='center', linespacing=1.2)
    for i, dx in ((0, 14), (9, -6)):
        ax.annotate(f'{shares[i]:.1f}%', (xs[i], shares[i]), xytext=(dx, 12), textcoords='offset points',
                    ha='center', color=INK, fontsize=11.5, fontweight='bold')
    ax.set_xlim(0.5, 10.5); ax.set_ylim(0, max(shares) * 1.18)
    ax.set_xticks(xs, ['Poorest\n10%', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', 'Richest\n10%'])
    ax.tick_params(axis='x', labelcolor=INK2, labelsize=10)
    ax.yaxis.set_major_formatter(lambda x, _: f'{x:.0f}%')
    ax.grid(axis='y', color=GRID, lw=0.8); ax.set_axisbelow(True)
    f.subplots_adjust(left=0.09, right=0.84, top=0.8, bottom=0.2)
    title(f, 'One number, ten very different experiences',
          f'Gasoline as a share of take-home pay at \\${m["price"]:.2f} a gallon, households ranked by income in tenths')
    foot(f, 'Source: BLS Consumer Expenditure Survey 2023, the last year BLS published income after taxes, moved to the current\n'
            'pump price at the same gallons. The poorest tenth reports spending far above its income, so its share runs high.')
    f.savefig(OUT / '06-distribution.png', facecolor=BG); plt.close(f)


def chart_timeline():
    """Two tracks since 1978: how recorded music changed, and how the CPI changed."""
    music = [(1979, 'Sony Walkman'), (1983, 'CDs reach the U.S.'), (1999, 'Napster'), (2001, 'iPod'),
             (2007, 'iPhone'), (2011, 'Spotify in the U.S.')]
    cpi = [(1978, 'Item and outlet\nsample design'), (1983, 'Rental equivalence\nfor homeowners'), (1999, 'Geometric mean\nformula'),
           (2002, 'Chained CPI\npublished'), (2021, 'Gas prices from\noutside data'), (2023, 'Annual weight\nupdates')]
    f, ax = fig(5.0)
    x0, x1 = 1976, 2028
    for y, lab, col, side in [(1, music, S[2], 1), (0, cpi, S[0], -1)]:
        ax.plot([x0, x1], [y, y], color=col, lw=2.5, solid_capstyle='round')
        for i, (yr, name) in enumerate(lab):
            ax.plot(yr, y, 'o', ms=9, mfc=col, mec=BG, mew=2, zorder=3)
            off = 24 if (i % 2 == 0) else 64
            ax.annotate(f'{yr}\n{name}', (yr, y), xytext=(0, side * off), textcoords='offset points', ha='center',
                        va='bottom' if side > 0 else 'top', color=INK, fontsize=9.5, linespacing=1.25,
                        arrowprops=dict(arrowstyle='-', color=col, lw=1, shrinkA=0, shrinkB=4))
    ax.text(x0 - 0.5, 1, 'Recorded\nmusic', color=S[2], fontsize=12, fontweight='bold', ha='right', va='center', linespacing=1.2)
    ax.text(x0 - 0.5, 0, 'The CPI', color=S[0], fontsize=12, fontweight='bold', ha='right', va='center')
    ax.set_xlim(x0 - 9, x1 + 1); ax.set_ylim(-1.5, 2.1)
    ax.set_yticks([])
    ax.set_xticks([1980, 1990, 2000, 2010, 2020, 2026], ['1980', '1990', '2000', '2010', '2020', '2026'])
    ax.tick_params(axis='x', labelcolor=MUTED, labelsize=10.5, pad=6)
    f.subplots_adjust(left=0.02, right=0.98, top=0.8, bottom=0.16)
    title(f, 'Same starting line, 1978',
          'One industry was rebuilt from the ground up. The other improved around the edges.')
    foot(f, 'Sources: BLS CPI Handbook of Methods and BLS announcements; company and industry records for the music dates.')
    f.savefig(OUT / '07-timeline.png', facecolor=BG); plt.close(f)


def chart_two_incomes(m):
    """Gasoline as a share of take-home pay at two incomes, everything else held the same:
    married couple, no children, same cars, same driving."""
    from tax import after_tax
    cs = cpi_weight(m)
    pct = dict(model.INC_PCTL)
    panels = [('Lower-income household', pct[20]), ('Higher-income household', pct[80])]
    f, axes = plt.subplots(1, 2, figsize=(11.5, 5.6), dpi=200)
    f.patch.set_facecolor(BG)
    for ax, (lab, pre) in zip(axes, panels):
        ax.set_facecolor(BG)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.tick_params(length=0)
        inc = after_tax('mfj', pre)['after_tax']
        for i, g in enumerate(MPGS):
            for j, mi in enumerate(MILES):
                v = 100 * (mi / g) * m['price'] / inc      # share of take-home pay spent on gas
                col = cell_color(v, cs, m['price'])
                ax.add_patch(plt.Rectangle((j + 0.03, i + 0.03), 0.94, 0.94, color=col, lw=0))
                ax.text(j + 0.5, i + 0.5, f'{v:.0f}%' if v >= 10 else f'{v:.1f}%', ha='center', va='center', fontsize=10,
                        fontweight='bold', color='#0b0b0b' if lum(col) > 0.28 else '#ffffff')
        ax.set_xlim(0, len(MILES)); ax.set_ylim(len(MPGS), 0)
        ax.set_xticks([j + 0.5 for j in range(len(MILES))], [f'{mi // 1000}k' for mi in MILES])
        ax.set_yticks([i + 0.5 for i in range(len(MPGS))], [str(g) for g in MPGS])
        ax.tick_params(axis='both', labelcolor=INK2, labelsize=10)
        ax.set_title(f'{lab}: \\${pre:,} before tax, \\${inc:,.0f} take-home', loc='left', color=INK,
                     fontsize=12, fontweight='bold', pad=8)
        ax.set_xlabel('Miles driven a year, all cars', color=MUTED, fontsize=9.5)
    axes[0].set_ylabel('Miles per gallon', color=MUTED, fontsize=9.5)
    f.subplots_adjust(left=0.06, right=0.98, top=0.72, bottom=0.2, wspace=0.12)
    f.text(0.03, 0.965, 'The same driving, two incomes', fontsize=16, fontweight='bold', color=INK, va='top')
    f.text(0.03, 0.925, f'Gasoline as a share of take-home pay at \\${m["price"]:.2f} a gallon. Married couple, no children, '
                        'in both panels: only income differs.', fontsize=11, color=INK2, va='top')
    colored_line(f, 0.03, 0.885, [('Gasoline is ', INK2, False), (f'{cs:.1f}% of consumer spending in the CPI', INK, True),
                                  (' at this price.   ', INK2, False), ('Green', GREEN, True), (' is under that,   ', INK2, False),
                                  ('gray', '#8C9094', True), (' about the same,   ', INK2, False), ('red', RED, True),
                                  (' over.', INK2, False)], size=11)
    f.text(0.03, 0.055, 'Sources: BLS (CPI weight, our estimate from the July 2026 figure), Census Bureau (2025 income percentiles: '
                       '20th and 80th), IRS.\nFederal income and payroll taxes only.', fontsize=8.5, color=MUTED, va='bottom')
    f.text(0.03, 0.02, CREDIT, fontsize=9, color=INK2, va='bottom', fontweight='bold')
    f.savefig(OUT / '08-matrix-two-incomes.png', facecolor=BG); plt.close(f)


def cpi_slope_now(m):
    """Points the CPI gasoline weight adds per $1 a gallon, at the current price."""
    p, c = m['price'], m['cpi']
    return (model.cpi_weight_at(p + 0.01, c) - model.cpi_weight_at(p - 0.01, c)) / 0.02


def main():
    OUT.mkdir(exist_ok=True)
    m = json.loads((PROCESSED / 'model.json').read_text())
    chart_profiles(m); chart_price(m); chart_cex(); chart_matrix(m); chart_matrix_income(m)
    chart_distribution(m); chart_timeline(); chart_two_incomes(m)
    print('wrote', sorted(p.name for p in OUT.glob('*.png')))


if __name__ == '__main__':
    main()

