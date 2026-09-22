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


def cpi_weight_model(ri_dec):
    """Carry the December 2025 gasoline weight to any gas price.

    Relative importance moves with relative prices: RI_t = w0*g / (w0*g + (100-w0)*r),
    where g is the gasoline price relative to December 2025 and r is the price
    relative for everything else. r comes from the latest CPI month, holding
    non-gasoline prices where they are now. g at a pump price P is P divided by
    the December 2025 EIA average. This is our estimate, not a BLS figure.
    """
    months = [m for m, v in CPI['all_items'].items() if v is not None]
    latest = months[-1]
    a = CPI['all_items'][latest] / CPI['all_items']['2025-12']
    g_t = CPI['gasoline_all_types'][latest] / CPI['gasoline_all_types']['2025-12']
    r = (100 * a - ri_dec * g_t) / (100 - ri_dec)
    return dict(w0=ri_dec, r=r, p_dec=month_avg('2025-12'), latest_cpi_month=latest,
                ri_latest_month=100 * ri_dec * g_t / (ri_dec * g_t + (100 - ri_dec) * r))


def cpi_weight_at(price, m):
    g = price / m['p_dec']
    return 100 * m['w0'] * g / (m['w0'] * g + (100 - m['w0']) * m['r'])


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
    wm = cpi_weight_model(ri['Gasoline (all types)'])
    price_date, price = GAS[-1]
    out = dict(price=price, price_date=price_date, ri=ri, weight_model=wm,
               cpi_weight_now=cpi_weight_at(price, wm), profiles=[])
    print(f"Gas ${price} ({price_date}). CPI gasoline weight: Dec 2025 {ri['Gasoline (all types)']}%, "
          f"{wm['latest_cpi_month']} {wm['ri_latest_month']:.2f}%, at today's price {out['cpi_weight_now']:.2f}% (est.)")
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
