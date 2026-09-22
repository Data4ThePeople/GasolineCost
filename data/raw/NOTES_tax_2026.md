# 2026 federal individual tax parameters (income tax + FICA)

Researched 2026-09-22. For a calculator turning pre-tax income into after-tax
income. Tax year 2026 unless noted.

## Sources

| Key | Document | URL |
|---|---|---|
| RP | IRS Rev. Proc. 2025-32 (2026 inflation adjustments, reflects OBBBA, P.L. 119-21) | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf |
| NR | IRS newsroom, "IRS releases tax inflation adjustments for tax year 2026, including amendments from the One, Big, Beautiful Bill" | https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill |
| SR | IRS newsroom, "Check your eligibility for the new enhanced deduction for seniors" | https://www.irs.gov/newsroom/check-your-eligibility-for-the-new-enhanced-deduction-for-seniors |
| OB | IRS newsroom, "Tax deductions for working Americans and seniors" (OBBBA) | https://www.irs.gov/newsroom/one-big-beautiful-bill-act-tax-deductions-for-working-americans-and-seniors |
| 151 | 26 U.S.C. 151(d)(5)(C) (as added by OBBBA sec. 70103) | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section151&num=0&edition=prelim |
| 24 | 26 U.S.C. 24 (as amended by OBBBA sec. 70104) | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section24&num=0&edition=prelim |
| CTC | IRS, Child Tax Credit page | https://www.irs.gov/credits-deductions/individuals/child-tax-credit |
| 751 | IRS Topic 751, Social Security and Medicare withholding rates | https://www.irs.gov/taxtopics/tc751 |
| 560 | IRS Topic 560, Additional Medicare Tax | https://www.irs.gov/taxtopics/tc560 |
| SSA | SSA press release, "Social Security Announces 2.8 Percent Benefit Increase for 2026" (2025-10-24) | https://www.ssa.gov/news/en/press/releases/2025-10-24.html |
| 915 | IRS Pub. 915 (2025 edition), Social Security and Equivalent Railroad Retirement Benefits | https://www.irs.gov/publications/p915 |

## 1. Ordinary income brackets (RP sec. 4.01, Tables 1-3)

Taxable income thresholds; each rate applies to income over the lower bound.

| Rate | Single (Table 3) | MFJ / surviving spouse (Table 1) | Head of household (Table 2) |
|---|---|---|---|
| 10% | 0 - 12,400 | 0 - 24,800 | 0 - 17,700 |
| 12% | 12,400 - 50,400 | 24,800 - 100,800 | 17,700 - 67,450 |
| 22% | 50,400 - 105,700 | 100,800 - 211,400 | 67,450 - 105,700 |
| 24% | 105,700 - 201,775 | 211,400 - 403,550 | 105,700 - 201,750 |
| 32% | 201,775 - 256,225 | 403,550 - 512,450 | 201,750 - 256,200 |
| 35% | 256,225 - 640,600 | 512,450 - 768,700 | 256,200 - 640,600 |
| 37% | over 640,600 | over 768,700 | over 640,600 |

Cumulative tax at each threshold, per RP (check values for code):

| Threshold | Single | MFJ | HoH |
|---|---|---|---|
| start of 12% | 1,240 | 2,480 | 1,770 |
| start of 22% | 5,800 | 11,600 | 7,740 |
| start of 24% | 17,966 | 35,932 | 16,155 |
| start of 32% | 41,024 | 82,048 | 39,207 |
| start of 35% | 58,448 | 116,896 | 56,631 |
| start of 37% | 192,979.25 | 206,583.50 | 191,171 |

Single and MFJ brackets also match NR. (MFS brackets equal Single except
35% ends at 384,350; not needed.) Note: in the PDF text layer the Table 1/2
captions sit next to the wrong tables; the values above are placed by their
consistency with NR and the base amounts.

## 2. Standard deduction (RP sec. 4.14)

| Item | Amount | Cite |
|---|---|---|
| Single / MFS | 16,100 | RP 4.14(1); NR |
| MFJ / surviving spouse | 32,200 | RP 4.14(1); NR |
| Head of household | 24,150 | RP 4.14(1); NR |
| Additional (65+ or blind), married, per person per condition | 1,650 | RP 4.14(3) |
| Additional (65+ or blind), unmarried (Single/HoH), per condition | 2,050 | RP 4.14(3) |
| Dependent's standard deduction | greater of 1,350 or earned income + 450 | RP 4.14(2) |

## 3. OBBBA senior deduction (26 U.S.C. 151(d)(5)(C); SR; OB)

| Item | Value | Cite |
|---|---|---|
| Amount | 6,000 per qualified individual age 65+ by year end (12,000 if both spouses qualify) | 151(d)(5)(C)(i); SR |
| Years | Tax years 2025 through 2028 (beginning before 1/1/2029) | 151(d)(5)(C)(i); SR |
| Phase-out start (MAGI) | 75,000 (all other returns); 150,000 (joint) | 151(d)(5)(C)(ii); SR; OB |
| Phase-out rate | 6% of MAGI over threshold | 151(d)(5)(C)(ii) (statute; IRS newsroom pages do not state the rate) |
| MAGI | AGI + exclusions under secs. 911, 931, 933 (for most people, MAGI = AGI) | 151(d)(5)(C)(ii) |
| Not indexed | Fixed dollar amounts in statute | 151 |
| Other conditions | Available whether itemizing or not; must file jointly if married; SSN required | OB; SR |
| Full phase-out (derived) | Single: 175,000 MAGI. MFJ: 250,000 MAGI | Derived: 6,000 / 0.06 = 100,000 above threshold |

UNCONFIRMED from a primary IRS source: whether, for MFJ with two qualified
spouses, the 6% reduction applies to each 6,000 separately (combined 12,000
falls by 12% of excess, gone at 250,000) or to the combined amount. The
statute reduces "the $6,000 amount" per individual, which reads as each one
separately; both readings reach zero at 250,000 MAGI. Verify against
Schedule 1-A (Form 1040) instructions before coding.

## 4. Child Tax Credit (RP sec. 4.05; 26 U.S.C. 24; CTC)

| Item | 2026 value | Cite |
|---|---|---|
| Max credit per qualifying child (under 17) | 2,200 | RP 4.05(1); 24(h)(2) as indexed |
| Refundable portion (ACTC) max per child | 1,700 | RP 4.05(2) |
| Phase-out threshold (MAGI) | 400,000 MFJ; 200,000 all others (not indexed) | 24(h)(3); CTC |
| Phase-out rate | 50 per 1,000 (or fraction) of MAGI over threshold | 24(b)(1) |
| ACTC earned income formula | 15% of earned income over 2,500 | 24(d)(1)(B)(i) with 24(h)(6); CTC |
| Permanence | OBBBA made sec. 24(h) permanent | RP sec. 2.03; 24 |
| SSN | Child needs SSN valid for work; OBBBA also requires taxpayer (at least one spouse if MFJ) SSN | CTC |

Coding note: ACTC = min(unused CTC, 1,700 x children, 15% x (earned income -
2,500)). The 2,200 nonrefundable part offsets income tax first. (The formula
for 3+ children using excess of Social Security taxes over EIC is omitted;
it rarely binds.) The 500 credit for other dependents is not covered here.

## 5. Earned Income Tax Credit (RP sec. 4.06)

| Item | 0 children | 1 child | 2 children | 3+ children |
|---|---|---|---|---|
| Earned income amount (max credit reached) | 8,680 | 13,020 | 18,290 | 18,290 |
| Maximum credit | 664 | 4,427 | 7,316 | 8,231 |
| Phase-out begins, Single/HoH | 10,860 | 23,890 | 23,890 | 23,890 |
| Phase-out complete, Single/HoH | 19,540 | 51,593 | 58,629 | 62,974 |
| Phase-out begins, MFJ | 18,140 | 31,160 | 31,160 | 31,160 |
| Phase-out complete, MFJ | 26,820 | 58,863 | 65,899 | 70,244 |

- Investment income limit: 12,200 (RP 4.06(2)).
- Phase-in and phase-out rates are statutory (26 U.S.C. 32(b)(1)), not in RP.
  Not separately fetched; they can be derived from the table (max credit /
  earned income amount; max credit / (complete - begin)): phase-in 7.65%,
  34%, 40%, 45%; phase-out 7.65%, 15.98%, 21.06%, 21.06% for 0/1/2/3+.
  Derived, not quoted from a primary source.
- Phase-out uses the greater of AGI or earned income.
- Childless EITC requires age 25-64 (statute; not confirmed in this pass).
- Recommendation for the calculator: include EITC only for the lower-income
  profile, since the credit is zero above 70,244 (MFJ, 3+ kids).

## 6. FICA (751; 560; SSA)

| Item | Value | Cite |
|---|---|---|
| Social Security wage base 2026 | 184,500 | 751 ("For earnings in 2026, this base limit is $184,500"); SSA press release 2025-10-24 |
| OASDI employee rate | 6.2% up to wage base | 751 |
| Medicare (HI) employee rate | 1.45%, no cap | 751 |
| Additional Medicare Tax | 0.9% on wages over threshold | 560 |
| Additional Medicare thresholds | 250,000 MFJ; 125,000 MFS; 200,000 Single/HoH/other (statutory, not indexed) | 560 |
| Employer withholding rule | Employer withholds 0.9% on wages over 200,000 regardless of filing status | 751 |

Note: SSA.gov pages returned HTTP 403 to the fetch tool; the 184,500 figure
was confirmed from the IRS Topic 751 text and from SSA search result
snippets of the 2026 COLA press release and fact sheet.

## 7. Taxation of Social Security benefits (915; 26 U.S.C. 86)

Provisional income = AGI excluding SS + tax-exempt interest + 50% of SS benefits.

| Filing status | Base amount (up to 50% taxable) | Adjusted base (up to 85% taxable) |
|---|---|---|
| Single / HoH / QSS / MFS living apart | 25,000 | 34,000 |
| MFJ | 32,000 | 44,000 |
| MFS living with spouse | 0 | 0 |

Taxable benefits (Pub. 915 Worksheet 1 logic), with PI = provisional income,
B = base, A = adjusted base, SS = benefits:
- PI <= B: 0.
- B < PI <= A: min(50% x SS, 50% x (PI - B)).
- PI > A: min(85% x SS, 85% x (PI - A) + min(50% x SS, 50% x (A - B))).
  The second term's cap is 4,500 single (50% of 9,000) and 6,000 MFJ (50% of 12,000).

These thresholds are statutory and not indexed. Confirmed from the 2025
edition of Pub. 915; a 2026 edition was not checked, but the amounts have not
changed since 1993.

## Items not confirmed from a primary source

1. Senior deduction phase-out for MFJ with two qualifying spouses: per-person vs combined application (both end at 250,000).
2. EITC phase-in/phase-out percentages (derived from the RP table, not quoted).
3. SSA.gov page text for the wage base (blocked); confirmed through IRS Topic 751 instead.
