"""Tie-out: recompute every number that appears in the tool, the charts or a headline,
and cross-check the profiles against actual spending in the Consumer Expenditure Survey.

    .venv/bin/python src/tieout.py     -> data/processed/tieout.md
"""
import json
import cex, model
from common import PROCESSED

L = []
def out(s=''):
    L.append(s); print(s)


def eia_year_avg(year):
    v = [p for d, p in model.GAS if d.startswith(str(year))]
    return sum(v) / len(v)


def main():
    m = json.loads((PROCESSED / 'model.json').read_text())
    nhts = json.loads((PROCESSED / 'nhts_miles.json').read_text())
    wm, price = m['weight_model'], m['price']

    out('# Tie-out'); out()
    out(f"Gas price: ${price:.3f}, week of {m['price_date']} (EIA). Shown as ${price:.2f}.")
    out(f"December 2025 EIA average: ${wm['p_dec']:.4f}")
    out(f"CPI gasoline relative importance, Dec 2025: {m['ri']['Gasoline (all types)']}% (motor fuel {m['ri']['Motor fuel']}%)")
    out(f"CPI gasoline weight at the {wm['latest_cpi_month']} index (est.): {wm['ri_latest_month']:.2f}%")
    out(f"CPI gasoline weight at ${price:.2f} (est.): {model.cpi_weight_at(price, wm):.2f}%")
    for p in (3.00, 4.00, 5.00, 6.00, 7.00):
        out(f"  at ${p:.2f}: {model.cpi_weight_at(p, wm):.2f}%")
    out()

    out('## Profiles at today\'s price'); out()
    out('| Profile | Miles | Gallons | Gas a year | Pre-tax | Federal tax | FICA | After-tax | Share | Share, miles at low/high end of 95% margin |')
    out('|---|---|---|---|---|---|---|---|---|---|')
    for p in m['profiles']:
        t = p['tax_detail']
        gal = sum(c['miles'] / c['mpg'] for c in p['cars'])
        cost = gal * price
        assert abs(cost - p['cost']) < 1e-6
        # independent recompute of miles from the NHTS cells
        cell_moe = {c['miles']: next(v['scaled_moe95'] for v in nhts['cells'].values() if v['scaled'] == c['miles']) for c in p['cars']}
        lo = sum((c['miles'] - cell_moe[c['miles']]) / c['mpg'] for c in p['cars']) * price
        hi = sum((c['miles'] + cell_moe[c['miles']]) / c['mpg'] for c in p['cars']) * price
        share = 100 * cost / t['after_tax']
        out(f"| {p['name']} | {sum(c['miles'] for c in p['cars']):,} | {gal:,.0f} | ${cost:,.0f} | ${p['income']:,} | "
            f"${t['federal']:,.0f} | ${t['fica']:,.0f} | ${t['after_tax']:,.0f} | {share:.1f}% | "
            f"{100*lo/t['after_tax']:.1f}% to {100*hi/t['after_tax']:.1f}% |")
    out()
    out('Share at other prices:'); out()
    prices = (3.00, 4.00, 5.00, 6.00, 7.00)
    out('| Profile | ' + ' | '.join(f'${x:.2f}' for x in prices) + ' |')
    out('|---|' + '---|' * len(prices))
    for p in m['profiles']:
        out(f"| {p['name']} | " + ' | '.join(f"{100*model.gas_cost(p['cars'], x)/p['after_tax']:.1f}%" for x in prices) + ' |')
    out()

    out('## Tax check'); out()
    med = m['profiles'][0]
    out(f"Median household after federal tax and FICA: ${med['after_tax']:,.0f}. Census median post-tax household income "
        f"(federal, state and payroll taxes, CPS ASEC Tax Model): ${model.INC_MEDIAN_HH_POSTTAX:,}. "
        f"Difference {100*(med['after_tax']/model.INC_MEDIAN_HH_POSTTAX-1):+.1f}%.")
    out()

    out('## Reality check against the Consumer Expenditure Survey'); out()
    out('Gallons implied by CEX "gasoline and other fuels" spending, divided by the EIA annual average regular price. '
        'CEX includes diesel, out-of-town gasoline and EV charging, and all figures are means per consumer unit.'); out()
    p23, p24 = eia_year_avg(2023), eia_year_avg(2024)
    out(f"EIA annual average regular: 2023 ${p23:.3f}, 2024 ${p24:.3f}"); out()
    out('| CEX group (2024) | Gas spending | Vehicles | Gallons per CU | Gallons per vehicle | 2023 share of after-tax income | 2023 share moved to today\'s price |')
    out('|---|---|---|---|---|---|---|')
    q23, q24 = cex.read('cu-income-quintiles-before-taxes', 2023), cex.read('cu-income-quintiles-before-taxes', 2024)
    a23, a24 = cex.read('cu-area-type', 2023), cex.read('cu-area-type', 2024)
    g23, g24 = cex.read('reference-person-age-ranges', 2023), cex.read('reference-person-age-ranges', 2024)
    for name, d24, d23 in [(n, q24[n], q23[n]) for n in q24] + [('Rural', a24['Rural'], a23['Rural']), ('Urban', a24['Urban'], a23['Urban']),
                                                                ('65 years and older', g24['65 years and older'], g23['65 years and older'])]:
        gal = d24['gas'] / p24
        s23 = 100 * d23['gas'] / d23['income_after']
        out(f"| {name} | ${d24['gas']:,.0f} | {d24['vehicles']} | {gal:,.0f} | {gal / d24['vehicles']:,.0f} | {s23:.1f}% | {s23 * price / p23:.1f}% |")
    out()
    out('Our profiles, gallons per vehicle: ' + '; '.join(
        f"{p['name']} {sum(c['miles']/c['mpg'] for c in p['cars'])/len(p['cars']):,.0f}" for p in m['profiles']))
    vm1_gal = 460.3645618006586
    out(f"FHWA VM-1 2024 gallons per light-duty vehicle: {vm1_gal:,.0f}")
    out()
    out('"Moved to today\'s price" assumes the same gallons as in 2023. People drive a little less when gas costs more, so this is an upper bound.')
    (PROCESSED / 'tieout.md').write_text('\n'.join(L) + '\n')


if __name__ == '__main__':
    main()
