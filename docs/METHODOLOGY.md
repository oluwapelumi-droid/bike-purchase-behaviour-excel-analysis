# Methodology

## Objective

Explore demographic and commuting characteristics associated with bicycle purchases to suggest testable customer-targeting hypotheses.

## Preparation

1. Preserve the original bike-buyers workbook as a source reference.
2. Inspect 1,026 source rows and identify 26 exact duplicate customer records.
3. Retain 1,000 unique customers and standardize category spelling.
4. Create a binary Purchased Bike indicator and accurately named age segments: 25–30, 31–53, and 54+.
5. Verify categorical grouping totals against the 1,000-customer base.

## Measures

- **Customers:** number of distinct cleaned customer rows in a group.
- **Buyers:** count with Purchased Bike = Yes.
- **Non-buyers:** Customers minus Buyers.
- **Purchase rate:** Buyers divided by Customers in the group. Do not confuse purchase rate with each group's share of all buyers.
- **Average income:** arithmetic mean of the reported income values, in **unspecified units**.

## Quality assurance

1,000 customers = 481 buyers + 519 non-buyers. The overall purchase rate is 48.1%. Filtered category totals should reconcile with filtered overall KPIs. Avoid charting Grand Total as if it were a customer segment.

## Limitations

- Public educational dataset; not independently verified transactional records.
- No transaction dates, bicycle prices, marketing costs, or conversion attribution.
- Descriptive associations cannot demonstrate causality.
- Group sizes differ; avoid choosing a campaign solely on the highest rate.
- Age bins should be shown transparently and not called adolescent when they represent adults.

## Recommendations as hypotheses

Test commuter-focused messaging for the 2–5 mile segment, car-free customer positioning, and age-appropriate messaging for ages 31–53. Compare conversion and acquisition economics in a real pilot before committing budgets.
