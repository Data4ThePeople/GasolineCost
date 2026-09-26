"""Fetch the gas price and CPI inputs into data/raw/.

    .venv/bin/python src/fetch_prices.py            everything
    .venv/bin/python src/fetch_prices.py --weekly   EIA and CPI only (scripts/weekly.sh)

- EIA weekly U.S. regular gasoline retail price (API v2), full history.
- BLS CPI relative importance table, December 2025 (xlsx, not in the API).
- BLS CPI-U index levels for gasoline (all types), motor fuel and all items,
  used to carry the December 2025 weight forward to the latest month.
"""
import json, sys, urllib.parse
from datetime import date
from common import RAW, get, keys, write_json

EIA_URL = 'https://api.eia.gov/v2/petroleum/pri/gnd/data/'
EIA_SERIES = 'EMM_EPMR_PTE_NUS_DPG'   # U.S. Regular All Formulations Retail Gasoline Prices
RI_YEAR = 2025                        # file year = weight vintage (December 2025)
RI_URL = f'https://www.bls.gov/cpi/tables/relative-importance/{RI_YEAR}.xlsx'
BLS_URL = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'
CPI_SERIES = {'CUUR0000SETB01': 'gasoline_all_types', 'CUUR0000SETB': 'motor_fuel', 'CUUR0000SA0': 'all_items'}


def eia_gasoline(key):
    # Sort must be descending: ascending silently drops the newest week
    # (found in CrackSpreadCalc, 2026-08-06).
    rows, offset, total = [], 0, None
    while total is None or len(rows) < total:
        p = [('api_key', key), ('frequency', 'weekly'), ('data[0]', 'value'),
             ('facets[series][]', EIA_SERIES), ('sort[0][column]', 'period'),
             ('sort[0][direction]', 'desc'), ('offset', offset), ('length', 5000)]
        r = json.loads(get(EIA_URL + '?' + urllib.parse.urlencode(p)))['response']
        total = int(r['total'])
        if not r['data']:
            break
        rows += r['data']
        offset += len(r['data'])
    periods = [d['period'] for d in rows]
    assert len(periods) == len(set(periods)), 'duplicate weeks in EIA response'
    nulls = [d['period'] for d in rows if d['value'] is None]
    if nulls:
        print(f'  EIA: {len(nulls)} weeks with no value, dropped: {sorted(nulls)[:5]}...')
    return sorted((d['period'], float(d['value'])) for d in rows if d['value'] is not None)


def bls_cpi(key):
    out = {}
    for start, end in ((2006, 2015), (2016, date.today().year)):   # API allows 20 years per call
        body = json.dumps({'seriesid': list(CPI_SERIES), 'startyear': str(start), 'endyear': str(end),
                           'registrationkey': key}).encode()
        r = json.loads(get(BLS_URL, data=body, headers={'Content-Type': 'application/json'}))
        assert r['status'] == 'REQUEST_SUCCEEDED', r.get('message')
        for s in r['Results']['series']:
            d = out.setdefault(CPI_SERIES[s['seriesID']], {})
            for x in s['data']:
                if x['period'].startswith('M') and x['period'] != 'M13':
                    k = f"{x['year']}-{x['period'][1:]}"
                    assert k not in d, f'duplicate month {k}'
                    # '-' marks a month BLS did not publish (October 2025,
                    # lost to the federal shutdown). Kept as None, never filled.
                    d[k] = None if x['value'].strip() == '-' else float(x['value'])
    return {k: dict(sorted(v.items())) for k, v in out.items()}


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    k = keys()
    gas = eia_gasoline(k('EIA_API_KEY'))
    write_json(RAW / 'eia_gasoline_regular_weekly.json', {'series': EIA_SERIES, 'data': gas})
    print(f'EIA regular gasoline: {len(gas)} weeks, latest {gas[-1]}')

    # The relative importance table comes out once a year; the weekly job
    # leaves it alone so a re-download never shows up as a change.
    if '--weekly' not in sys.argv:
        b = get(RI_URL)
        assert b.startswith(b'PK'), f'{RI_URL} did not return an xlsx'
        (RAW / f'cpi_relative_importance_{RI_YEAR}.xlsx').write_bytes(b)
        print(f'BLS relative importance {RI_YEAR}: {len(b):,} bytes')

    cpi = bls_cpi(k('BLS_API_KEY'))
    write_json(RAW / 'bls_cpi_u_nsa.json', cpi, indent=1)
    print('BLS CPI-U:', {s: list(v.items())[-1] for s, v in cpi.items()})


if __name__ == '__main__':
    sys.exit(main())
