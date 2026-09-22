"""Annual miles per vehicle for each profile, from the 2022 NHTS public-use microdata.

    .venv/bin/python src/nhts.py      -> data/processed/nhts_miles.json

Input: data/raw/driving/nhts2022_csv/ (NHTS 2022 v2.1, https://nhts.ornl.gov).
Weight WTHHFIN. SEs by Taylor linearization, strata STRATUMID, household as PSU
(the 2022 NHTS has no replicate weights).

ANNMILES is self-reported and has impossible values: 2.8% of weighted vehicles
report over 100,000 miles a year, many of them odometer readings. Those are
treated as missing ("clean100"). After that, NHTS still totals less than
FHWA's external count of household-vehicle miles, so every cell is scaled by
one factor: FHWA miles per household vehicle / NHTS clean100 miles per
household vehicle (Summary of Travel Trends 2022, Table 2-10). The NHTS
supplies the differences between groups; FHWA supplies the level.
"""
import json
import numpy as np
import pandas as pd
from common import RAW, PROCESSED

D = RAW / 'driving' / 'nhts2022_csv'
CAP = 100_000
LDV = [1, 2, 3, 4]                       # car, van, SUV, pickup
# Summary of Travel Trends 2022, Table 2-10, external benchmark columns
FHWA_HH_VMT_MILLIONS = 2_619_421
FHWA_HH_VEHICLES_THOUSANDS = 252_468
MIN_N = 250                              # smallest unweighted cell we use


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


def main():
    if not D.exists():   # the unzipped CSVs are not committed; the zip is
        import zipfile
        zipfile.ZipFile(RAW / 'driving' / 'nhts2022_csv.zip').extractall(D)
    h = pd.read_csv(D / 'hhv2pub.csv')
    v = pd.read_csv(D / 'vehv2pub.csv')
    p = pd.read_csv(D / 'perv2pub.csv')
    assert not h.HOUSEID.duplicated().any() and not v.duplicated(['HOUSEID', 'VEHID']).any()

    ages = p.groupby('HOUSEID').R_AGE
    h['all65'] = h.HOUSEID.map(ages.min().ge(65)).fillna(False)
    h['young_single'] = (h.HHSIZE == 1) & h.HOUSEID.map(ages.max().between(18, 34)).fillna(False)
    v = v.merge(h[['HOUSEID', 'all65', 'young_single']], on='HOUSEID')
    v['miles'] = v.ANNMILES.where((v.ANNMILES >= 0) & (v.ANNMILES <= CAP))
    allhh = v[v.miles.notna()]
    ldv = allhh[allhh.VEHTYPE.isin(LDV)]

    base, _ = wmean_se(allhh.miles, allhh.WTHHFIN, allhh.STRATUMID, allhh.HOUSEID)
    fhwa = FHWA_HH_VMT_MILLIONS * 1e6 / (FHWA_HH_VEHICLES_THOUSANDS * 1e3)
    k = fhwa / base

    cells = {
        'all_ldv': ldv,
        'veh1': ldv[ldv.HHVEHCNT == 1],
        'veh2': ldv[ldv.HHVEHCNT == 2],
        'veh3': ldv[ldv.HHVEHCNT == 3],
        'young_single_veh1': ldv[ldv.young_single & (ldv.HHVEHCNT == 1)],
        'rural_veh2': ldv[(ldv.URBRUR == 2) & (ldv.HHVEHCNT == 2)],
        'inc25_50_veh2': ldv[ldv.HHFAMINC_IMP.isin([4, 5]) & (ldv.HHVEHCNT == 2)],
        'inc100_150_veh3': ldv[ldv.HHFAMINC_IMP.isin([8, 9]) & (ldv.HHVEHCNT == 3)],
        'all65_veh1': ldv[ldv.all65 & (ldv.HHVEHCNT == 1)],
        'all65_veh2': ldv[ldv.all65 & (ldv.HHVEHCNT == 2)],
    }
    out = {'k': round(k, 4), 'fhwa_miles_per_hh_vehicle': round(fhwa, 1),
           'nhts_clean100_miles_per_hh_vehicle': round(base, 1), 'cells': {}}
    for name, d in cells.items():
        m, se = wmean_se(d.miles, d.WTHHFIN, d.STRATUMID, d.HOUSEID)
        pickup = (d.WTHHFIN * (d.VEHTYPE == 4)).sum() / d.WTHHFIN.sum()
        out['cells'][name] = dict(n=int(len(d)), nhts_mean=round(m, 1), se=round(se, 1),
                                  scaled=round(m * k), scaled_moe95=round(1.96 * se * k),
                                  pickup_share=round(pickup, 4), usable=len(d) >= MIN_N)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    (PROCESSED / 'nhts_miles.json').write_text(json.dumps(out, indent=1))
    print(f"k = {k:.4f} (FHWA {fhwa:,.0f} / NHTS clean100 {base:,.0f} miles per household vehicle)")
    for n, c in out['cells'].items():
        print(f"  {n:18s} n={c['n']:5d}  NHTS {c['nhts_mean']:8,.0f} ± {1.96*c['se']:6,.0f}  scaled {c['scaled']:7,}  pickups {c['pickup_share']:.1%}  {'' if c['usable'] else 'TOO SMALL'}")


if __name__ == '__main__':
    main()
