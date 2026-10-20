# Gasoline as a share of household take-home pay

This project compares the CPI's gasoline weight with what gasoline costs six example
U.S. households as a share of their take-home pay after federal taxes. It includes an
interactive tool where readers can change the gas price and enter their own miles,
fuel economy and income.

## Live links

- Tool: https://data4thepeople.github.io/GasolineCost/
- Embed version: https://data4thepeople.github.io/GasolineCost/embed.html
- Post: https://www.data4thepeople.com/p/gasoline-share-of-income

The tool's gas price updates weekly. The post's own numbers and charts stay as published.

## What's here

- `posts/gasoline-share-of-income/` : the post text (`POST.md`) and its chart images.
- `src/` : the Python code.
  - `fetch_prices.py` : downloads EIA gas prices, BLS CPI index levels and the BLS relative importance table.
  - `nhts.py` : annual miles per vehicle for each household profile, from NHTS 2022 microdata.
  - `tax.py` : 2026 federal income tax and payroll tax.
  - `cex.py` : reads the Consumer Expenditure Survey tables.
  - `model.py` : household profiles, gas cost, share of take-home pay, and the CPI gasoline weight at any price.
  - `tieout.py` : recomputes every published number and checks the profiles against the Consumer Expenditure Survey.
  - `charts.py` : static charts for the post.
  - `build.py` and `template.html` : build the interactive tool.
- `data/raw/` : downloaded source files, plus `NOTES_*.md` files with the URL and table name behind each input.
- `data/processed/` : `model.json`, `nhts_miles.json` and the tie-out report `tieout.md`.
- `dist/` and `docs/` : the built tool (`index.html` and `embed.html`). GitHub Pages serves `docs/`.
- `charts/` : chart images as built by `charts.py`.
- `scripts/weekly.sh` : the weekly update job (fetch, rebuild, commit).
- `DATASETS.md` : full notes on every data source, its quirks, and open issues.

## Data sources

| Agency | Dataset | Used for |
|---|---|---|
| U.S. Energy Information Administration | Weekly U.S. regular gasoline retail price, all formulations (API v2, series `EMM_EPMR_PTE_NUS_DPG`) | Current and historical pump price |
| U.S. Bureau of Labor Statistics | CPI relative importance, December 2025 | Gasoline's weight in the CPI |
| U.S. Bureau of Labor Statistics | CPI-U index levels (gasoline, motor fuel, all items) | Carrying the CPI weight forward to the latest month |
| U.S. Bureau of Labor Statistics | Consumer Expenditure Survey, 2023 and 2024 | Reality check on the profiles |
| U.S. Census Bureau | Income in the United States: 2025, P60-289 (CPS ASEC) | Household incomes |
| U.S. Census Bureau | American Community Survey 1-year 2024, B08201 and B19013 | Vehicles available per household |
| U.S. Census Bureau | Vintage 2025 population estimates | U.S. population |
| Federal Highway Administration | National Household Travel Survey 2022, NextGen NHTS v2.1 | Miles driven per vehicle |
| Federal Highway Administration | Highway Statistics 2024, Table VM-1 | On-road fuel economy |
| Internal Revenue Service | Rev. Proc. 2025-32, Pub. 915 | 2026 federal tax parameters |
| Social Security Administration | 2026 wage base and COLA fact sheet | Payroll tax and retired couple's benefits |
| U.S. Environmental Protection Agency | Automotive Trends Report, 2025 edition | Context only |

See `DATASETS.md` for versions, coverage, known quirks and attribution.

## How to rebuild

Requirements: Python 3 in a `.venv` at the repo root with `pandas`, `numpy`,
`openpyxl` and `matplotlib`. `build.py` also runs checks with macOS JavaScriptCore and
Google Chrome, so the full build runs on a Mac.

API keys: `EIA_API_KEY` and `BLS_API_KEY`. A contact address for the download
User-Agent is read from `D4TP_CONTACT_EMAIL`. These are loaded from a private env file
outside the repo and are not included here.

```sh
# 1. Fetch gas prices, CPI index levels and the CPI relative importance table
.venv/bin/python src/fetch_prices.py

# 2. (Optional) Recompute miles per vehicle. Unzip data/raw/driving/nhts2022_csv.zip
#    into data/raw/driving/nhts2022_csv/ first. The output is already committed.
.venv/bin/python src/nhts.py

# 3. Build the model
.venv/bin/python src/model.py

# 4. Tie-out report
.venv/bin/python src/tieout.py

# 5. Charts for the post
.venv/bin/python src/charts.py

# 6. Build the tool into dist/ and docs/
.venv/bin/python src/build.py
```

The weekly job, `scripts/weekly.sh`, runs `fetch_prices.py --weekly` (EIA and CPI
only), then `model.py` and `build.py` if either source changed.

## Method notes

- Gasoline cost is gallons burned times the price, divided by take-home pay after
  federal income and payroll taxes. State and local income taxes are left out, which
  makes take-home pay higher and every share lower than it would be with them.
- Miles come from the 2022 NHTS. Vehicles reporting over 100,000 miles a year are
  treated as missing, and every cell is then scaled so the total matches FHWA's count
  of household vehicle miles.
- The CPI comparison starts from the BLS published gasoline weight for July 2026,
  3.77%, and moves it to any pump price using the change in the EIA price and the
  change in all other CPI prices.
- The six households are built from published averages for real groups. No single
  family matches all of the inputs at once.
- `build.py` checks that the tool's numbers match `model.py` for every profile at
  three prices before it writes the page.

Data 4 The People
