"""Weighted driving profiles from the 2022 NextGen NHTS public-use CSV (v2.1).

Source zip: https://nhts.ornl.gov/media/2022/download/csv.zip (unzipped to nhts2022_csv/).
Weight: WTHHFIN (7-day national household weight, trimmed in v2.0) for households and vehicles.
SEs: Taylor linearization, stratified by STRATUMID, household as the PSU (the 2022 NHTS has
no replicate weights; the Weighting Memo recommends Taylor series).

Mileage variable: ANNMILES (self-reported, annualized). -9 = not ascertained, top-coded 200,000.
Three versions are reported:
  raw      : all ANNMILES >= 0
  clean100 : ANNMILES > 100,000 treated as missing (implausible, likely odometer readings)
  clean50  : ANNMILES > 50,000 treated as missing (sensitivity)
Household totals drop any household with a missing (or excluded) vehicle mileage.

Run: .venv/bin/python data/raw/driving/nhts2022_profiles.py
Writes: data/raw/driving/nhts2022_computed_profiles.csv
"""
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
D = HERE / 'nhts2022_csv'
h = pd.read_csv(D / 'hhv2pub.csv')
v = pd.read_csv(D / 'vehv2pub.csv')
p = pd.read_csv(D / 'perv2pub.csv')

INC = {1: '<$10k', 2: '$10-15k', 3: '$15-25k', 4: '$25-35k', 5: '$35-50k', 6: '$50-75k',
       7: '$75-100k', 8: '$100-125k', 9: '$125-150k', 10: '$150-200k', 11: '$200k+'}
INC5 = {1: '<$25k', 2: '<$25k', 3: '<$25k', 4: '$25-50k', 5: '$25-50k', 6: '$50-100k', 7: '$50-100k',
        8: '$100-150k', 9: '$100-150k', 10: '$150k+', 11: '$150k+'}
LDV = [1, 2, 3, 4]  # car, van, SUV, pickup


def wmedian(x, w):
    o = np.argsort(x.values); x, w = x.values[o], w.values[o]
    c = np.cumsum(w); return float(x[np.searchsorted(c, c[-1] / 2)])


def wmean_se(y, w, strata, psu):
    """Ratio mean sum(wy)/sum(w) with stratified Taylor SE, PSU = household."""
    y, w = y.values.astype(float), w.values.astype(float)
    W = w.sum(); m = (w * y).sum() / W
    z = pd.DataFrame({'s': strata.values, 'u': psu.values, 'z': w * (y - m) / W})
    z = z.groupby(['s', 'u']).z.sum().reset_index()
    var = 0.0
    for _, g in z.groupby('s'):
        n = len(g)
        if n > 1:
            var += n / (n - 1) * ((g.z - g.z.mean()) ** 2).sum()
    return m, var ** 0.5


rows = []


def add(section, group, var, d, y, w='WTHHFIN', median=True):
    d = d[d[y].notna()]
    m, se = wmean_se(d[y], d[w], d.STRATUMID, d.HOUSEID)
    rows.append(dict(section=section, group=group, measure=var, mean=round(m, 4), se=round(se, 4),
                     moe95=round(1.96 * se, 4),
                     median=round(wmedian(d[y], d[w]), 1) if median else np.nan,
                     n_unweighted=len(d), weighted_total=round(d[w].sum())))


# person-based household flags
p1 = p[p.PERSONID == 1].set_index('HOUSEID').R_AGE
allold = p.groupby('HOUSEID').R_AGE.min().ge(65)
h['HH_65'] = h.HOUSEID.map(p1).ge(65)
h['ALL_65'] = h.HOUSEID.map(allold).fillna(False)
h['VEHGRP'] = h.HHVEHCNT.clip(upper=4).map({0: '0', 1: '1', 2: '2', 3: '3', 4: '4+'})
h['INC'] = h.HHFAMINC_IMP.map(INC); h['INC5'] = h.HHFAMINC_IMP.map(INC5)
h['UR'] = h.URBRUR.map({1: 'Urban', 2: 'Rural'})
v = v.merge(h[['HOUSEID', 'HH_65', 'ALL_65', 'VEHGRP', 'INC', 'INC5', 'UR']], on='HOUSEID')

for ver, cap in [('raw', None), ('clean100', 100000), ('clean50', 50000)]:
    mi = v.ANNMILES.where(v.ANNMILES >= 0)
    if cap: mi = mi.where(mi <= cap)
    v['MI'] = mi
    # vehicle level
    add(f'vehicle_{ver}', 'All household vehicles', 'annual miles per vehicle', v, 'MI')
    lv = v[v.VEHTYPE.isin(LDV)]
    add(f'vehicle_{ver}', 'Light-duty (car/van/SUV/pickup)', 'annual miles per vehicle', lv, 'MI')
    for t, nm in {1: 'Car', 2: 'Van', 3: 'SUV', 4: 'Pickup'}.items():
        add(f'vehicle_{ver}', nm, 'annual miles per vehicle', v[v.VEHTYPE == t], 'MI')
    for g in ['Urban', 'Rural']:
        add(f'vehicle_{ver}', g, 'annual miles per light-duty vehicle', lv[lv.UR == g], 'MI')
    # household level: sum over all vehicles, drop households with any missing
    agg = v.groupby('HOUSEID').agg(tot=('MI', 'sum'), nmiss=('MI', lambda s: s.isna().sum()))
    hh = h.merge(agg, on='HOUSEID', how='left')
    hh.loc[hh.HHVEHCNT == 0, ['tot', 'nmiss']] = [0, 0]
    hh['HHMI'] = hh.tot.where(hh.nmiss == 0)
    veh = hh[hh.HHVEHCNT > 0]
    sec = f'household_{ver}'
    add(sec, 'All households (incl. 0-vehicle)', 'household annual vehicle miles', hh, 'HHMI')
    add(sec, 'Vehicle-owning households', 'household annual vehicle miles', veh, 'HHMI')
    for g in ['1', '2', '3', '4+']:
        add(sec, f'HHVEHCNT={g}', 'household annual vehicle miles', veh[veh.VEHGRP == g], 'HHMI')
    for g in ['Urban', 'Rural']:
        add(sec, f'{g}, all households', 'household annual vehicle miles', hh[hh.UR == g], 'HHMI')
        add(sec, f'{g}, vehicle-owning', 'household annual vehicle miles', veh[veh.UR == g], 'HHMI')
    for k in dict.fromkeys(INC5.values()):
        add(sec, f'Income {k}, all households', 'household annual vehicle miles', hh[hh.INC5 == k], 'HHMI')
        add(sec, f'Income {k}, vehicle-owning', 'household annual vehicle miles', veh[veh.INC5 == k], 'HHMI')
    for k in INC.values():
        add(sec, f'Income {k} (HHFAMINC_IMP), vehicle-owning', 'household annual vehicle miles',
            veh[veh.INC == k], 'HHMI')
    for flag, nm in [('HH_65', 'Primary respondent (PERSONID 01) 65+'),
                     ('ALL_65', 'All person-file members 65+')]:
        add(sec, f'{nm}, all households', 'household annual vehicle miles', hh[hh[flag]], 'HHMI')
        add(sec, f'{nm}, vehicle-owning', 'household annual vehicle miles', veh[veh[flag]], 'HHMI')
        add(sec, f'NOT {nm}, vehicle-owning', 'household annual vehicle miles', veh[~veh[flag]], 'HHMI')
    if ver == 'raw':
        tot = (hh.HHMI.fillna(0) * hh.WTHHFIN).sum()
        miss = hh[hh.HHMI.isna()].WTHHFIN.sum()
        print('weighted total annual household VMT (raw ANNMILES, missing HH excluded):', round(tot / 1e6), 'million;',
              'excluded HH weight', round(miss))

# fleet composition (no mileage)
v['PICKUP'] = (v.VEHTYPE == 4).astype(float); v['SUV'] = (v.VEHTYPE == 3).astype(float)
v['PKSUV'] = v.VEHTYPE.isin([3, 4]).astype(float)
v['GASDIESEL'] = v.VEHFUEL.isin([1, 2, 3]).astype(float)
v['VEHAGE_'] = v.VEHAGE.where(v.VEHAGE > 0); v['VEHYEAR_'] = v.VEHYEAR.where(v.VEHYEAR > 0)
lv = v[v.VEHTYPE.isin(LDV)]
groups = [('All', v, lv, h)] + [(g, v[v.UR == g], lv[lv.UR == g], h[h.UR == g]) for g in ['Urban', 'Rural']] + \
         [(f'Income {k}', v[v.INC5 == k], lv[lv.INC5 == k], h[h.INC5 == k]) for k in dict.fromkeys(INC5.values())] + \
         [('Primary respondent 65+', v[v.HH_65], lv[lv.HH_65], h[h.HH_65])]
for g, dv, dl, dh in groups:
    add('fleet', g, 'share pickup (of all HH vehicles)', dv, 'PICKUP', median=False)
    add('fleet', g, 'share SUV (of all HH vehicles)', dv, 'SUV', median=False)
    add('fleet', g, 'share pickup+SUV (of all HH vehicles)', dv, 'PKSUV', median=False)
    add('fleet', g, 'share gas/diesel/biodiesel fuel (of all HH vehicles)', dv, 'GASDIESEL', median=False)
    add('fleet', g, 'vehicle age, light-duty (VEHAGE)', dl, 'VEHAGE_')
    add('fleet', g, 'model year, light-duty (VEHYEAR)', dl, 'VEHYEAR_')
    add('fleet', g, 'vehicles per household (HHVEHCNT)', dh, 'HHVEHCNT')

out = pd.DataFrame(rows)
out.to_csv(HERE / 'nhts2022_computed_profiles.csv', index=False)
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 1000); pd.set_option('display.max_colwidth', 60)
print(out.to_string())
