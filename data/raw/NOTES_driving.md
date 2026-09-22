# Driving-profile inputs: sources and figures

Gathered 2026-09-22. All raw files are in `data/raw/driving/`. Nothing here is rounded by hand; values are as published or as computed by `data/raw/driving/nhts2022_profiles.py` (full output with SEs in `data/raw/driving/nhts2022_computed_profiles.csv`, 198 rows).

---

## 1. FHWA 2022 NextGen National Household Travel Survey (NHTS), public-use microdata

**Files and URLs**
- Data: https://nhts.ornl.gov/media/2022/download/csv.zip -> `driving/nhts2022_csv.zip`, unzipped to `driving/nhts2022_csv/` (files `hhv2pub.csv`, `vehv2pub.csv`, `perv2pub.csv`, `tripv2pub.csv`, `ldtv2pub.csv`; file dates 2025-04-14 = Version 2.1)
- Codebook: https://nhts.ornl.gov/media/2022/doc/codebook.xlsx (and .pdf)
- User's Guide V2.01: https://nhts.ornl.gov/media/2022/doc/2022%20NextGen%20NHTS%20User's%20Guide%20V201_PubUse.pdf
- Derived Variables V2.1: https://nhts.ornl.gov/media/2022/doc/2022%20NextGen%20NHTS%20Derived%20Variables-PubUseV2.1.pdf
- Compatibility with Prior Data V2.1: https://nhts.ornl.gov/media/2022/doc/2022%20NextGen%20NHTS%20Compatibility%20with%20Prior%20Data%20V2.1.pdf
- Release notes V2.1: https://nhts.ornl.gov/media/2022/doc/2022%20NextGen%20NHTS%20V2.1%20Release%20Notes.pdf
- Weighting Memo: https://nhts.ornl.gov/media/2022/doc/2022%20NextGen%20NHTS%20Weighting%20Memo.pdf
- Summary of Travel Trends: 2022 NHTS: https://nhts.ornl.gov/assets/2022/pub/2022_NHTS_Summary_Travel_Trends.pdf

**Sample (User's Guide Table 10):** 7,893 households (weighted 127,544,707); 16,997 persons age 5+ (305,560,925); 14,684 household vehicles (232,837,104); 31,074 trips. Fielded January 2022 to January 2023. National sample only; add-on households are not in the file. FHWA says it is valid at the national, census-division, and urban/rural levels only.

**Variables used**
- `ANNMILES` (vehicle file): "Self-reported annualized mile estimate." Derivation (Derived Variables doc): if the vehicle was owned 12+ months, `ANNMILES = VEHMILES` (miles driven in past 12 months); if owned less than a year, `ANNMILES = ESTMILES / VEHOWNMO * 12`. -9 = not ascertained (213 vehicles). Top-coded at 200,000. **There is no BESTMILE (modeled) variable in 2022**, unlike 2017.
- `WTHHFIN` household weight (trimmed in V2.0), used for households and vehicles.
- `HHVEHCNT`, `URBRUR` (1 urban, 2 rural), `HHFAMINC_IMP` (income with imputation, no missing), `VEHTYPE`, `VEHAGE`, `VEHYEAR`, `VEHFUEL`, `R_AGE` (person file, top-coded 92), `STRATUMID`.
- SEs: Taylor linearization, strata = `STRATUMID`, household = PSU (2022 has no replicate weights; FHWA recommends Taylor series). MOE = 1.96 x SE.

### Data-quality problem with 2022 ANNMILES (important)

- 346 of 14,471 vehicles with a mileage report (2.80% of weighted vehicles) report more than 100,000 miles a year; 108 (0.99%) sit at the 200,000 top-code. Many look like odometer readings, not annual miles.
- Weighted mean of raw ANNMILES x all 232,837,104 household vehicles = **3,252.4 billion miles**. The Summary of Travel Trends (Table 2-10) benchmark for household-type vehicle VMT in 2022 is **2,619,421 million**, and total VMT for all motor vehicles, trucks included, was about 3.2 trillion. The raw mean cannot be right.
- Treating ANNMILES > 100,000 as missing gives 2,256.0 billion (86% of the benchmark). Treating > 50,000 as missing gives 1,879.6 billion (72%).
- Medians are barely affected. **Recommendation: use the "clean100" means or the medians. Do not use raw means.** All three versions are in the CSV.
- Separately, FHWA reports that the travel-day (trip-based) VMT in the 2022 NHTS was only 71% of the external benchmark, down from 80% in 2017 (Summary of Travel Trends, p. 17, Table 2-10). FHWA links this to more online shopping, telework, and similar changes, and says more research is needed. The 2022 NHTS also changed how it defines a completed household and moved to web-only (99% web). It also found more non-travelers than expected and adjusted the weights for that (Compatibility doc).
- Household totals below drop any household with a missing or excluded vehicle mileage. Under clean100 that leaves 7,501 of 7,893 households.
- "Household vehicles" includes motorcycles, RVs, and EVs. Light-duty = VEHTYPE 1-4 (car, van, SUV, pickup). 94.71% of weighted household vehicles run on gas, diesel, or biodiesel.

### 1a. Annual miles per household vehicle (weighted, WTHHFIN)

| Group | clean100 mean | MOE | Median | n | raw mean | clean50 mean |
|---|---|---|---|---|---|---|
| All household vehicles | 9,689.2 | 715.4 | 6,000 | 14,125 | 13,968.4 | 8,072.8 |
| Light-duty (car/van/SUV/pickup) | 10,003.4 | 729.1 | 7,000 | 13,467 | 14,355.7 | 8,345.3 |
| Car | 9,695.2 | | 6,000 | 6,114 | 14,793.5 | 7,887.9 |
| Van | 10,583.4 | | 7,000 | 634 | 15,107.9 | 8,727.4 |
| SUV | 10,475.2 | | 8,000 | 4,410 | 14,246.6 | 8,949.5 |
| Pickup | 9,795.8 | | 6,000 | 2,309 | 13,124.7 | 8,354.1 |
| Urban, light-duty | 9,791.9 | | 6,500 | 10,201 | 14,566.4 | 8,153.1 |
| Rural, light-duty | 10,695.7 | | 7,200 | 3,266 | 13,657.4 | 8,975.7 |

(MOE column for the first two rows only. Every other MOE is in the CSV `moe95` column. Raw medians: all vehicles 6,667, light-duty 7,000.)

### 1b. Household annual vehicle miles (sum of ANNMILES over the household's vehicles), clean100

| Group | Mean | Median | n HH |
|---|---|---|---|
| All households incl. 0-vehicle | 17,227.1 | 11,200 | 7,501 |
| Vehicle-owning households | 18,914.4 | 12,634 | 7,025 |
| HHVEHCNT = 1 | 11,482.6 | 7,000 | 2,500 |
| HHVEHCNT = 2 | 19,977.2 | 15,500 | 3,017 |
| HHVEHCNT = 3 | 26,402.2 | 21,000 | 989 |
| HHVEHCNT = 4+ | 33,802.1 | 27,156 | 519 |
| Urban, vehicle-owning | 17,863.6 | 12,000 | 5,549 |
| Rural, vehicle-owning | 22,945.8 | 16,800 | 1,476 |
| Urban, all HH | 16,014.5 | 10,000 | 5,995 |
| Rural, all HH | 22,262.0 | 16,000 | 1,506 |
| Income < $25k, vehicle-owning | 14,150.7 | 5,300 | 697 |
| Income $25-50k, vehicle-owning | 15,537.2 | 10,000 | 1,231 |
| Income $50-100k, vehicle-owning | 19,309.5 | 13,000 | 2,354 |
| Income $100-150k, vehicle-owning | 20,372.9 | 16,180 | 1,424 |
| Income $150k+, vehicle-owning | 23,108.9 | 18,000 | 1,319 |
| Income < $25k, all HH | 9,459.5 | 1,360 | 948 |
| Primary respondent (PERSONID 01) 65+, vehicle-owning | 13,069.3 | 9,273 | 2,369 |
| Primary respondent under 65, vehicle-owning | 21,192.1 | 15,000 | 4,656 |
| All person-file members 65+, vehicle-owning | 12,136.1 | 8,000 | 1,923 |
| All person-file members 65+, all HH | 11,113.4 | 7,000 | 2,032 |

- The CSV also has all 11 HHFAMINC brackets. Cells below about 200 households (the three brackets under $25k) have MOEs of 3,675 to 6,008 miles.
- Raw and clean50 versions of every row are in the CSV. For example, HHVEHCNT = 1 households average 18,340.3 miles raw and 8,470.7 under clean50. The low-income means are the most sensitive to the outliers: <$25k vehicle-owning is 32,220.2 raw vs 14,150.7 clean100.
- "65+" caveats: the person file covers only members age 5+. For 4+ person households, only 75% of members had to complete the survey. There is no HHRESP variable; PERSONID 01 answered the household questions in every household, so PERSONID 01 stands in for the householder.
- `HHFAMINC` is pre-tax household income, in brackets.

### 1c. Fleet mix and vehicle age (weighted)

| Group | Pickup share | SUV share | Pickup+SUV | LDV mean age (VEHAGE) | LDV mean model year | Median MY | Veh/HH |
|---|---|---|---|---|---|---|---|
| All | 16.05% | 30.16% | 46.22% | 10.14 | 2011.89 | 2014 | 1.8255 |
| Urban | 12.43% | 30.81% | 43.24% | 9.73 | 2012.31 | 2014 | 1.7309 |
| Rural | 27.85% | 28.05% | 55.90% | 11.52 | 2010.51 | 2013 | 2.2209 |
| Income < $25k | 14.96% | 18.66% | 33.62% | 14.11 | 2007.91 | 2008 | 1.0018 |
| Income $25-50k | 16.69% | 26.37% | 43.06% | 11.41 | 2010.62 | 2012 | 1.5385 |
| Income $50-100k | 18.40% | 28.30% | 46.69% | 10.37 | 2011.66 | 2014 | 1.9633 |
| Income $100-150k | 16.95% | 34.56% | 51.50% | 9.03 | 2013.02 | 2015 | 2.1780 |
| Income $150k+ | 11.96% | 36.21% | 48.17% | 8.35 | 2013.71 | 2016 | 2.3329 |
| Primary respondent 65+ | 17.37% | 29.77% | 47.14% | 10.54 | 2011.50 | 2014 | 1.6988 |

Shares use all household vehicles as the denominator. Age and model year cover light-duty vehicles only. The published Summary of Travel Trends Table 6-4 gives a 2022 mean household-vehicle age of 10.32 years (MOE 0.23) and a vehicle mix of 44.6% auto, 4.7% van, 30.2% SUV, 16.1% pickup. It includes RVs and "other trucks" in its age figure, which is why it differs slightly from 10.14.

### 1d. Published NHTS summary figures (Summary of Travel Trends 2022)

- Table 2-8: average daily VMT per household 39.70 (MOE 2.63) in 2022, vs 48.81 in 2017. This comes from travel-day trips, not ANNMILES.
- Table 3-4: average annual VMT per household, all purposes, 14,489 (MOE 945.0) in 2022, vs 17,815 in 2017 (network-calculated trip distance, trip-based).
- Table 2-10: household vehicles 232,837 thousand (NHTS) vs 252,468 thousand (external). VMT 1,848,031 million (NHTS) vs 2,619,421 million (external) = 71%.
- The trip-based 14,489 and the clean100 ANNMILES household mean of 17,227.1 are different measures. Neither matches FHWA's highway-count totals.

---

## 2. FHWA Highway Statistics Table VM-1 (2024 edition, updated February 2026)

- Page: https://www.fhwa.dot.gov/policyinformation/statistics/2024/vm1.cfm
- File: https://www.fhwa.dot.gov/policyinformation/statistics/2024/xls/vm1.xlsx -> `driving/fhwa_vm1_2024.xlsx` (also the 2023 edition `fhwa_vm1_2023.xlsx`)
- Coverage: all registered vehicles, including business and fleet use, not just households. Built from HPMS traffic counts, MF-21 fuel, MV-1 registrations, and Polk data, plus modeling. 2025 edition not yet published (404).

| Item (2024 row) | LDV short WB (<=121 in) | LDV long WB (>121 in) | All light-duty |
|---|---|---|---|
| Average miles traveled per vehicle | 10,811.99 | 10,707.17 | 10,786.65 |
| Average fuel consumed per vehicle (gal) | 422.58 | 578.88 | 460.36 |
| Average miles per gallon | 25.5857 | 18.4963 | 23.4307 |
| VMT (millions) | 2,222,414.75 | 701,692.70 | 2,924,107.45 |
| Registered vehicles | 205,550,881 | 65,534,861 | 271,085,742 |

2023 row, same file: miles per vehicle 11,025.76 / 11,360.32 / 11,105.91. MPG 24.6588 / 17.9363 / 22.5846. All motor vehicles: 11,071.41 miles per vehicle and 19.17 mpg in 2024.

Caveat: VM-1 mpg is VMT divided by fuel. It is the best available on-road average for the whole existing fleet, but EVs are counted as vehicles and miles while using almost no fuel, which raises the ratio a little. VM-1 does not break EVs out.

---

## 3. EPA Automotive Trends Report, 2025 edition (EPA-420-R-26-001, February 2026)

- Report: https://www.epa.gov/system/files/documents/2026-02/420r26001.pdf -> `driving/epa_trends_2025_report_420r26001.pdf`
- Executive summary: https://www.epa.gov/system/files/documents/2026-02/420s26001.pdf
- Landing page: https://www.epa.gov/automotive-trends/download-automotive-trends-report
- Metric: "estimated real-world" 5-cycle fuel economy (43% city / 57% highway), production-weighted harmonic average of **new** vehicles by model year. BEVs and PHEVs are included in mpge. MY2024 is final; MY2025 is preliminary. The final MY2024 figure came in 0.8 mpg below its preliminary value (Table A.1).

| | MY2024 (final) | MY2025 (prelim) |
|---|---|---|
| All new vehicles (Table 2.1) | 27.2 mpg | 28.1 mpg |
| All new vehicles, excluding BEVs/PHEVs (ES text) | 25.6 mpg | n/a |
| Sedan/wagon (Table 3.2) | 33.5 | 36.2 |
| Car SUV | 39.2 | 37.6 |
| Truck SUV | 25.7 | 26.3 |
| Minivan/van | 26.1 | 28.2 |
| Pickup | 20.5 | 21.3 |
| Car production share (Table 3.1) | 34.3% | 34.7% |
| Truck production share | 65.7% | 65.3% |

- Cars vs trucks as a whole: the PDF does not print these (only the interactive Qlik tool shows them). I derived them as production-weighted harmonic means of Table 3.2, with cars = sedan/wagon + car SUV and trucks = truck SUV + minivan/van + pickup. These shares add up exactly to the Table 3.1 car and truck shares. **Derived: MY2024 cars 35.08, trucks 24.38 (all 27.23 vs published 27.2). MY2025 prelim cars 36.66, trucks 25.03.** Label these as derived from rounded table values.
- The pickup figure excluding BEVs/PHEVs is 20.3 mpg (from the ES-3 figure label).
- EPA does not publish a fleet-wide on-road figure for vehicles already on the road. Use FHWA VM-1 (22.5846 in 2023, 23.4307 in 2024 for all light-duty).

**BTS National Transportation Statistics Table 4-12 / 4-23: not obtained.** www.bts.gov returned HTTP 403 (Akamai "Access Denied") to curl and to WebFetch. BTS builds those tables from FHWA VM-1, so VM-1 above is the primary source.

---

## 4. Average age of light vehicles in operation (S&P Global Mobility)

- **12.8 years** (as of 2025, published May 21, 2025). Passenger cars 14.5 years; light trucks 11.9 years; 289 million light vehicles in operation; scrappage rate 4.5%. BEVs 3.7, PHEVs 4.9, hybrids 6.4 years.
- Source: https://press.spglobal.com/2025-05-21-U-S-Vehicle-Age-Rises-Again-to-12-8-Years-in-2025,-According-to-S-P-Global-Mobility -> `driving/spglobal_vehicle_age_2025_pressrelease.html`
- **A 2026 figure was not found.** Web searches on 2026-09-22 returned nothing newer than the May 2025 release. If S&P published one in May 2026, it was not indexed. Do not cite 13 years; that was a CCC projection repeated in trade press, not an S&P figure.
- For comparison: NHTS 2022 household light-duty mean age was 10.14 years (computed) and 10.32 years (published). S&P's figure is higher because it counts all registered light vehicles, including fleets, and uses a different method.
