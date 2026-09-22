"""Read the BLS Consumer Expenditure Survey group tables in data/raw/cex/.

Each "mean, item share, average, standard error" table has an item column and one
column per group; each item is a heading row followed by Mean / Share / SE / RSE rows.
"""
import warnings
import pandas as pd
from common import RAW

warnings.filterwarnings('ignore', module='openpyxl')
ITEMS = {'income_before': 'Income before taxes', 'income_after': 'Income after taxes',
         'spending': 'Average annual expenditures', 'gas': 'Gasoline and other fuels'}


def read(table, year):
    df = pd.read_excel(RAW / 'cex' / f'mis-{table}-{year}.xlsx', header=None)
    hdr = [str(x).replace('\n', ' ').strip() for x in df.iloc[2].tolist()]
    names = [n if n != 'nan' else None for n in hdr]
    col0 = df[0].astype(str).str.strip()
    out = {n: {} for n in names[1:] if n}
    for key, label in ITEMS.items():
        idx = df.index[col0.str.startswith(label)]
        if not len(idx):
            continue                       # 2024 tables have no after-tax income
        i = idx[0]
        mean_row = df.iloc[i + 1]; se_row = df.iloc[i + 2] if key != 'gas' else df.iloc[i + 3]
        assert str(mean_row[0]).strip() == 'Mean', (table, year, label)
        for j, n in enumerate(names):
            if j and n:
                out[n][key] = float(mean_row[j])
                out[n][key + '_se'] = float(se_row[j])
    vi = df.index[col0 == 'Vehicles'][0]
    for j, n in enumerate(names):
        if j and n:
            out[n]['vehicles'] = float(df.iloc[vi][j])
    return out


if __name__ == '__main__':
    for t in ('cu-income-quintiles-before-taxes', 'cu-area-type', 'reference-person-age-ranges'):
        for y in (2023, 2024):
            print(t, y, {k: {a: round(b) if a != 'vehicles' else b for a, b in v.items() if not a.endswith('_se')} for k, v in read(t, y).items()})
