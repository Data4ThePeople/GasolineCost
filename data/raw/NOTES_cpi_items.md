# How the CPI actually measures things, item by item

Background brief. Compiled 2026-09-23.

Purpose: know which CPI item indexes are directly priced, which are modeled, and
which ones changed method recently enough that a long time series is not one
consistent thing. Written for the gasoline-share-of-income post, so the motor
fuel section is the most detailed.

## How to read this file

- Every claim has a URL. Claims I could not confirm on a BLS page are marked
  **[UNCONFIRMED]** with what I could and could not verify.
- "Relative importance" = the item's weight as a percent of the CPI-U, December
  2025, from `data/raw/cpi_relative_importance_2025.xlsx` (Table 1, 2024
  weights). Same file the project already uses.
- Tool note: `curl` to bls.gov returns 403. Fetching through a browser-style
  fetcher works fine. BLS `.xlsx` data files could not be opened by any tool
  available in this session; where a number lives only in one of those files it
  is flagged.

---

## Which items changed most drastically, ranked

If a chart crosses one of these dates, the series on either side is not the same
measurement. Ordered by how much the method changed, not by weight.

| Item | Date | What happened | Weight (CPI-U) |
|---|---|---|---|
| **Wireless telephone service** | **July 2025** | All BLS collection ended. Index is now a monthly hedonic regression's *predicted* prices on a vendor's scrape of plan listings. Also changed in 2017 (hedonics at replacement). | 1.34% |
| **Gasoline** | **June 2021** | 4,000 BLS quotes/month → 6.1 million crowd-sourced observations/day. | 2.90% |
| **New vehicles** | **April 2022** | BLS-collected sticker-area prices → 250,000 real dealer transactions/month. | 3.84% |
| **Health insurance** | **Oct 2023 / Apr 2024** | Annual unsmoothed → semiannual, 2-year moving average. Removed the sawtooth. | 0.89% |
| **Physicians' + outpatient hospital** | **Oct 2024** | Private-insurance portion → purchased medical claims data. | ~2.5% combined |
| **Leased cars and trucks** | **April 2025** | Survey → 70,000 vendor lease transactions/month. | small |
| **Shelter (OER)** | **Jan 2023** | Reweighted by neighborhood structure type, lifting detached houses. | 26.2% |
| **Used cars** | **Jan 2018**, **Jan 2024** | 3-month moving average → single-month change (2018); mileage adjustment by age (2024). | 2.76% |
| **All items — weights** | **Jan 2023** | Biennial 2-year CE data → annual single-year. | 100% |
| **All items — outlet frame** | **Oct 2019** | TPOPS retired; outlet sample now from the Consumer Expenditure Survey. | 100% |
| **Smartphones** | **Jan/Apr 2018** | Hedonic adjustment + directed substitution twice a year. | small |
| **Apparel, household goods** | **March 2019** | A department store's corporate price feed entered production. | part of 2.37% |
| **Hospital services** | **Jan 1997** | Input pricing → treatment-episode pricing. "Hospital room," in the CPI since 1935, discontinued. | 2.17% |
| **Owner housing** | **Jan 1983** | House prices + mortgage interest → rental equivalence. | 26.2% |

**And two non-methodological breaks that matter just as much:**
- **April and June 2025:** budget-driven collection suspensions (Lincoln, Provo,
  Buffalo entirely; about 15 percent of the sample in 72 other areas).
- **October 2025:** no CPI at all. First gap since January 1921.

## 0. The three big structural facts

**Weights are now updated every year, not every two years.** Starting with
January 2023 data, CPI weights come from a single year of Consumer Expenditure
Survey data (2021 for the 2023 weights) and are refreshed annually. Before that,
weights came from two years of CE data and were updated every two years.
Announced 2022-05-24, effective January 2023 data.
https://www.bls.gov/cpi/notices/2022/methodology-changes-2022.htm

**The CPI is built from 7,776 basic indexes** — 32 index areas by 243 item
strata. Roughly 94,000 to 100,000 prices per month in the Commodities and
Services survey, about two-thirds collected by in-person store visits, the rest
by phone, website and app (about 8 percent from e-commerce). Plus about 8,000
rent quotes a month in the Housing survey.
https://www.bls.gov/opub/hom/cpi/design.htm
https://www.bls.gov/opub/hom/cpi/data.htm

**Not everything is priced every month.** Fuels and a few other items are priced
monthly in all 75 collection areas. Most other commodities and services are
priced monthly only in Chicago, Los Angeles and New York, and every *other*
month everywhere else. So for most items outside the three biggest cities, the
monthly index movement is built from bimonthly collection.
https://www.bls.gov/opub/hom/cpi/design.htm

### What the CPI is trying to be, and how it handles taxes

The CPI approximates a **conditional cost-of-living index**: the expenditure
needed to reach a base-period standard of living at current prices, holding
constant everything outside market transactions. In practice it is a measure of
price change for a fixed-quality basket.

The price concept is the consumer's **out-of-pocket price, including sales and
excise taxes**. So:

- **Sales and excise taxes are in.** A state gas tax increase raises the CPI
  gasoline index. This is the correct treatment for a share-of-income story.
- **Income and other direct taxes are out.**
- **Tariffs are not a separate item**, but reach the index indirectly through the
  prices producers and retailers charge.
- **Investment is out**: stocks, bonds, real estate, houses as assets, business
  expenses. This is the formal reason houses are handled by rental equivalence.
- **Employer-paid benefits are out**, counted as income rather than consumption.
  This is why the health insurance index covers only the consumer's own share.
- Also out: gambling losses, gifts, finance charges, illegal goods.

https://www.bls.gov/opub/hom/cpi/concepts.htm

### Alternative (non-BLS-collected) data sources now in production

From the Handbook's data sources page, with the dates BLS gives:

| Item | Source | In production since |
|---|---|---|
| Airline fares | U.S. DOT ticket database (for sampling, not pricing) | long-standing |
| Apparel and household goods | Corporate price data from a participating firm | date not given |
| Postage | USPS public price lists | long-standing |
| Prescription drugs | A large firm's bulk price data | date not given |
| Used cars and trucks | J.D. Power Information Network | long-standing |
| Gasoline | Crowd-sourced secondary source dataset | June 2021 release |
| New vehicles | J.D. Power transaction data | April 2022 data (May 2022 release) |
| Medical claims (physicians', hospital) | Secondary source claims data | October 2024 data (Nov 2024 release) |
| Leased cars and trucks | Vendor transaction data | announced 2025-05-13 |
| Wireless telephone services | Secondary source + alternative index method | announced 2025-08-12 |

https://www.bls.gov/opub/hom/cpi/data.htm
https://www.bls.gov/cpi/notices/2025/methodology-changes-2025.htm

The pattern to notice: since 2021, BLS has been swapping BLS field collection
for vendor and transaction data one item at a time, and the pace picked up in
2024 and 2025. Six of the ten rows above landed in the last five years.

---

## 1. Shelter — 35.6 percent of the CPI-U

The single biggest thing in the index, and the one built the most indirectly.

**Relative importance (Dec 2025, CPI-U):** Shelter 35.625. Owners' equivalent
rent of residences 26.204. Rent of primary residence 7.840.

### What is actually collected

The CPI Housing Survey collects rent from a sample of rental units. About 8,000
rent quotes a month. Each sampled unit is visited or phoned, and BLS asks the
occupant what they pay.
https://www.bls.gov/opub/hom/cpi/data.htm

**Nothing is collected from homeowners about their housing costs.** Not mortgage
payments, not home prices, not property taxes.

### Rental equivalence, adopted January 1983

Before 1983 the CPI treated an owner-occupied house as a good you buy, and the
homeownership component included house prices and mortgage interest costs. That
made the index move with mortgage rates, which meant Fed rate hikes mechanically
raised measured inflation.

BLS replaced it with **rental equivalence**: the cost of owner-occupied housing
is the implicit rent the owner would pay to rent the same home, unfurnished and
without utilities. Adopted **January 1983 for the CPI-U** and **January 1985 for
the CPI-W**.
https://www.bls.gov/opub/hom/cpi/history.htm

OER is not collected from owners. The *weight* comes from the Consumer
Expenditure Survey, which asks homeowners to estimate what their home would rent
for. The *price movement* comes from the rent sample — from renters.
https://www.bls.gov/cpi/factsheets/owners-equivalent-rent-and-rent.htm

So about 26 percent of the CPI is a rent index applied to homeowners.

### The six-panel, six-month rotation, and why shelter lags

Sampled neighborhoods (segments) are split into **six panels**. One panel is
priced each month, so every unit is priced **twice a year**, six months apart.
Panel 1 in January and July, panel 2 in February and August, and so on.
https://www.bls.gov/opub/hom/cpi/design.htm
https://www.bls.gov/cpi/factsheets/owners-equivalent-rent-and-rent.htm

The monthly rent index change is then set to roughly **one-sixth of the
six-month change** observed in that month's panel, on the assumption the rent
rose gradually across the six months.
https://www.bls.gov/opub/hom/cpi/design.htm

Separately, BLS replaces about one-sixth of the rental housing sample each year
using the latest Census data.

**Three separate sources of lag, stacking:**

1. **Six-month observation interval.** A rent change is not seen until the unit
   is next visited, on average about three months after it happens, and the
   observed jump is then smoothed across six months.
2. **Lease structure.** The CPI rent index covers *all* rents — new leases,
   renewals, and rents in the middle of a lease term. Most tenants in any given
   month are mid-lease and paying a rent set months or years ago. Market rents
   move first, and only reach the index as leases turn over.
3. **Smoothing.** The one-sixth rule spreads any observed change forward in
   time by construction.

### The New Tenant Rent research series (R-CPI-NTR)

BLS publishes a research series that isolates the leading edge. The **New Tenant
Rent Index (R-CPI-NTR)** uses only the *first* rent observation after a new
tenant moves into a sampled unit — what a mover would face today. A companion
**All Tenant Regressed Rent Index (R-CPI-ATR)** covers new and continuing
tenants using the same regression method.

- Both use a regression "repeat rent" method on pairs of rents for the same
  unit.
- **Quarterly**, not monthly. Series begins **2005**.
- Released about **three months after quarter end** (Q1 in April).
- **Perpetually revised** — the whole series is re-estimated every period as
  more paired observations accumulate. Official CPI rent is never revised.
- Outliers: NTR/ATR drop the top and bottom 1 percent; official CPI caps at
  +2000 / −95 percent.

https://www.bls.gov/pir/new-tenant-rent.htm
https://www.bls.gov/cpi/research-series/r-cpi-ntr.htm

**Methodology update April 2025:** the basic-index-area indexes are now
aggregated with a different set of expenditure-based weights.
https://www.bls.gov/pir/ntr/methodologyupdate2025.htm

**How much does it lead?** Fed and BLS researchers put it at **about four
quarters** (roughly a year) for new-tenant rent versus CPI rent, and about **one
quarter** for all-tenant regressed rent versus CPI rent. [UNCONFIRMED as a BLS
number — the four-quarter figure comes from Fed research (Dallas Fed 2023,
Richmond Fed 2024, Cleveland Fed WP 22-38) and secondary summaries, not from a
BLS methodology page.]
https://www.dallasfed.org/research/economics/2023/0620
https://www.richmondfed.org/research/national_economy/macro_minute/2024/new_renters_and_rent_cpi_20240206
https://www.clevelandfed.org/publications/working-paper/2022/wp-2238-disentangling-rent-index-differences

### BLS's own answer on whether rental equivalence lowered inflation

Worth quoting in the post, because the "they switched to rental equivalence to
hide inflation" claim is common and BLS answers it directly. From the
misconceptions factsheet: rental equivalence, when introduced in 1983,
**increased** measured shelter inflation, and over **1983 to 2007** the rental
equivalence measure rose **140 percent** against **79 percent** for house prices
over the same period.
https://www.bls.gov/cpi/factsheets/common-misconceptions-about-cpi.htm

That is BLS defending its own method, so treat it as a position, not a neutral
audit. But the direction is the opposite of the usual accusation, and the post
should say so if it raises the question at all.

### Recent shelter method changes

- **January 2023: OER unit weighting changed.** BLS now uses neighborhood-level
  Census information on housing structure type to weight the OER sample, giving
  more weight to detached houses that were underrepresented in the rent sample.
  Announced 2022-09-02.
  https://www.bls.gov/cpi/notices/2022/methodology-changes-2022.htm
  This matters: detached homes and apartments were moving at different rates in
  2022-2023, and OER is 26 percent of the index.

- **October 2025: the housing panel was not collected at all.** See section 11.

### What is imputed in shelter

Vacant units are imputed from the average rent change of recently occupied units
in the same area. Non-responding units are imputed from the average rent change
within the same nominal rent class (low, medium, high) in the same location.
https://www.bls.gov/cpi/tables/imputation.htm

---

## 2. Motor fuel and gasoline — 2.98 percent of the CPI-U

**This is the project's own subject, so this section is the most detailed.**

**Relative importance (Dec 2025, CPI-U):** Motor fuel 2.981. Gasoline (all
types) 2.895. Other motor fuels 0.086. For the CPI-W the same figures are 4.078
and 3.971 — gasoline is a noticeably bigger share of the wage-earner basket.
Total energy is 6.383 (CPI-U) and 8.052 (CPI-W).

### The June 2021 break: gasoline stopped being BLS-collected

This is the most important fact for the post. **The CPI gasoline index is no
longer built from BLS field collection.** Since the release of **June 2021
indexes**, it is built from a purchased secondary-source dataset.

https://www.bls.gov/cpi/factsheets/motor-fuel.htm
https://www.bls.gov/cpi/factsheets/acm-gasoline.htm
https://www.bls.gov/cpi/notices/2021/methodology-changes-2021.htm

The scale of the change, in BLS's own numbers:

| | Old (BLS survey) | New (secondary source) |
|---|---|---|
| Observations | about 4,000 price quotes/month | **6.1 million observations/month** |
| Outlets | about 1,400 | **91,272 stations/day** |
| Frequency | monthly visit | **daily** |

https://www.bls.gov/cpi/factsheets/acm-gasoline.htm

### What the price actually is

- The dataset holds "the daily average price per gallon observed by the vendor's
  users" at each outlet, with the outlet's ZIP code and state.
- **Prices include sales and excise taxes.** (Direct quote from the BLS
  factsheet: "Prices include sales and excise taxes.") So the CPI gasoline index
  is the pump price a consumer pays, tax-inclusive. A gas-tax change shows up in
  the index as a price change, exactly as it does in EIA's weekly series.
- Prices are **self-reported by users** of the vendor's app, not a probability
  sample of outlets and not a census. BLS says so plainly: these are
  "observations self-reported by users of the secondary source."
- For gasoline, **every** observation inside CPI geography is eligible and used —
  there is no outlet sample any more.
- **Separate index per fuel type** (grade). BLS publishes special relative
  series and average prices for each type of gasoline monthly.

https://www.bls.gov/cpi/factsheets/motor-fuel.htm
https://www.bls.gov/cpi/factsheets/acm-gasoline.htm

**[UNCONFIRMED — vendor identity.]** BLS does not name the vendor anywhere I
could find. The underlying BLS research paper, "A Nontraditional Data Approach
to the CPI Gasoline Index" (Bieler, Popko, Niedergall and Sung, December 2019),
describes the source as a crowd-sourced website and mobile application whose
free public database is web-scraped with permission. Outside commentary
identifies this as GasBuddy. I could not confirm the name on any BLS page and
the post should not assert it.
https://www.aeaweb.org/conference/2020/preliminary/paper/n8b4hBsT

### How the index is computed

- Daily automatic extraction and preprocessing, with outlier removal.
- Aggregation is a **weighted geometric mean (Jevons)** of counties within an
  index area.
- **County-level weights**: county-to-index-area population proportions from
  Census, combined with Consumer Expenditure Survey gasoline expenditure weights
  for each index area. This is an unusual amount of sub-area weighting detail
  for a CPI item and it exists because the data are geographically dense.
- Missing prices use **cell-relative imputation**.

https://www.bls.gov/cpi/factsheets/acm-gasoline.htm

Note: the ACM factsheet says "biennial weights are obtained from the Consumer
Expenditure Survey," which is stale wording — CPI weights went annual with
January 2023 data. Treat the weights as annual now.

### Other motor fuels (diesel, alternative fuels) — still BLS-collected

Only 0.086 percent of the CPI-U. Still priced the old way: outlets automatically
selected at every sampled motor fuel retailer in the current survey, collected
**daily** as a per-gallon price, and **including excise and sales taxes**.
https://www.bls.gov/cpi/factsheets/motor-fuel.htm

### Why this matters for the post

1. **The gasoline series has a methodology break in mid-2021.** Any chart of CPI
   gasoline spanning 2021 crosses from a 4,000-quote survey to a 6.1-million-
   observation crowd-sourced feed. BLS did not publish a quantified effect on
   measured inflation, and I found none. Flag it rather than assert it.
2. **Gasoline is one of the few items priced monthly in all 75 areas** and now
   daily. It is close to the least-imputed, most-directly-measured thing in the
   CPI — the opposite of shelter and health insurance. That is a genuinely
   strong point to make: the gasoline number is about as real as CPI numbers get.
3. **Tax-inclusive.** No adjustment needed to compare CPI gasoline to pump
   prices or to EIA.
4. **Crowd-sourced self-reports** are the one weakness. The sample skews toward
   people who use a price-comparison app, which plausibly skews toward
   lower-priced stations. BLS uses index *relatives* (ratios), so a constant
   level bias cancels; a bias that varies over time would not.

---

## 3. Health insurance — 0.89 percent of the CPI-U

The most indirect index in the CPI, and the one whose published movements say
the least about what consumers pay.

### The indirect "retained earnings" method

BLS does **not** price health insurance premiums for the health insurance index.
The reasoning: most of a premium is a pass-through payment for medical care,
which the CPI already prices directly under hospital services, physicians'
services, drugs and so on. Counting premiums too would double-count.

So the health insurance index prices only the *insurer's own service*: the part
of premiums not paid out as benefits. **Retained earnings = premiums minus
benefits paid.** BLS holds retained earnings per policy constant in real terms
and lets the index move with it.

https://www.bls.gov/cpi/additional-resources/improvements-cpi-health-insurance-index.htm
https://www.bls.gov/cpi/factsheets/medical-care.htm

**Data source:** the National Association of Insurance Commissioners (NAIC)
annual statutory financial reports, plus California Department of Managed Health
Care data. Financial statements, not prices.

Two source changes in five years:
- **September 2018 data (announced 2018-11-23):** the retained earnings ratio for
  commercial insurance moved from **A.M. Best** to **NAIC plus California DMHC**.
  https://www.bls.gov/cpi/notices/2018/methodology-changes-2018.htm
- **April 2021:** BLS stopped using data from a national nonprofit carrier, so the
  calculation now rests on **NAIC and California DMHC only**.
  https://www.bls.gov/cpi/notices/2021/methodology-changes-2021.htm

### Why it was so volatile, and the October 2023 fix

Under the old method, retained earnings were updated **once a year** from annual
data, **with no smoothing**. Each October the index took a single step reflecting
a full year of insurer financials, then ran flat at that rate for twelve months.
That produced the pattern readers noticed: the health insurance CPI fell around
4 percent *per month* for most of a year starting October 2022, then flipped to
rising about 1 percent per month from October 2023. Those are not monthly price
events; they are one annual number spread over twelve months.

**Announced 2023-08-22, first applied with October 2023 data**, following a
recommendation from the National Academies' Committee on National Statistics
(CNSTAT):

1. **Smoothing.** A **2-year simple moving average** is applied to retained
   earnings. BLS's rationale is that the relevant concept is the *ex ante*
   expected price, not the *ex post* realized loss ratio, which swings with
   unpredictable utilization.
2. **Semiannual instead of annual updates.** From **April 2024 data (May 2024
   release)**, retained earnings update **twice a year** using half-year data —
   April and October data, released in May and November. This **cuts the lag by
   six months**.
3. A transition: the October 2023 update spread 2022 data over six months rather
   than twelve, with a correction term so the switch from unsmoothed to smoothed
   relatives did not leave a permanent level distortion.

https://www.bls.gov/cpi/notices/2023/methodology-changes-2023.htm
https://www.bls.gov/cpi/additional-resources/improvements-cpi-health-insurance-index.htm

Also useful: BLS's own MLR article on measuring *total premium* inflation as an
alternative.
https://www.bls.gov/opub/mlr/2024/article/measuring-total-premium-inflation-for-health-insurance-in-the-cpi.htm

### December 2025: long-term care removed

Announced 2025-12-18. Traditional stand-alone long-term care insurance plans no
longer enroll new customers, and current LTC coverage is typically a hybrid life
insurance add-on that is out of CPI scope. LTC was removed from both pricing and
weighting in the health insurance index.
https://www.bls.gov/cpi/notices/2025/methodology-changes-2025.htm

### Bottom line for a reader

The health insurance line in the CPI is an accounting residual from insurer
financial statements, updated twice a year, smoothed over two years. It is not a
premium. It should never be described as "what health insurance costs."

---

## 4. Used cars and trucks — 2.76 percent of the CPI-U

**Source:** J.D. Power Valuation Services, collected on the **first of each
month**. A sample of **480 vehicles** drawn from the J.D. Power Information
Network with probability proportionate to sales. Sample last rotated in **2018**.

**Quality adjustment:** the same manufacturer-cost adjustments applied to those
vehicles when they were new. Annual model-year update each September keeps
vehicle age consistent; discontinued models get a comparable replacement.

**January 2024 change (announced 2024-02-13, effective with January 2024 data):**
the mileage/depreciation adjustment switched from a single stable annual mileage
figure per make and model to an **average monthly mileage based on the vehicle's
age**, following an exponential decay curve. Seasonally adjusted indexes were
rebuilt on the new basis.

https://www.bls.gov/cpi/factsheets/used-cars-and-trucks.htm
https://www.bls.gov/cpi/notices/2024/methodology-changes-2024.htm

**[UNCONFIRMED — what J.D. Power replaced and when.]** The factsheet does not
state the original adoption date or the prior source. The Handbook lists J.D.
Power for used vehicles without a date, implying it predates the recent
alternative-data wave. Do not date it in the post.

---

## 5. New vehicles — 3.84 percent of the CPI-U

**The April 2022 break.** Announced 2022-01-13, effective with **April 2022 data
(May 2022 release)**: BLS replaced its own collected new-vehicle prices with
**transaction data from J.D. Power**. At the same time motorcycles were dropped
from the index and the combined "new cars and trucks" series was discontinued.
Seasonally adjusted indexes kept BLS-collected data through 2022 and moved over
in 2023.
https://www.bls.gov/cpi/notices/2022/methodology-changes-2022.htm

**What is in the data today:** transaction-level records from participating
dealers, about **250,000 transactions per month**, with **40 variables**
including rebate values and vehicle characteristics. These are actual negotiated
transaction prices net of rebates, not sticker prices.
https://www.bls.gov/cpi/factsheets/new-vehicles.htm

**Quality adjustment:** manufacturer-supplied cost estimates for identifiable
quality differences between model years — reliability, durability, safety, fuel
economy, maneuverability, speed, acceleration and deceleration, carrying
capacity, comfort and convenience. **The new vehicles factsheet does not
describe a hedonic regression** for new vehicles; it is the manufacturer-cost
method. (See section 6 for where hedonics actually are used.)

**Model-year changeover:** when the newer model year outsells its predecessor,
the old-to-new price change is shown for one "changeover" month, and the new
model year replaces the old from then on.

**Two more recent tweaks:**
- 2023-01-04: improvements to the time-series filter that separates the cyclical
  trend from short-term fluctuation in the transaction data.
- 2023-03-08: model-year changeovers flagged non-comparable are now excluded
  from the year-over-year calculation, effective with February 2023 data.
https://www.bls.gov/cpi/notices/2023/methodology-changes-2023.htm

There is also a June 2024 new-vehicles notice worth reading if the post touches
vehicles: https://www.bls.gov/cpi/notices/2024/june-2024-new-vehicles.htm

**Leased cars and trucks** moved to vendor transaction data too, announced
2025-05-13, replacing survey-based collection. About **70,000 eligible leasing
transactions a month**, with the monthly lease price built from capitalized cost,
residual value, money factor and taxes, aggregated with a **Törnqvist** formula
on expenditure shares. BLS does not name the vendor.
https://www.bls.gov/cpi/notices/2025/methodology-changes-2025.htm
https://www.bls.gov/cpi/factsheets/leased-cars-and-trucks.htm

---

## 6. Apparel, televisions, computers, wireless service — hedonics

**Relative importance (Dec 2025, CPI-U):** Apparel 2.368. Televisions 0.107.
Information technology, hardware and services 1.714. Wireless telephone services
1.340.

### Where hedonics actually are used today

Authoritative current list: https://www.bls.gov/cpi/quality-adjustment/

**Hedonic adjustment:**
- **Apparel and footwear** — nearly every garment stratum (men's, boys', women's,
  girls' outerwear, tops, pants, dresses, suits, undergarments, footwear), plus
  watches.
- **Electronics and communications** — wireless phone service (hedonic
  *imputation*), land-line telephone services, internet access, phones and
  accessories and smartwatches, televisions, cable and satellite TV, other video
  equipment, photographic equipment.
- **Appliances** — refrigerators and freezers, washers and dryers, ranges and
  cooktops, microwave ovens.
- **Housing** — rent of primary residence and owners' equivalent rent, for "age
  bias, structural change, facility adjustments."

**Cost-based (direct) adjustment, NOT hedonic:** personal computers and
peripherals, new car and truck purchase, used cars and trucks, vehicle leasing.

Models are re-estimated about every two years.
https://www.bls.gov/cpi/quality-adjustment/questions-and-answers.htm

**Correction worth carrying into the post:** personal computers, the single most
cited example of CPI hedonics, have **not** been hedonically adjusted since
**2003**. See below.

### Adoption dates

The current quality-adjustment page carries no dates. The dated table is in Paul
Liegey, "Hedonic Quality Adjustments in the U.S. CPI: A Statistical Agency
Perspective," ZEW conference, Mannheim, April 2002, p. 29.
https://www.bls.gov/cpi/white-papers/hedonic-quality-adjustments-statistical-agency-perspective.pdf

| Item | Effective with CPI for |
|---|---|
| Personal computers | **January 1998** (discontinued 2003) |
| Televisions | **January 1999** |
| Audio products | January 2000 |
| Camcorders | January 2000 |
| VCRs, DVD players | April 2000 |
| Refrigerators, microwave ovens | July 2000 |
| Clothes washers (and dryers) | October 2000 (2000) |

Later:
- **January 2018:** smartphones / phones, accessories and smartwatches.
- **January 2019:** five models for residential telephone, internet access,
  cable/satellite TV and bundles.
- **2017:** wireless telephone service, hedonic at item replacement. **July 2025:**
  full hedonic imputation.
- **Shelter and apparel:** since roughly the late 1980s / early 1990s.

### The number that matters: BLS's estimate of the effect

From the misconceptions factsheet, verbatim:

> "Since 1998, hedonic models have been introduced in several other components,
> mostly consumer durables such as personal computers and televisions, but these
> newer areas have a combined weight of only about one percent in the CPI. A
> recent article by BLS economists estimated that the hedonic models currently
> used in the CPI outside of the shelter and apparel areas have increased the
> annual rate of change of the All Items CPI, but by only about 0.005 percent per
> year."

The underlying paper is **Greenlees and McClelland, "Addressing misconceptions
about the Consumer Price Index," MLR August 2008**.
https://www.bls.gov/opub/mlr/2008/08/art1full.pdf

Verbatim from it:

> "The total CPI weight for all products subject to hedonic adjustment is about
> 32 percent, but almost all of this total is accounted for by shelter and apparel
> items… Personal computers, microwave ovens, televisions, and other commodities
> for which hedonic models were more recently introduced have a combined weight
> of only about 1 percent in the CPI."

> "The CPI price indexes for shelter include hedonic adjustments for the gradual
> aging of the rental housing units in the CPI sample, and those adjustments
> regularly **increase** the rate of change of the indexes by at least **0.2
> percentage point per year**… the BLS estimates that the hedonic quality
> adjustments introduced since 1998 have had an upward impact in five item
> categories and a downward impact in five. The overall impact… has been quite
> modest and in an **upward, not downward, direction**."

**Three things here are counterintuitive and all three are quotable:**

1. About **32 percent** of the CPI by weight is subject to some hedonic
   adjustment — but that is almost entirely **shelter and apparel**, not
   electronics.
2. The shelter age-bias hedonic **raises** measured shelter inflation by at least
   **0.2 percentage points a year**. It is by far the largest hedonic effect in
   the index and it runs upward.
3. Everything introduced since 1998 nets to about **+0.005 percentage points a
   year** on the all-items CPI — upward, and a rounding error.

Footnote 35 sources the 0.005 to Johnson, Reed and Stewart, "Price measurement in
the United States: a decade after the Boskin Report," MLR May 2006, p. 15, and
notes it excludes personal computers.

Item-level simulations from the 2002 white paper (p. 25), difference between the
published index and an experimental quality-adjusted index:

| Stratum | Period | Hedonic impact |
|---|---|---|
| Computers | 1998/06-12 | 6.5% lower, annualized |
| Televisions | 1993/08-1997/08 | 0.1% lower, average annual |
| Audio products | 1998 | 1.4% **higher** |
| Camcorders | 1999 | 0.2% lower |
| VCRs | 1999 | 1.0% **higher** |
| Refrigerators | 1999-2000 | unchanged |
| Microwaves | 1999-2000 | 0.2% lower |
| Washers | 1999-2000 | 0.6% lower |
| Dryers | 1999-2000 | unchanged |

BLS's summary: "Given the relatively small index impacts—computers being the
exception—that hedonic quality adjustments have produced, combined with the small
item weights, the overall impact on the (all items) CPI is negligible."

### Apparel

Offer prices for specific garments, collected monthly or bimonthly by BLS field
staff in stores and on outlet websites. Each apparel entry-level item has its own
hedonic regression; when a garment disappears and is replaced, the coefficients
value the difference in characteristics. BLS publishes a page per model, for
example:

- Men's suits: "entered the CPI in 1992," five updates since; current model on
  about 280 web-collected observations from May and June 2022. Variables include
  brand tier, fiber, hand-stitching, single button, pre-hemmed, flexible
  waistband. https://www.bls.gov/cpi/quality-adjustment/mens-suits.htm
- Women's dresses: "first incorporated into the CPI in 1992," **nine** revisions
  since; current model on about 1,880 observations from about 75 outlets, July
  and August 2024, newly including jumpsuits and rompers.
  https://www.bls.gov/cpi/quality-adjustment/womens-dresses.htm
- Boys' shirts and sweaters: model entered September 2004.
- Men's underwear: "the first-ever CPI quality adjustment model for men's
  underwear," 823 observations from January-February 2023 plus web-scraped data
  from a large national retailer; page modified June 2023.

**[UNCONFIRMED — the 1991 date.]** I could not confirm 1991 on a BLS source. BLS
item pages date the oldest apparel models to **1992**. The founding research is
Paul R. Liegey Jr., "Apparel price indexes: effects of hedonic adjustment," MLR
May 1994 — https://www.bls.gov/opub/mlr/1994/05/art6full.pdf — which is a scanned
image PDF with no text layer and could not be read. **Safe wording: "hedonic
models entered the CPI's apparel indexes in the early 1990s and have been
re-estimated every few years since."**

**The corporate apparel data — dated.** The Handbook says only that "One firm
provides BLS with a large volume of price data rather than allowing data
collectors to collect data in stores," undated. The date is in the BLS-authored
big-data paper: a department store ("CorpX") began supplying BLS with a monthly
dataset of average price and sales revenue per product per outlet in **May 2016**;
BLS assessed it for two years and "**approved its use in production beginning with
the March 2019 index**."
https://www.nber.org/system/files/chapters/c14280/revisions/c14280.rev1.pdf

Two details worth noting: the retailer stopped letting data collectors into
stores, which is why the feed exists; and the data carry only short product
descriptions with no structured feature fields, which "prevents constructing
hedonic regressions" on them — so BLS draws a PPS sample from the transactions,
chains matched-model relatives within a year, and resamples twice a year assuming
constant quality across the annual link.

### Televisions

**Hedonic since January 1999.** https://www.bls.gov/cpi/quality-adjustment/televisions.htm
Research basis: Moulton, LaFleur and Moses, "Research on Improved Quality
Adjustment in the CPI: The Case of Televisions," Ottawa Group, April 1999. It
replaced ordinary link/impute substitution, under which about 15 percent of the TV
sample went permanently unavailable each month.

About 400 observations in the sample; checklist characteristics are verified
against manufacturer and retailer web pages. BLS publishes a worked coefficient
example: "LCD direct view and plasma televisions have prices that are about 70%
greater than CRT televisions, all other characteristics being equal."

**The magnitude, and the trap.** The published TV index (CUUR0000SERA01, NSA,
rebased Dec 2024 = 100) went from **5857.5 in December 1997 to 96.6 in August
2026** — a **98.3 percent decline**, about one sixty-first of its 1997 level.

This is the single most-cited "the CPI is fake" statistic. It is also mostly not
about hedonics:

- **BLS has never attributed the decline to hedonics.** The only BLS estimate of
  the hedonic contribution is that "the television index would have been
  approximately 0.1 percent lower per year with the quality adjustments applied
  from August 1993 to August 1997" (2002 white paper, p. 5). That is 0.1 percent a
  year against a 98 percent cumulative fall.
- The fall is driven by ordinary matched-model price collection on a product whose
  real prices collapsed.
- BLS's own recent research brackets the official index rather than beating it
  down: over **January 2021 - June 2023** the official TV CPI fell 15.3 percent,
  while one-stage and two-stage hedonic imputation indexes fell 12.6 and 19.5
  percent.
  https://www.bls.gov/opub/mlr/2024/article/alternative-data-sources-for-high-tech-products-in-the-cpi.htm

**[Note] The 98.3 percent figure is computed from the published BLS series, not
published by BLS as a statement.** It is correct, but it is arithmetic, not a
quote.

### Personal computers — hedonics dropped in 2003

https://www.bls.gov/cpi/factsheets/personal-computers.htm

Today, "computers, peripherals, and smart home assistant devices" within
information technology commodities. BLS collectors return monthly to sampled
outlets for current prices including discounts. Computers are exempt from standard
replacement procedure because manufacturers continuously release better models.
Two distinctive features:

- **Directed substitution, since January 2000.** Collectors replace an aging
  computer with a new one at the same *quality tier* with updated attributes,
  whether or not the old model is still on sale. Three tiers on CPU speed, RAM and
  storage; tier definitions refreshed **every six months**.
- **Attribute-cost quality adjustment, since 2003.** Quality differences are
  valued from the cost of five attribute groups — CPU model, RAM type and amount,
  hard-drive storage, video card, monitor size — with component prices taken from
  OEM websites and updated monthly.

**What it replaced:** hedonic regression, effective with the CPI for **January
1998** (the CPI used the PPI's desktop-computer regressions, which the PPI had run
since December 1990). Greenlees and McClelland (2008), footnotes 35 and 36:
"in 2003, the CPI program implemented a new approach that derives the values of
computer attributes from information on the Internet, rather than from estimated
hedonic regressions," and "the BLS stopped using hedonic quality adjustments for
new computers in the CPI in 2003."

**Effect:** the one BLS figure is that the annual rate of growth of the PC index
was reduced by 6.5 percent during the 1998 period studied. With a weight under a
tenth of a percent, the all-items effect is a rounding error.

### Wireless telephone service — rebuilt twice

**How it is priced today** (since July 2025):
https://www.bls.gov/cpi/factsheets/wireless-telephone-service.htm
https://www.bls.gov/cpi/additional-resources/alternative-data-wireless-telephone.htm

- **What:** service plans and their characteristics — voice, text, cellular data,
  all service and per-plan charges. Plan characteristics include included data and
  hotspot data allowances. MNO and MVNO plans. Device installment payments
  excluded.
- **From whom:** monthly, from a telecom market research vendor using web-scraping
  and manual methods, supplying "a near universe of wireless telephone service
  plans available to consumers and their offer prices and characteristics." **No
  BLS field collection.**
- **Weights:** household survey data purchased from a second market research firm.
  "Data purchases and weighting-data updates occur every two years."
- **Method:** a predictive hedonic regression of price on plan characteristics is
  estimated **every month** on all plans — hedonic *imputation*, not adjustment at
  replacement — and aggregated with a **Törnqvist** formula. Area tax rates applied
  before the national index.

**Timeline:**

| Effective | Change |
|---|---|
| **2017** | Hedonic quality adjustment **at item replacement** begins. "Since 2017, BLS has used quality-adjusted prices at item replacement to calculate the CPI for wireless telephone services." |
| **January 2019** | Five hedonic models for residential telephone, internet, cable/satellite TV, bundles. |
| **February 2019** | Commercial household survey data used to direct field staff toward the most important plans at sample initiation. |
| **July 2025 indexes, released 2025-08-12** | Survey collection **replaced entirely** by secondary-source data plus monthly hedonic imputation and Törnqvist. Replaced "the traditional Commodities and Services (C&S) Pricing Survey, which relied on BLS data collectors sampling outlets and obtaining offer prices for specific, constant-characteristic service plans on a monthly or bimonthly basis." BLS: the new method "is not reliant on item replacement." |

**[UNCONFIRMED — the "2017 sample rebuild."]** There is **no BLS notice describing
a 2017 sample rebuild** of the wireless index. The 2017 methodology-changes notice
lists only the used-cars change. What is documented is (i) hedonic adjustment at
replacement beginning 2017 and (ii) the February 2019 sample-initiation change.
The defensible mechanism for March 2017: carriers reintroduced unlimited-data
plans in late February 2017, and under the new hedonic treatment the added data
counted as a quality improvement, so the measured constant-quality price fell hard.

Current caveat BLS publishes: "Currently, the CPI records changes in wireless
telephone plans from 4G networks to 5G networks, but does not quality adjust for
these changes." https://www.bls.gov/cpi/factsheets/telecommunications.htm

#### The March 2017 drop — the real numbers

From the CPI news release for March 2017, published 2017-04-14:
https://www.bls.gov/news.release/archives/cpi_04142017.htm

- Wireless telephone services: **−7.0 percent in March 2017**, which BLS called
  **"the largest 1-month decline in the history of the index."**
- 12-month change March 2016 to March 2017: **−11.4 percent**.
- All items −0.3 percent for the month. BLS: "A decline in the gasoline index was
  the largest factor, with a decrease in the index for wireless telephone services
  also contributing."
- **Core CPI −0.1 percent for the month, "its first decline since January 2010";
  +2.0 percent over 12 months, "the smallest 12-month increase since November
  2015."**
- Relative importance as of February 2017: wireless telephone services **1.695
  percent** of the CPI-U; all items less food and energy 79.191 percent.

Index levels (CUUR0000SEED03): Jan 2017 53.435 → Feb 52.679 → **Mar 49.002** →
Apr 48.153 → Dec 2017 48.066. The Feb-to-Apr fall was 8.6 percent and the index
never recovered.

**[UNCONFIRMED — the "0.2 percentage point off core CPI" figure.]** BLS does not
publish contribution decompositions like this, and no BLS or Fed document states
0.2 pp for core CPI. The arithmetic from BLS's own published numbers:
1.695 / 79.191 = 2.14 percent of core; 2.14% × 7.0% ≈ **0.15 percentage point**
off core CPI, and since it is a level shift, off the 12-month core rate for the
following twelve months. Using the Feb-Apr 8.6 percent cumulative drop gives about
0.18 pp. **"Roughly 0.15 to 0.2 percentage point" is defensible as our own
arithmetic on BLS data. Do not attribute it to BLS or the Fed.**

What the Fed did publish:
- FEDS Note, "Common and idiosyncratic inflation," 2020-03-05: in March 2017 the
  wireless index fell 52 percent at an annual rate, **shaving about 8 basis points
  off the monthly percent change in core PCE prices**, attributed to both the CPI
  methodological change and Verizon's and AT&T's reintroduction of unlimited data
  plans in late February 2017 (the two then held nearly 70 percent of U.S.
  subscriptions). Note: core **PCE**, monthly, not core CPI.
  https://www.federalreserve.gov/econres/notes/feds-notes/common-and-idiosyncratic-inflation-20200305.html
- Chair Yellen, 2017-10-15 speech, described "one-off reductions in some categories
  of prices, especially a large decline in quality-adjusted prices for wireless
  telephone services." No figure attached.
  https://www.federalreserve.gov/newsevents/speech/yellen20171015a.htm

**Why BLS rebuilt it in 2025.** BLS research found the old method badly
understated the decline: over **December 2018 - December 2022**, "the one-stage
hedonic imputation index fell 11.6 percent, the two-stage hedonic imputation index
fell 3.1 percent, and the official CPI for wireless telephone services increased
4.8 percent."
https://www.bls.gov/opub/mlr/2024/article/alternative-data-sources-for-high-tech-products-in-the-cpi.htm

### Smartphones / telephone hardware

https://www.bls.gov/cpi/factsheets/telephone-hardware.htm — smartphones are not
published as a separate index; they sit inside "telephone hardware, calculators,
and other consumer information items."

- **What is priced:** "the price collected for a cell phone (including smart
  phones) is the entire cost of the phone, with any promotions or sales deducted
  from the price" — the full unsubsidized purchase price, checked monthly at
  carrier stores, big-box retailers and online outlets.
- **Quality adjustment introduced January 2018**, hedonic regression on screen
  resolution, processor speed, camera capability and similar. Models are estimated
  on "a secondary source that specializes in capturing smartphone prices from a
  wide variety of retailers."
- **Directed substitution began April 2018** — phones replaced about twice a year
  to track release cycles.

Both dates corroborated independently by Aizcorbe, Byrne and Sichel, "Getting
Smart About Phones," FEDS Working Paper 2019-012, February 2019.
https://www.federalreserve.gov/econres/feds/files/2019012pap.pdf

**[UNCONFIRMED — the effect.] BLS has published no estimate.** The Fed paper
explains why outsiders cannot check it either: "We cannot… compare the BLS price
index for mobile phones (or smartphones) to other indexes because the index for
mobile phones is not reported separately." The Fed authors' own smartphone hedonic
falls about 16 percent a year (2010-2018); folding it in would make the overall
PCE price index rise about **4 to 5 basis points less per year over 2010-2017**.
That is a Fed estimate for PCE, not a BLS estimate and not CPI.

---

## 7. Medical care services and prescription drugs

**Relative importance (Dec 2025, CPI-U):** Medical care services 6.935.
Hospital and related services 2.618, of which hospital services 2.167.
Physicians' services 1.684. Medical care commodities 1.489, of which
prescription drugs 0.973.

### What price is collected today

Primary source: https://www.bls.gov/cpi/factsheets/medical-care.htm

**The price is the total reimbursement to the provider** — not the list price,
not the patient's copay alone. BLS's own worked example: an office visit where
the patient pays a $20 copay and the insurer pays $80 is priced at **$100**.
Eligible payers are private insurance, Medicare Part B and Medicare Part C.

- **Hospital services** pricing unit: "a hospital visit, defined by a specific
  medical service and a specific diagnosis or medical condition." Either itemized
  fee-for-service billing or a lump-sum billing unit such as a **DRG** payment,
  including room and board, labs and everything else on the bill. Hospital
  outlets are sampled from **American Hospital Association** data and are priced
  for **8 years** — 4 static, then 4 of semiannual rotation. That is double the
  standard CPI outlet life (see the February 2019 rotation change in section 10).
- **Physicians' services** pricing unit: "a doctor's visit, defined by a specific
  medical service," identified by **CPT code**. Standard rotation — one-eighth
  every 6 months, full rotation every 4 years.
- **Out of scope:** employer-paid insurance premiums, and fully tax-funded care
  (Medicare Part A, Medicaid).
- **Carry-forward is routine here.** Verbatim from the factsheet, for both
  physicians and hospitals: "Most offices that are approved for carry forward are
  priced between 2 and 4 months per year," and "For non-pricing months, the last
  collected price for each quote is carried forward for use in the current month
  index." A large share of the traditionally collected medical care sample is not
  freshly priced in any given month.

### January 1997: hospital services restructured

The change is **not** on the medical care factsheet. It is on the Handbook
history page and in two 1996 Monthly Labor Review articles by Elaine M. Cardenas.

https://www.bls.gov/opub/hom/cpi/history.htm
https://www.bls.gov/opub/mlr/1996/12/art6full.pdf ("Revision of the CPI hospital
services component," December 1996, pp. 40-48)
https://www.bls.gov/opub/mlr/1996/07/art4full.pdf ("The CPI for hospital
services: concepts and procedures," July 1996, pp. 32-42)

**Effective January 1997.** What changed:

- **Item definition.** "The new item definition identifies a hospital visit with
  multiple inputs as a single item; the current definition treats each input to a
  visit as a separate item." The priced unit became the hospital visit, taken
  from the contents of a live hospital bill. The Handbook summarizes it as
  "initiated a single hospital services item stratum with a treatment-oriented
  item definition" and "discontinued pricing of the inputs to hospital services."
- **Structure.** Three published strata (two inpatient — "hospital room" and
  "other inpatient services" including nursing homes — plus "outpatient
  services") collapsed into two: **hospital services** and **nursing home
  services**. The **hospital room index, in the CPI since 1935, was
  discontinued.** New strata based to December 1996 = 100.
- **Prices.** "Integral to this redefinition is an intensification of BLS'
  long-standing efforts to obtain hospital transaction (reimbursement) prices
  rather than hospital list (chargemaster) prices." Field staff pick a payer by
  revenue-based disaggregation, then take the most recently closed-out bill.
- New collection instrument fielded May 1996; items reselected nationwide May
  through August 1996.
- **Scope:** the CPI hospital universe is only privately insured and self-paying
  patients. Medicare, Medicaid, auto PIP, workers' comp and state payers for jail
  inmates are removed before disaggregation.

**Important correction to the usual telling.** 1997 was **not** a clean switch
from list to transaction prices. For fee-for-service contracts — still "a
substantial proportion of insurance plans" in 1996 — and for self-payers, field
staff recorded a bundle of core services and "will report chargemaster prices for
each item of the core description available from the bill… The reported price
becomes the sum of the listed components minus any formally negotiated discounts
to the insurers off the chargemaster fee." List prices net of negotiated
discounts stayed in the index. BLS's own word for the change was
"intensification." **Do not write "in 1997 the CPI switched from list prices to
transaction prices."**

**[UNCONFIRMED — the inflation effect.]** There is **no BLS-published quantitative
estimate** of what the 1997 revision did to measured inflation. The MLR article
gives qualitative expectations only. The one nearby number is a sample-composition
statistic from the 1992-1994 pilot: "The representation of nonchargemaster prices
in the 'hospital services' index was increased from **6 percent to approximately
20 percent**." That is not an inflation effect. Any inflation-effect claim would
have to come from the NBER *Medical Care Output and Productivity* literature
(Berndt, Cutler, Frank, Griliches, Newhouse, Triplett), not from BLS.

### October 2024: medical claims data

Announced 2024-11-13, effective with **October 2024 indexes (November 2024
release)**.
https://www.bls.gov/cpi/notices/2024/methodology-changes-2024.htm
https://www.bls.gov/cpi/additional-resources/use-of-medical-claims-data-physicians-and-hospital-services.htm

- BLS "replaced the data collected by the BLS for the private insurance portion
  of physicians' services and outpatient hospital services with secondary source
  medical claims data."
- **Source:** purchased from a national health insurance aggregator, not named.
  Claims are provider bills to insurers, carrying diagnosis codes, procedure codes
  and service cost. The vendor strips price outliers and ineligible provider types
  and procedure codes. **MEPS** supplies payer-type shares for weighting.
- **Formula:** an annually chained **Lowe index** using prior-year average monthly
  quantities, reweighted at CPT subcategory level to match population expenditure
  shares.
- **Rotation:** every **2 years** (25 percent of PSUs every 6 months, April and
  October), against the traditional 4 years. Claims arrive with a **3-month lag**.
- **Scope is narrow and this is the key point.** Verbatim: "These data only
  replace data for services covered by private insurance; services paid for by
  cash (self-pay), Medicare part B, and all inpatient hospital services are still
  collected via the Commodity & Services survey and are combined with the claims
  data to calculate the final indexes." **Inpatient hospital services are still
  surveyed the 1997 way.**

**Published effect** — the one case where BLS did publish a backcast. MLR
February 2023, Bieler, Cho, Gayer, Matsumoto, Parker and Wang, "Incorporating
medical claims data in the Consumer Price Index."
https://www.bls.gov/opub/mlr/2023/article/incorporating-medical-claims-data-in-the-cpi.htm

Over **January 2016 – March 2020 (51 months)**, annualized:

| Index | Traditional | Claims-based |
|---|---|---|
| Physicians' services, private insurance only | +1.4% | **+1.1%** |
| Physicians' services, all payer | +1.2% | +1.0% to +1.1% |
| Outpatient hospital services, all payer | +3.7% | +3.2% to +4.4% |

So claims data ran **lower** for physicians' services by about 0.3 percentage
points a year. For outpatient hospital the sign was not stable across methods.
Results held with the 3-month lag applied.

**Why BLS moved:** medical care response rates fell from about **90 percent in
2002 to about 50 percent in 2019, and below 40 percent in 2021**. BLS began
researching purchased claims data around 2015.
https://www.bls.gov/opub/mlr/2023/article/improving-response-rates-and-representativity-in-the-cpi-medical-care-index.htm
(This matches the response-rate table in section 12: medical care collected 47.4
percent of eligible quotes in 2016 and 32.0 percent in 2024.)

### Prescription drugs

**What is priced:** "The tracked price is the total reimbursement to the retailer
from the patient and all eligible payers for a single prescription." Eligible
payers: self-pay, commercial insurance, **Medicare Part D**. Medicaid is out of
scope.

**Sampling:** pharmacies provide **the last 20 prescriptions dispensed**; each is
given a selection probability equal to its price divided by the total price of
all 20. About five or six quotes per pharmacy. Outlets priced about 4 years, with
one-eighth rotating every 6 months.

**Bulk price data:** the Handbook says a large firm provides bulk price data for
prescription drugs, undated. https://www.bls.gov/opub/hom/cpi/data.htm
**[PARTIALLY UNCONFIRMED]** The MLR 2023 response-rate article says that from
**March 2015** BLS receives a bimonthly dataset from a pharmaceutical retailer
(anonymized as "Corp Y") of average in-store transaction prices, which helps
offset the overrepresentation of self-pay prices in the store-collected sample.
BLS never states that the Handbook's "large firm" and "Corp Y" are the same
source, and never names the firm. Treat March 2015 as applying to the Corp Y file
specifically.

#### Generics: the January 1995 rule

Primary source: **BLS Working Paper 263, February 1995**, Armknecht, Moulton and
Stewart, *Improvements to the Food at Home, Shelter, and Prescription Drug
Indexes in the U.S. Consumer Price Index*.
https://www.bls.gov/osmr/research-papers/1995/pdf/ec950010.pdf

**Before 1995**, verbatim: "when a branded drug under patent is sampled, we have
historically continued to price that brand even when it loses its patent, as long
as it remains for sale in the outlet. Generic drugs typically enter the CPI only
through sample rotation, where any price change from the previous sample is
**linked**." Linked means the brand-to-generic price drop was treated as
non-inflationary and never appeared as a price decline. The CPI simply did not
capture the biggest price event in a drug's life.

**Effective with the January 1995 index**, verbatim: "The CPI prescription drug
analyst will keep track of when all branded drugs lose patent protection. **Six
months after a drug loses its patent, that particular drug will be resampled**
using probability proportional to expenditures for that drug in that specific
outlet." And: "When a generic version is selected in place of [the brand], we
will reflect in the U.S. CPI **the entire price difference (i.e., price decline)**
between the brand drug and the 'equivalent' generic."

BLS notes this is *less* conservative than Griliches and Cockburn's approach,
since some consumers perceive a quality difference between brand and generic and
BLS treats the whole gap as pure price change.

**BLS's own statement of effect:** "This change in CPI procedures will have the
effect of **slightly slowing the rate of growth in the CPI prescription drugs
component**." **No number is given, anywhere.** Motivated by Griliches and
Cockburn (1994), "Generics and New Goods in Pharmaceutical Price Indexes," AER
84(5): 1213-32.

Do not conflate this with the Handbook history page's 1995 entry ("Implemented
new sample procedures to prevent overweighting items whose prices are likely to
rise") — that refers to the food-at-home sample-aging change in the same working
paper.

#### How the rule has drifted since

1. **Selection measure changed and BLS never announced it.** The 1995 paper says
   resample "using probability proportional to **expenditures**." The current
   factsheet says "probabilities **proportional to the share of prescriptions sold
   at the pharmacy in the past 3 months**." The 2011 BLS methodology report
   already describes the prescription-count version. **[UNCONFIRMED]** No BLS
   notice dates this shift. It is a difference between two BLS documents, not a
   documented change event.
2. **The resample happens once.** Current factsheet: BLS "will resample all
   previous instances where the brand was selected because no generic existed at
   the time," and "If the brand is selected again, we simply continue to price the
   brand."
3. **The 6-month window is a target, not a rule.** From BLS, "The pharmaceutical
   industry: an overview of CPI, PPI, and IPP methodology" (2011, modified 2021):
   "although we target a period within 6 months for this redisaggregation step,
   the actual procedures may occur before or after, depending on respondent burden
   and cooperation."
   https://www.bls.gov/ppi/methodology-reports/the-pharmaceutical-industry-an-overview-of-cpi-ppi-and-ipp-methodology.pdf
4. **The retail dataset automates it.** MLR 2023 says the Corp Y file "automates
   the process of incorporating generic prices into the index as generic versions
   of drugs penetrate the market," removing manual patent-expiration tracking for
   that part of the sample.

BLS calculates but **does not publish** separate brand and generic
prescription-drug subindexes. Drugs transitioning off patent are held out of those
unpublished sub-indexes, but their price changes do flow into the published
prescription drug index. The prescription drug formula moved from modified
Laspeyres to **geometric mean in January 1999**.

#### The best-known critique points the other way

**Bosworth, Bieler (BLS), Kleinrock, Koepcke and Berndt, "An Evaluation of the
CPI Indexes for Prescription Drugs," NBER Working Paper 24210, January 2018.**
https://www.nber.org/system/files/working_papers/w24210/w24210.pdf

Compares the CPI prescription drug sample against IQVIA transaction data,
2009-2013. Finding: "the IQVIA data indicate a **more rapid rate of price
increase** than reported in the CPI for the aggregate of all prescription drugs,"
with IQVIA above CPI in 8 of 12 therapeutic classes. Restricting IQVIA to cash
transactions had "a relatively minor effect"; a Törnqvist version widened the gap.
The authors "could detect no obvious reason."

Worth flagging for the post: this critique says the CPI drug index runs **too
low**, which is the opposite of the usual "generic substitution hides inflation"
framing. It is an NBER working paper with a BLS co-author using restricted BLS
microdata, not a BLS publication.

---

## 8. Airline fares — 0.88 percent of the CPI-U

Still priced by BLS, on the web, one trip at a time. Each quote gets **fixed
specifications** for advance reservation and day of week (for example, seven
weeks ahead, departing Tuesday), and the same trip is repriced under the same
rules each month.

- Fares include **all applicable taxes**, domestic and international, plus fuel
  surcharges and airport, security and baggage fees. Whether a quote includes a
  checked bag is assigned randomly based on DOT data, and only the first checked
  bag is tracked.
- The **sample** of trips comes from the **U.S. DOT ticket data bank** (October
  through December of the most recent year), which covers 40 percent of tickets
  sold by certified carriers. Trips are drawn with probability proportional to
  passengers.
- The resulting sample is mostly discount fares — roughly half priced at the
  lowest available fare and half at other specific discount fares.

**No move to transaction data.** The DOT data set the *sample*, not the prices.
The prices are still BLS web collection. I found no BLS announcement of an
alternative-data switch for airline fares.
https://www.bls.gov/cpi/factsheets/airline-fares.htm

---

## 9. Food at home and groceries — 8.33 percent of the CPI-U

**Short answer: no scanner data, not in 2026, and no announced plan.** Food at
home is still priced by people walking into stores.

**Relative importance (Dec 2025):** Food at home 8.325 (CPI-U), 9.524 (CPI-W).

### BLS tested scanner data and decided against it

Primary source, all three authors BLS (Crystal G. Konny was Chief of the Branch
of Consumer Prices; David M. Friedman was Associate Commissioner for Prices and
Living Conditions): "Big Data in the U.S. Consumer Price Index: Experiences &
Plans," June 2019.
https://www.nber.org/system/files/chapters/c14280/revisions/c14280.rev1.pdf

- BLS bought historical **Nielsen Scantrack** data at UPC and geographic-area
  level, five years ending 2010, about **2 million UPCs**.
- Coverage was the problem: the data "does not cover the full scope of outlet
  types covered in the CPI for Food at Home categories, **omitting convenience
  stores, bakeries, butchers, smaller grocery stores, warehouse stores, and gas
  stations**."
- About 80 percent of UPCs mapped directly to CPI categories; the rest were
  matched by hand.
- FitzGerald and Shoemaker (2013) tested Scantrack as a *replacement* for some
  food-at-home categories. Some tracked the CPI well. "Other categories with
  product cycles displayed **extreme downward declines** similar to other
  transaction data indexes" — the classic problem where entering and exiting
  goods drag a transaction index down. Researchers had to build common-good
  indexes excluding entering and exiting goods.
- **The conclusion, verbatim:** "Ultimately, BLS found that it was **less
  expensive to collect data in stores than to pay for Nielsen Scantrack** for the
  real-time data and geographic and outlet detail needed to support the monthly
  CPI. BLS plans to explore whether retailers would be willing to provide us
  corporate datasets, but unlike the examples discussed above, **BLS has not yet
  experienced many response or collection issues in Food At Home outlets**."

Earlier BLS scanner research: Ralph Bradley, "An Overview of the Research on
Potential Uses of Scanner Data in the U.S. CPI," 1998.
https://www.bls.gov/pir/journal/br02.pdf

### Status as of 2024-2026: nothing

- MLR December 2024, Brown and Smucker, "Alternative data sources for high-tech
  products in the CPI," says that outside postage, gasoline, used vehicles and new
  vehicles, nontraditional data have not directly replaced traditional collection,
  and that BLS intends to "pivot from using nontraditional data as a supplementary
  tool to using it as the very basis for CPI calculation" where cost-effective.
  **The article does not discuss food at home, groceries or scanner data at all.**
  https://www.bls.gov/opub/mlr/2024/article/alternative-data-sources-for-high-tech-products-in-the-cpi.htm
- The 2025 methodology-changes notice lists exactly three changes: long-term care
  out of health insurance, wireless telephone services to secondary source, leased
  cars and trucks to vendor transaction data. **Nothing on food.**
- A review of the **complete CPI notices list, 2019 through 2026**, turns up **no
  notice of any kind** announcing scanner data, grocery transaction data, or a
  food-at-home data-source change. https://www.bls.gov/cpi/notices/

BLS's own 2019 reasoning explains why food is last in line: the alternative-data
program has been driven by **collapsing response rates**, and grocery stores were
the one place BLS was still getting its prices. That is no longer as true — food
quote collection fell from 88.5 percent in 2016 to 78.1 percent in 2025 (section
12) — so this is a reasonable thing to watch, but it has not happened.

### The 2025 collection cuts and food

BLS published **no food-specific effect estimate**. The only quantification is the
all-items simulation: less than 0.01 percentage points on 12-month changes over
January 2019 - May 2025, with an unquantified warning that "the volatility of
subnational and sub-aggregate item indexes also is impacted." See section 11.

Note also: the imputation table at
https://www.bls.gov/cpi/tables/imputation-cs-data.htm carries **no item-level
breakdown** and only a rolling twelve months. A chart of "food imputation rose"
cannot be built from BLS published tables.

---

## 10. Other major measurement changes BLS itself flags

Beyond the item-specific ones above:

- **Annual weight updates from January 2023** (was biennial). Announced
  2022-05-24. https://www.bls.gov/cpi/notices/2022/methodology-changes-2022.htm
- **2018 geographic revision** — new primary sampling units phased in from 2018
  rather than all at once. A **2028 geographic revision** is already noticed
  (2026-07-27). https://www.bls.gov/cpi/notices/2026/geographic-revision.htm
- **Rebasing of selected CPI series**, announced 2026-05-12.
  https://www.bls.gov/cpi/notices/2026/rebasing.htm
- **Research CPI for product size changes (R-CPI-SC)**, 2024-05-29 — BLS's
  shrinkflation series. https://www.bls.gov/cpi/notices/2024/r-cpi-sc.htm
- **Research CPI by income quintile (R-CPI-I)**, 2023-09-13. Directly useful for
  a share-of-income post. https://www.bls.gov/cpi/notices/2023/r-cpi-i.htm
- **Food publication changes**, 2023-09-20.
  https://www.bls.gov/cpi/notices/2023/food-publication-changes.htm
- **Publication changes effective February 2025**, announced 2024-11-13.
  https://www.bls.gov/cpi/notices/2024/publication-changes.htm
- **Alternative collection modes** (web, app, phone in place of store visits),
  2019-10-25. https://www.bls.gov/cpi/notices/2019/alternative-collection.htm
- **October 2019: the Telephone Point-of-Purchase Survey (TPOPS) was retired.**
  A structural change most people miss. For decades the CPI drew its *outlet*
  sample — which stores to price in — from a separate telephone survey. From
  October 2019 the outlet frame comes from the **same Consumer Expenditure
  Survey** that supplies the weights: the Diary component for food and food away
  from home, the Interview component for everything else, refined against the
  Quarterly Census of Employment and Wages business registry. Announced
  2019-05-06. https://www.bls.gov/cpi/notices/2019/methodology-changes-2019.htm
- **February 2019: sample rotation slowed for electricity, utility gas service
  and hospital services** — from a 4-year refresh to an 8-year cycle (selected
  over 4 years, then held 4 years). Announced 2019-03-01. Same source. Hospital
  services is 2.17 percent of the CPI-U and its outlet sample is now up to 8
  years stale.
- **January 2019: residential telecommunications packages quality-adjusted** —
  land-line telephone, internet, and cable/satellite TV. Announced 2019-01-15.
- **January 2018: used cars moved from a three-month moving average to a single
  month price change**, so the index reflects price change closer to the
  reference period. Announced 2017-11-21. This is why used-car CPI became much
  more volatile from 2018 on, and it matters for anyone charting the 2021-2022
  used car spike against earlier cycles.
  https://www.bls.gov/cpi/notices/2017/methodology-changes-2017.htm
- **April 2018: physicians' services payer-type weights rebuilt** using the
  Medical Expenditure Panel Survey, raising the share of payments attributed to
  private insurance relative to uninsured and Medicare. Announced 2018-05-10.
  https://www.bls.gov/cpi/notices/2018/methodology-changes-2018.htm
- **April 2018: 33 average price series discontinued, 5 introduced.** Announced
  2018-02-14. Relevant if the post charts long average-price series. Same source.
- Full notice archive: https://www.bls.gov/cpi/notices/
- Methodology-change roundups by year:
  [2017](https://www.bls.gov/cpi/notices/2017/methodology-changes-2017.htm) ·
  [2018](https://www.bls.gov/cpi/notices/2018/methodology-changes-2018.htm) ·
  [2019](https://www.bls.gov/cpi/notices/2019/methodology-changes-2019.htm) ·
  [2021](https://www.bls.gov/cpi/notices/2021/methodology-changes-2021.htm) ·
  [2022](https://www.bls.gov/cpi/notices/2022/methodology-changes-2022.htm) ·
  [2023](https://www.bls.gov/cpi/notices/2023/methodology-changes-2023.htm) ·
  [2024](https://www.bls.gov/cpi/notices/2024/methodology-changes-2024.htm) ·
  [2025](https://www.bls.gov/cpi/notices/2025/methodology-changes-2025.htm)

### BLS's published effect estimates (the only quantified ones I found)

BLS almost never publishes "this change moved inflation by X." The few numbers
it does publish are on the misconceptions factsheet:

- **Hedonic quality adjustment:** BLS says hedonic adjustments run in both
  directions, that hedonic models in **shelter and apparel typically increase**
  measured index change, and that recent hedonic applications add only about
  **0.005 percentage points per year** of downward pressure on the overall CPI.
- **Rental equivalence:** increased shelter inflation on introduction; 140
  percent versus 79 percent for house prices, 1983-2007 (see section 1).
- **Substitution / geometric mean:** BLS rejects the "hamburger for steak" framing
  — substitution is only within narrow item categories, never across major
  groups.
- **International:** rental equivalence is used in 13 of 30 OECD countries and
  hedonic methods in 11; U.S. inflation exceeded 16 of 29 other OECD countries
  over 1997-2007.
- BLS explicitly rejects the claim that pre-1980 methods would show 11-12 percent
  inflation today.

https://www.bls.gov/cpi/factsheets/common-misconceptions-about-cpi.htm

This is BLS assessing BLS. Use it to represent the agency's position fairly, not
as independent verification.

### Older changes that still shape the long series

- **1983 (CPI-U) / 1985 (CPI-W):** rental equivalence replaces the asset-price
  treatment of owner-occupied housing.
- **1997:** hospital services move to treatment-episode pricing (section 7).
- **1999:** geometric mean formula adopted for most basic indexes, to account for
  consumer substitution within an item category.
- **1999-2000:** hedonic regression use expands.
- **2002:** Chained CPI-U (C-CPI-U) introduced to address upper-level
  substitution bias.

https://www.bls.gov/opub/hom/cpi/history.htm

---

## 11. The 2025 shutdown, and the collection cuts before it

This is the most important recent story about CPI data quality, and it is
separate from methodology.

### Budget-driven collection reductions, 2025

BLS suspended part of the CPI sample because it could not afford to collect it.

- **April 2025:** collection suspended entirely in **Lincoln, NE** and **Provo,
  UT**.
- **June 2025:** collection suspended entirely in **Buffalo, NY**.
- Across the other **72 areas**, about **15 percent of the sample** was suspended
  on average.
- Both the Commodities and Services survey and the Housing survey were cut.
- BLS: "The number of imputed items increased in April due to these actions."

BLS's own assessment: simulating the suspension back to 2018, the all-items U.S.
city average 12-month change differed from published CPI-U by **less than
0.01 percentage points on average**; it matched exactly in 52 of 77 months, was
0.1 pp higher in 14 and 0.1 pp lower in 11. BLS warns that **subnational and
item-level indexes** are more affected and did not quantify that.

https://www.bls.gov/cpi/notices/2025/collection-reduction.htm
https://www.bls.gov/cpi/notices/2025/more-information-collection-reduction.htm

### The 43-day shutdown: October 2025 CPI does not exist

CPI collection stopped **October 1 through November 12, 2025**.

- **There is no October 2025 CPI.** No all-items index, no core. BLS could not
  retroactively collect the prices. The monthly CPI had been published
  continuously since January 1921.
- The **November 2025** CPI was released late, on **December 18, 2025**, and was
  built from roughly half a month of collection.
- **Housing:** the April/October panel — one of the six — was simply not
  collected in October 2025. BLS's hierarchical imputation fell all the way
  through to **carry-forward**: April 2025 rents were carried into October 2025,
  so the October 2025 rent and OER indexes equal their September 2025 values.
  Because that same panel is on a six-month cycle, the gap also **distorted the
  April 2026 rent and OER indexes**, and BLS says published and research indexes
  reconverged once the panel was collected again in April 2026.
- **Consumer Expenditure data for October and November 2025 are also missing**,
  which feeds CPI *weights*. BLS convened NABE and CNSTAT expert panels (meeting
  2026-05-07/08) and chose a **survey weight adjustment factor** approach.

https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi.htm
https://www.bls.gov/cpi/notices/2025/2025-federal-government-shutdown-impact-on-cpi.htm
https://www.bls.gov/cpi/notices/2026/missing-ce-data-panels.htm
https://www.bls.gov/opub/mlr/2026/article/counterfactual-imputation-approaches-for-the-housing-component-of-the-october-2025-cpi.htm

---

## 12. What is imputed rather than directly priced

### The three imputation methods

**Home cell (same cell):** the missing price takes the average price change of
sampled items in the **same item category and same location**. This is the
preferred method.

**Different cell:** item category held constant, **geography widened** — first to
the region, then across regions. Less precise.

**Carry forward:** the current month's price is set equal to last month's. Used
when nothing else is available, and for some price-regulated items.

For **housing**: vacant units take the average rent change of recently occupied
units in the same area; non-responses take the average rent change within the
same nominal rent class (low, medium, high) in the same location.

**Class-mean imputation** is a separate technique used mainly for vehicles,
durables and apparel, where price change is estimated from comparable
replacement items being rotated in at the same time.

https://www.bls.gov/cpi/tables/imputation.htm
https://www.bls.gov/opub/hom/cpi/calculation.htm

### What BLS publishes, and a trap to avoid

BLS publishes monthly imputation tables from **January 2019 to present**, one for
the Commodities and Services survey and one for the Housing survey.
https://www.bls.gov/cpi/tables/imputation.htm
https://www.bls.gov/cpi/tables/imputation-cs-data.htm

**The published percentages are shares of the *imputed* quotes, not of all
quotes.** They sum to 100 across home cell, different cell and carry forward.
Recent C&S values:

| Month | Home cell | Different cell | Carry forward |
|---|---|---|---|
| Sep 2025 | 60% | 40% | 0% |
| Nov 2025 | 66% | 34% | 0% |
| Dec 2025 | 60% | 40% | 0% |
| Jan 2026 | 62% | 38% | 0% |
| Feb 2026 | 60% | 40% | 0% |
| Mar 2026 | 61% | 39% | 0% |
| Apr 2026 | 60% | 40% | 0% |
| May 2026 | 63% | 37% | 0% |
| Jun 2026 | 61% | 39% | 0% |
| Jul 2026 | 63% | 37% | 0% |
| Aug 2026 | 62% | 38% | 0% |

(October 2025 is absent — the lapse in appropriations.)

**Widely repeated error.** Bloomberg (2025-09-11), Apollo and others reported
that "the share of imputed prices rose to 36 percent in August 2025, up from
9 percent in February," and several outlets restated this as "36 percent of CPI
prices are estimated." Read against the BLS table, the 36 percent is the
**different-cell share of the prices that were already being imputed** — that is,
a deterioration in the *quality* of imputation, not the level of it. The real
finding is still bad, and still a story: BLS increasingly cannot find a
same-category, same-city price to impute from. But the sentence "36 percent of
CPI prices are made up" is wrong. **Do not repeat it.**
https://www.bloomberg.com/news/articles/2025-09-11/bls-leans-more-on-second-best-option-for-filling-in-cpi-blanks

### The number you actually want: the response rate tables

The share of prices that are *not collected* — and therefore imputed — comes from
BLS's annual response rate tables, not the imputation tables.
https://www.bls.gov/cpi/tables/response-rates/

BLS defines two stages. The **collection rate** is responding sample units over
eligible sample units. The **percent used in estimation** is sample units used in
estimation over eligible units, and BLS states plainly that "imputed prices, when
used in estimation, are counted in this estimate." The gap between eligible and
collected is the imputed share.

I pulled Table R-1 (CPI-U, U.S. city average) from the published files for 2016,
2019, 2024 and 2025 and computed the rates. **These are BLS's own numbers, from
BLS's own files.** This is the strongest, cleanest evidence in this brief.

**Commodities and Services survey — percent of eligible price quotes actually
collected**

| Group | 2016 | 2019 | 2024 | 2025 |
|---|---|---|---|---|
| **All quotes** | **81.8%** | **79.1%** | **72.6%** | **69.5%** |
| Food | 88.5% | 88.0% | 84.6% | 78.1% |
| Housing (excl. shelter) | 87.2% | 81.7% | 74.3% | 72.1% |
| Transportation | 90.3% | 86.0% | 73.7% | 70.0% |
| Medical care | 47.4% | 47.2% | **32.0%** | 39.5% |
| Recreation | 79.8% | 76.8% | 71.0% | 68.4% |
| Education and communication | 85.6% | 87.1% | 75.0% | 74.5% |
| Other goods and services | 87.5% | 82.3% | 67.9% | 66.5% |
| Apparel | 60.7% | 60.6% | 63.9% | 58.7% |
| Outlets | 93.6% | 90.2% | 86.6% | 77.4% |

2025 raw counts: 950,134 eligible quotes, 660,296 collected, 658,024 used in
estimation. The eligible sample itself shrank too — 1,144,695 quotes in 2016 and
1,163,081 in 2024, down to 950,134 in 2025.

**Housing survey — percent of eligible units that actually reported a rent**

| | 2016 | 2019 | 2024 | 2025 |
|---|---|---|---|---|
| Eligible units | 96,999 | 74,644 | 82,249 | 73,015 |
| Rent reported | 67,884 | 46,619 | 46,166 | 35,985 |
| **Percent reporting** | **70.0%** | **62.5%** | **56.1%** | **49.3%** |
| Found vacant | 6.6% | 5.3% | 4.0% | 3.9% |
| Not interviewed, not vacant | 23.4% | 24.5% | 29.7% | **38.6%** |

Files: https://www.bls.gov/cpi/tables/response-rates/2016.pdf ·
`2019.xlsx` · `2024.xlsx` · `2025.xlsx` at
https://www.bls.gov/cpi/tables/response-rates/

### What this actually supports

**The defensible headline: in 2025, fewer than half of the housing units in the
CPI sample reported a rent — 49.3 percent, down from 70.0 percent in 2016.** The
rest were imputed. Shelter is 35.6 percent of the CPI-U. That is a real,
primary-sourced, checkable statement, and it is stronger than the garbled
"36 percent of prices are imputed" claim circulating in the press.

**Second: overall quote collection fell from 81.8 percent in 2016 to 69.5 percent
in 2025.** Roughly 30 percent of the CPI's price quotes are now imputed rather
than collected, against about 18 percent a decade ago.

**Caveats to state plainly:**

- Imputation is normal and always has been. Even 2016 was not 100 percent.
  The story is the *trend*, not the existence.
- **2025 is contaminated.** The collection cuts (April and June 2025) and the
  43-day shutdown both fall in 2025, so the 2025 row mixes long-run response
  decline with two one-off events. The 2016 → 2024 comparison (81.8 → 72.6
  percent for quotes, 70.0 → 56.1 percent for housing) is the cleaner trend, and
  it is already bad enough without 2025.
- **Apparel's low rate is mostly by design.** BLS explains that the apparel
  sample is doubled and half is deliberately designated out of season at any
  time, so many quotes are eligible but not meant to be collected. Do not use
  apparel as evidence of decline.
- **Medical care has always been the worst** — under half its quotes collected
  even in 2016, and 32 percent in 2024. Medical care services is 6.9 percent of
  the CPI-U.
- These are *annual* figures. Monthly rates move around.

**Gasoline does not appear in this table at all any more**, because since June
2021 it is not collected by the survey. It is the item least exposed to this
whole problem.

**[UNCONFIRMED]** Secondary sources claim BLS permits up to 50 percent of prices
in a cell to be imputed. I could not confirm that on a BLS page.

### Ranking the items by how directly they are measured

Most directly priced, least modeled:

1. **Gasoline** — 6.1 million daily observations, actual posted pump prices,
   every observation used, tax-inclusive. 2.9 percent of the index.
2. **New vehicles** — 250,000 actual dealer transactions a month, but with
   manufacturer-cost quality adjustment layered on.
3. **Used vehicles** — real valuation data, but a fixed 480-vehicle sample with
   mileage and quality adjustment.
4. **Food at home, most commodities** — real shelf prices, but collected
   bimonthly outside three cities, and increasingly imputed.

Most modeled or indirect:

1. **Owners' equivalent rent (26.2 percent of the CPI-U)** — no owner is ever
   asked what they paid. A rent index from renters, smoothed over six months,
   reweighted by structure type, applied to homeowners. By weight, this is by
   far the largest modeled component of the CPI.
2. **Health insurance (0.89 percent)** — an accounting residual from insurer
   financial statements, two-year smoothed, updated twice a year.
3. **Rent of primary residence (7.84 percent)** — directly collected, but each
   unit only twice a year, with one-sixth smoothing.
4. **Medical care services (6.9 percent)** — worst response rate in the index for
   the survey-collected half, routine carry-forward for 8 to 10 months of the
   year per office, and the private-insurance half now comes from a purchased
   claims file with a 3-month lag.
5. **Wireless telephone services (1.34 percent)** — since July 2025, no collected
   prices at all. A hedonic regression is re-estimated every month on a vendor's
   scrape of plan listings, and the index is built from *predicted* prices.
6. **Anything with hedonic quality adjustment** — the published price change is
   the observed change minus a regression's estimate of the value of changed
   features. By weight that is **about 32 percent of the CPI**, almost all of it
   shelter and apparel (Greenlees and McClelland 2008). See section 6.

Together, shelter alone is **35.6 percent** of the CPI-U, and the OER piece —
26.2 percent — is imputed from a different population than the one it describes.
That single fact is the most defensible "the index is more modeled than you
think" point available, and it does not require the disputed imputation
statistics.

### The honest version of the "modeled" argument

The strong claims are all available without exaggeration:

- 26.2 percent of the CPI is owners' equivalent rent, priced from renters.
- In 2025, 49.3 percent of eligible CPI housing units reported a rent.
- Overall quote collection fell from 81.8 percent (2016) to 69.5 percent (2025).
- Medical care collected 32.0 percent of eligible quotes in 2024.
- There was no October 2025 CPI at all.

The weak claims that will not survive a fact-check:

- "36 percent of CPI prices are imputed" — that is the different-cell share of
  imputed prices. See above.
- "Hedonics hide inflation" — BLS's own estimate is +0.005 pp a year, upward, and
  the biggest hedonic in the index (shelter age bias) adds at least 0.2 pp a year.
- "Rental equivalence was adopted to lower inflation" — it raised measured shelter
  inflation on introduction.
- "TV prices fell 98 percent because of hedonics" — BLS's hedonic estimate for TVs
  is 0.1 percent a year. The decline is real prices.
- "The CPI switched from list to transaction prices for hospitals in 1997" — it
  was partial, and BLS called it an "intensification."

---

## Source list

**BLS Handbook of Methods, chapter 17 (CPI)**
- Home: https://www.bls.gov/opub/hom/cpi/home.htm
- Concepts: https://www.bls.gov/opub/hom/cpi/concepts.htm
- Data sources: https://www.bls.gov/opub/hom/cpi/data.htm
- Design: https://www.bls.gov/opub/hom/cpi/design.htm
- Calculation: https://www.bls.gov/opub/hom/cpi/calculation.htm
- History: https://www.bls.gov/opub/hom/cpi/history.htm

**Factsheets** — index: https://www.bls.gov/cpi/factsheets/
- Rent and OER: https://www.bls.gov/cpi/factsheets/owners-equivalent-rent-and-rent.htm
- Motor fuel: https://www.bls.gov/cpi/factsheets/motor-fuel.htm
- Gasoline secondary source: https://www.bls.gov/cpi/factsheets/acm-gasoline.htm
- New vehicles: https://www.bls.gov/cpi/factsheets/new-vehicles.htm
- Used cars and trucks: https://www.bls.gov/cpi/factsheets/used-cars-and-trucks.htm
- Leased cars and trucks: https://www.bls.gov/cpi/factsheets/leased-cars-and-trucks.htm
- Medical care: https://www.bls.gov/cpi/factsheets/medical-care.htm
- Airline fares: https://www.bls.gov/cpi/factsheets/airline-fares.htm
- Wireless telephone service: https://www.bls.gov/cpi/factsheets/wireless-telephone-service.htm
- Personal computers: https://www.bls.gov/cpi/factsheets/personal-computers.htm
- Average prices: https://www.bls.gov/cpi/factsheets/average-prices.htm
- Common misconceptions: https://www.bls.gov/cpi/factsheets/common-misconceptions-about-cpi.htm

**Research series and tables**
- New Tenant Rent: https://www.bls.gov/pir/new-tenant-rent.htm
- R-CPI-NTR: https://www.bls.gov/cpi/research-series/r-cpi-ntr.htm
- NTR/ATR 2025 method update: https://www.bls.gov/pir/ntr/methodologyupdate2025.htm
- Imputation: https://www.bls.gov/cpi/tables/imputation.htm
- Response rates: https://www.bls.gov/cpi/tables/response-rates/

**Quality adjustment and hedonics**
- Current model list: https://www.bls.gov/cpi/quality-adjustment/
- Q&A: https://www.bls.gov/cpi/quality-adjustment/questions-and-answers.htm
- Techniques: https://www.bls.gov/cpi/quality-adjustment/hedonic-price-adjustment-techniques.htm
- Televisions model: https://www.bls.gov/cpi/quality-adjustment/televisions.htm
- Apparel models: `/mens-suits.htm` `/womens-dresses.htm` `/boys-shirts.htm` `/mens-underwear.htm`
- Liegey 2002 white paper (the dated adoption table):
  https://www.bls.gov/cpi/white-papers/hedonic-quality-adjustments-statistical-agency-perspective.pdf
- Greenlees and McClelland, MLR August 2008 (the 0.005 and 0.2 pp figures):
  https://www.bls.gov/opub/mlr/2008/08/art1full.pdf

**Method documentation pages**
- Health insurance improvements: https://www.bls.gov/cpi/additional-resources/improvements-cpi-health-insurance-index.htm
- Medical claims data: https://www.bls.gov/cpi/additional-resources/use-of-medical-claims-data-physicians-and-hospital-services.htm
- Wireless alternative data: https://www.bls.gov/cpi/additional-resources/alternative-data-wireless-telephone.htm
- 2025 shutdown Q&A: https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi.htm

**Older primary sources**
- Cardenas, "Revision of the CPI hospital services component," MLR Dec 1996:
  https://www.bls.gov/opub/mlr/1996/12/art6full.pdf
- Cardenas, "The CPI for hospital services: concepts and procedures," MLR Jul 1996:
  https://www.bls.gov/opub/mlr/1996/07/art4full.pdf
- Armknecht, Moulton and Stewart, BLS Working Paper 263, Feb 1995 (the January
  1995 generic-drug rule):
  https://www.bls.gov/osmr/research-papers/1995/pdf/ec950010.pdf
- Liegey, "Apparel price indexes: effects of hedonic adjustment," MLR May 1994
  (scanned image, no text layer): https://www.bls.gov/opub/mlr/1994/05/art6full.pdf
- Pharmaceutical industry CPI/PPI/IPP methodology (2011, mod. 2021):
  https://www.bls.gov/ppi/methodology-reports/the-pharmaceutical-industry-an-overview-of-cpi-ppi-and-ipp-methodology.pdf
- March 2017 CPI news release (the wireless drop):
  https://www.bls.gov/news.release/archives/cpi_04142017.htm

**Monthly Labor Review**
- Total-premium health insurance: https://www.bls.gov/opub/mlr/2024/article/measuring-total-premium-inflation-for-health-insurance-in-the-cpi.htm
- Assessing and improving CPI accuracy: https://www.bls.gov/opub/mlr/2024/article/assessing-and-improving-the-accuracy-of-the-cpi.htm
- Alternative data for high-tech products: https://www.bls.gov/opub/mlr/2024/article/alternative-data-sources-for-high-tech-products-in-the-cpi.htm
- COVID impacts on collection and missing data: https://www.bls.gov/opub/mlr/2025/article/impacts-of-covid-19-on-collection-and-missing-data-in-the-cpi.htm
- October 2025 housing counterfactual imputation: https://www.bls.gov/opub/mlr/2026/article/counterfactual-imputation-approaches-for-the-housing-component-of-the-october-2025-cpi.htm
- Medical care response rates: https://www.bls.gov/opub/mlr/2023/article/improving-response-rates-and-representativity-in-the-cpi-medical-care-index.htm
- Incorporating medical claims data (the backcast): https://www.bls.gov/opub/mlr/2023/article/incorporating-medical-claims-data-in-the-cpi.htm
- Residential telecom index improvements: https://www.bls.gov/opub/mlr/2023/article/improvements-to-the-cpi-index-series-for-residential-telecommunications-services.htm

**Outside**
- Konny, Williams and Friedman (all BLS), "Big Data in the U.S. Consumer Price
  Index: Experiences and Plans," 2019 — the scanner-data and CorpX source:
  https://www.nber.org/system/files/chapters/c14280/revisions/c14280.rev1.pdf
- Bosworth, Bieler, Kleinrock, Koepcke and Berndt, "An Evaluation of the CPI
  Indexes for Prescription Drugs," NBER WP 24210, Jan 2018:
  https://www.nber.org/system/files/working_papers/w24210/w24210.pdf
- Aizcorbe, Byrne and Sichel, "Getting Smart About Phones," FEDS WP 2019-012:
  https://www.federalreserve.gov/econres/feds/files/2019012pap.pdf
- FEDS Note, "Common and idiosyncratic inflation," 2020-03-05 (the 8 bp core PCE
  figure for March 2017):
  https://www.federalreserve.gov/econres/notes/feds-notes/common-and-idiosyncratic-inflation-20200305.html
- National Academies, *Modernizing the Consumer Price Index for the 21st
  Century* (2022, the CNSTAT panel behind the health insurance change):
  https://nap.nationalacademies.org/read/26485/
- Cleveland Fed WP 22-38, disentangling rent index differences:
  https://www.clevelandfed.org/publications/working-paper/2022/wp-2238-disentangling-rent-index-differences
- Brookings, how the CPI handles housing:
  https://www.brookings.edu/articles/how-does-the-consumer-price-index-account-for-the-cost-of-housing/
