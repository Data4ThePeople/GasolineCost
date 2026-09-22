# Datasets

Written September 22, 2026, during Step 1. The research notes behind each section are in
`data/raw/NOTES_*.md`, which give every URL and table name. "Checked" means we measured it
in this project; "not verified" means we are repeating the publisher or have not looked.

## Open issues

1. **NHTS annual miles are self-reported and noisy** (see the NHTS section). We cap them,
   then scale to FHWA's total. The profile miles rest on that choice.
2. **Incomes are 2025 dollars; tax law is 2026.** Census income for 2025 is the newest.
   Applying 2026 brackets, which are indexed for inflation, to 2025 incomes
   understates tax slightly, which overstates after-tax income slightly, which
   understates the gas share. The effect is small and runs against our finding.
3. **After-tax income here is federal only.** Census's post-tax median also subtracts
   state and local income tax. Our median household comes out $1,426 below Census's
   post-tax median ($74,634 vs. $76,060), because a household with the median pretax
   income is not the same as the household with the median post-tax income, and our
   median profile is a married couple with no children. Checked; see tie-out.
4. **BLS stopped publishing CEX after-tax income with the 2024 data.** The latest
   after-tax gas shares from one survey are for 2023.
5. **The comparison line is the CPI gasoline weight at today's price, 4.3%, our estimate.**
   It starts from the latest relative importance BLS has published for gasoline, July
   2026, 3.77% (figure from Eric; our rebuild from the December table gives 3.770%, and
   the build fails if they differ by 0.005 or more). We move it to today's price with the
   EIA pump price change since July ($3.932 to $4.478) and the change in all other CPI
   prices since July (+0.23% through August). Result 4.261%, shown as 4.3%. The same
   formula moves the weight with the tool's price slider ($3: 2.9%, $5: 4.7%, $7: 6.5%),
   so every comparison is at the same price. Decided September 22. The formula, its four
   assumptions and the sensitivity test are in the relative importance section below.
6. **October 2025 CPI was never published** (federal shutdown). We do not use that month.

---

## EIA weekly U.S. regular gasoline retail price (U.S. Energy Information Administration)

**What it is.** Average retail price of regular gasoline, all formulations, U.S., in
dollars per gallon, including taxes. One value per week, dated Monday.

**Where it comes from.** EIA API v2, route `petroleum/pri/gnd`, series
`EMM_EPMR_PTE_NUS_DPG`. Key `EIA_API_KEY`. `src/fetch_prices.py` writes
`data/raw/eia_gasoline_regular_weekly.json`.

**Version and vintage.** Pulled September 22, 2026. Latest week September 21, 2026:
$4.478. Weekly, released Monday evenings.

**Coverage.** August 20, 1990 to present, 1,884 weeks in the API, 6 of them null
(December 1990 to January 1991), which we drop. Checked. How EIA samples stations and
weights them is not verified here; the method page should be read before publication.

**Changes over time.** Not relevant: we use the latest week and the December 2025 average.

**Missing data.** The 6 null weeks above. None since 1991.

**Revisions.** EIA rarely revises weekly retail prices. Not verified.

**Units and rounding.** Dollars per gallon to 3 decimals.

**Known quirks.** The API drops the newest week when sorted ascending (found in
CrackSpreadCalc, 2026-08-06). We sort descending. The December 2025 average of the 5
weekly values is $2.8944; the page uses it to move the CPI weight with price.

**Uncertainty.** Not published in the API. Not verified.

**License and attribution.** Public domain. Credit "U.S. Energy Information Administration".

---

## CPI relative importance, December 2025 (U.S. Bureau of Labor Statistics)

**What it is.** Each item's share of the CPI-U market basket, in percent of all items,
as of December 2025. Gasoline (all types) is 2.895; motor fuel is 2.981. For CPI-W
(wage earners) the figures are 3.971 and 4.078.

**Where it comes from.** `https://www.bls.gov/cpi/tables/relative-importance/2025.xlsx`,
Table 1. Not in the BLS API. BLS returns 403 unless the user agent starts like a browser.
Saved as `data/raw/cpi_relative_importance_2025.xlsx`.

**Version and vintage.** Built from 2024 expenditure weights (from the CEX), moved
forward to December 2025 by each item's price change. The 2026 file (December 2026) does
not exist yet (404, checked).

**Coverage.** U.S. city average, urban consumers (CPI-U covers about 90% of the
population, per BLS; not verified here).

**Changes over time.** BLS now updates weights every year. Relative importance moves
between weight updates as relative prices change: when gasoline rises faster than
everything else, its share rises.

**Known quirks.** The table's special aggregates section overlaps the item tree; we read
only rows above "Special aggregate indexes". The build fails if gasoline or motor fuel
changes from 2.895 or 2.981.

**What the weight means.** Total gasoline spending by all urban consumers divided by
their total spending. Households with no car, households that drive little, and
high-spending households all count. It is a share of spending, not of income, and not
the share for any typical household. That is the gap this project measures.

**How the CPI line is calculated (the method behind open issue 5).** In `src/model.py`,
`cpi_weight_basis()` and `cpi_weight_at()`. At a pump price P:

    weight(P) = w * g / (w * g + (100 - w) * r)

- **w = 3.77**, the gasoline (all types) relative importance BLS published for July 2026,
  the latest month available. Rebuilt here from the December 2025 table and the CPI-U
  indexes as 3.770%; the build fails if that drifts from 3.77 by 0.005 or more.
- **g = P / $3.9322**, the price against the July 2026 EIA average.
- **r = 1.00231**, the price relative for everything except gasoline, solved from the
  August 2026 CPI release: all items rose 0.318% from July, gasoline rose 2.53%, which
  leaves the rest at +0.23%. It is held at that value at every price.

At $4.478 this gives 4.261%, shown as 4.3%. The curve is nearly straight: 0.911 points
per $1 at that price, and 0.911 averaged from $2 to $7.

**The four assumptions in that line, and which way each one bends it.**

1. **Quantities are fixed.** The same gallons are bought at $7 as at $2, and the rest of
   the basket does not change. This is how BLS itself moves relative importance between
   weight years, but drivers do cut back when prices spike, so at high prices our line
   very likely sits above what BLS would publish. Bends the line **up**.
2. **Everything else stays at its August 2026 level.** Non-gasoline prices do not respond
   to gasoline at all here. Higher fuel does feed into airfares, delivery and food, which
   would raise the denominator and lower gasoline's share. Bends the line **up**.
3. **The pump price and the CPI gasoline index move one for one.** The weakest of the
   four. From July to August 2026 the EIA average rose 3.20% while CPI gasoline rose
   2.53%, a pass-through of 0.79. Collection timing differs and the CPI covers all
   grades while we track regular. At that 0.79 rate the weight at $4.478 would be
   **4.16% instead of 4.261%**. Bends the line **up** by about a tenth of a point.
4. **The July base is sound.** It rests on BLS's 2024 spending weights, price-updated.
   Checked against our own rebuild, as above.

All four run the same way: the CPI line is, if anything, a little too high, so the gap
between a driving household and the CPI is understated rather than overstated. Checked
September 22, 2026.

**December 2023 file.** `data/raw/cpi_relative_importance_2023.xlsx` (2022 weights):
gasoline (all types) 3.261, motor fuel 3.372. Used only in chart 3, beside 2023 CEX
spending, so both are from the same year.

**License and attribution.** Public domain. Credit "U.S. Bureau of Labor Statistics".

## CPI-U index levels (U.S. Bureau of Labor Statistics)

**What it is.** Not seasonally adjusted CPI-U, U.S. city average: gasoline all types
(CUUR0000SETB01), motor fuel (CUUR0000SETB), all items (CUUR0000SA0), 2006 to August 2026.

**Where it comes from.** BLS API v2 with `BLS_API_KEY`, `data/raw/bls_cpi_u_nsa.json`.

**Missing data.** October 2025 is "-" for all items and motor fuel (not collected during
the shutdown); gasoline has a value. Stored as null, never filled. Checked.

**Revisions.** NSA CPI is not revised. Used only for the ratio above.

---

## Income in the United States: 2025, P60-289 (U.S. Census Bureau, CPS ASEC)

**What it is.** Household money income (pretax, cash) and post-tax income for 2025.

**Where it comes from.** Released September 15, 2026. Tables in `data/raw/census/`
(Table 4 for group medians, Table 5 and H-1 for percentiles, Table 10 for post-tax
percentiles), and `p60-289.pdf`.

**Figures we use.** All households: median $87,460 (MOE $1,040), post-tax $76,060.
Family households $112,900. Householder 65+ $59,680. Outside metro areas $68,670.
Pretax percentiles: 10th $20,010, 20th $35,800, 40th $68,600, 60th $110,300, 80th
$182,400, 90th $261,300, 95th $354,000.

**Coverage.** Civilian noninstitutional population plus people in noninstitutional group
quarters. The weighted response rate for the 2026 CPS ASEC was 61.3% (62.0% the year
before); Census's Appendix B discusses nonresponse bias (not read in full). Census fills
missing income answers by imputation; the share imputed for 2025 is not verified here.

**Post-tax income is modeled.** Census does not ask about taxes. The CPS ASEC Tax Model
simulates federal, state, and some local income taxes, FICA, and credits for tax year
2025 (P60-289, "Post-Tax Income"). So Census's post-tax median is itself a model result.

**Changes over time.** Only 2025 is used.

**Suppressed values.** Census publishes the 10th, 20th, 30th and so on to the 95th
percentile. There is no 25th percentile in the published tables.

**Units and rounding.** Current 2025 dollars, rounded to $10.

**License and attribution.** Public domain. Credit "U.S. Census Bureau, Current
Population Survey, 2026 Annual Social and Economic Supplement".

## ACS 1-year 2024, B08201 and B19013 (U.S. Census Bureau)

Used for one fact: the median household has 2 vehicles available (8.5% none, 33.2% one,
36.3% two, 14.4% three, 7.6% four or more; 132.7 million households). The 2025 ACS
1-year has not been released (Census is reviewing it against a Commerce Department
disclosure order). ACS income ($81,604) is not mixed with CPS income anywhere.

---

## National Household Travel Survey 2022, NextGen NHTS v2.1 (FHWA)

**What it is.** A national survey of households, their people, vehicles, and one travel
day. We use the vehicle file's ANNMILES (the respondent's estimate of miles driven in
the past 12 months) and household traits.

**Where it comes from.** `https://nhts.ornl.gov`, public CSV,
`data/raw/driving/nhts2022_csv/`. Code in `src/nhts.py`.

**Coverage.** 7,893 households, 14,684 vehicles, 14,008 of them light-duty. Weight
WTHHFIN. FHWA says 2022 results are valid at the national, census division, and
urban/rural level only. The survey was 99% web in 2022.

**Checked, light-duty vehicles, weighted:**
- 1.64% have no mileage answer.
- 2.82% report over 100,000 miles a year (108 at the 200,000 top code). Many look like
  odometer readings. We treat these as missing.
- 95.55% are usable.
- 71.8% of usable answers are round thousands. These are estimates, not odometer
  records, and the median is a poor summary. We use means.
- Household income is imputed for 1.29% of households (weighted).

**How we set the level.** After the cap, NHTS averages 9,689 miles per household vehicle.
FHWA's external benchmark in the Summary of Travel Trends 2022 (Table 2-10) is 2,619,421
million miles on 252,468 thousand household vehicles, or 10,375 miles per vehicle.
Every NHTS cell is multiplied by 10,375 / 9,689 = 1.0708. The NHTS gives the differences
between groups; FHWA gives the level.

**Cells used (per light-duty vehicle, scaled, with 95% margin).**
| Cell | Vehicles (n) | Miles per vehicle | ± |
|---|---|---|---|
| 1-vehicle households | 2,489 | 12,188 | 1,047 |
| 2-vehicle households | 6,048 | 11,092 | 587 |
| 3-vehicle households | 2,864 | 9,993 | 789 |
| Rural, 2 vehicles | 1,241 | 11,782 | 1,410 |
| Income $25k to $50k, 2 vehicles | 871 | 9,748 | 1,664 |
| Everyone 65+, 1 vehicle | 867 | 8,928 | 1,601 |

A cell for young single adults (one person, 18 to 34, one car) had only 239 vehicles and a
margin of about ±4,500 miles, so the single young adult uses the 1-vehicle cell.

**Changes over time.** 2022 has no BESTMILE (the modeled mileage 2017 had). Trip-based
VMT in 2022 was 71% of the benchmark, down from 80% in 2017. Not comparable with 2017
without adjustment.

**Known quirks.** The person file covers members 5 and older; "everyone 65+" means every
listed member is 65 or older.

**Uncertainty.** Taylor-linearized SEs with STRATUMID strata, household as PSU (no
replicate weights in 2022). Margins above.

**License and attribution.** Public domain. Credit "Federal Highway Administration,
2022 National Household Travel Survey".

## Highway Statistics 2024, Table VM-1 (FHWA)

**What it is.** Annual vehicle miles, vehicles, fuel used, and miles per gallon by
vehicle class for all registered vehicles, including business fleets.

**Figures we use.** Light-duty short wheelbase 25.5857 mpg; long wheelbase 18.4963 mpg;
all light-duty 23.4307 mpg. Miles per vehicle: 10,786.65 all light-duty.

**Where it comes from.** `data/raw/driving/fhwa_vm1_2024.xlsx` (published February
2026). The 2025 edition is not out.

**Coverage and filling.** FHWA builds VM-1 from state fuel and travel reports and splits
it across vehicle classes with its own models. The class split and the mpg are modeled
estimates, not measurements of individual vehicles (per FHWA's notes; the method paper
has not been read in full).

**Changes over time.** Vehicle classes were redefined in 2011. Only 2024 is used.

**License and attribution.** Public domain. Credit "Federal Highway Administration,
Highway Statistics 2024".

## EPA Automotive Trends Report, 2025 edition (context only)

New model-year 2024 vehicles average 27.2 mpg in real-world driving (25.6 excluding EVs
and plug-in hybrids). This is for new vehicles only. The average vehicle on the road is
12.8 years old (S&P Global Mobility, May 2025), so we use FHWA's on-road fleet figure,
not EPA's.

---

## Consumer Expenditure Survey, 2023 and 2024 (U.S. Bureau of Labor Statistics)

**What it is.** Average annual spending and income per consumer unit, by group. We use
it as a reality check on the profiles, not as a profile input.

**Where it comes from.** 2024 tables released December 19, 2025 (later than usual);
2023 tables released September 2024. `data/raw/cex/`.

**Key definitions.** "Gasoline and other fuels" (since 2023): gasoline, diesel, gasoline
bought on out-of-town trips, and EV charging. Motor oil left the category in 2023.

**Figures we use (2023, gas as share of after-tax income).** All consumer units 3.1%.
Income quintiles, lowest to highest: 8.2%, 5.3%, 4.1%, 3.2%, 1.9%. Rural 3.9%, urban 2.9%.

**Changes over time.** BLS stopped publishing income after taxes starting with 2024
data (TAXSIM-based taxes discontinued). The category change in 2023 breaks comparison
with 2022 and earlier.

**Known quirks.** All figures are means per consumer unit, not medians per household.
The lowest income groups report spending about twice their income, so income-based
shares for those groups run high. CEX quintile cut points differ from CPS quintiles.
BLS fills missing income answers by multiple imputation (not verified for 2024).

**Uncertainty.** Standard errors are in the tables. All-CU 2024 "gasoline and other
fuels" $2,645, SE $34.55.

**License and attribution.** Public domain. Credit "U.S. Bureau of Labor Statistics,
Consumer Expenditure Surveys".

---

## Tax parameters, tax year 2026 (IRS, SSA)

IRS Rev. Proc. 2025-32 (brackets, standard deduction, extra deduction for 65+, child tax
credit, EITC), 26 U.S.C. 151(d)(5)(C) (the $6,000 senior deduction, 2025 to 2028), SSA
2026 wage base $184,500, IRS Pub. 915 (taxable Social Security). Full table with
citations in `data/raw/NOTES_tax_2026.md`. `src/tax.py` checks the cumulative tax at
every bracket start against the Rev. Proc. tables.

SSA 2026 COLA fact sheet: aged couple, both receiving benefits, $3,208 a month after the
2.8% COLA (`data/raw/ssa/ssa_2026_cola_factsheet.pdf`).

---

## Model assumptions (not data)

| Profile | Income | Tax household | Cars and miles | mpg |
|---|---|---|---|---|
| Median household | $87,460, CPS median | Married, no children | 2 × 11,092 (NHTS 2-vehicle) | 23.43 (VM-1 all light-duty) |
| Single young adult | $50,000, Eric's figure | Single | 1 × 12,188 (NHTS 1-vehicle) | 25.59 (VM-1 short wheelbase) |
| Rural family | $68,670, CPS outside metro areas | Married, 2 children | 2 × 11,782 (NHTS rural, 2 vehicles) | car 25.59, pickup 18.50 |
| Lower-income family | $35,800, CPS 20th percentile | Married, 2 children | 2 × 9,748 (NHTS $25k to $50k, 2 vehicles) | 23.43 |
| Retired couple | $59,680, CPS householder 65+; $38,496 Social Security, rest pension | Married, both 65+ | 1 × 8,928 (NHTS everyone 65+, 1 vehicle) | 23.43 |
| Suburban three-car family | $112,900, CPS family households | Married, 2 children | 3 × 9,993 (NHTS 3-vehicle) | 23.43 |

- All income is wages except the retired couple's. No state or local tax.
- Rural pickup: 29.5% of vehicles in rural 2-vehicle households are pickups (NHTS,
  checked), so a car and a pickup is a common pairing, not the average.
- The "Your household" calculator assumes a household from the number of cars: 1 car,
  single; 2 cars, a married couple; 3 or more, a married couple with two children, and
  says so under the result.
- "About N in 10 households earn less" interpolates linearly between Census's published
  pretax percentiles.
