"""Profiles, gas cost, share of after-tax income, and CPI's gasoline weight at any price.

    .venv/bin/python src/model.py     -> data/processed/model.json

Every input is read from data/raw or data/processed, or cited inline. The page's
JavaScript repeats this arithmetic; build.py checks that the two agree.
"""
import json
from common import RAW, PROCESSED
from tax import after_tax

# --- Inputs read from fetched files ----------------------------------------
GAS = json.loads((RAW / 'eia_gasoline_regular_weekly.json').read_text())['data']
CPI = json.loads((RAW / 'bls_cpi_u_nsa.json').read_text())
NHTS = json.loads((PROCESSED / 'nhts_miles.json').read_text())['cells']

# BLS relative importance, December 2025, CPI-U (Table 1, 2024 weights).
# Read from the xlsx by ri_from_xlsx(); these anchors make a new vintage fail loudly.
RI_ANCHORS = {'Gasoline (all types)': 2.895, 'Motor fuel': 2.981}



def vm1_mpg(year=2024):
    """Miles per gallon from FHWA Highway Statistics 2024, Table VM-1 (published February 2026):
    light-duty short wheelbase, long wheelbase, and all light-duty vehicles."""
    import pandas as pd
    df = pd.read_excel(RAW / 'driving' / 'fhwa_vm1_2024.xlsx', header=None)
    label = df[1].astype(str)
    rows = [i for i in df.index if label[i].strip().startswith('Average miles travele')
            and 'gallon' in label.get(i + 1, '')]
    assert len(rows) == 1, rows
    r = df.iloc[rows[0]]
    assert int(r[0]) == year and str(df.iloc[7, 2]).strip() == 'VEHICLES' and 'SHORT' in str(df.iloc[8, 2])
    assert 'LONG' in str(df.iloc[8, 5]) and 'LIGHT DUTY' in str(df.iloc[7, 8])
    return float(r[2]), float(r[5]), float(r[8])


MPG_SHORT_WB, MPG_LONG_WB, MPG_ALL_LDV = vm1_mpg()   # about 25.59, 18.50, 23.43

# Census P60-289, income year 2025 (released Sept 15, 2026)
INC_MEDIAN_HH = 87_460         # Table 4, all households, median money income
INC_MEDIAN_HH_POSTTAX = 76_060 # Table 4, median post-tax income (fed + state + payroll taxes)
INC_MEDIAN_FAMILY = 112_900    # Table 4, family households
INC_MEDIAN_65 = 59_680         # Table 4, householder 65 and older
INC_MEDIAN_NONMETRO = 68_670   # Table 4, outside metropolitan areas
INC_P20 = 35_800               # Table H-1, upper limit of lowest quintile
# Pretax percentile cut points, for "about N in 10 households earn less" (Table 5 and H-1)
INC_PCTL = [(10, 20_010), (20, 35_800), (40, 68_600), (50, 87_460), (60, 110_300),
            (80, 182_400), (90, 261_300), (95, 354_000)]

# SSA 2026 COLA fact sheet: aged couple, both receiving benefits, after 2.8% COLA
SS_COUPLE_MONTHLY = 3_208


def ri_from_xlsx():
    import pandas as pd
    df = pd.read_excel(RAW / 'cpi_relative_importance_2025.xlsx', header=None)
    tree = df.iloc[:df.index[df[1].astype(str).str.startswith('Special aggregate')][0]]
    out = {}
    for name, want in RI_ANCHORS.items():
        rows = tree[tree[1].astype(str).str.strip() == name]
        assert len(rows) == 1, f'{name}: {len(rows)} rows'
        out[name] = float(rows.iloc[0, 2])
        out[name + ' (CPI-W)'] = float(rows.iloc[0, 3])
        assert abs(out[name] - want) < 1e-9, f'{name}: {out[name]} != anchor {want}'
    return out


def month_avg(prefix):
    v = [p for d, p in GAS if d.startswith(prefix)]
    assert v, prefix
    return sum(v) / len(v)


# Latest monthly relative importance BLS has published for gasoline (all types),
# per Eric: July 2026, 3.77%. We rebuild it from the December 2025 table and the
# CPI-U indexes, and the build fails if the two disagree.
RI_LATEST_MONTH, RI_LATEST_PUBLISHED = '2026-07', 3.77


def cpi_weight_basis(ri_dec):
    """What the CPI gasoline weight needs to be computed at any pump price.

    Step 1: carry December 2025 to RI_LATEST_MONTH with the CPI-U indexes (the way
    BLS updates relative importance between weight years) and check it against the
    published figure. Step 2: r = the change in all other CPI prices since that
    month, from the newest CPI-U release. cpi_weight_at() then moves the weight to
    any pump price, measured against that month's EIA average. Our estimate.
    """
    G, A = CPI['gasoline_all_types'], CPI['all_items']
    m0 = RI_LATEST_MONTH
    ri0 = 100 * ri_dec * (G[m0] / G['2025-12']) / (100 * A[m0] / A['2025-12'])
    assert abs(ri0 - RI_LATEST_PUBLISHED) < 0.005, f'rebuilt {m0} weight {ri0:.3f} != published {RI_LATEST_PUBLISHED}'
    latest = [k for k, v in A.items() if v is not None][-1]
    a, g_cpi = A[latest] / A[m0], G[latest] / G[m0]
    r = (100 * a - ri0 * g_cpi) / (100 - ri0)          # everything except gasoline, since m0
    return dict(dec=ri_dec, month=m0, month_ri=ri0, month_price=month_avg(m0), r=r, other_prices_through=latest)


def cpi_weight_at(price, b):
    """CPI gasoline weight (percent) at pump price `price`: RI = w*g / (w*g + (100-w)*r)."""
    g = price / b['month_price']
    return 100 * b['month_ri'] * g / (b['month_ri'] * g + (100 - b['month_ri']) * b['r'])


def v(cell, mpg, label):
    return dict(miles=NHTS[cell]['scaled'], mpg=mpg, label=label)


PROFILES = [
    dict(id='median', name='Median household', blurb='Married couple, two cars, median household income',
         income=INC_MEDIAN_HH, tax=dict(status='mfj', kids=0),
         cars=[v('veh2', MPG_ALL_LDV, 'Car 1'), v('veh2', MPG_ALL_LDV, 'Car 2')]),
    dict(id='single', name='Single young adult', blurb='One car, $50,000 salary',
         income=50_000, tax=dict(status='single', kids=0),
         cars=[v('veh1', MPG_SHORT_WB, 'Car')]),
    dict(id='rural', name='Rural family', blurb='Married, two kids, a car and a pickup, median rural income',
         income=INC_MEDIAN_NONMETRO, tax=dict(status='mfj', kids=2),
         cars=[v('rural_veh2', MPG_SHORT_WB, 'Car'), v('rural_veh2', MPG_LONG_WB, 'Pickup')]),
    dict(id='lower', name='Lower-income family', blurb='Married, two kids, two cars, 20th percentile income',
         income=INC_P20, tax=dict(status='mfj', kids=2),
         cars=[v('inc25_50_veh2', MPG_ALL_LDV, 'Car 1'), v('inc25_50_veh2', MPG_ALL_LDV, 'Car 2')]),
    dict(id='retired', name='Retired couple', blurb='Both 65+, one car, Social Security plus a pension',
         income=INC_MEDIAN_65, tax=dict(status='mfj', kids=0, seniors=2, social_security=12 * SS_COUPLE_MONTHLY),
         cars=[v('all65_veh1', MPG_ALL_LDV, 'Car')]),
    dict(id='suburban', name='Suburban three-car family', blurb='Married, two kids and a teen driver, median family income',
         income=INC_MEDIAN_FAMILY, tax=dict(status='mfj', kids=2),
         cars=[v('veh3', MPG_ALL_LDV, f'Car {i}') for i in (1, 2, 3)]),
]


def taxes(p):
    t = dict(p['tax'])
    ss = t.pop('social_security', 0.0)
    if t.get('seniors'):
        return after_tax(t['status'], 0.0, kids=t['kids'], seniors=t['seniors'], pension=p['income'] - ss, social_security=ss)
    return after_tax(t['status'], p['income'], kids=t['kids'])


def gas_cost(cars, price):
    return sum(c['miles'] / c['mpg'] for c in cars) * price


def main():
    ri = ri_from_xlsx()
    price_date, price = GAS[-1]
    cw = cpi_weight_basis(ri['Gasoline (all types)'])
    cw['now'] = cpi_weight_at(price, cw)
    out = dict(price=price, price_date=price_date, ri=ri, cpi=cw,
               cpi_weight_now=cw['now'], profiles=[])
    print(f"Gas ${price} ({price_date}). CPI gasoline weight: Dec 2025 {ri['Gasoline (all types)']}%, "
          f"{cw['month']} {cw['month_ri']:.3f}% (rebuilt; published {RI_LATEST_PUBLISHED}%), "
          f"at today's price {cw['now']:.3f}% (est., from {cw['month']} pump price ${cw['month_price']:.3f})")
    for p in PROFILES:
        t = taxes(p)
        cost = gas_cost(p['cars'], price)
        share = 100 * cost / t['after_tax']
        miles = sum(c['miles'] for c in p['cars'])
        out['profiles'].append(dict(p, after_tax=t['after_tax'], tax_detail=t, cost=cost, share=share))
        print(f"  {p['name']:26s} {miles:6,} mi  {cost:6,.0f}/yr  after-tax {t['after_tax']:8,.0f}  "
              f"share {share:4.1f}%  share of pretax {100*cost/p['income']:4.1f}%")
    PROCESSED.mkdir(parents=True, exist_ok=True)
    (PROCESSED / 'model.json').write_text(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
