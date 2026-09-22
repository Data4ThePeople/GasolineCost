# Income and Consumer Expenditure Survey notes

Gathered 2026-09-22. Raw files are in `data/raw/census/` and `data/raw/cex/`.
Every percentage below was computed from the downloaded files; see "How the
shares were computed" at the end.

## Quick summary

- **Newest CPS ASEC (income year 2025) is out.** Released September 15, 2026,
  as P60-289. Median household money income (pretax) was **$87,460**. Post-tax
  median was **$76,060**. The 2024 figures, restated in 2025 dollars, are
  $85,210 and $73,760. (Last year's report gave $83,730 and $72,330 in 2024
  dollars.)
- **The 2025 ACS 1-year is not out.** The release date is still to be set. The
  Census Bureau says it is checking the release against a new Commerce
  Department disclosure-avoidance order. ACS 2024 1-year values are used below.
- **The 2025 CEX is not out.** The newest CEX is 2024 data, released December
  19, 2025. That release was later than usual; the 2023 data came out September
  25, 2024. Calling the 2025 URLs returns 404.
- **Big caveat: starting with 2024 data, BLS stopped publishing CEX "income
  after taxes".** Footnote b in the multi-year table says: "Beginning with 2024
  publication, estimates developed by TAXSIM models will no longer be
  published." Personal taxes are also gone. So:
  - For gasoline as a share of **after-tax** income, the newest figures in the
    same survey and year are **2023**. Those tables are downloaded too.
  - For 2024, I report gasoline as a share of **pretax** income and of total
    expenditures. I also report an *estimated* after-tax share, clearly
    labeled: 2024 pretax income times that group's 2023 after-tax/pretax
    ratio. That column is an estimate I made, not a BLS figure.
- **No CEX table by number of vehicles exists.** BLS does not publish one in
  the calendar-year, cross-tab or geographic sets. Each table does give
  average vehicles per CU and the percent of CUs owning or leasing at least
  one vehicle.

## A. Census household income

### A1. CPS ASEC 2026 (income in 2025), report P60-289, "Income in the United States: 2025"

- Release date: September 15, 2026.
- Report page: https://www.census.gov/library/publications/2026/demo/p60-289.html
- PDF: https://www2.census.gov/library/publications/2026/demo/p60-289.pdf (saved as `data/raw/census/p60-289.pdf`)
- Tables: `https://www2.census.gov/programs-surveys/demo/tables/p60/289/tableN.xlsx`, N = 1 to 12 (saved as `data/raw/census/p60-289_tableN.xlsx`)
- Technical documentation: https://www2.census.gov/programs-surveys/cps/techdocs/cpsmar26.pdf
- MOE = 90% margin of error, as printed by Census.

**Money income (pretax) vs. post-tax income, 2025, current dollars.** Source:
Table 4, "Summary Measures by Selected Characteristics Using Money Income and
Post-Tax Income: 2025" (https://www2.census.gov/programs-surveys/demo/tables/p60/289/table4.xlsx)

| Group | Households (000) | Median money income | MOE | Median post-tax income | MOE | Post-tax vs money |
|---|---|---|---|---|---|---|
| All households | 137,100 | $87,460 | 1,040 | $76,060 | 712 | -13.0% |
| Family households | 88,000 | $112,900 | 1,543 | $98,020 | 1,096 | -13.2% |
| ...Married-couple | 64,720 | $132,400 | 1,841 | $112,600 | 1,154 | -14.9% |
| ...Female householder, no spouse | 15,670 | $63,530 | 1,933 | $58,600 | 1,327 | -7.8% |
| ...Male householder, no spouse | 7,610 | $86,000 | 2,509 | $76,460 | 2,870 | -11.1% |
| Nonfamily households | 49,060 | $52,200 | 690 | $45,990 | 922 | -11.9% |
| Householder under 65 | 95,170 | $101,900 | 770 | $85,280 | 985 | -16.3% |
| Householder 65 and older | 41,890 | $59,680 | 1,093 | $56,750 | 971 | -4.9% |
| Inside metro areas | 118,500 | $91,450 | 849 | $78,740 | 777 | -13.9% |
| ...Inside principal cities | 46,440 | $81,710 | 1,254 | $70,620 | 1,239 | -13.6% |
| ...Outside principal cities | 72,040 | $98,370 | 2,004 | $84,440 | 1,168 | -14.2% |
| Outside metro areas | 18,570 | $68,670 | 2,518 | $62,090 | 2,100 | -9.6% |

The table also has breakouts by race, Hispanic origin, nativity, region,
education, and 10-year age groups. The nonmetro row is the closest CPS gets to
"rural". Metro/nonmetro is not the same as the Census urban/rural definition or
the CEX urban/rural split.

**Year-over-year, in 2025 dollars.** Money income is from Table 1
(https://www2.census.gov/programs-surveys/demo/tables/p60/289/table1.xlsx).
Post-tax income is from Table 3
(https://www2.census.gov/programs-surveys/demo/tables/p60/289/table3.xlsx) and
Table 8 (https://www2.census.gov/programs-surveys/demo/tables/p60/289/table8.xlsx).
- Median money income: 2024 $85,210 (MOE 1,069), 2025 $87,460 (MOE 1,040), +2.6%.
- Median post-tax income: 2024 $73,760 (MOE 776), 2025 $76,060 (MOE 712), +3.1%.
- Post-tax, householder 65+: 2024 $54,600, 2025 $56,750.
- Post-tax, family households: 2024 $95,670, 2025 $98,020.
- Census defines post-tax income as money income minus federal and state income
  taxes and payroll taxes, plus tax credits such as the EITC. The definition is
  in the table footnotes.

**Percentiles of pretax money income, 2025.** Quintile upper limits come from
Table H-1, "Limits for Household Income Quintiles and Top 5 Percent of All
Households: 1967 to 2025"
(https://www2.census.gov/programs-surveys/cps/tables/time-series/historical-income-households/h01ar.xlsx,
saved as `data/raw/census/cps_h01ar.xlsx`), current dollars:

| Percentile (quintile upper limit) | 2025 | 2024 (2024 dollars) |
|---|---|---|
| 20th (lowest quintile upper limit) | $35,800 | $34,160 |
| 40th | $68,600 | $65,000 |
| 60th | $110,300 | $105,000 |
| 80th | $182,400 | $175,300 |
| 95th (lower limit of top 5%) | $354,000 | $335,900 |

Table 5 gives the 10th percentile ($20,010), the 50th ($87,460) and the 90th
($261,300).

**Percentiles of post-tax income, 2025.** Source: Table 10, "Selected Measures
of Household Post-Tax Income Dispersion: 2009 to 2025"
(https://www2.census.gov/programs-surveys/demo/tables/p60/289/table10.xlsx):
10th $20,140; 20th $34,560; 30th $47,840; 40th $60,930; 50th $76,060; 60th
$93,750; 70th $116,300; 80th $146,800; 90th $201,600; 95th $268,300. The same
table gives 2024 values in 2025 dollars; the 20th percentile was $33,740 and
the 40th was $59,020.

**25th percentile:** Census does not publish it in these tables. The published
cut points are the 10th, 20th, 30th and so on up to the 95th. Getting the 25th
would require the CPS ASEC microdata.

### A2. ACS 1-year 2024, via the Census API

- Release date of the 2024 ACS 1-year: September 11, 2025.
- Query: `https://api.census.gov/data/2024/acs/acs1?get=NAME,B19013_001E,B19013_001M,B08201_001E,...,B08201_006E&for=us:1` (key omitted). Saved as `data/raw/census/acs1_2024_us_B19013_B08201.json`.
- The 2025 endpoint returned 404.

| Variable | Value | MOE |
|---|---|---|
| B19013_001E Median household income (2024 inflation-adjusted dollars) | $81,604 | 128 |
| B08201_001E Households, total | 132,737,146 | 140,273 |
| B08201_002E No vehicle available | 11,310,673 (8.5%) | 72,714 |
| B08201_003E 1 vehicle | 44,094,691 (33.2%) | |
| B08201_004E 2 vehicles | 48,156,355 (36.3%) | |
| B08201_005E 3 vehicles | 19,125,439 (14.4%) | |
| B08201_006E 4 or more vehicles | 10,049,988 (7.6%) | |

So 91.5% of households have at least one vehicle available.

**ACS urban/rural median income:** not available for 2024 via the API. The
urban/rural geographic components (ucgid 0100001US and 0100043US) returned
errors. ACS stopped publishing urban/rural geographic components after the
2020 Census urban-area changes. Skipped.

### CPS vs. ACS

The ACS median ($81,604 for 2024) is lower than the CPS ASEC median ($83,730
for 2024 in 2024 dollars). The CPS ASEC is the Census Bureau's official source
for national income. It asks many more detailed income questions, and it is
the only one of the two with a post-tax measure. The ACS is a larger sample,
built for geographic detail. It has a rolling 12-month reference period, and
its universe and inflation adjustment differ from the CPS. Pick one source per
comparison and do not mix medians across the two.

## B. BLS Consumer Expenditure Survey (CEX)

- Latest release: "Consumer Expenditures--2024", USDL-25-1586, released
  December 19, 2025. https://www.bls.gov/news.release/cesan.nr0.htm
- Tables index: https://www.bls.gov/cex/tables.htm
- Headline figures, 2024: 135.76 million consumer units (CUs). Average income
  before taxes was $104,207 and average annual expenditures were $78,535.
  "Gasoline and other fuels" averaged $2,645 (3.4% of spending). Gasoline alone
  was $2,411.
- The 2023 tables were released September 2024. The 2023 values below come
  from those original tables. The 2021-2024 multi-year table revised 2023 total
  expenditures from $77,280 to $77,158. Its 2023 gasoline figures ($2,694 and
  $2,449) and 2023 income figures match the originals.

Files downloaded (`data/raw/cex/`):
- `cu-all-detail-2024.xlsx`, Table 2500, all CUs, full item detail: https://www.bls.gov/cex/tables/calendar-year/mean/cu-all-detail-2024.xlsx
- `cu-all-multi-year-2021-2024.xlsx`, all CUs, 2021-2024; it has after-tax income for 2021-2023: https://www.bls.gov/cex/tables/calendar-year/mean/cu-all-multi-year-2021-2024.xlsx
- `mis-<table>-2024.xlsx` and `mis-<table>-2023.xlsx`. These are the "mean, item share, average, standard error" tables for quintiles, deciles, housing tenure, area type (urban/rural), population size of area, age of reference person, and CU composition. The URL pattern is `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/<table>-<year>.xlsx`. The `mis-` prefix is only added to the local file name.

### CEX caveats

1. **The gasoline line changed in 2023.** Starting with 2023 data, the category
   is "Gasoline and other fuels". It replaced "Gasoline, other fuels, and
   motor oil"; see footnote g in the multi-year table. Motor oil is no longer
   in it. In 2024, for all CUs, it breaks down as: Gasoline $2,410.75; diesel
   $75.41; gasoline on out-of-town trips $148.94; EV charging $9.96. Total:
   $2,645.06, from Table 2500.
   The "Gasoline" line in the group tables **excludes gasoline bought on
   out-of-town trips**. Gasoline including trips is about $2,560 for all CUs in
   2024. For comparisons with the CPI "motor fuel" or "gasoline (all types)"
   weight, "Gasoline and other fuels" is the closer match, because it includes
   trip gasoline and diesel.
   The multi-year table shows 2022 "Gasoline" as $2,805. That value is under
   the old definition and is not comparable with 2023-2024.
2. **All CEX income and spending figures are means, not medians.** Means per
   consumer unit are pulled up by high earners. The CPS medians are per
   household. A consumer unit is close to a household but not the same: one
   household can contain more than one CU.
3. **Low incomes are underreported in the CEX.** The lowest quintile and
   decile report spending of about 2 times their income ($35,046 in spending
   vs. $16,658 in income in 2024). So gasoline as a share of income looks very
   high for those groups (7.6% of pretax income for the lowest quintile, 12.5%
   for the lowest decile). Gasoline as a share of spending is the steadier
   measure for low-income groups. Present income-based shares for the bottom
   groups with this caveat.
4. **Quintiles are based on income before taxes.** In 2024, the lower limits
   were $29,932, $57,452, $94,511 and $155,925. These are CU-based limits and
   differ from the CPS household quintile limits.
5. **Standard errors** are in the tables and are shown in parentheses below. A
   rough 95% interval is plus or minus 1.96 SE. Examples: all-CU gas and fuels
   in 2024 is $2,645 with SE $34.55; rural is $3,294 with SE $66.23.
6. **The 2024 after-tax estimate is mine, not BLS's.** The formula is 2024
   pretax income times (2023 after-tax / 2023 pretax) for the same group. It
   assumes each group's effective tax rate did not change from 2023 to 2024.
   Present it as an estimate, or use the 2023 after-tax shares.
7. In 2023, after-tax income is above pretax income for the lowest quintile and
   the lowest 3 deciles. That is because refundable credits exceed taxes for
   those groups (lowest quintile personal taxes: -$575).
8. "Urban" and "rural" follow the BLS definitions in Table 1721. Table 2400
   uses "Outside urban area", which has nearly the same values as "Rural".
9. **No CEX table by number of vehicles.** Average vehicles and the percent
   owning or leasing a vehicle come from the characteristics section of each
   table. The ACS B08201 counts above give the household distribution by
   vehicles available.

### CEX results by group

Columns: "Gas & other fuels" is the "Gasoline and other fuels" mean (SE).
"Gasoline" is the gasoline-only line (SE). Persons and Vehicles are averages
per CU. "% owning/leasing vehicle" is the share of CUs with at least one
vehicle owned or leased. Income and spending are annual dollars, means per CU.
* marks an estimate, per caveat 6.

#### Income quintiles (Table 1101)

2024 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-income-quintiles-before-taxes-2024.xlsx`  
2023 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-income-quintiles-before-taxes-2023.xlsx`

**2024** (no after-tax income published). Gas = "Gasoline and other fuels" mean (SE); Gasoline = gasoline line alone.

| Group | CUs (000) | Income before taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of pretax income | Gas&fuels % of expenditures | Gasoline % of expenditures | Est. after-tax income* | Gas&fuels % of est. after-tax* |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 135,760 | 104,207 | 78,535 | 2,645 (34.55) | 2,411 (34.35) | 2.4 | 1.9 | 89% | 2.5% | 3.4% | 3.1% | 89,942 | 2.9% |
| Lowest 20 percent | 27,139 | 16,658 | 35,046 | 1,262 (51.46) | 1,177 (43.46) | 1.6 | 1 | 68% | 7.6% | 3.6% | 3.4% | 17,272 | 7.3% |
| Second 20 percent | 27,186 | 42,925 | 50,054 | 2,031 (57.25) | 1,893 (53.19) | 2.1 | 1.6 | 88% | 4.7% | 4.1% | 3.8% | 42,788 | 4.7% |
| Third 20 percent | 26,959 | 74,474 | 66,900 | 2,643 (60.16) | 2,442 (61.04) | 2.5 | 1.9 | 93% | 3.5% | 4.0% | 3.7% | 69,809 | 3.8% |
| Fourth 20 percent | 27,205 | 121,548 | 89,972 | 3,350 (63.43) | 3,058 (62.69) | 2.9 | 2.3 | 96% | 2.8% | 3.7% | 3.4% | 108,887 | 3.1% |
| Highest 20 percent | 27,272 | 264,510 | 150,342 | 3,932 (80.87) | 3,477 (73.82) | 3.2 | 2.7 | 97% | 1.5% | 2.6% | 2.3% | 211,036 | 1.9% |

**2023** (last year with published after-tax income):

| Group | CUs (000) | Income before taxes | Income after taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of after-tax income | Gasoline % of after-tax income | Gas&fuels % of expenditures | Gasoline % of expenditures |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 134,556 | 101,805 | 87,869 | 77,280 | 2,694 (35.84) | 2,449 (31.35) | 2.5 | 1.9 | 89% | 3.1% | 2.8% | 3.5% | 3.2% |
| Lowest 20 percent | 26,719 | 15,596 | 16,171 | 33,776 | 1,324 (41.03) | 1,233 (35.37) | 1.6 | 1 | 70% | 8.2% | 7.6% | 3.9% | 3.7% |
| Second 20 percent | 26,984 | 40,751 | 40,621 | 48,923 | 2,134 (40.23) | 1,969 (35.41) | 2.1 | 1.6 | 88% | 5.3% | 4.8% | 4.4% | 4.0% |
| Third 20 percent | 27,027 | 71,057 | 66,606 | 65,487 | 2,700 (41.46) | 2,505 (46.14) | 2.5 | 1.9 | 93% | 4.1% | 3.8% | 4.1% | 3.8% |
| Fourth 20 percent | 26,902 | 116,717 | 104,559 | 87,922 | 3,369 (54.71) | 3,082 (50.57) | 2.9 | 2.3 | 96% | 3.2% | 2.9% | 3.8% | 3.5% |
| Highest 20 percent | 26,924 | 264,518 | 211,042 | 150,093 | 3,936 (101.43) | 3,447 (86.92) | 3.2 | 2.6 | 97% | 1.9% | 1.6% | 2.6% | 2.3% |

#### Income deciles (Table 1110)

2024 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-income-deciles-before-taxes-2024.xlsx`  
2023 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-income-deciles-before-taxes-2023.xlsx`

**2024** (no after-tax income published). Gas = "Gasoline and other fuels" mean (SE); Gasoline = gasoline line alone.

| Group | CUs (000) | Income before taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of pretax income | Gas&fuels % of expenditures | Gasoline % of expenditures | Est. after-tax income* | Gas&fuels % of est. after-tax* |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 135,760 | 104,207 | 78,535 | 2,645 (34.55) | 2,411 (34.35) | 2.4 | 1.9 | 89% | 2.5% | 3.4% | 3.1% | 89,942 | 2.9% |
| Lowest 10 percent | 13,665 | 9,612 | 31,660 | 1,205 (82.18) | 1,113 (71.34) | 1.6 | 0.9 | 59% | 12.5% | 3.8% | 3.5% | 10,319 | 11.7% |
| Second 10 percent | 13,474 | 23,805 | 38,473 | 1,320 (47.07) | 1,242 (40.32) | 1.6 | 1.2 | 77% | 5.5% | 3.4% | 3.2% | 24,364 | 5.4% |
| Third 10 percent | 13,612 | 36,188 | 46,340 | 1,885 (86.89) | 1,770 (83.93) | 2 | 1.5 | 87% | 5.2% | 4.1% | 3.8% | 36,744 | 5.1% |
| Fourth 10 percent | 13,574 | 49,681 | 53,778 | 2,176 (57.69) | 2,017 (52.62) | 2.2 | 1.6 | 90% | 4.4% | 4.0% | 3.8% | 48,842 | 4.5% |
| Fifth 10 percent | 13,467 | 65,170 | 62,880 | 2,495 (93.88) | 2,323 (90.87) | 2.3 | 1.8 | 92% | 3.8% | 4.0% | 3.7% | 61,597 | 4.1% |
| Sixth 10 percent | 13,492 | 83,760 | 70,913 | 2,791 (83.94) | 2,561 (79.58) | 2.6 | 1.9 | 94% | 3.3% | 3.9% | 3.6% | 78,004 | 3.6% |
| Seventh 10 percent | 13,533 | 106,439 | 81,716 | 3,092 (82.74) | 2,827 (75.88) | 2.8 | 2.1 | 96% | 2.9% | 3.8% | 3.5% | 97,058 | 3.2% |
| Eighth 10 percent | 13,672 | 136,502 | 98,158 | 3,606 (94.11) | 3,287 (87.87) | 2.9 | 2.5 | 96% | 2.6% | 3.7% | 3.3% | 120,576 | 3.0% |
| Ninth 10 percent | 13,678 | 182,587 | 121,317 | 3,897 (122.14) | 3,459 (110.44) | 3.2 | 2.6 | 98% | 2.1% | 3.2% | 2.9% | 156,418 | 2.5% |
| Highest 10 percent | 13,594 | 346,942 | 179,513 | 3,966 (99.26) | 3,495 (94.7) | 3.2 | 2.8 | 97% | 1.1% | 2.2% | 1.9% | 266,715 | 1.5% |

**2023** (last year with published after-tax income):

| Group | CUs (000) | Income before taxes | Income after taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of after-tax income | Gasoline % of after-tax income | Gas&fuels % of expenditures | Gasoline % of expenditures |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 134,556 | 101,805 | 87,869 | 77,280 | 2,694 (35.84) | 2,449 (31.35) | 2.5 | 1.9 | 89% | 3.1% | 2.8% | 3.5% | 3.2% |
| Lowest 10 percent | 13,225 | 8,438 | 9,059 | 31,900 | 1,169 (52.5) | 1,082 (40.37) | 1.6 | 0.9 | 60% | 12.9% | 11.9% | 3.7% | 3.4% |
| Second 10 percent | 13,495 | 22,610 | 23,141 | 35,602 | 1,475 (44.96) | 1,381 (40.94) | 1.6 | 1.2 | 80% | 6.4% | 6.0% | 4.1% | 3.9% |
| Third 10 percent | 13,589 | 34,351 | 34,879 | 45,739 | 1,957 (58.02) | 1,807 (52.42) | 2 | 1.5 | 86% | 5.6% | 5.2% | 4.3% | 4.0% |
| Fourth 10 percent | 13,395 | 47,244 | 46,446 | 52,148 | 2,314 (57.64) | 2,134 (48.61) | 2.2 | 1.6 | 90% | 5.0% | 4.6% | 4.4% | 4.1% |
| Fifth 10 percent | 13,525 | 62,076 | 58,673 | 60,929 | 2,601 (66.67) | 2,440 (65.35) | 2.4 | 1.8 | 93% | 4.4% | 4.2% | 4.3% | 4.0% |
| Sixth 10 percent | 13,502 | 80,054 | 74,553 | 70,050 | 2,799 (57.07) | 2,571 (60.91) | 2.6 | 2 | 94% | 3.8% | 3.4% | 4.0% | 3.7% |
| Seventh 10 percent | 13,426 | 102,530 | 93,494 | 80,213 | 3,302 (79.18) | 3,042 (73.34) | 2.8 | 2.2 | 96% | 3.5% | 3.3% | 4.1% | 3.8% |
| Eighth 10 percent | 13,476 | 130,851 | 115,584 | 95,606 | 3,435 (75.32) | 3,121 (76.14) | 3 | 2.4 | 97% | 3.0% | 2.7% | 3.6% | 3.3% |
| Ninth 10 percent | 13,433 | 175,332 | 150,203 | 119,303 | 3,779 (102.3) | 3,322 (96.18) | 3.2 | 2.6 | 96% | 2.5% | 2.2% | 3.2% | 2.8% |
| Highest 10 percent | 13,491 | 353,318 | 271,617 | 180,758 | 4,093 (142.82) | 3,573 (114.17) | 3.2 | 2.7 | 98% | 1.5% | 1.3% | 2.3% | 2.0% |

#### Housing tenure (Table 1710)

2024 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-housing-tenure-2024.xlsx`  
2023 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-housing-tenure-2023.xlsx`

**2024** (no after-tax income published). Gas = "Gasoline and other fuels" mean (SE); Gasoline = gasoline line alone.

| Group | CUs (000) | Income before taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of pretax income | Gas&fuels % of expenditures | Gasoline % of expenditures | Est. after-tax income* | Gas&fuels % of est. after-tax* |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 135,760 | 104,207 | 78,535 | 2,645 (34.55) | 2,411 (34.35) | 2.4 | 1.9 | 89% | 2.5% | 3.4% | 3.1% | 89,942 | 2.9% |
| Homeowner / Total | 88,118 | 125,105 | 90,117 | 2,999 (41.32) | 2,697 (39.72) | 2.6 | 2.3 | 95% | 2.4% | 3.3% | 3.0% | 106,623 | 2.8% |
| Homeowner / Homeowner with mortgage | 50,122 | 150,918 | 104,329 | 3,374 (56.9) | 3,034 (51.87) | 2.9 | 2.4 | 97% | 2.2% | 3.2% | 2.9% | 127,620 | 2.6% |
| Homeowner / Homeowner without mortgage | 37,995 | 91,054 | 70,906 | 2,504 (56.44) | 2,252 (53.96) | 2.2 | 2.1 | 93% | 2.8% | 3.5% | 3.2% | 78,971 | 3.2% |
| Renter | 47,642 | 65,555 | 57,108 | 1,991 (45.46) | 1,882 (44.24) | 2.2 | 1.2 | 76% | 3.0% | 3.5% | 3.3% | 59,052 | 3.4% |

**2023** (last year with published after-tax income):

| Group | CUs (000) | Income before taxes | Income after taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of after-tax income | Gasoline % of after-tax income | Gas&fuels % of expenditures | Gasoline % of expenditures |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 134,556 | 101,805 | 87,869 | 77,280 | 2,694 (35.84) | 2,449 (31.35) | 2.5 | 1.9 | 89% | 3.1% | 2.8% | 3.5% | 3.2% |
| Homeowner / Total | 87,579 | 121,500 | 103,551 | 88,055 | 3,018 (40.9) | 2,714 (36.48) | 2.6 | 2.3 | 96% | 2.9% | 2.6% | 3.4% | 3.1% |
| Homeowner / Homeowner with mortgage | 50,778 | 145,268 | 122,842 | 101,290 | 3,318 (56.3) | 2,983 (54.28) | 2.9 | 2.3 | 97% | 2.7% | 2.4% | 3.3% | 2.9% |
| Homeowner / Homeowner without mortgage | 36,801 | 88,705 | 76,934 | 69,306 | 2,605 (60.08) | 2,343 (53.45) | 2.2 | 2.1 | 94% | 3.4% | 3.0% | 3.8% | 3.4% |
| Renter | 46,977 | 65,089 | 58,632 | 57,186 | 2,090 (52.3) | 1,954 (43.68) | 2.2 | 1.2 | 76% | 3.6% | 3.3% | 3.7% | 3.4% |

#### Type of area, urban/rural (Table 1721)

2024 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-area-type-2024.xlsx`  
2023 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-area-type-2023.xlsx`

**2024** (no after-tax income published). Gas = "Gasoline and other fuels" mean (SE); Gasoline = gasoline line alone.

| Group | CUs (000) | Income before taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of pretax income | Gas&fuels % of expenditures | Gasoline % of expenditures | Est. after-tax income* | Gas&fuels % of est. after-tax* |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 135,760 | 104,207 | 78,535 | 2,645 (34.55) | 2,411 (34.35) | 2.4 | 1.9 | 89% | 2.5% | 3.4% | 3.1% | 89,942 | 2.9% |
| Urban / Total urban | 109,673 | 104,927 | 79,068 | 2,491 (40.24) | 2,293 (37.4) | 2.4 | 1.7 | 87% | 2.4% | 3.2% | 2.9% | 90,052 | 2.8% |
| Urban / Urban principal city | 47,610 | 96,391 | 73,643 | 2,185 (62.01) | 2,001 (55.69) | 2.3 | 1.5 | 81% | 2.3% | 3.0% | 2.7% | 82,329 | 2.7% |
| Urban / Other urban | 62,063 | 111,475 | 83,215 | 2,725 (56.13) | 2,518 (48.38) | 2.5 | 1.9 | 92% | 2.4% | 3.3% | 3.0% | 95,968 | 2.8% |
| Rural | 26,087 | 101,182 | 76,300 | 3,294 (66.23) | 2,905 (63.13) | 2.6 | 2.5 | 94% | 3.3% | 4.3% | 3.8% | 89,609 | 3.7% |

**2023** (last year with published after-tax income):

| Group | CUs (000) | Income before taxes | Income after taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of after-tax income | Gasoline % of after-tax income | Gas&fuels % of expenditures | Gasoline % of expenditures |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 134,556 | 101,805 | 87,869 | 77,280 | 2,694 (35.84) | 2,449 (31.35) | 2.5 | 1.9 | 89% | 3.1% | 2.8% | 3.5% | 3.2% |
| Urban / Total urban | 108,971 | 103,373 | 88,718 | 78,056 | 2,562 (37.26) | 2,362 (34.48) | 2.4 | 1.7 | 87% | 2.9% | 2.7% | 3.3% | 3.0% |
| Urban / Urban principal city | 46,483 | 94,879 | 81,038 | 71,504 | 2,224 (43.26) | 2,054 (39.69) | 2.3 | 1.5 | 81% | 2.7% | 2.5% | 3.1% | 2.9% |
| Urban / Other urban | 62,488 | 109,691 | 94,432 | 82,886 | 2,814 (49.79) | 2,591 (46) | 2.5 | 1.9 | 92% | 3.0% | 2.7% | 3.4% | 3.1% |
| Rural | 25,585 | 95,130 | 84,249 | 73,967 | 3,255 (101.52) | 2,821 (82.56) | 2.6 | 2.5 | 95% | 3.9% | 3.3% | 4.4% | 3.8% |

#### Population size of area (Table 2400)

2024 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-population-area-size-2024.xlsx`  
2023 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-population-area-size-2023.xlsx`

**2024** (no after-tax income published). Gas = "Gasoline and other fuels" mean (SE); Gasoline = gasoline line alone.

| Group | CUs (000) | Income before taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of pretax income | Gas&fuels % of expenditures | Gasoline % of expenditures | Est. after-tax income* | Gas&fuels % of est. after-tax* |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 135,760 | 104,207 | 78,535 | 2,645 (34.55) | 2,411 (34.35) | 2.4 | 1.9 | 89% | 2.5% | 3.4% | 3.1% | 89,942 | 2.9% |
| Outside urban area | 26,082 | 101,101 | 76,298 | 3,294 (66.28) | 2,905 (63.17) | 2.6 | 2.5 | 94% | 3.3% | 4.3% | 3.8% | 89,537 | 3.7% |
| Urban consumer units / All urban consumer units | 109,678 | 104,946 | 79,068 | 2,491 (40.25) | 2,293 (37.41) | 2.4 | 1.7 | 87% | 2.4% | 3.2% | 2.9% | 90,068 | 2.8% |
| Urban consumer units / Less than 100,000 | 15,818 | 80,124 | 65,892 | 2,476 (86.74) | 2,172 (81.01) | 2.4 | 2 | 92% | 3.1% | 3.8% | 3.3% | 72,050 | 3.4% |
| Urban consumer units / 100,000 to 249,999 | 7,485 | 80,225 | 68,939 | 2,516 (159.31) | 2,258 (138.07) | 2.5 | 1.8 | 88% | 3.1% | 3.6% | 3.3% | 71,954 | 3.5% |
| Urban consumer units / 250,000 to 999,999 | 30,740 | 95,058 | 74,093 | 2,578 (80.65) | 2,378 (68.91) | 2.3 | 1.7 | 86% | 2.7% | 3.5% | 3.2% | 82,513 | 3.1% |
| Urban consumer units / 1,000,000 to 2,499,999 | 17,879 | 107,609 | 78,300 | 2,349 (120.04) | 2,180 (115.53) | 2.4 | 1.7 | 90% | 2.2% | 3.0% | 2.8% | 93,490 | 2.5% |
| Urban consumer units / 2,500,000 to 4,999,999 | 16,325 | 135,024 | 97,246 | 2,629 (78.02) | 2,425 (77.37) | 2.4 | 1.8 | 91% | 1.9% | 2.7% | 2.5% | 112,364 | 2.3% |
| Urban consumer units / 5,000,000 and more | 21,431 | 120,951 | 86,136 | 2,380 (66.68) | 2,268 (66.62) | 2.6 | 1.5 | 81% | 2.0% | 2.8% | 2.6% | 100,895 | 2.4% |

**2023** (last year with published after-tax income):

| Group | CUs (000) | Income before taxes | Income after taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of after-tax income | Gasoline % of after-tax income | Gas&fuels % of expenditures | Gasoline % of expenditures |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 134,556 | 101,805 | 87,869 | 77,280 | 2,694 (35.84) | 2,449 (31.35) | 2.5 | 1.9 | 89% | 3.1% | 2.8% | 3.5% | 3.2% |
| Outside urban area | 25,585 | 95,130 | 84,249 | 73,967 | 3,255 (101.52) | 2,821 (82.56) | 2.6 | 2.5 | 95% | 3.9% | 3.3% | 4.4% | 3.8% |
| Urban consumer units / All urban consumer units | 108,971 | 103,373 | 88,718 | 78,056 | 2,562 (37.26) | 2,362 (34.48) | 2.4 | 1.7 | 87% | 2.9% | 2.7% | 3.3% | 3.0% |
| Urban consumer units / Less than 100,000 | 15,209 | 77,766 | 69,930 | 64,014 | 2,724 (96.29) | 2,433 (88.51) | 2.3 | 2 | 92% | 3.9% | 3.5% | 4.3% | 3.8% |
| Urban consumer units / 100,000 to 249,999 | 7,818 | 76,682 | 68,776 | 65,252 | 2,549 (175.74) | 2,310 (157.4) | 2.2 | 1.7 | 87% | 3.7% | 3.4% | 3.9% | 3.5% |
| Urban consumer units / 250,000 to 999,999 | 29,956 | 96,288 | 83,581 | 73,942 | 2,610 (73.02) | 2,416 (65.46) | 2.4 | 1.8 | 89% | 3.1% | 2.9% | 3.5% | 3.3% |
| Urban consumer units / 1,000,000 to 2,499,999 | 17,653 | 103,413 | 89,845 | 78,372 | 2,495 (110.64) | 2,308 (103.74) | 2.4 | 1.8 | 90% | 2.8% | 2.6% | 3.2% | 2.9% |
| Urban consumer units / 2,500,000 to 4,999,999 | 16,932 | 129,016 | 107,364 | 96,007 | 2,595 (55.03) | 2,373 (50.42) | 2.4 | 1.7 | 88% | 2.4% | 2.2% | 2.7% | 2.5% |
| Urban consumer units / 5,000,000 and more | 21,403 | 120,915 | 100,865 | 83,902 | 2,416 (78.7) | 2,289 (80.35) | 2.6 | 1.5 | 81% | 2.4% | 2.3% | 2.9% | 2.7% |

#### Age of reference person (Table 1300)

2024 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/reference-person-age-ranges-2024.xlsx`  
2023 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/reference-person-age-ranges-2023.xlsx`

**2024** (no after-tax income published). Gas = "Gasoline and other fuels" mean (SE); Gasoline = gasoline line alone.

| Group | CUs (000) | Income before taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of pretax income | Gas&fuels % of expenditures | Gasoline % of expenditures | Est. after-tax income* | Gas&fuels % of est. after-tax* |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 135,760 | 104,207 | 78,535 | 2,645 (34.55) | 2,411 (34.35) | 2.4 | 1.9 | 89% | 2.5% | 3.4% | 3.1% | 89,942 | 2.9% |
| Under 25 years | 6,700 | 48,514 | 47,283 | 1,841 (120.8) | 1,706 (115.36) | 1.9 | 1.2 | 73% | 3.8% | 3.9% | 3.6% | 44,339 | 4.2% |
| 25-34 years | 20,340 | 102,494 | 74,475 | 2,655 (81.1) | 2,444 (80.22) | 2.6 | 1.6 | 87% | 2.6% | 3.6% | 3.3% | 90,202 | 2.9% |
| 35-44 years | 24,275 | 128,285 | 91,229 | 3,099 (69.48) | 2,829 (65.74) | 3.3 | 1.9 | 91% | 2.4% | 3.4% | 3.1% | 110,644 | 2.8% |
| 45-54 years | 22,165 | 141,121 | 100,327 | 3,702 (98.01) | 3,379 (84.13) | 3 | 2.3 | 92% | 2.6% | 3.7% | 3.4% | 118,612 | 3.1% |
| 55-64 years | 23,911 | 121,571 | 84,946 | 2,768 (64.18) | 2,522 (61.87) | 2.2 | 2.1 | 91% | 2.3% | 3.3% | 3.0% | 100,301 | 2.8% |
| 65 years and older | 38,369 | 67,462 | 61,432 | 1,806 (38.97) | 1,623 (31.82) | 1.8 | 1.8 | 87% | 2.7% | 2.9% | 2.6% | 61,844 | 2.9% |
| 65-74 years | 22,577 | 75,460 | 65,354 | 2,144 (48.68) | 1,908 (37.84) | 1.9 | 2 | 90% | 2.8% | 3.3% | 2.9% | 68,426 | 3.1% |
| 75 years and older | 15,792 | 56,028 | 55,834 | 1,322 (54.23) | 1,216 (45.49) | 1.6 | 1.5 | 82% | 2.4% | 2.4% | 2.2% | 52,403 | 2.5% |

**2023** (last year with published after-tax income):

| Group | CUs (000) | Income before taxes | Income after taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of after-tax income | Gasoline % of after-tax income | Gas&fuels % of expenditures | Gasoline % of expenditures |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 134,556 | 101,805 | 87,869 | 77,280 | 2,694 (35.84) | 2,449 (31.35) | 2.5 | 1.9 | 89% | 3.1% | 2.8% | 3.5% | 3.2% |
| Under 25 years | 6,041 | 56,107 | 51,278 | 49,560 | 2,164 (132.73) | 2,028 (126.65) | 2 | 1.2 | 72% | 4.2% | 4.0% | 4.4% | 4.1% |
| 25-34 years | 21,082 | 96,514 | 84,939 | 71,867 | 2,593 (69.75) | 2,394 (62.9) | 2.6 | 1.5 | 86% | 3.1% | 2.8% | 3.6% | 3.3% |
| 35-44 years | 23,612 | 126,466 | 109,075 | 90,939 | 3,235 (70.94) | 2,938 (66.89) | 3.4 | 1.9 | 92% | 3.0% | 2.7% | 3.6% | 3.2% |
| 45-54 years | 22,721 | 137,601 | 115,653 | 97,319 | 3,561 (107.86) | 3,233 (95.39) | 2.9 | 2.2 | 92% | 3.1% | 2.8% | 3.7% | 3.3% |
| 55-64 years | 23,927 | 117,905 | 97,276 | 83,379 | 2,909 (57.56) | 2,663 (57.56) | 2.2 | 2.1 | 91% | 3.0% | 2.7% | 3.5% | 3.2% |
| 65 years and older | 37,173 | 64,326 | 58,969 | 60,087 | 1,826 (33.47) | 1,621 (25.09) | 1.7 | 1.8 | 88% | 3.1% | 2.7% | 3.0% | 2.7% |
| 65-74 years | 21,584 | 72,190 | 65,461 | 65,149 | 2,107 (35.73) | 1,885 (29.3) | 1.9 | 2 | 91% | 3.2% | 2.9% | 3.2% | 2.9% |
| 75 years and older | 15,589 | 53,438 | 49,981 | 53,031 | 1,437 (63.38) | 1,255 (40.17) | 1.6 | 1.5 | 84% | 2.9% | 2.5% | 2.7% | 2.4% |

#### Composition of consumer unit (Table 1502)

2024 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-composition-2024.xlsx`  
2023 file: `https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-composition-2023.xlsx`

**2024** (no after-tax income published). Gas = "Gasoline and other fuels" mean (SE); Gasoline = gasoline line alone.

| Group | CUs (000) | Income before taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of pretax income | Gas&fuels % of expenditures | Gasoline % of expenditures | Est. after-tax income* | Gas&fuels % of est. after-tax* |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 135,760 | 104,207 | 78,535 | 2,645 (34.55) | 2,411 (34.35) | 2.4 | 1.9 | 89% | 2.5% | 3.4% | 3.1% | 89,942 | 2.9% |
| Married couple consumer units / Total | 65,173 | 144,988 | 101,455 | 3,484 (51.31) | 3,143 (48.67) | 3.2 | 2.5 | 96% | 2.4% | 3.4% | 3.1% | 123,595 | 2.8% |
| Married couple consumer units / Married couple only | 29,434 | 120,105 | 88,687 | 2,778 (56.45) | 2,460 (49.62) | 2 | 2.3 | 95% | 2.3% | 3.1% | 2.8% | 100,467 | 2.8% |
| Married couple consumer units / Married couple with children / Total | 30,318 | 168,471 | 113,585 | 4,041 (92.77) | 3,665 (83.51) | 4 | 2.6 | 97% | 2.4% | 3.6% | 3.2% | 144,177 | 2.8% |
| Married couple consumer units / Oldest child under 6 | 4,661 | 161,271 | 105,709 | 2,937 (124.31) | 2,620 (107.36) | 3.5 | 1.9 | 93% | 1.8% | 2.8% | 2.5% | 137,987 | 2.1% |
| Married couple consumer units / Oldest child 6 to 17 | 14,910 | 175,737 | 117,355 | 4,068 (94.99) | 3,624 (91.94) | 4.2 | 2.5 | 97% | 2.3% | 3.5% | 3.1% | 148,190 | 2.7% |
| Married couple consumer units / Oldest child 18 or older | 10,748 | 161,512 | 111,908 | 4,481 (176.12) | 4,175 (159.4) | 4 | 3.1 | 98% | 2.8% | 4.0% | 3.7% | 141,498 | 3.2% |
| Married couple consumer units / Other married couple consumer units | 5,420 | 148,763 | 103,121 | 4,209 (169.83) | 3,932 (158.31) | 4.8 | 2.6 | 94% | 2.8% | 4.1% | 3.8% | 134,649 | 3.1% |
| One parent, at least one child under 18 | 6,161 | 61,118 | 61,857 | 2,187 (109.25) | 2,038 (102.94) | 3 | 1.2 | 82% | 3.6% | 3.5% | 3.3% | 60,035 | 3.6% |
| Single person and other consumer units | 64,426 | 67,075 | 56,587 | 1,840 (38.25) | 1,706 (38.43) | 1.7 | 1.4 | 82% | 2.7% | 3.3% | 3.0% | 58,770 | 3.1% |

**2023** (last year with published after-tax income):

| Group | CUs (000) | Income before taxes | Income after taxes | Avg annual expenditures | Gas & other fuels (SE) | Gasoline (SE) | Persons | Vehicles | % owning/leasing vehicle | Gas&fuels % of after-tax income | Gasoline % of after-tax income | Gas&fuels % of expenditures | Gasoline % of expenditures |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All consumer units | 134,556 | 101,805 | 87,869 | 77,280 | 2,694 (35.84) | 2,449 (31.35) | 2.5 | 1.9 | 89% | 3.1% | 2.8% | 3.5% | 3.2% |
| Married couple consumer units / Total | 64,830 | 141,798 | 120,876 | 100,161 | 3,523 (63.68) | 3,157 (53.18) | 3.2 | 2.4 | 96% | 2.9% | 2.6% | 3.5% | 3.2% |
| Married couple consumer units / Married couple only | 29,676 | 124,468 | 104,117 | 88,684 | 2,860 (59.44) | 2,521 (49.73) | 2 | 2.4 | 97% | 2.7% | 2.4% | 3.2% | 2.8% |
| Married couple consumer units / Married couple with children / Total | 29,501 | 158,539 | 135,677 | 111,112 | 4,027 (97.98) | 3,622 (85.78) | 4 | 2.5 | 96% | 3.0% | 2.7% | 3.6% | 3.3% |
| Married couple consumer units / Oldest child under 6 | 5,384 | 147,584 | 126,276 | 101,399 | 3,173 (130.45) | 2,858 (95.58) | 3.5 | 2 | 94% | 2.5% | 2.3% | 3.1% | 2.8% |
| Married couple consumer units / Oldest child 6 to 17 | 14,020 | 170,772 | 144,003 | 117,808 | 4,094 (109.26) | 3,629 (92.6) | 4.2 | 2.4 | 97% | 2.8% | 2.5% | 3.5% | 3.1% |
| Married couple consumer units / Oldest child 18 or older | 10,097 | 147,394 | 129,129 | 106,799 | 4,389 (172.41) | 4,020 (169.73) | 4 | 2.9 | 97% | 3.4% | 3.1% | 4.1% | 3.8% |
| Married couple consumer units / Other married couple consumer units | 5,652 | 145,410 | 131,614 | 102,493 | 4,376 (276.39) | 4,065 (262.3) | 4.9 | 2.7 | 96% | 3.3% | 3.1% | 4.3% | 4.0% |
| One parent, at least one child under 18 | 6,872 | 53,408 | 52,462 | 58,343 | 2,359 (82.28) | 2,232 (76.61) | 3.1 | 1.3 | 85% | 4.5% | 4.3% | 4.0% | 3.8% |
| Single person and other consumer units | 62,853 | 65,847 | 57,694 | 55,689 | 1,876 (28.73) | 1,743 (27.4) | 1.7 | 1.4 | 82% | 3.3% | 3.0% | 3.4% | 3.1% |
## How the shares were computed

- Gas&fuels % of income = "Gasoline and other fuels" mean / income mean, for
  the same group and year.
- Gas&fuels % of expenditures = the same mean / "Average annual expenditures"
  mean. It matches BLS's own "Share" row after rounding; for example, BLS
  gives 3.4 for all CUs in 2024.
- These are ratios of means, not the average of each CU's own share.
- Extraction scripts were run from the session scratchpad, not the project.
  Every value can be checked against the raw xlsx files listed above.
