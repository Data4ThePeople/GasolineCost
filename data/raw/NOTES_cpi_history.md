# CPI methodology: a background brief

Research notes for the gasoline-share-of-income post. Compiled 2026-09-23.
Primary sources are BLS unless noted. Every claim carries a document name and
a full URL. Items not confirmed from a primary source are marked
**[UNCONFIRMED]**.

**Access notes.** `bls.gov` serves WebFetch fine but blocks plain `curl` and
blocks the imputation history spreadsheet to non-browser requests.
`ssa.gov` and the HTML page for CRS IN12596 on `congress.gov` both returned
403; the CRS PDF mirror works. `federalregister.gov` redirects automated
fetches to an "unblock" page; the public-inspection PDF is readable.

**Three corrections to widely repeated claims** are set out in the box at the
end of section 4. Read those before writing anything about 2025 data quality.

---

## 1. Origins and the first index

### The wartime trigger

The CPI began as a cost-of-living measure built to settle wage disputes in
World War I shipyards. BLS: "rapid increases in prices, particularly in
shipbuilding centers, made a more comprehensive index essential for
calculating cost-of-living adjustments."
- *History*, BLS Handbook of Methods, CPI chapter.
  https://www.bls.gov/opub/hom/cpi/history.htm

Two separate requests drove it:

1. **1917, the Shipbuilding Labor Adjustment Board.** "The first wartime
   request for a study of the cost of living came in 1917 from the
   Shipbuilding Labor Adjustment Board, which was formed only shortly before
   the request, with the dual mission of informing itself of the cost of
   living in the many shipbuilding districts subject to its jurisdiction and
   tracking changes in the cost of living as time progressed." Commissioner
   Royal Meeker got $75,000 from President Wilson to survey **18 major
   shipbuilding centers**, fielded in early 1918. BLS itself calls this study
   inadequate: it still used 1901 expenditure weights and had no item
   specifications.
2. **The National War Labor Board** then funded a national survey: $300,000,
   rising to about $650,000 with defense supplements. It collected expenditure
   data from **12,000 families in 92 cities across 42 states** in **1917-19**,
   restricted to incomes of $900-$2,500. BLS: "This index represents the
   formal beginning of a regular, comprehensive national consumer price index
   program."

- *The first hundred years of the Consumer Price Index: a methodological and
  political history*, Monthly Labor Review, April 2014.
  https://www.bls.gov/opub/mlr/2014/article/the-first-hundred-years-of-the-consumer-price-index.htm
  (PDF: https://www.bls.gov/opub/mlr/2014/article/pdf/the-first-hundred-years-of-the-consumer-price-index.pdf)
- The Handbook uses "92 industrial centers" for the same survey.
  https://www.bls.gov/opub/hom/cpi/history.htm

Worth knowing for a journalism piece: the survey excluded "non-English
speaking families who have been less than five years in the United States,"
and although data were collected from Black families, only households where
white male wage earners and clerical workers supplied most of the income
entered the official index (MLR 2014).

### First publication: 1919, 32 cities

Where the 32 comes from, verbatim from MLR 2014: "the Bureau retroactively
used prices collected in retail establishments for December of each year from
1913 to 1917 in **19 industrial centers** and in an additional **13 cities**
for December of 1917. Regular retail price collection began after 1917 in all
**32 major industrial centers**. Depending on the article priced, pricing
occurred one to four times per year. ... the Bureau began **semiannual
publication of a retail price index in 1919**."

- *Chronology of changes in the Consumer Price Index*, BLS: "Began
  publication of separate indexes for 32 cities (1919)."
  https://www.bls.gov/cpi/additional-resources/historical-changes.htm

### First national index: 1921

"Began regular publication of a national index, the U.S. city average (1921):
Based index on an **unweighted average of the city indexes**; Estimated U.S.
city average back to **1913**." Washington, DC was added to the pricing
sample in 1921.
- https://www.bls.gov/cpi/additional-resources/historical-changes.htm

**Small source conflict, reconciled by BLS itself.** The chronology says the
1913 backcast used "food prices only"; MLR 2014 says it used wholesale price
movements. A Handbook footnote reconciles them: "Retail prices of food and
wholesale prices of other items were used to estimate price change from 1914
back to 1913."

### Original item structure and geographic scope

**Six major groups: food, clothing, rent, fuels, house furnishings, and
miscellaneous**, with "pricing limited to items selected in advance to
represent their categories."
- BLS Handbook of Methods, Chapter 17 (CPI), 2018 PDF, Exhibit 1.
  https://www.bls.gov/opub/hom/pdf/cpi-20180214.pdf

Geographic scope: urban wage-earner and clerical-worker families in the 32
surveyed industrial centers, priced in central cities only. The exact count of
individual priced items in 1919 is **[UNCONFIRMED]**; BLS Bulletin No. 1517,
*The Consumer Price Index: History and Techniques*, is the place to look
(https://fraser.stlouisfed.org/title/consumer-price-index-history-techniques-169/fulltext).

### The name changes

Not one event but five, all from Appendix 3 of the 2018 Handbook PDF
(https://www.bls.gov/opub/hom/pdf/cpi-20180214.pdf):

| Effective | Title |
|---|---|
| pre-1945 | "Indexes of the cost of living of wage earners and lower salaried workers in large cities" |
| **1945** | "Consumer's Price Index for Moderate Income Families in Large Cities" |
| **January 1953** | Short title **"Consumer Price Index"** becomes official |
| **January 1964** | "Consumer Price Index for Urban Wage Earners and Clerical Workers" |
| **January 1978** | Two indexes: CPI-W and CPI-U |

Why: the wartime Mitchell Committee and the President's Committee on the Cost
of Living found no methodological fault but recommended a name change "to
clarify any ambiguity or misunderstanding about what it actually measured."
Commissioner Hinrichs proposed the new name in July 1945; Secretary Frances
Perkins refused, and her successor Lewis Schwellenbach adopted it.

**Flag:** MLR 2014 dates the change to July 1945, Handbook Appendix 3 to
September 1945. Both are BLS. Safest phrasing: "in 1945, effective with the
September index."

### One early stress test worth citing

A 1935 reweighting by Margaret Hogg showed that using 1917-19 expenditure
weights for a 1913-based index biased the results. That helped motivate the
1934-36 expenditure survey (14,500 families, 42 cities) behind the 1940
revision. It is the earliest documented case of the weight-staleness problem
that annual weight updates are still chasing.
- MLR 2014, https://www.bls.gov/opub/mlr/2014/article/the-first-hundred-years-of-the-consumer-price-index.htm

---

## 2. How the modern structure was assembled

### The comprehensive revisions

BLS counts six comprehensive revisions since 1940, plus a 2018 geographic
revision and an announced 2028 one. Effective dates below are the **index
reference month**; the revised index normally published the following month,
with a six-month overlap against the old series.

Sources for this block: *Chronology of changes in the Consumer Price Index*,
https://www.bls.gov/cpi/additional-resources/historical-changes.htm ; 2018
Handbook PDF, Exhibit 1 and Appendix 3,
https://www.bls.gov/opub/hom/pdf/cpi-20180214.pdf ; *History*, Handbook of
Methods, https://www.bls.gov/opub/hom/cpi/history.htm

**1940 — first comprehensive revision** (published May 1941)
- Weights from the **1934-36** consumer expenditure study.
- Priced in the **34 largest cities**; the U.S. city average became a
  **weighted** average of cities, replacing the 1921 unweighted method.
- Acted on an American Statistical Association advisory committee.
- 1925-1940 recomputed retroactively with the new group weights.

**Interim, 1940-1953** (including the **January 1951** adjustment)
- WWII: BLS "discontinued the pricing of unavailable items, such as new cars
  and household appliances" and raised weights on substitutes. A linking
  method for item substitution was adopted in 1942.
- **January 1951** (published March 1951): reweighted seven cities from 1947
  and 1949 expenditure surveys; re-based population weights on the 1950
  census; **"Adjusted rent index to remove 'new unit bias' caused by rent
  control"** — corrected back to 1940; added frozen foods and televisions.
- The rent correction belongs to 1951, not 1953.

**1953 — second comprehensive revision** (effective January 1953)
- Weights from the **1950 Survey of Consumer Expenditures** (about 8,000
  urban families, 91 cities).
- Refined the target population to urban wage-earner and clerical-worker
  families.
- Added medium and small cities; coverage extended down to urban places of
  2,500+. Area count rose to **46**.
- Added restaurant meals. Homeowner costs moved to an **"asset" formulation**
  built from five homeownership costs, including mortgage interest. This is
  the approach that rental equivalence replaced in 1983.

**1964 — third comprehensive revision** (effective January 1964)
- Weights from **1960-61** expenditure patterns; 1960 census population
  weights; **50 areas**, rising to 56 in January 1966.
- **Added single-person households** to the target population.
- **Extended pricing to the suburbs** of sampled metro areas for the first
  time.
- Context: the **1961 Stigler Committee** (Price Statistics Review Committee)
  argued that a rigidly fixed basket cannot give "a realistic measure" in the
  presence of new products and quality change. BLS declined the
  constant-utility framing then, but the report drove later changes to outlet
  and item sampling and to quality adjustment.

**1978 — fourth comprehensive revision** (effective January 1978). The
structural break. Verbatim from the chronology:
- "Added a new Consumer Price Index: the **CPI for All Urban Consumers, or the
  CPI-U**"
- "Renamed the older CPI [as] the **CPI-W**"
- "Used weights from a **1972-1973** survey of consumer expenditures and the
  1970 census"
- "**Expanded the sample to 85 areas**" (up from 56)
- "Increased minimum pricing frequency from quarterly to bimonthly";
  "Implemented monthly pricing in five largest areas"
- "**Introduced probability sampling methods at all stages of CPI sampling**"
- "Introduced **checklists** that define each category of spending"
- "Developed estimates of the CPI's sampling error and optimal sample
  allocation"

**Interim, 1978-1987**
- **1981:** "Implemented new **Point-of-Purchase Survey (POPS)**; Selected
  retail outlets with **probability proportional to consumer spending**
  therein; Eliminated reliance on outdated secondary-source sampling frames;
  Began rotating outlet and item samples every 5 years."
- **January 1983 (CPI-U) / January 1985 (CPI-W):** rental equivalence. See
  section 3.

**1987 — fifth comprehensive revision** (effective January 1987)
- Weights from the **1982-84 Consumer Expenditure Survey** and the 1980
  census; **91 areas**.
- Redesigned the CPI housing survey; improved sampling, collection,
  processing and estimation.
- Appendix 3, footnote 28: item weights from the **Continuing POPS (CPOPS)**
  1985-89; **"first 'rolling revision'"** — the first revision phased in over
  several years rather than dropped in one month.

**1998 — sixth comprehensive revision** (effective January 1998)
- Weights from the **1993-95 Consumer Expenditure Survey** and the 1990
  census.
- **Extensively revised the item classification system.** The resulting
  four-level structure, in BLS's words: "The **eight major groups** are made
  up of **70 expenditure classes (ECs)**, which in turn are divided into
  **211 item strata**. ... Within each item stratum, one or more substrata,
  called **entry-level items (ELIs)**, are defined. ELIs are the ultimate
  sampling units for items."
- New geographic and housing samples, **87 PSUs**.
- **Computer-assisted data collection.**
- Added the **Telephone Point-of-Purchase Survey (TPOPS)**, which "allows
  rotation of outlet and item samples **by item category and geographic area,
  rather than by area alone**."
- Companion article: *Overview of the 1998 revision of the Consumer Price
  Index*, Greenlees and Mason, MLR December 1996.
  https://www.bls.gov/opub/mlr/1996/article/overview-of-the-1998-revision-of-the-consumer-price-index.htm
  (full text: https://www.bls.gov/opub/mlr/1996/12/art1full.pdf)

**2018 — geographic revision** (effective January 2018)
- The geographic sample's **first rotation since 1998**.
- PSUs cut from **87 to 75** — 23 self-representing (the 21 CBSAs above 2.5
  million plus Anchorage and Honolulu) and 52 non-self-representing.
- Based on the **2010 census**; PSUs now defined by OMB **Core Based
  Statistical Area** definitions; micropolitan areas brought into scope.
- Stratification moved from four census regions x three city-size classes to
  the **nine census divisions**.
- **Index areas cut from 38 to 32, reducing basic indexes from 8,018 to
  6,752** — done deliberately to raise the average number of quotes per
  item-area cell and cut finite-sample bias.
- Publication: nine census-division indexes added; region-by-city-size series
  discontinued; separate publication ended for Cincinnati, Cleveland,
  Milwaukee, Pittsburgh and Portland.
- *The 2018 revision of the Consumer Price Index geographic sample*, MLR
  October 2016.
  https://www.bls.gov/opub/mlr/2016/article/the-2018-revision-of-the-cpi-geographic-sample.htm

**2028 — announced geographic revision.** See section 4.

### The item-and-outlet sample design, and the POPS timeline

Probability sampling at every stage arrived with the **1978** revision. The
outlet frame has four eras:

| Period | Outlet frame source |
|---|---|
| before 1978 | secondary-source lists ("outdated secondary-source sampling frames") |
| **1974** | a one-off Point-of-Purchase Survey supplying item weights for the 1978 revision (2018 Handbook, Appendix 3, fn. 22: "Item weights based on Points of Purchase Survey in 1974") |
| **1981-** | **POPS / Continuing POPS (CPOPS)**, run by Census for BLS; outlets selected with probability proportional to reported consumer spending; 5-year rotation, one-fifth of areas per year (4-year from 2002) |
| **1998-** | **TPOPS**, quarterly CATI with random-digit dialing; rotation by item category as well as area |
| **October 2019** | **TPOPS ended.** The outlet frame moved to the **Consumer Expenditure Survey** (Diary for food, Interview for the rest), refined against the Quarterly Census of Employment and Wages |

CE-outlet transition dates: CE outlet-question testing began April 2016; full
CE implementation April 2019; TPOPS ended October 2019; CPI processing of CE
outlet data began February 2020; **first CE-sourced outlet samples used in
index calculation November 2021**; TPOPS-sourced samples fully rotated out by
**May 2025**.
- *Consumer Price Index outlet samples from the Consumer Expenditure Surveys*,
  MLR 2022. https://www.bls.gov/opub/mlr/2022/article/cpi-outlet-samples-from-the-ce.htm

The current Handbook states it plainly: "The outlets where prices are
collected are selected based on data from the CE survey."
- https://www.bls.gov/opub/hom/cpi/data.htm

**This resolves an apparent contradiction.** The Handbook *History* chapter
credits the 1978 revision with POPS; the *Chronology* puts POPS in the
1978-1987 improvements block. Both are right: a POPS was fielded in **1974**
to supply the 1978 revision's weights, and the **continuing** POPS as an
ongoing rotation vehicle began in **1981**.

### The Consumer Expenditure Survey as the weight source

- Before 1980 the CE ran roughly **every ten years**: 1901, 1917-19, 1934-36,
  1950, 1960-61, 1972-73.
- **1980: the CE became a continuous, ongoing survey**, with a quarterly
  Interview component and a two-week Diary component. BLS attributes the
  change to the 1970s oil shocks and 13%+ inflation in 1979-80 making
  decade-old weights untenable.
- Despite continuous collection from 1980, **CPI weights kept being replaced
  only at comprehensive revisions until January 2002**, when biennial updates
  began. Annual single-year updates began January 2023.
- *The Consumer Expenditure Survey: 30 years as a continuous survey*, BLS.
  https://www.bls.gov/cex/research_papers/pdf/the-consumer-expenditure-survey-30-years-as-a-continuous-survey.pdf

That 22-year gap between continuous collection and biennial use is a good
detail for the post: the data existed long before the index used it.

### Two-stage aggregation

Current Handbook, verbatim from the 2018 PDF: "The CPI is calculated in **two
stages**. The first stage is the calculation of **basic indexes**, which show
the average price change of the items within each of the 8,018 CPI item-area
combinations. ... The weights for the first stage come from the **sampling
frame** for the category in the area. At the **second stage**, aggregate
indexes are produced by averaging across subsets ... The weights for the
second stage are derived from reported **expenditures from the Consumer
Expenditure Survey (CE)**."

The current online version: "The first stage of the CPI is to calculate basic
indexes for each of the **7,776** item-area combinations that compose the CPI"
— **32 index areas x 243 basic items**.
- https://www.bls.gov/opub/hom/cpi/calculation.htm
- https://www.bls.gov/opub/hom/cpi/design.htm

The 243 exceeds the 211 item strata because health-insurance retained earnings
is computed at ELI rather than stratum level. That is a computational detail,
not a structural revision.

**[UNCONFIRMED] — the date two-stage aggregation was introduced.** No BLS
primary document I found dates it. The defensible statement is that the item
stratum x index area basic-index structure with probability sampling at every
stage dates to the **1978** revision, and the strata and area counts were
reset at each later revision (211 strata in 1998; 38 to 32 areas in 2018). Do
not assert a single year.

### The Laspeyres framing, with quotes

From the Handbook *Calculation* chapter
(https://www.bls.gov/opub/hom/cpi/calculation.htm), verbatim:
- "**A modified Laspeyres price index is used to aggregate basic indexes into
  published CPI-U and CPI-W indexes.**"
- "**The Laspeyres index uses estimated quantities from the predetermined
  expenditure reference period β to weight each basic item-area index.**"

From the 2018 Handbook PDF (https://www.bls.gov/opub/hom/pdf/cpi-20180214.pdf),
verbatim: "The CPI-U and the CPI-W use a **Laspeyres formula** to average the
price changes across categories of items. It is sometimes said that the
Laspeyres formula provides an 'upper bound' on the COLI index. ... Since 1999,
the CPI program has used the **geometric mean formula** to average price
change within most item categories." And: "**The other strata use the
Laspeyres formula average, which all strata used prior to 1999.**"

Which strata still use the Laspeyres form at the basic level: selected shelter
services (rent of primary residence, owners' equivalent rent, housing at
school excluding board), selected utilities and government fees, and selected
medical care services (prescription drugs, physicians' services, hospital
services, dental services, other medical professionals, nursing homes and
adult day care).
- https://www.bls.gov/opub/hom/cpi/calculation.htm

On the cost-of-living question, BLS's own words: "**The CPI frequently is
called a cost-of-living index, but it differs in important ways from a
complete cost-of-living measure**," and it "is sometimes termed a
**conditional cost-of-living index**."
- https://www.bls.gov/cpi/questions-and-answers.htm
- https://www.bls.gov/opub/hom/cpi/concepts.htm
- Fullest treatment: *Addressing misconceptions about the Consumer Price
  Index*, Greenlees and McClelland, MLR August 2008.
  https://www.bls.gov/opub/mlr/2008/article/addressing-misconceptions-about-the-consumer-price-index.htm
  (full text: https://www.bls.gov/opub/mlr/2008/08/art1full.pdf)

---

## 3. Major methodology changes since 1990

The single most useful primary list is the R-CPI-U-RS change table, which
records every change BLS could apply retroactively and the years it applied
it to.
- *Changes in CPI methodology* (R-CPI-U-RS).
  https://www.bls.gov/cpi/research-series/r-cpi-u-rs-changes.htm

### 1983 — rental equivalence for owner-occupied housing

Announced by Commissioner Janet Norwood on **October 27, 1981**. Effective
with **January 1983** data for the CPI-U and **January 1985** data for the
CPI-W. Before 1983 BLS measured homeowner costs largely through house prices
and mortgage interest; double-digit interest rates in the late 1970s made that
untenable. Rental equivalence imputes to owner-occupied units the rate of
change in rent observed for comparable rental units. Handbook Appendix 3:
"Changed homeowners' costs from asset approach to flow-of-service approach
(rental equivalence)."
- *Owners' Equivalent Rent and the Consumer Price Index: 30 Years and
  Counting*, BLS Beyond the Numbers, vol. 2.
  https://www.bls.gov/opub/btn/volume-2/pdf/owners-equivalent-rent-and-the-consumer-price-index-30-years-and-counting.pdf
- *Treatment of owner-occupied housing in the CPI*.
  https://www.bls.gov/cpi/additional-resources/treatment-owner-occupied-housing.htm
- R-CPI-U-RS entry: "Changed homeowners' component from cost of purchase to
  value of rental services," applied back to 1978-1982.

**Effect on measured inflation.** BLS does not publish a single headline
number. Its qualitative statement: differences between the R-CPI-U-RS and the
published CPI-U before 1999 are "substantial, reflecting major methodological
changes such as the switch to a rental equivalence approach for shelter in
1983 and the adoption of a geometric means formula in 1999," while "the
monthly percent change in the R-CPI-U-RS is very similar to the published
CPI-U for years after 2001."
- https://www.bls.gov/cpi/research-series/r-cpi-u-rs-home.htm

Adjacent housing changes from the R-CPI-U-RS table: **1985** new imputation
for rental vacancy price changes; **1988** adjustment for the aging of housing
units; **1995** shelter formula revised (6-month chained estimator replacing
the composite estimator) and improved estimation of homeowners' implicit rent.

### 1996 — the Boskin Commission

**Title:** *Toward a More Accurate Measure of the Cost of Living*, the final
report of the Advisory Commission to Study the Consumer Price Index. The
Senate Finance print is **S. Prt. 104-72**. **Date: December 4, 1996.**
Members: Michael J. Boskin (chair), Zvi Griliches, Robert J. Gordon, Dale W.
Jorgenson, Sherwin Rosen.
- https://www.finance.senate.gov/imo/media/doc/Prt104-72.pdf
  (The SSA mirror at https://www.ssa.gov/history/reports/boskinrpt.html 403s
  automated fetches but is the usual citation.)

**Headline finding:** the CPI overstated the cost of living by about **1.1
percentage points per year**, plausible range **0.8 to 1.6**, and about 1.3
points per year before 1996.

| Component | Estimated bias (pp/yr) |
|---|---|
| Upper-level substitution | 0.40 |
| Lower-level substitution / formula | 0.25 |
| Quality change | 0.20 |
| New products | 0.15 |
| New outlets | 0.10 |
| **Total** | **1.1** |

**What BLS did in response.** GAO catalogued **seven** methodological changes
between December 1996 and June 1999, plus three announced and not yet
implemented:

| Change | Effective | Quantified effect, per GAO |
|---|---|---|
| Hospital services pricing | January 1997 | not quantified |
| Personal computer prices (hedonic) | January 1998 | "lowered the rate of growth in the personal computer index by approximately 6.5 percent in 1998" |
| **Geometric mean estimator** | **January 1999** | "reduce the rate of growth of the CPI by approximately **0.2 percentage point per year**" |
| Television pricing (hedonic) | January 1999 | "would have lowered the rate of growth in the television index by approximately 0.1 percent per year" (Aug 1993-Aug 1997) |
| Utility refunds treatment | January 1999 | not quantified; no long-run effect |
| Pollution control measures | January 1999 | not quantified; raises the CPI |
| Housing estimation system revision | January 1999 | not quantified |

Announced but not yet implemented as of June 1999: item-based sample rotation;
reducing the age of expenditure weights; increasing weight-update frequency
(planned for 2002).

**GAO did not publish its own single bias estimate.** It polled four former
commission members, whose individual views of the remaining bias ranged from
**0.73 to 0.9 percentage points** per year, against the original 1.1.
- GAO, *Consumer Price Index: Update of Boskin Commission's Estimate of Bias*,
  **GAO/GGD-00-50**, February 2000.
  https://www.gao.gov/assets/ggd-00-50.pdf
  HTML mirror (this is the readable one):
  https://www.govinfo.gov/content/pkg/GAOREPORTS-GGD-00-50/html/GAOREPORTS-GGD-00-50.htm

Note for accuracy: the commonly repeated "0.65 percentage points residual
bias" figure does **not** appear as a GAO conclusion. Use the 0.73-0.9 range
and attribute it to the four former commissioners, not to GAO.

**[UNCONFIRMED]** — the "CPI Improvement Initiative launched in 1998, funded
at $2.1 million in year one" detail. It circulates in secondary summaries; I
did not find it in a BLS or GAO document.

### 1999 — geometric mean formula for lower-level aggregation

Effective with **January 1999** data. Applied to index categories covering
about **61 percent** of CPI-U consumer spending and **64 percent** of CPI-W
spending. BLS expected it to **reduce the annual rate of increase in the CPI
by about 0.2 percentage point per year**.
- *New CPI estimator expected to lower inflation rate by 0.2 percent*, The
  Economics Daily, BLS, March 1999.
  https://www.bls.gov/opub/ted/1999/Mar/wk4/art03.htm
- *Changes in the Formula for Calculating Basic Components of the CPI*, MLR,
  October 1998. https://www.bls.gov/mlr/1998/10/art1full.pdf

The intuition BLS uses: the arithmetic mean assumes households always buy the
same quantity of each item; the geometric mean assumes they spend the same
share on each item, so a 10 percent price rise implies a 10 percent quantity
fall. It captures substitution **within** an item-area cell only, not across
categories.

Sequencing note: BLS had already removed an upward "seasoning" bias in
**1995** (food at home) and extended the fix to **all commodities and
services in 1996**, per the R-CPI-U-RS table.

### Quality adjustment and hedonic regression

Hedonic regression estimates how much of a price change is attributable to
measurable changes in a product's characteristics, and removes that part.

| Year | Categories |
|---|---|
| 1988 | housing **[PARTIALLY UNCONFIRMED]** — from BLS research papers, not the chronology |
| **1991** | apparel (R-CPI-U-RS table) |
| **January 1998** | personal computers (R-CPI-U-RS table) |
| **1999** | televisions (R-CPI-U-RS table) |
| **2000** | audio equipment, video equipment, refrigerators and freezers, clothes washers and dryers, microwave ovens, college textbooks (R-CPI-U-RS table) |
| **1999-2000** | BLS's own summary line: "Expanded the use of hedonic regression in quality adjustment" |
| by 2018 | smartphones, residential telephone services, internet services, cable and satellite television **[PARTIALLY UNCONFIRMED]** |

- https://www.bls.gov/cpi/research-series/r-cpi-u-rs-changes.htm
- https://www.bls.gov/opub/hom/cpi/history.htm
- *A Review of Hedonic Price Adjustment Techniques for Products Experiencing
  Rapid and Complex Quality Change*, BLS.
  https://www.bls.gov/cpi/quality-adjustment/hedonic-price-adjustment-techniques.htm

Related non-hedonic quality changes from the R-CPI-U-RS table: **1987**
quality adjustment of used car prices after model changes; **1998** automobile
finance charges removed as out of scope; **1999** pollution control regulation
changes reclassified as price change; **2016** prescription drug index formula
changed to a Laspeyres approach.

### 2002 — the Chained CPI-U (C-CPI-U)

First published **August 2002**. Uses a **superlative Tornqvist formula** with
weights that move with actual monthly expenditure, so it captures substitution
**across** categories, which the CPI-U cannot. Published only for the U.S.
city average, using the **CPI-U population** — it is a formula difference, not
a population difference.
- *Introducing the Chained Consumer Price Index*.
  https://www.bls.gov/cpi/additional-resources/chained-cpi-introduction.htm
  (PDF: https://www.bls.gov/cpi/additional-resources/chained-cpi-introduction.pdf)

Three vintages of every month: **initial** (published with the CPI-U),
**interim** (the following February), **final** (14-25 months later, on actual
expenditure data). Practical consequence for journalism: today's C-CPI-U for
recent months is not the number that ends up in the historical record.

**Effect.** BLS's own simulation for 1990-2000 put the average difference
between a weight-updated CPI-U and the C-CPI-U at **0.32 percent per year**.
The often-quoted "0.25 to 0.3 percentage points per year since 2000" is a
secondary summary, not a BLS headline figure — **[PARTIALLY UNCONFIRMED]**.

### Weight updates: decennial, then biennial (2002), then annual (2023)

- **Before 2002:** weights were replaced only at comprehensive revisions,
  roughly every ten years.
- **January 2002:** **biennial** updates begin, from **1999-2000** CE data,
  using **two** calendar years. The CE sample was enlarged so two years would
  suffice. Outlet rotation moved from a 5-year to a 4-year cycle. R-CPI-U-RS
  entry: "Weight updates increased to every two years instead of approximately
  ten years."
- **January 2023:** **annual** updates using a **single** calendar year of CE
  data. Announced May 2022; Federal Register notice published **August 24,
  2022**; effective with January 2023 data released **February 10, 2023**. The
  first annual weights used **2021** CE data, replacing biennial weights based
  on 2019-2020.
  - *Updating Spending Weights Annually Based on a Single Calendar Year of
    Data*, 87 FR (Aug. 24, 2022).
    https://www.federalregister.gov/documents/2022/08/24/2022-17994/updating-spending-weights-annually-based-on-a-single-calendar-year-of-data
    (readable copy: https://public-inspection.federalregister.gov/2022-17994.pdf)
  - https://www.bls.gov/cpi/tables/relative-importance/weight-update-information-2023.htm
  - *Weight, wait up! Increasing the relevance of Consumer Price Index
    weights*, BLS blog, 2023.
    https://www.bls.gov/blog/2023/weight-wait-up-increasing-the-relevance-of-consumer-price-index-weights.htm

**Why:** it cuts the average lag between purchase and index use from **36
months to 24 months**. COVID-era swings in spending were the proximate
motivation.

**Effect on measured inflation:** BLS research covering 2002-2020 found the
CPI-U annual inflation rate "would have been lower by **0.031 percentage
points per year** during this period" under annual rather than biennial
weights. Small, and in the same direction as every other substitution fix.
- https://www.bls.gov/cpi/tables/relative-importance/weight-update-information-2023.htm

### Population definitions: CPI-U, CPI-W, C-CPI-U

- **CPI-W** is the original lineage: urban wage earners and clerical workers.
  Since 1978 it covers households where at least one member was employed 37+
  weeks in clerical, sales, service, laborer, construction and similar
  occupations, and it was broadened then "to include wage earners and clerical
  workers in the entire nonfarm parts of metropolitan areas." It excludes
  professional and salaried workers, part-time workers, the self-employed and
  the unemployed. **About 30 percent** of the U.S. population.
- **CPI-U** was created in the **1978** revision: all urban consumers, "over
  90 percent of the U.S. population," meaning all urban households in
  core-based statistical areas and in urban places of 10,000+ inhabitants. It
  excludes rural, farm, military and institutional populations.
- **C-CPI-U** uses the CPI-U population.

Sources: https://www.bls.gov/cpi/questions-and-answers.htm ;
https://www.bls.gov/cpi/additional-resources/historical-changes.htm

**No change to the population definitions since 1978** turned up in any
source. The 2018 geographic redesign changed which areas are sampled, not who
is in scope. BLS also publishes an experimental **CPI-E / R-CPI-E** for
Americans 62 and older, published back to 1982 starting in **2008**.

### 2018-2020s: alternative data (corporate, scanner, web-scraped)

BLS's one-line summary for **2020-2022**: "Expanded the use of third-party
data sources in the estimation of the CPI."
- https://www.bls.gov/opub/hom/cpi/history.htm

| Item | Source | Effective |
|---|---|---|
| Airline fares | U.S. DOT database | date not given on the page |
| Prescription drugs | large-volume data from a single firm | date not given |
| Used cars and trucks | J.D. Power Information Network | pre-2021 |
| **Gasoline** | secondary-source dataset replacing in-person and website collection | **June 2021** |
| **New vehicles** | J.D. Power transaction data | **April 2022** |
| **Physicians' and outpatient hospital services**, private-insurance portion | secondary-source medical claims data | **October 2024** data, announced 2024-11-13 |
| **Leased cars and trucks** | vendor transaction data | **April 2025** data, announced 2025-05-13 |
| **Wireless telephone services** | secondary-source data plus non-traditional index methods | **July 2025** data, announced 2025-08-12 |
| Televisions | national retailer API, three collections per month since Oct 2020 | research only as of Dec 2024 |

- *Data sources*, Handbook of Methods. https://www.bls.gov/opub/hom/cpi/data.htm
- *Recent and upcoming methodology changes: 2024*, 2024-11-13.
  https://www.bls.gov/cpi/notices/2024/methodology-changes-2024.htm
- *Recent and upcoming methodology changes: 2025*, 2025-12-18.
  https://www.bls.gov/cpi/notices/2025/methodology-changes-2025.htm
- Wireless detail:
  https://www.bls.gov/cpi/additional-resources/alternative-data-wireless-telephone.htm

**Gasoline matters most for our post.** Since June 2021 the CPI gasoline index
has not come from data collectors visiting stations; it comes from a secondary
dataset. Worth a sentence in the methodology note.

**Read the December 2024 MLR article carefully before citing it.** *Alternative
data sources for high-tech products in the CPI*, Craig Brown and Jeremy
Smucker, MLR December 2024,
https://www.bls.gov/opub/mlr/2024/article/alternative-data-sources-for-high-tech-products-in-the-cpi.htm
presents **research** indexes, not adopted ones, and says explicitly that
"nontraditional data have not directly replaced traditional data collection
for most of the CPI market basket" outside exceptions like gasoline and used
vehicles. Its research gaps are large: televisions, Jan 2021-June 2023, the
official index fell 15.3 percent while a two-stage hedonic model fell 19.5
percent; wireless services, Dec 2018-Dec 2022, the official index rose 4.8
percent while a one-stage hedonic model fell 11.6 percent.

### Other recent methodology items

- **January 2024 data** (announced 2024-02-13) — used cars and trucks: mileage
  adjustment switched from a single fixed mileage per make and model to a
  monthly average mileage based on vehicle age.
  https://www.bls.gov/cpi/notices/2024/methodology-changes-2024.htm
- **November 2025 data** (announced 2025-12-18) — long-term care insurance
  removed from the health insurance index, because standalone LTC plans no
  longer enroll and hybrid plans are out of CPI scope.
  https://www.bls.gov/cpi/notices/2025/methodology-changes-2025.htm

---

## 4. What changed in 2024-2026

### 2024

There was **no 2024 CPI collection reduction**. The real 2024 items:

| Announced | Effective | What |
|---|---|---|
| **2024-05-10** | after March 2024 data | three average price series discontinued. https://www.bls.gov/cpi/notices/2024/ap-publication-changes.htm |
| **2024-05-15** | n/a | CPI and Real Earnings files went public about 30 minutes early on 2024-05-15; OMB and DOL OIG notified. https://www.bls.gov/cpi/notices/2024/early-data-release-05152024.htm |
| **2024-07-11** | June 2024 data | the June 2024 **new vehicles** index was estimated "with fewer observed transaction prices than in previous months" because of the CDK software outage affecting auto dealers. The index still met publication criteria. https://www.bls.gov/cpi/notices/2024/june-2024-new-vehicles.htm |
| **2024-11-13** | **2025-02-12**, with January 2025 data | five CPI indexes and two average-price series discontinued **for all metro areas, census divisions and region/size classes**, kept at the national level only: electricity; utility (piped) gas; energy services; fuels and utilities; household energy. AP series dropped: electricity per KWH, utility (piped) gas per therm. "Pet food" renamed "pet food and treats." https://www.bls.gov/cpi/notices/2024/publication-changes.htm |
| **2024-11-13** | October 2024 data | medical claims data for physicians' and outpatient hospital services (see section 3) |

Note for the gasoline post: the sub-national energy indexes were cut in
February 2025. If you want a metro-level energy or motor-fuel series after
that date, check availability before planning a chart.

### 2025 — collection reductions and suspended areas

**Early June 2025 — *Notice of CPI collection reductions*.** BLS: "In April,
BLS suspended CPI data collection entirely in **Lincoln, NE**, and **Provo,
UT**. In June, BLS suspended collection entirely in **Buffalo, NY**." And:
"BLS makes reductions when current resources can no longer support the
collection effort." BLS said the actions "have minimal impact on the overall
all-items CPI-U and CPI-W indexes" but may "increase the volatility of
subnational or item-specific indexes," and that "the number of imputed items
increased in April due to these actions." Both the Commodities and Services
survey and the Housing survey were affected.
- https://www.bls.gov/cpi/notices/2025/collection-reduction.htm

**Date caveat.** The BLS page is dated **June 16, 2025** and carries a
correction ("We have amended this notice to reflect an error found in the CPI
response rate for April"). DOL's own letter to Sen. Ruben Gallego, signed by
Acting Assistant Secretary Tim Cummings and dated **July 31, 2025**, refers to
"its announcement on **June 4, 2025**." Press coverage began June 4-5.
Safest phrasing: "announced in early June 2025; the BLS notice now carries a
June 16, 2025 date after a correction."
- https://www.gallego.senate.gov/wp-content/uploads/2025/08/Sen.-Gallego-Response-June-10-2025.pdf

**July 29, 2025 — *More information on CPI collection reductions*.** BLS added
that "**roughly 15 percent of the sample in the other 72 areas also was
suspended from collection, on average**." BLS simulated the suspensions back
to 2018: over **January 2019 to May 2025**, simulated 12-month percent changes
"differed from the published CPI for all urban consumers (CPI-U) estimates by
**less than 1/100th of a percentage point on average**," matching the official
CPI-U in **52 of 77 months**, running 0.1 pp higher in 14 and 0.1 pp lower in
11. BLS explicitly did **not** measure the impact on subnational or item-level
indexes. No commitment to resume: "BLS will continue to evaluate survey
operations and efficiently assign available resources to data collection."
- https://www.bls.gov/cpi/notices/2025/more-information-collection-reduction.htm

From the DOL letter (primary, 2025-07-31): "Starting in April, BLS suspended
CPI data collection in **3 of the 75 cities** it regularly covers." Prices
still came from "about **23,000** retail and service establishments," rents
from "about **40,000** landlords or tenants nationally." BLS field data
collection employees "were not eligible for the second deferred resignation
program."

**Cause.** BLS's own notices say "resources" and do not name the federal
hiring freeze. The hiring-freeze attribution is **secondary** (press and CRS
context), and CRS adds that "according to BLS, these reductions are meant to
be temporary." **[UNCONFIRMED]** in BLS's own words.
- CRS Insight **IN12596**, *The Consumer Price Index: Data Quality*, Lida R.
  Weinstock, **August 18, 2025**.
  https://www.congress.gov/crs_external_products/IN/PDF/IN12596/IN12596.1.pdf
  (the congress.gov HTML page 403s; the PDF works)

**[UNCONFIRMED]** — whether Lincoln, Provo and Buffalo collection has been
restored as of 2026-09-23. No BLS notice announces restoration.

### 2025 — imputation, stated correctly

**Primary source:** *Imputation*, BLS CPI,
https://www.bls.gov/cpi/tables/imputation.htm (last modified 2026-09-11).
Published since 2019.

BLS's definitions:
- **Home cell imputation** "uses the average change in price observed for
  sampled products or services in the same category and same location as the
  missing product's price."
- **Different cell imputation** keeps the item category and widens the
  geography — BLS's own example is using observed price changes for bread in a
  different region.

**The tables show the mix of imputation methods among prices that were
already imputed. They are not the share of all CPI prices that are imputed.**
BLS says so on the page: "**They do not represent an overall imputation rate
for each survey.**" The three columns sum to 100.

Table 1, imputation source for the commodities and services price survey,
percent (https://www.bls.gov/cpi/tables/imputation-cs-data.htm; the live page
shows a rolling 13 months):

| Month | Home cell | Different cell | Carry forward |
|---|---|---|---|
| Aug 2025 | 64 | 36 | 0 |
| Sep 2025 | 60 | 40 | 0 |
| Oct 2025 | n/a | n/a | n/a |
| Nov 2025 | 66 | 34 | 0 |
| Dec 2025 | 60 | 40 | 0 |
| Jan 2026 | 62 | 38 | 0 |
| Feb 2026 | 60 | 40 | 0 |
| Mar 2026 | 61 | 39 | 0 |
| Apr 2026 | 60 | 40 | 0 |
| May 2026 | 63 | 37 | 0 |
| Jun 2026 | 61 | 39 | 0 |
| Jul 2026 | 63 | 37 | 0 |
| Aug 2026 | 62 | 38 | 0 |

Footnote: "The Oct 2025 data values are not available due to the 2025 lapse in
appropriations." A companion housing table
(https://www.bls.gov/cpi/tables/imputation-housing-data.htm) splits into
"non-interview" and "vacancy"; August 2025 was 92 / 8.

Earlier monthly values are **[UNCONFIRMED]** against BLS directly, because the
full history file
(https://www.bls.gov/cpi/tables/imputation-source-201901-present.xlsx) is
download-blocked to non-browser requests. Secondary values in circulation:
February 2025 = 9 percent different-cell; April 2025 = 29 percent; July 2025 =
32 percent; August 2025 = 36 percent, "the highest in data back to 2019."
Bloomberg's August figure matches the BLS table exactly, which is good
evidence it is the same series.
- Bloomberg, *BLS Leans More on Second-Best Option for Filling in CPI Blanks*,
  2025-09-11.
  https://www.bloomberg.com/news/articles/2025-09-11/bls-leans-more-on-second-best-option-for-filling-in-cpi-blanks

Background: *Impacts of COVID-19 on collection and missing data in the CPI*,
MLR 2025.
https://www.bls.gov/opub/mlr/2025/article/impacts-of-covid-19-on-collection-and-missing-data-in-the-cpi.htm

### 2025 — the cancelled October CPI

**Primary:** *Revised news release dates following the 2025 and 2026 lapses in
appropriations*, last modified 2026-02-12.
https://www.bls.gov/bls/2025-lapse-revised-release-dates.htm

| Release | Reference period | Previously scheduled | Revised |
|---|---|---|---|
| CPI | October 2025 | Thursday, November 13, 2025 | **Canceled** |
| CPI | November 2025 | Wednesday, December 10, 2025 | **Thursday, December 18, 2025** |
| CPI | December 2025 | Tuesday, January 13, 2026 | no change |

BLS: it "**did not publish an all items or an all items less food and energy
estimate for October 2025**"; it "could not collect October 2025 reference
period survey data due to a lapse in appropriations" and "is unable to
retroactively collect these data." For a few indexes built from non-survey
sources, BLS retroactively acquired most October data and published those
October values with the November release.

**Collection window lost: "BLS did not collect CPI data from October 1, 2025,
through November 12, 2025"** — 43 days.
- https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi.htm
- Notice pointing to it, 2025-12-17:
  https://www.bls.gov/cpi/notices/2025/2025-federal-government-shutdown-impact-on-cpi.htm

**September 2025 CPI was published late, specifically so Social Security could
run.** BLS moved it from October 15 to **Friday, October 24, 2025**, saying:
"**This release allows the Social Security Administration to meet statutory
deadlines necessary to ensure the accurate and timely payment of benefits.**"
- *September 2025 CPI Release Rescheduled*, posted 2025-10-10.
  https://www.bls.gov/bls/092025-cpi-reschedule-notice.htm
- The release itself, USDL-25-1502, 2025-10-24:
  https://www.bls.gov/news.release/archives/cpi_10242025.htm — "Note that
  September CPI data collection was completed before the lapse in
  appropriations." September 2025: +0.3 percent seasonally adjusted month over
  month, +3.0 percent over 12 months.

**How BLS handled the missing month**, from the shutdown FAQ
(https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm):
- **October 2025**: the hierarchical imputation algorithm "resolved to the
  carry-forward method for all survey samples." Commodities and services
  prices were carried forward from **September 2025**; rents were carried
  forward from **April 2025**, leaving rent and owners' equivalent rent
  unchanged for October. BLS rejected trend-adjusted forecasts, interpolation
  and econometric models, citing time constraints and a refusal to manipulate
  the data "unscientifically."
- **November 2025**: collection resumed **November 14, 2025** (the shutdown
  ended November 12). November indexes compared collected November prices
  against the **imputed** October prices. The November release carried no
  1-month percent changes where October data were missing.
- **2025 annual averages**: most series are the average of **11** published
  values, excluding October; bimonthly "even" series the average of **5**;
  bimonthly "odd" series normally, from all 12.
- **Seasonal adjustment**: BLS approximated the missing October value as the
  **geometric mean of the September and November** index values; two series
  also missing November used the geometric mean of September and December.

The December 2025 news release (**January 13, 2026**) states flatly: "The Oct
and Nov 2025 data values are not available due to the 2025 lapse in
appropriations."
- https://www.bls.gov/news.release/archives/cpi_01132026.htm

**The housing distortion is quantified, and it is the most citable number in
this whole episode.** Mark Bowman and Craig Brown, *Counterfactual imputation
approaches for the housing component of the October 2025 CPI*, MLR,
**2026-05-12**:
https://www.bls.gov/opub/mlr/2026/article/counterfactual-imputation-approaches-for-the-housing-component-of-the-october-2025-cpi.htm
BLS tested four alternatives to carry-forward (backcast, interpolate,
forecast, categorical average). Against the published carry-forward result,
October 2025 one-month changes would have been:
- **Rent: 0.24 to 0.53 percent higher**
- **Owners' equivalent rent: 0.27 to 0.59 percent higher**

All approaches converge back to the published levels by **April 2026**, when
the April/October rent panel was resurveyed. So the distortion also touched
the April 2026 rent and OER indexes.

Other knock-ons:
- Research rent series paused: *Changes to R-CPI-NTR and R-CPI-ATR publication
  schedule*, 2026-01-27. The 2025 Q3 release was deferred and the series moved
  to a one-quarter lag.
  https://www.bls.gov/cpi/notices/2026/r-cpi-ntr-and-r-cpi-atr-publication-schedule.htm
- Treasury invoked its TIPS index contingency provisions.
  https://home.treasury.gov/news/press-releases/sb0324

**Social Security COLA.** The 2026 COLA was **2.8 percent**, announced
**October 24, 2025**, computed normally from third-quarter (July-September)
CPI-W because September data were collected before the shutdown. The missing
October CPI did not affect it; the only effect was a nine-day delay in the
announcement. **[UNCONFIRMED]** — ssa.gov returns 403 to automated fetches, so
this rests on press reporting plus the BLS rescheduling notice quoted above.
Verify at https://www.ssa.gov/cola/ before publishing the 2.8 figure.

### 2025 — leadership and oversight

Facts only, no commentary.

| Date | Event | Source |
|---|---|---|
| **2025-08-01** | Commissioner **Erika McEntarfer** removed by the President, the same day BLS reported July payrolls up 73,000 with May and June revised down by a combined 258,000. | Washington Post 2025-08-01 https://www.washingtonpost.com/business/2025/08/01/trump-fires-bls-chief/ ; CNBC https://www.cnbc.com/2025/08/01/trump-erika-mcentarfer-jobs-report-fired.html . Also referenced in CRS IN12596 (2025-08-18). |
| **Aug 2025 - Aug 2026** | Deputy Commissioner **William J. Wiatrowski** served as Acting Commissioner. BLS's own bio page: he "served as Acting Commissioner from January 2017 to March 2019, March 2023 to January 2024, and **August 2025 to August 2026**." | **Primary:** https://www.bls.gov/bls/senior_staff/wiatrowski.htm (last modified 2026-08-11) |
| autumn 2025 | E.J. Antoni nominated, then withdrawn. **[UNCONFIRMED]** — exact dates not pinned down. | press |
| **2026-01-30** | **Brett Matsumoto** nominated. **[UNCONFIRMED]**, press only. | |
| **2026-08-07** | Senate confirmed Matsumoto, 51-47. **[UNCONFIRMED]**, press only. | |
| **2026-08-11** | Matsumoto sworn in as the 17th Commissioner. Corroborated indirectly by the BLS bio page's "August 2026" end date for the acting term. | |

**No CPI program change is attributable to the leadership change**, and I
would not assert one.

Oversight documents, both primary:
- **GAO-26-107538**, *Federal Statistics: Stakeholders Said Jobs Report
  Generally Meets Their Needs, but Opportunities Exist to Improve Data
  Quality*, released **2026-06-02**. Notes funding constraints, staffing
  reductions and 2025 shutdown delays slowing modernization. **This is about
  the jobs report, not the CPI.** https://www.gao.gov/assets/gao-26-107538.pdf
- **DOL OIG 17-26-001-11-001**, *BLS Reduced Risk of Improper Disclosure of
  Essential Economic Information Yet Additional Improvements Are Needed*, June
  2026. Covers three 2024 incidents including the May 2024 early CPI release.
  https://oig.dol.gov/public/reports/oa/2026/17-26-001-11-001.pdf

### 2026 — what actually changed

**A second, short shutdown.** A lapse in appropriations began **January 31,
2026** and ended in early February. Five BLS releases slipped by two to five
days; the **January 2026 CPI moved from Wednesday February 11 to Friday
February 13, 2026**. **No CPI month was lost** this time.
- https://www.bls.gov/bls/2025-lapse-revised-release-dates.htm (retitled
  "Revised news release dates following the 2025 and 2026 lapses in
  appropriations")
- The shutdown's start and end dates are **[UNCONFIRMED]** from a primary
  source; press puts reopening on the afternoon of Tuesday, February 3, 2026.

| Announced | Effective | Change |
|---|---|---|
| **2026-01-12/13** | **2026-02-11**, with January 2026 data | Three title changes: "care of invalids and elderly at home" becomes **"home health care"**; "technical and business school tuition and fees" becomes **"technical and vocational school tuition and fixed fees"**; "housing at school, excluding board" becomes **"lodging while at school."** https://www.bls.gov/cpi/notices/2025/publication-changes-2026.htm |
| same | after the December 2025 data release | **CPI compressed tape format files discontinued** for the CU, CW, AP and SU surveys. Historical data stay in the standard time-series downloads. This is a file format, not index series. |
| **2026-02-06** | **2026-02-13** | Updated seasonal factors. For January 2026, **57 series** adjusted using intervention analysis (selected food and beverage items, motor fuels, vehicles). Revised seasonal factors and seasonally adjusted indexes recalculated for **2021 to 2025**. For 2026, 36 of the 81 components of the U.S. city average all-items index are not seasonally adjusted. https://www.bls.gov/cpi/notices/2026/seasonal-adjustment.htm |
| — | **January 2026** data | **Annual weight update** to **2024** CE data. See section 5; confirmed primary from the relative importance table header. |
| **2026-05-12** | with **April 2026** data | **Rebasing to December 2024 = 100** for: elementary and high school tuition and fees; information technology hardware and services; telephone hardware, calculators and other consumer information items; tobacco and smoking products; hospital and related services; televisions; other video equipment; tuition, other school fees and childcare — at U.S. city average, all four regions, and named metros. Indexes recalculated back to inception. https://www.bls.gov/cpi/notices/2026/rebasing.htm ; list at https://www.bls.gov/cpi/additional-resources/rebased-series.htm |
| **2026-07-27** | **January 2028** indexes, published **February 2028** | **2028 geographic revision.** New geographic sample from the **2020 decennial census**, adding **14 new non-self-representing PSUs** in three waves. First wave of six in 2028: **Chambersburg PA, Green Bay WI, Indianapolis IN, Pittsfield MA, Punta Gorda FL, Sacramento CA**; the other eight in 2029-2030. Fourteen current areas will be discontinued and county definitions elsewhere may change. https://www.bls.gov/cpi/notices/2026/geographic-revision.htm |
| 2026-03-19, 2026-07-23 | — | Two electricity index corrections. https://www.bls.gov/cpi/notices/2026/ |

**As of 2026-09-23 BLS has not posted a "Recent and upcoming methodology
changes: 2026" notice.** The index at
https://www.bls.gov/cpi/additional-resources/recent-upcoming-methodology-changes.htm
runs 2017 through 2025 only. No new alternative-data adoption has been
announced for 2026.

CPI releases have run on schedule since February. The most recent is **August
2026 data, released 2026-09-11** (USDL-26-1496): +0.4 percent seasonally
adjusted month over month, +3.4 percent over 12 months. September 2026 CPI is
scheduled for 2026-10-14.
- https://www.bls.gov/news.release/cpi.htm

**Reorganization: proposed, not enacted.** The FY2026 President's Budget
proposed cutting BLS budget and staffing by roughly 8 percent and moving BLS
from Labor to Commerce. The enacted appropriation did not include the move;
**BLS remains in the Department of Labor**. **[UNCONFIRMED]** against the
enacted law text — check govinfo before asserting it. CRS R48643,
https://www.congress.gov/crs-product/R48643 ; P.L. 119-74 signed 2026-01-23,
https://www.congress.gov/bill/119th-congress/house-bill/6938

### Sample size drift

BLS's own numbers are not internally consistent across pages. Use the monthly
technical note as the current figure.

| Source | Figure |
|---|---|
| Monthly news release technical note (Sep 2026) | "about **6,000 housing units** and approximately **22,000 retail establishments**" in **75 urban areas** |
| Handbook, *Design* | "about 6,000 housing units and approximately **23,000** retail establishments" |
| Handbook, *Overview* (mod. 2025-01-30) | "about **94,000 prices** and **8,000 rental housing units** quotes each month" |
| Handbook, *Data sources* | Commodities and Services survey collects "approximately **100,000 prices** monthly"; Housing survey "about 8,000 rental housing quotes monthly"; "approximately two-thirds of price collection in the CPI is done by personal visits" |
| DOL letter, July 2025 | "about 23,000 retail and service establishments"; rents from "about 40,000 landlords or tenants nationally" |

Sources: https://www.bls.gov/news.release/cpi.nr0.htm ;
https://www.bls.gov/opub/hom/cpi/design.htm ;
https://www.bls.gov/opub/hom/cpi/home.htm ;
https://www.bls.gov/opub/hom/cpi/data.htm

---

> ### Three corrections to claims in wide circulation
>
> **1. "40 percent of CPI prices are imputed" is wrong.** The BLS table gives
> the *mix of imputation methods among prices that were already imputed*, and
> BLS states on the page: "They do not represent an overall imputation rate
> for each survey." The correct sentence is: "of the prices BLS had to
> impute, about 40 percent were imputed from a different cell." Claims that
> "half the CPI is imputed" conflate the two denominators.
>
> **2. The ~350 discontinued indexes were Producer Price Indexes, not CPI.**
> Announced 2025-07-30, phased August 2025 through February 2026, about 350 of
> roughly 10,000 PPIs, under 1 percent of the PPI.
> https://www.bls.gov/ppi/notices/2025/bls-to-discontinue-selected-ppis.htm
> BLS's *Discontinued CPI and AP Series* page lists **no CPI series
> discontinued in 2025 or 2026**; the most recent are the five energy indexes
> and two average-price series announced in November 2024 and effective
> February 2025.
> https://www.bls.gov/cpi/additional-resources/discontinued-series.htm
>
> **3. There was no June 2024 CPI collection reduction.** The collection
> reduction was **June 2025**. The 2024 event often blended into it is the
> 2024-11-13 notice discontinuing sub-national energy indexes effective
> 2025-02-12.

---

## 5. How weights are set now

**Schedule.** Annual, since January 2023. Each January release brings a new
weight year: "Each year with the January CPI release the expenditure reference
period is updated to use the most recent Consumer Expenditure data."
- *Calculation*, Handbook of Methods. https://www.bls.gov/opub/hom/cpi/calculation.htm

**Which CE year feeds the current weights: a two-year lag.** The weights in
force through calendar **2026** come from **2024** Consumer Expenditure Survey
data. Primary confirmation is the relative importance table header itself:
"Table 1 (**2024 Weights**). Relative importance of components in the Consumer
Price Indexes: U.S. city average, **December 2025**."
- https://www.bls.gov/cpi/tables/relative-importance/2025.htm

| CPI calendar year | CE weight year | RI table as of |
|---|---|---|
| 2023 | 2021 | December 2022 |
| 2024 | 2022 | December 2023 |
| 2025 | 2023 | December 2024 |
| **2026** | **2024** | **December 2025** |
| 2027 (scheduled Feb 2027) | 2025, with the shutdown gap patched | December 2026 |

**Which indexes use them.** CPI-U, CPI-W, the initial and interim C-CPI-U, the
R-CPI-E and the CPI research series.
- https://www.bls.gov/cpi/tables/relative-importance/weight-update-information-2023.htm

**How relative importance moves between updates.** It is not frozen. Relative
importance is a component's "expenditure or value weight expressed as a
percentage of all items within an area," and between annual updates BLS
**price-updates** it: multiply the prior relative importance by the ratio of
the current index level to the prior index level, then normalize so all items
equals 100. **Quantities are held fixed; only prices move.**
- *Relative Importance and Weight Information for the Consumer Price Indexes*.
  https://www.bls.gov/cpi/tables/relative-importance/home.htm

This is exactly why gasoline's relative importance rises when gasoline prices
rise, with no change in how much anyone drove. It is the single most important
thing to explain in the post if we use relative importance at all.

**Cost weights.** BLS also publishes additive **cost weights** — estimated
spending totals at a given month's prices — back to December 2011, released in
January alongside each weight update, with the caveat that "Release of this
data may be delayed due to resource availability and other constraints."
- https://www.bls.gov/cpi/tables/relative-importance/cost-weights.htm

### The unresolved 2027 weight problem

The 2025 shutdown also cost BLS the **October and November 2025 Consumer
Expenditure** data. Those feed the 2025 consumer spending estimates that
become the **CPI-U and CPI-W weights introduced with the January 2027
indexes**, plus C-CPI-U monthly weights for July-December 2025.

- Background paper, revised **2026-06-30**: *Handling missing 2025 CE data*,
  https://www.bls.gov/cpi/additional-resources/handling-missing-2025-CE-data.htm
  Three options considered: weight adjustments, unit-level modeling, domain
  estimation. That revision says "these findings are not intended to
  presuppose a preferred approach."
- The shutdown Q&A page says BLS "selected the **survey weight adjustment
  factor approach** to prioritize the timely release of planned publications,"
  and describes it concretely: in the CE **Interview** Survey BLS "adjusted
  the 1/3 fewer expenditures in July and October 2025 by 3 and the 2/3 fewer
  expenditures in August and September 2025 by 3/2"; in the **Diary** Survey it
  used "October weights as a copy of September weights, and November weights
  as a copy of December weights."
  https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm
- **These two BLS pages appear to conflict** on whether a method has been
  chosen. The Q&A reads as the later, decided position; the June 30 paper as
  pre-decision background. Confirm which is current before writing about it.
- Expert panels: **NABE and CNSTAT, May 7-8, 2026**, open to the public.
  Notice posted 2026-04-28.
  https://www.bls.gov/cpi/notices/2026/missing-ce-data-panels.htm
- Published dates: final C-CPI-U for Jul-Sep 2025 on 2026-08-12; 2025 consumer
  spending on **2026-10-29**; final C-CPI-U for Oct-Dec 2025 on 2026-11-10;
  CPI-U/CPI-W weight update **February 2027**.
- Also: *Addressing missing consumer expenditure data due to the 2025 lapse in
  appropriations*, MLR 2026.
  https://www.bls.gov/opub/mlr/2026/article/addressing-missing-consumer-expenditure-data-due-to-the-2025-lapse-in-appropriations.htm

### What this means for the gasoline post

1. The December 2025 relative importance table (2024 weights) is the right
   weight source for anything about CPI-implied gasoline shares in 2026.
2. Any 2026 relative importance figure is a price-updated version of a **2024**
   spending pattern, not a measurement of 2026 spending.
3. The CPI gasoline index has come from a secondary dataset, not from field
   collection, since **June 2021**.
4. Sub-national energy indexes were discontinued effective **February 2025**,
   so metro-level energy series stop there.
5. October 2025 has no CPI value. Any 12-month or month-over-month series
   spanning it needs a note.

---

## Open items

1. **[Resolved]** The CE year behind the January 2026 weight update: 2024,
   confirmed by the relative importance table header.
2. **[Resolved]** The 2026 Social Security COLA: 2.8 percent, based on Q3 2025
   CPI-W, unaffected by the missing October. Still verify at ssa.gov, which
   403s automated fetches.
3. **[Resolved]** POPS dating: 1974 one-off for the 1978 revision; continuing
   POPS from 1981.
4. Still open: the item count in the 1919 index — see BLS Bulletin No. 1517 on
   FRASER.
5. Still open: the date two-stage aggregation was introduced. No BLS document
   dates it.
6. Still open: whether Lincoln, Provo and Buffalo collection resumed.
7. Still open: monthly different-cell imputation values before August 2025;
   the BLS history spreadsheet is download-blocked.
8. Still open: whether the June 30, 2026 CE paper or the shutdown Q&A reflects
   BLS's final method for the 2027 weights.

## Master source list

- Handbook of Methods, Chapter 17 (CPI): https://www.bls.gov/opub/hom/cpi/
  — History https://www.bls.gov/opub/hom/cpi/history.htm
  | Concepts https://www.bls.gov/opub/hom/cpi/concepts.htm
  | Data sources https://www.bls.gov/opub/hom/cpi/data.htm
  | Design https://www.bls.gov/opub/hom/cpi/design.htm
  | Calculation https://www.bls.gov/opub/hom/cpi/calculation.htm
- 2018 Handbook chapter 17 PDF (Exhibit 1 chronology, Appendix 3
  characteristics table): https://www.bls.gov/opub/hom/pdf/cpi-20180214.pdf
- Chronology of changes in the CPI:
  https://www.bls.gov/cpi/additional-resources/historical-changes.htm
- R-CPI-U-RS methodology changes:
  https://www.bls.gov/cpi/research-series/r-cpi-u-rs-changes.htm
- CPI questions and answers: https://www.bls.gov/cpi/questions-and-answers.htm
- CPI notices index: https://www.bls.gov/cpi/notices/
- Imputation tables: https://www.bls.gov/cpi/tables/imputation.htm
- Relative importance and weights:
  https://www.bls.gov/cpi/tables/relative-importance/home.htm
- MLR, *The first hundred years of the Consumer Price Index* (2014):
  https://www.bls.gov/opub/mlr/2014/article/the-first-hundred-years-of-the-consumer-price-index.htm
- MLR, *Addressing misconceptions about the Consumer Price Index* (2008):
  https://www.bls.gov/opub/mlr/2008/article/addressing-misconceptions-about-the-consumer-price-index.htm
- MLR, *Overview of the 1998 revision of the CPI* (1996):
  https://www.bls.gov/opub/mlr/1996/article/overview-of-the-1998-revision-of-the-consumer-price-index.htm
- MLR, *The 2018 revision of the CPI geographic sample* (2016):
  https://www.bls.gov/opub/mlr/2016/article/the-2018-revision-of-the-cpi-geographic-sample.htm
- MLR, *CPI outlet samples from the Consumer Expenditure Surveys* (2022):
  https://www.bls.gov/opub/mlr/2022/article/cpi-outlet-samples-from-the-ce.htm
- MLR, *Alternative data sources for high-tech products in the CPI* (2024):
  https://www.bls.gov/opub/mlr/2024/article/alternative-data-sources-for-high-tech-products-in-the-cpi.htm
- MLR, *Counterfactual imputation approaches for the housing component of the
  October 2025 CPI* (2026):
  https://www.bls.gov/opub/mlr/2026/article/counterfactual-imputation-approaches-for-the-housing-component-of-the-october-2025-cpi.htm
- Boskin Commission final report, S. Prt. 104-72 (1996-12-04):
  https://www.finance.senate.gov/imo/media/doc/Prt104-72.pdf
- GAO/GGD-00-50 (Feb 2000):
  https://www.govinfo.gov/content/pkg/GAOREPORTS-GGD-00-50/html/GAOREPORTS-GGD-00-50.htm
- CRS IN12596, *The Consumer Price Index: Data Quality* (2025-08-18):
  https://www.congress.gov/crs_external_products/IN/PDF/IN12596/IN12596.1.pdf
- Federal Register, annual single-year weights (2022-08-24):
  https://www.federalregister.gov/documents/2022/08/24/2022-17994/updating-spending-weights-annually-based-on-a-single-calendar-year-of-data
- Revised release dates after the 2025 and 2026 lapses:
  https://www.bls.gov/bls/2025-lapse-revised-release-dates.htm
- 2028 geographic revision notice:
  https://www.bls.gov/cpi/notices/2026/geographic-revision.htm
- CE as a continuous survey:
  https://www.bls.gov/cex/research_papers/pdf/the-consumer-expenditure-survey-30-years-as-a-continuous-survey.pdf
