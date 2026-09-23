# Fact-check: "what the CPI is used for" sentence

Checked 2026-09-23. Primary sources only (SSA, IRS, OPM, DoD, CMS/Medicaid, HHS ASPE,
USDA, TreasuryDirect/eCFR, Federal Reserve, BLS, CRS, U.S. Code).

**Headline:** the sentence is directionally right on all seven clauses, but two clauses
name the wrong index if a reader assumes "the CPI" means the headline CPI-U:

- Social Security and federal pensions run on **CPI-W**, not CPI-U.
- Tax brackets and the standard deduction have run on the **chained CPI (C-CPI-U)**
  since 2018, not CPI-U.

One clause (SNAP) rests on a description of the law that **changed on October 1, 2025**.
One clause (Fed) is fine only because it says "sits on the table" and not "targets."

---

## 1. "It moves Social Security checks and federal retiree pensions."

**True. Index is CPI-W in every case.**

- **Social Security / SSI.** Sec. 215(i) of the Social Security Act, 42 U.S.C. 415(i).
  The COLA is the increase in the average **CPI-W** for the third calendar quarter over
  the third quarter of the last year a COLA was paid. CPI-W = Consumer Price Index for
  Urban Wage Earners and Clerical Workers.
  - https://www.ssa.gov/oact/cola/latestCOLA.html
  - CRS 94-803, *Social Security: Cost-of-Living Adjustments* (updated 2026-05-27):
    https://www.congress.gov/crs-product/94-803
- **CSRS.** 5 U.S.C. 8340(b). Full CPI-W change, same third-quarter measure.
- **FERS — the nuance that would make a flat claim wrong.** FERS gets a "diet COLA":
  if CPI-W inflation is 2.0% or less, FERS gets the full amount; between 2.0% and 3.0%,
  FERS gets exactly 2.0%; above 3.0%, FERS gets CPI-W minus 1 percentage point. Most
  FERS retirees also get **no** COLA at all before age 62 (exceptions for disability,
  law enforcement, air traffic controllers, survivors). Example: for January 2026, CPI-W
  rose 2.8% Q3-2024 to Q3-2025, so CSRS got 2.8% and FERS got 2.0%.
  - CRS 94-834, *Cost-of-Living Adjustments for Federal Civil Service Annuities*:
    https://www.congress.gov/crs-product/94-834
  - CRS IF12354 on FERS COLA and the Equal COLA Act:
    https://www.congress.gov/crs-product/IF12354
  - OPM: https://www.opm.gov/support/retirement/faq/cost-of-living-adjustments/
- **Military retired pay.** 10 U.S.C. 1401a. Note the statute is loosely worded:
  1401a(g)(1) defines "price index" only as "the Consumer Price Index (all items, United
  States city average) published by the Bureau of Labor Statistics," and (g)(2) sets the
  base quarter as the quarter ending September 30. DoD implements it with **CPI-W**,
  matching the Social Security and CSRS COLA. Members who took the Career Status Bonus
  (REDUX, entered on/after 1986-08-01 and elected the bonus) get CPI-W **minus 1
  percentage point** under 1401a(b)(3). Effective date is December 1 (in the January
  check).
  - Statute: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section1401a
  - DoD: https://militarypay.defense.gov/Pay/Retirement/Cola.aspx
  - CRS RL34751, *Military Retirement: Background and Recent Developments*:
    https://www.congress.gov/crs-product/RL34751

**Rewording to consider.** "Federal retiree pensions" is true but uneven — FERS annuitants
get a trimmed COLA and usually none before 62. Safe version: "It moves Social Security
checks and, in a trimmed form, federal and military retiree pensions." If the piece is
about CPI-U specifically, say CPI-W here.

---

## 2. "It adjusts tax brackets and the standard deduction."

**True, but the index is the chained CPI (C-CPI-U), not CPI-U — and has been since 2018.**

- **Statute.** IRC 26 U.S.C. 1(f)(3): the cost-of-living adjustment is "the percentage
  (if any) by which the C-CPI-U for the preceding calendar year exceeds the CPI for
  calendar year 2016..." 26 U.S.C. 1(f)(6) defines C-CPI-U as the Chained Consumer Price
  Index for All Urban Consumers published by BLS, averaged over the **12-month period
  ending August 31**.
  - https://www.law.cornell.edu/uscode/text/26/1
- **When it changed.** Tax Cuts and Jobs Act of 2017 (P.L. 115-97, sec. 11002) switched
  federal tax indexing from CPI-U to C-CPI-U for tax years beginning after 2017. That
  switch was **permanent** even though the rate cuts were not. Before 2018 it was CPI-U.
  - CRS RL34498, *Federal Individual Income Tax Brackets, Standard Deductions, and
    Personal Exemption: 1988 to 2026*: https://www.congress.gov/crs-product/RL34498
- **After the 2025 law (OBBBA, P.L. 119-21).** Still C-CPI-U. Sec. 70101 made the
  2018–2025 rate tables permanent. It also changed the base year for part of the bracket
  schedule: 26 U.S.C. 1(j)(3) now substitutes 2017 for 2016 "solely for purposes of
  determining the dollar amounts at which any rate bracket higher than 12 percent ends
  and at which any rate bracket higher than 22 percent begins," which gives the tops of
  the **10% and 12% brackets one extra year of inflation** (2016→2017) starting in 2026.
  Standard deduction amounts were reset by statute for 2025 ($15,750 single / $23,625 HoH
  / $31,500 MFJ) and are indexed by C-CPI-U from there.
- **2026 figures** (Rev. Proc. 2025-32): standard deduction $16,100 single and MFS,
  $24,150 head of household, $32,200 married filing jointly.
  - IRS: https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill
  - Rev. Proc. 2025-32: https://www.irs.gov/pub/irs-drop/rp-25-32.pdf
- **Why it matters to a reader.** The chained CPI grows more slowly than CPI-U, so
  brackets and the standard deduction rise more slowly than the headline inflation number
  people see in the news. That is real money, and it is the opposite direction from the
  Social Security clause in the same sentence.

**Rewording to consider.** "It adjusts tax brackets and the standard deduction — using a
slower-moving version of the index called the chained CPI."

---

## 3. "It sets the rebates drug makers owe Medicaid and Medicare when they raise prices
faster than inflation."

**True. All three rebate mechanisms use CPI-U.**

- **Medicaid additional (inflation) rebate.** Sec. 1927(c)(2) of the Social Security Act,
  42 U.S.C. 1396r-8(c)(2). Statutory text: the manufacturer owes more when average
  manufacturer price rises faster than the baseline AMP "increased by the percentage by
  which the consumer price index for all urban consumers (United States city average) for
  the month before the month in which the rebate period begins exceeds such index for
  **September 1990**" (or, for drugs first marketed after October 1990, the month before
  the month the drug was first marketed).
  - https://www.law.cornell.edu/uscode/text/42/1396r-8
  - Extended to non-innovator multiple source ("N") drugs by the Bipartisan Budget Act of
    2015, sec. 602. CMS release:
    https://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Prescription-Drugs/Downloads/Rx-Releases/State-Releases/state-rel-175.pdf
- **Medicare Part B inflation rebate.** Inflation Reduction Act of 2022, SSA sec.
  1847A(i). Quarterly. Manufacturer owes a rebate when the Part B payment amount for a
  single-source drug or biological exceeds an inflation-adjusted benchmark, escalated by
  **CPI-U** from a 2021 benchmark (benchmark quarter CY2021Q3; benchmark period CPI-U =
  January 2021 for drugs marketed by then).
  - https://www.cms.gov/files/document/medicare-part-b-inflation-rebate-program-revised-guidance.pdf
- **Medicare Part D inflation rebate.** SSA sec. 1860D-14B. Annual, applicable period
  October–September. The benchmark price is escalated by **CPI-U**, where the applicable
  period CPI-U is the **October** CPI-U of the period and the benchmark period CPI-U is
  January 2021 for drugs approved on or before October 1, 2021.
  - https://www.cms.gov/files/document/medicare-part-d-inflation-rebate-program-revised-guidance.pdf
  - CMS program overview:
    https://www.cms.gov/priorities/medicare-prescription-drug-affordability/overview/medicare-inflation-rebate-program
  - CRS IF12203, *Selected Health Provisions of the Inflation Reduction Act*:
    https://www.congress.gov/crs-product/IF12203

**Nuance that does not break the sentence but is worth knowing.** These are not
year-over-year comparisons. Each program measures the price against a **fixed baseline**
(September 1990 for Medicaid, 2021 for Medicare) compounded by CPI-U ever since, so a
manufacturer can owe a rebate in a year it did not raise the price at all. Medicare
rebates are paid into the Medicare trust funds, not to patients directly.

---

## 4. "It updates the poverty guidelines that decide who qualifies for help."

**True. CPI-U.**

- Census Bureau **poverty thresholds** (the statistical measure) are updated each year by
  the change in the **CPI-U**, all items.
- HHS **poverty guidelines** (the administrative/eligibility version, 42 U.S.C. 9902(2))
  are the prior year's Census thresholds raised by the CPI-U change and smoothed/rounded.
- 2026 guidelines: the 2024 Census weighted-average thresholds (P60-287) were multiplied
  by a price inflator of about 1.0263 and rounded to the nearest $20. CPI-U all items:
  313.689 for CY2024, 321.943 for CY2025, a **2.63 percent** increase.
  - ASPE computations:
    https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines/prior-hhs-poverty-guidelines-federal-register-references/2026-poverty-guidelines-computations
  - Federal Register, *Annual Update of the HHS Poverty Guidelines*, 2026-01-15:
    https://www.federalregister.gov/documents/2026/01/15/2026-00755/annual-update-of-the-hhs-poverty-guidelines
    (federalregister.gov 302s plain fetches to an "unblock" page; content confirmed via
    ASPE and search snippets)
- **Live detail worth a line in the post.** Because of the October 2025 government
  shutdown, BLS did not publish a CPI-U for October 2025, so the 2026 guidelines compare
  an **11-month 2025 average** (October excluded) with the full 12 months of 2024.
  Sourced from ASPE/FR text via search snippets; the ASPE computations page I fetched
  shows the 313.689 / 321.943 figures but did not itself restate the 11-month note.
  *Flag: lightly confirmed.*
- Nuance: the guidelines, not the thresholds, are what programs use for eligibility
  (Medicaid, ACA subsidies, Head Start, LIHEAP, etc.), so "decide who qualifies for help"
  is accurate. The Supplemental Poverty Measure is built differently and is **not** a
  CPI-indexed threshold.

---

## 5. "and the food plan behind SNAP benefits."

**True, but the mechanism described in the brief is the PRE-October-2025 mechanism. This
is the clause most likely to be stated wrong.**

- SNAP maximum allotments equal the cost of USDA's **Thrifty Food Plan** for a reference
  family of four in **June**, effective the following **October 1**. 7 U.S.C. 2012(u),
  7 U.S.C. 2017(a).
- **What changed.** The One Big Beautiful Bill Act of 2025 (P.L. 119-21, sec. 10101)
  rewrote 7 U.S.C. 2012(u)(3)(C), which now reads: "on October 1, 2025, and on each
  October 1 thereafter, adjust the cost of the thrifty food plan to reflect changes in the
  **Consumer Price Index for All Urban Consumers**, published by the Bureau of Labor
  Statistics of the Department of Labor, for the most recent 12-month period ending in
  June." The same section bars cost-increasing re-evaluations of the market basket: the
  next re-evaluation may come no earlier than October 1, 2027 and must be cost-neutral
  (2012(u)(4)(A)–(B)).
  - Statute: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title7-section2012
  - CRS R48552, *SNAP and Related Nutrition Programs in P.L. 119-21*:
    https://www.congress.gov/crs-product/R48552 — "Any annual adjustment to the cost of
    the plan must be based on the Consumer Price Index for All Urban Consumers."
- **The older, indirect mechanism (still how the TFP cost report is built).** USDA's
  Center for Nutrition Policy and Promotion reprices the TFP market basket monthly using
  **CPI subindexes matched to each market basket category** — "eggs" to the CPI for eggs,
  "dark-green vegetables" to the CPIs for fresh, frozen and canned vegetables — with
  weighted averages where a category maps to more than one CPI, all measured against June
  2021. That is food-at-home component CPIs, not the all-items CPI.
  - https://www.fna.usda.gov/research/cnpp/usda-food-plans
  - https://www.fna.usda.gov/cnpp/thrifty-food-plan-2021
- **UNCONFIRMED.** Whether FNS applied the all-items CPI-U or the matched food CPIs to the
  October 1, 2025 (FY2026) adjustment. fns.usda.gov and fna.usda.gov return **403** to
  plain fetches, and the FY2026 COLA memo PDF path 404s. The FY2026 COLA page is
  https://www.fna.usda.gov/snap/allotment/cola/fy26 if it can be opened in a browser.

**Rewording to consider.** "and the food plan behind SNAP benefits" is safe and stays
true either way. Do **not** write that SNAP is adjusted by food-at-home CPI components
without qualifying the year, and do not write that SNAP is indexed to the overall CPI
without noting that it goes through the Thrifty Food Plan and uses a June-to-June window.

---

## 6. "It pays the interest on savings bonds and Treasury notes that are supposed to
protect people from inflation."

**True. Both use non-seasonally-adjusted CPI-U. Two small precision issues.**

- **Series I savings bonds.** TreasuryDirect: the inflation rate is based on the
  **non-seasonally adjusted CPI-U for all items, including food and energy**. It is reset
  every May 1 and November 1 and reflects the six-month change in that index (the November
  rate uses March→September; the May rate uses September→March). Governing regulation:
  31 CFR part 359.
  - https://treasurydirect.gov/savings-bonds/i-bonds/i-bonds-interest-rates/
  - https://www.govinfo.gov/content/pkg/CFR-2024-title31-vol2/pdf/CFR-2024-title31-vol2-sec359-11.pdf
- **TIPS.** 31 CFR 356.2 defines the index as "the monthly **non-seasonally adjusted U.S.
  City Average All Items Consumer Price Index for All Urban Consumers**, published by the
  Bureau of Labor Statistics." Appendix B to part 356: the Reference CPI for the first day
  of a month is the CPI for the **third preceding calendar month** (April 1 uses January's
  CPI), interpolated linearly for other days — an approximate **three-month lag**. The
  Index Ratio is the Reference CPI for a date divided by the Reference CPI for the issue
  date.
  - https://www.law.cornell.edu/cfr/text/31/356.2
  - https://www.ecfr.gov/current/title-31/subtitle-B/chapter-II/subchapter-A/part-356/appendix-Appendix%20B%20to%20Part%20356
- **Precision issue A — "pays the interest."** For TIPS the CPI does not set the interest
  rate; it adjusts the **principal**, and a fixed coupon rate is applied to the
  inflation-adjusted principal. For I bonds the CPI sets the inflation half of a composite
  rate. "Pays the interest" is close enough for a general reader but "sets what they pay"
  is more accurate.
- **Precision issue B — "Treasury notes."** TIPS are issued as 5- and 10-year notes and
  30-year bonds. "Treasury notes" is slightly narrow; "inflation-protected Treasury
  securities" or "Treasury bonds and notes" is cleaner.

---

## 7. "And it sits on the table when the Federal Reserve decides what to do with interest
rates."

**Fair as written. Do not upgrade it to "the Fed targets the CPI" — that is wrong.**

- The FOMC's target is defined on **PCE, not CPI**. 2025 Statement on Longer-Run Goals and
  Monetary Policy Strategy, verbatim: "The Committee reaffirms its judgment that inflation
  at the rate of 2 percent, **as measured by the annual change in the price index for
  personal consumption expenditures**, is most consistent over the longer run with the
  Federal Reserve's statutory maximum employment and price stability mandates."
  - https://www.federalreserve.gov/monetarypolicy/monetary-policy-strategy-tools-and-communications-statement-on-longer-run-goals-monetary-policy-strategy-2025.htm
  - https://www.federalreserve.gov/monetarypolicy/files/fomc_longerrungoals.pdf
  - https://www.federalreserve.gov/faqs/economy_14400.htm
- **Why "sits on the table" is still fair.** Three concrete links, all documentable:
  1. BLS CPI price data are a **source input** to many components of the BEA PCE price
     index, so a CPI surprise mechanically moves the measure the Fed does target.
  2. **TIPS breakevens**, the market's inflation compensation measure that the Fed and its
     staff watch, are priced off CPI-U (see item 6) — Fed research uses them directly, e.g.
     https://www.federalreserve.gov/pubs/feds/2008/200805/index.html
  3. The CPI release is a scheduled input to the FOMC's pre-meeting data flow, and the
     Fed's own economy-at-a-glance page presents PCE as the target measure while the CPI
     is reported alongside: https://www.federalreserve.gov/economy-at-a-glance-inflation-pce.htm
  The Summary of Economic Projections forecasts **PCE and core PCE**, not CPI.
- Suggested guardrail sentence if the post needs it: "The Fed's 2 percent goal is written
  in terms of a different index, the PCE price index, but the CPI feeds it and moves the
  market's inflation bets."

---

## Major uses the sentence omits

Ranked by how likely a reader is to expect them.

1. **Union contract COLAs, rents and leases, alimony and child support.** BLS itself leads
   with these: "Consumer Price Indexes are often used to escalate or adjust payments for
   rents, wages, alimony, child support, and other obligations." The most frequent
   escalation use is private-sector collective bargaining. These are private contracts and
   state law, not federal statute, and they typically use CPI-U or a local-area CPI.
   - https://www.bls.gov/cpi/factsheets/escalation.htm
   - https://www.bls.gov/bls/escalation.htm
2. **Federal civil penalties.** The Federal Civil Penalties Inflation Adjustment Act
   Improvements Act of 2015 requires every agency to raise its civil monetary penalties
   each year by the change in **CPI-U for October**, published no later than January 15.
   *Live caveat:* OMB memo M-26-11 (April 2026), titled "Cancellation of Penalty Inflation
   Adjustments for 2026," appears to have canceled the 2026 round.
   https://www.whitehouse.gov/wp-content/uploads/2026/04/M-26-11-Cancellation-of-Penalty-Inflation-Adjustments-for-2026-Regarding-the-Federal-Civil-Penalties-Inflation-Adjustment-Act-Improvements-Act-of-2015.pdf
   *Flag: title confirmed, full text not read.*
3. **School meal and child care food reimbursement rates.** Sections 11 and 17A of the
   Richard B. Russell National School Lunch Act, 42 U.S.C. 1759a and 1766a. Adjusted each
   July 1 by the **CPI-U Food Away From Home** series for the 12 months ending in May. The
   SY2026-27 rates reflect a 3.54 percent increase (May 2025 to May 2026).
   - https://www.federalregister.gov/documents/2026/07/16/2026-14252/national-school-lunch-special-milk-and-school-breakfast-programs-national-average-paymentsmaximum
4. **Medicare premiums.** The Part B **hold-harmless** provision, SSA sec. 1839(f), caps
   most beneficiaries' dollar Part B premium increase at their dollar Social Security COLA
   — so CPI-W indirectly governs what tens of millions of people actually pay. IRMAA
   income thresholds are indexed to CPI-U.
   - CRS R45324, *The Interaction Between Medicare Premiums and Social Security COLAs*:
     https://www.congress.gov/crs-product/R45324
   - https://www.ssa.gov/OP_Home/ssact/title18/1839.htm
5. **Everything that rides the Social Security COLA.** SSI federal benefit rate, veterans'
   disability compensation and DIC, and railroad retirement tier I all move by the same
   CPI-W number.

## Worth a line: things readers assume are CPI-indexed and are not

- The **federal minimum wage** has never been indexed to anything.
- The **Social Security taxable wage base** and the benefit-formula bend points are
  indexed to the national **Average Wage Index**, not the CPI. Only the COLA is CPI.
- The **Fed's 2 percent goal** is PCE (item 7).
- The **TANF block grant** is not indexed at all.

## Scale, if a number is wanted

BLS: the CPI "affects the income of more than 108 million people because of statutory
action: over 67 million Social Security beneficiaries and over 41 million SNAP
recipients, among other programs." Population coverage: CPI-U covers over 90 percent of
the U.S. population; CPI-W about 30 percent.
- https://www.bls.gov/cpi/questions-and-answers.htm
- https://www.bls.gov/cpi/factsheets/escalation.htm

## What could not be confirmed

- Which CPI series FNS actually applied to the October 1, 2025 SNAP adjustment
  (fns.usda.gov and fna.usda.gov return 403 to plain fetches; the FY2026 COLA memo PDF
  404s at the expected paths).
- The full text of OMB M-26-11 on the 2026 civil penalty adjustments (title only).
- The 11-month-CPI-U note in the 2026 poverty guidelines Federal Register notice was
  confirmed only from search snippets; federalregister.gov 302s plain fetches.
