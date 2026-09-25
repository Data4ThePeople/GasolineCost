# Social posts: We still measure inflation with a tape deck

Post URL: https://www.data4thepeople.com/p/gasoline-share-of-income
Tool URL: https://data4thepeople.github.io/GasolineCost

The ask has a name now: **Inflation 4 The People (I4TP)**. One line, used the same way everywhere:

```
Inflation 4 The People: report inflation as a distribution of real household experiences, not a single average.
```

---

## X / Twitter thread

```
1/ The CPI says gasoline is 4.3% of what Americans spend.

For a family at the 20th percentile of income, it is 8.7% of their take-home pay.

Same pump. Same price. Different life.

We built a free tool so you can find your own number.
```

```
2/ Here is what the CPI's number actually is.

It adds up all the gasoline everyone bought and divides by everything everyone bought. Households with no car are in there too.

One number comes out. It belongs to nobody.
```

```
3/ So we built the households back in, from the government's own data: Census incomes, federal highway driving surveys, IRS tax rules.

Median household: $4,240 a year on gas, 5.7% of take-home pay.
Lower-income family: 8.7%.
Rural family: 7.7%.
Retired couple: 2.9%.
```

```
4/ The bigger gap is what happens when prices move.

Two households, same car, same 20,000 miles a year.

Each $1 at the pump costs the one earning $35,800 about 2.4% of take-home pay.

The one earning $182,400: 0.6%.

The CPI: 0.9%.
```

```
5/ We divide by take-home pay, not by total spending, on purpose.

Spending includes what people borrow. A measure built on spending can call a household fine while it goes deeper into debt buying necessities.

We would rather not treat borrowed money like earned money.
```

```
6/ Why is one number carrying all of this?

The CPI's current design was rolled out in 1978. One year later, Sony released the Walkman.

Music went cassette, CD, MP3, streaming. Inflation measurement got better surveys and kept the architecture.
```

```
7/ The data to do better already exists, and it is public.

We are calling the ask Inflation 4 The People (I4TP): report inflation as a distribution of real household experiences, not a single average.

Start with gasoline. It is the easiest one.
```

```
8/ Free tool, no signup, nothing you type leaves your browser.

Read the piece and find your own number:
https://www.data4thepeople.com/p/gasoline-share-of-income

#I4TP
```

---

## LinkedIn

```
The CPI says gasoline is 4.3% of what Americans spend. For a family at the 20th percentile of income, it is 8.7% of their take-home pay.

Both numbers are correct. They answer different questions.

The CPI's weight adds up all the gasoline everyone bought and divides by everything everyone bought, including households with no car. It is an average across one imaginary household, and it is used to set Social Security raises, tax brackets, drug rebates and poverty guidelines, all of which land on real paychecks.

So we rebuilt the households from public data: Census incomes, the federal travel survey for miles driven and gas mileage, and the 2026 tax rules for what a family actually takes home.

The median American household spends $4,240 a year on gas, 5.7% of take-home pay. A lower-income family is at 8.7%. A rural family with a car and a pickup, 7.7%. A retired couple, 2.9%.

The sharper finding is the slope. Take two households that drive identically, 20,000 miles a year at 25 miles per gallon. Every dollar added at the pump costs the household earning $35,800 about 2.4% of its take-home pay, and the household earning $182,400 about 0.6%. The CPI's figure is 0.9%.

The design we still use dates to 1978. A year later Sony released the Walkman. Recorded music has been rebuilt from the ground up since; inflation measurement got better surveys and kept the architecture.

We are calling the ask Inflation 4 The People, or I4TP: report inflation as a distribution of real household experiences, not a single average. The data already exists and it is public.

The piece includes a free tool. Put in your own miles, mileage and income and see where you land. Nothing you type leaves your browser.

https://www.data4thepeople.com/p/gasoline-share-of-income
```

---

## Bluesky / Threads (short, standalone)

```
The CPI says gas is 4.3% of what Americans spend.

For a family at the 20th percentile it is 8.7% of take-home pay. For a retired couple, 2.9%.

One number cannot hold that.

Inflation 4 The People: publish the distribution.

https://www.data4thepeople.com/p/gasoline-share-of-income
```

```
Two households. Same car, same 20,000 miles a year.

Every $1 at the pump takes 2.4% of take-home pay from the one earning $35,800, and 0.6% from the one earning $182,400.

The CPI reports 0.9%.

Find your own number:
https://www.data4thepeople.com/p/gasoline-share-of-income
```

---

## Notes

- Every number here appears in the post: 4.3%, 8.7%, 5.7%, 7.7%, 2.9%, $4,240, 2.4%, 0.6%, 0.9%, $35,800, $182,400.
- All of them are tied to the September 21, 2026 gas price of $4.478. If the price moves before these go out, rerun `src/model.py` and update.
- The hero (cassette in the gasoline pool) is the image for every platform. Email export at `images/gasoline-share-of-income-hero-email.jpg` is 275 KB and works fine as a social card.
- For a chart instead of the hero, use `images/04-lines-two-incomes.png`, the two-income slope chart. It carries the argument without any reading.
