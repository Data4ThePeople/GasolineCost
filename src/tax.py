"""Federal income tax and FICA for tax year 2026. Pre-tax income in, after-tax income out.

Sources for every parameter are in data/raw/NOTES_tax_2026.md (IRS Rev. Proc.
2025-32 for the inflation-adjusted amounts, the statute for OBBBA items).
Scope: federal income tax plus employee FICA. No state or local tax. Wage and
pension income only: no capital gains, self-employment, itemizing or credits
beyond the child tax credit and EITC. The page's JavaScript mirrors this file
line for line; model.py checks the two agree.
"""
import math

# Start of each bracket, for rates 10, 12, 22, 24, 32, 35, 37% (Rev. Proc. 2025-32 sec. 4.01)
RATES = [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
BRACKETS = {
    'single': [0, 12_400, 50_400, 105_700, 201_775, 256_225, 640_600],
    'mfj':    [0, 24_800, 100_800, 211_400, 403_550, 512_450, 768_700],
    'hoh':    [0, 17_700, 67_450, 105_700, 201_750, 256_200, 640_600],
}
STD_DEDUCTION = {'single': 16_100, 'mfj': 32_200, 'hoh': 24_150}      # sec. 4.14
EXTRA_65 = {'single': 2_050, 'mfj': 1_650, 'hoh': 2_050}              # per person 65+
SENIOR_DEDUCTION = 6_000                                              # per person 65+, 2025-2028 (OBBBA)
SENIOR_PHASEOUT_START = {'single': 75_000, 'mfj': 150_000, 'hoh': 75_000}
SENIOR_PHASEOUT_RATE = 0.06
CTC_PER_CHILD = 2_200                                                 # sec. 4.05
ACTC_MAX_PER_CHILD = 1_700
ACTC_FLOOR, ACTC_RATE = 2_500, 0.15
CTC_PHASEOUT_START = {'single': 200_000, 'mfj': 400_000, 'hoh': 200_000}
# EITC by number of children 0..3 (sec. 4.06)
EITC_MAX = [664, 4_427, 7_316, 8_231]
EITC_EARNED_FOR_MAX = [8_680, 13_020, 18_290, 18_290]
EITC_PHASEOUT_START = {'single': [10_860, 23_890, 23_890, 23_890], 'mfj': [18_140, 31_160, 31_160, 31_160]}
EITC_PHASEOUT_END = {'single': [19_540, 51_593, 58_629, 62_974], 'mfj': [26_820, 58_863, 65_899, 70_244]}
SS_WAGE_BASE, SS_RATE, MEDICARE_RATE = 184_500, 0.062, 0.0145
ADDL_MEDICARE_RATE = 0.009
ADDL_MEDICARE_START = {'single': 200_000, 'mfj': 250_000, 'hoh': 200_000}
# Taxable Social Security (Pub. 915); not indexed
SS_BASE1 = {'single': 25_000, 'mfj': 32_000, 'hoh': 25_000}
SS_BASE2 = {'single': 34_000, 'mfj': 44_000, 'hoh': 34_000}


def bracket_tax(taxable, status):
    tax, b = 0.0, BRACKETS[status]
    for i, rate in enumerate(RATES):
        top = b[i + 1] if i + 1 < len(b) else float('inf')
        if taxable > b[i]:
            tax += (min(taxable, top) - b[i]) * rate
    return tax


def taxable_social_security(benefits, other_income, status):
    if benefits <= 0:
        return 0.0
    prov = other_income + benefits / 2
    b1, b2 = SS_BASE1[status], SS_BASE2[status]
    if prov <= b1:
        return 0.0
    if prov <= b2:
        return min(0.5 * benefits, 0.5 * (prov - b1))
    return min(0.85 * benefits, 0.85 * (prov - b2) + min(0.5 * benefits, 0.5 * (b2 - b1)))


def eitc(earned, agi, status, kids):
    k = min(kids, 3)
    st = 'mfj' if status == 'mfj' else 'single'
    start, end, mx = EITC_PHASEOUT_START[st][k], EITC_PHASEOUT_END[st][k], EITC_MAX[k]
    phase_in = mx * min(earned, EITC_EARNED_FOR_MAX[k]) / EITC_EARNED_FOR_MAX[k]
    income = max(earned, agi)
    if income >= end:
        return 0.0
    phase_out = mx * max(0.0, income - start) / (end - start)
    return max(0.0, min(phase_in, mx - phase_out))


def after_tax(status, wages, kids=0, seniors=0, pension=0.0, social_security=0.0):
    """Return a dict with the pieces. wages = earned income subject to FICA.
    pension = other fully taxable income (pensions, IRA withdrawals).
    kids = children under 17. seniors = people 65+ on the return."""
    other = wages + pension
    agi = other + taxable_social_security(social_security, other, status)
    senior_ded = 0.0
    if seniors:
        per = max(0.0, SENIOR_DEDUCTION - SENIOR_PHASEOUT_RATE * max(0.0, agi - SENIOR_PHASEOUT_START[status]))
        senior_ded = per * seniors
    deduction = STD_DEDUCTION[status] + EXTRA_65[status] * seniors + senior_ded
    taxable = max(0.0, agi - deduction)
    income_tax = bracket_tax(taxable, status)
    # $50 less for each $1,000 (or part of $1,000) of AGI over the threshold
    ctc_full = max(0.0, kids * CTC_PER_CHILD - 50 * math.ceil(max(0.0, agi - CTC_PHASEOUT_START[status]) / 1000))
    ctc_nonref = min(ctc_full, income_tax)
    actc = min(ctc_full - ctc_nonref, kids * ACTC_MAX_PER_CHILD, max(0.0, ACTC_RATE * (wages - ACTC_FLOOR)))
    e = eitc(wages, agi, status, kids) if seniors == 0 else 0.0
    federal = income_tax - ctc_nonref - actc - e
    fica = SS_RATE * min(wages, SS_WAGE_BASE) + MEDICARE_RATE * wages \
        + ADDL_MEDICARE_RATE * max(0.0, wages - ADDL_MEDICARE_START[status])
    gross = wages + pension + social_security
    return dict(gross=gross, agi=agi, deduction=deduction, taxable=taxable, income_tax=income_tax,
                ctc=ctc_nonref + actc, eitc=e, federal=federal, fica=fica, after_tax=gross - federal - fica)


def _check():
    # Cumulative tax at each bracket start, from the Rev. Proc. tables
    want = {'single': [1_240, 5_800, 17_966, 41_024, 58_448, 192_979.25],
            'mfj': [2_480, 11_600, 35_932, 82_048, 116_896, 206_583.50],
            'hoh': [1_770, 7_740, 16_155, 39_207, 56_631, 191_171]}
    for st, vals in want.items():
        for i, v in enumerate(vals):
            got = bracket_tax(BRACKETS[st][i + 1], st)
            assert abs(got - v) < 0.01, (st, i, got, v)
    print('bracket check ok')


if __name__ == '__main__':
    _check()
    for args in [('single', 50_000), ('mfj', 83_730, 2), ('mfj', 40_000, 2), ('single', 83_730), ('mfj', 0, 0, 2, 20_000, 38_000)]:
        r = after_tax(*args)
        print(args, {k: round(v) for k, v in r.items()})
