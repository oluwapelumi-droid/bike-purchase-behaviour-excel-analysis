# 🚲 Bike Purchase Behaviour Analysis | Excel Portfolio Case Study

**Turning a basic bicycle buyers dashboard into an interactive customer-segmentation analysis with decision-ready business recommendations.**

![Finished Excel dashboard](images/dashboard.png)

**Tools:** Microsoft Excel · `COUNTIF`/`COUNTIFS` · `AVERAGEIF`/`AVERAGEIFS` · Conditional formulas · Excel charts · Dropdown data validation · Data QA · Customer segmentation  
**Dataset:** Public educational **Bike Buyers** dataset associated with [Alex The Analyst's Excel tutorial repository](https://github.com/AlexTheAnalyst/Excel-Tutorial/blob/main/Excel%20Project%20Dataset.xlsx).  
**Scope:** 1,026 original records → 26 exact duplicates removed → **1,000 unique customer records**.  
**Outcome:** Descriptive insights and proposed experiments—not confirmed real-world sales results.

## Executive summary

| Customers analysed | Purchased a bike | Did not purchase | Observed purchase rate |
|---:|---:|---:|---:|
| **1,000** | **481** | **519** | **48.1%** |

**Key result:** The 2–5-mile commuting segment had the highest observed purchase rate (**58.6%**), whereas the 0–1-mile group produced the highest *number* of buyers (**200**). This contrast demonstrates why both segment *rate* and *size* should inform targeting decisions.

### Business question

If a hypothetical bicycle retailer wants to prioritize customer acquisition efforts, which audience segments in this dataset show greater interest in purchasing bicycles—and how should the marketing team validate those patterns?

### What I set out to examine

1. How commute distance and car ownership relate to bike purchasing.
2. Which age, occupation, and regional groups show higher or lower observed purchase rates.
3. Why conversion-style rates provide a fairer comparison than counts alone.
4. What business tests would best validate the descriptive findings.

## Data preparation and analysis approach

1. **Audit and deduplicate:** The source workbook held 1,026 data rows. There were 26 exact duplicate records/IDs and no conflicting repeated IDs; retaining one occurrence produced 1,000 customer profiles.
2. **Standardize categories:** Convert abbreviated gender and marital-status values to readable labels, harmonize the longest commute label, and normalize age bands.
3. **Correct an inaccurate label:** The original dashboard used `Adolescent` for ages **25–30**. The improved workbook uses `25–30`, `31–53`, and `54+` instead.
4. **Build traceable calculations:** Derive `Age Group` and `Purchase Flag` using Excel formulas. Use segment-specific `COUNTIF`/`COUNTIFS` to calculate customers, buyers, and rates.
5. **Improve the dashboard:** Replace misleading grand-total chart points with four segment purchase-rate charts and four KPI cards; add a **region dropdown filter** (`Dashboard!P5`).
6. **Check integrity:** Confirm 1,000 records, 481 buyers, 519 non-buyers, no missing values, unique customer IDs, and consistent segments.

**Metric definition:**

`Purchase rate = customers in segment with Purchased Bike = Yes / all customers in segment`

This is the *within-segment observed purchase rate*, not the percentage of total purchases that came from that segment.

## Findings

### 1. Commute distance—the clearest actionable split

| Commute | Customers | Buyers | Purchase rate |
|---|---:|---:|---:|
| 0–1 miles | 366 | 200 | **54.6%** |
| 1–2 miles | 169 | 77 | 45.6% |
| **2–5 miles** | 162 | 95 | **58.6%** |
| 5–10 miles | 192 | 76 | 39.6% |
| 10+ miles | 111 | 33 | **29.7%** |

The **2–5 mile segment led by purchase rate**, while the **0–1-mile segment led by customer and buyer volume**. A marketer could test short-commute messaging, but the dataset does not prove why those groups differ.

### 2. Car ownership—a potential mobility signal

| Cars owned | Customers | Buyers | Purchase rate |
|---:|---:|---:|---:|
| **0** | 247 | 151 | **61.1%** |
| 1 | 267 | 152 | 56.9% |
| 2 | 342 | 124 | 36.3% |
| 3 | 85 | 33 | 38.8% |
| 4 | 59 | 21 | 35.6% |

Customers with no cars showed a higher observed bike-purchase rate than households owning two cars. This suggests a *hypothesis* around bikes as alternative transport, not proof of causation.

### 3. Age—the middle band leads

| Age group | Customers | Buyers | Purchase rate |
|---|---:|---:|---:|
| 25–30 | 110 | 39 | 35.5% |
| **31–53** | 685 | 372 | **54.3%** |
| 54+ | 205 | 70 | 34.1% |

Ages **31–53** account for both the highest observed rate and largest number of buyers. These are dataset-specific, manually defined bands.

### 4. Region—rate and volume tell different stories

| Region | Customers | Buyers | Purchase rate |
|---|---:|---:|---:|
| Pacific | 192 | 113 | **58.9%** |
| Europe | 300 | 148 | 49.3% |
| North America | 508 | 220 | 43.3% |

The Pacific group has the highest observed rate, while North America has the highest **absolute number** of buyers. Targeting decisions should consider available audience, costs, and campaign testing—not just rank by rate.

### 5. Supporting profile insights

- **Gender:** Female 48.9% vs male 47.4%; a small descriptive difference and poor basis for gender-exclusive targeting.
- **Income:** Mean income is approximately **57,963 units for buyers** vs **54,875 units for non-buyers**. **Currency is not documented** in the workbook.
- **Marital status:** Single 54.1% vs married 42.9%; this may interact with age and other variables.

The workbook also contains complete segment summaries for education, occupation, children, and home ownership.

## Recommendations: experiments, not promises

| Priority | Hypothesis to test | Suggested pilot | Measurement |
|---|---|---|---|
| 1 | Shorter commuters respond to practical cycling benefits | A/B test commuting-focused messages for ≤5-mile audiences | Conversion lift and cost per acquisition |
| 2 | People owning fewer cars are more receptive to cycling as transport | Test mobility-oriented vs generic creatives | Incremental purchases vs holdout |
| 3 | Ages 31–53 could respond to differentiated products or value propositions | Age-relevant messaging test without excluding other groups | Response lift by cohort |
| 4 | Regional strategies may need localization | Comparable creative pilots in each region | Conversion, total qualified leads, CAC |
| 5 | Volume and rate need to be evaluated together | Rank opportunity by audience size *and* response performance | Incremental buyers and acquisition efficiency |

## How to use the workbook

1. Download [**Bike_Purchase_Behaviour_Analysis.xlsx**](workbook/Bike_Purchase_Behaviour_Analysis.xlsx) and open it in **Microsoft Excel**.
2. Open the **Dashboard** tab. Change the **region dropdown at P5** (`All regions`, `Europe`, `North America`, or `Pacific`). The four KPI cards and four charts are calculated from the filtered records.
3. Open **Interactive Metrics** to inspect the region-filtered chart inputs.
4. Open **Segment Analysis** to review full-dataset comparisons over **10 dimensions**; this sheet deliberately remains unfiltered for baseline comparisons.
5. Review **Income & Profiles**, **Insights & Actions**, and **QA & Methodology** to see the supporting calculations, interpretation, and data checks.

**Important:** The new workbook uses formula-driven summaries and an Excel *dropdown filter*, not Excel slicers or a pivot-table cross-filter. The original user-supplied file did contain PivotTables and an earlier dashboard, but this version uses a more auditable formula-based approach.

## Project files

```text
bike-purchase-behaviour-excel-analysis/
├── README.md                         # This portfolio case study
├── workbook/
│   └── Bike_Purchase_Behaviour_Analysis.xlsx
├── images/
│   ├── dashboard.png                # Final portfolio dashboard screenshot
│   └── original_dashboard_reference.png  # Starting dashboard, for comparison
├── data/
│   └── cleaned_bike_buyers.csv       # Cleaned records; age groups and flags materialized
├── analysis/
│   └── segment_metrics.csv          # 38 category-level metrics across 10 dimensions
├── docs/
│   ├── EXECUTIVE_BRIEF.md
│   ├── DATA_DICTIONARY.md
│   ├── METHODOLOGY.md
│   ├── PORTFOLIO_PRESENTATION.md
│   └── GITHUB_PUBLISHING_GUIDE.md
└── scripts/
    └── validate_metrics.py          # Reproduces and validates metrics using Python stdlib
```

### Reproduce the metric checks

From the repository root, run:

```bash
python scripts/validate_metrics.py
```

No additional packages are required. The project is **Excel-first**: the Python script only provides an independent reproducibility check, not an alternative dashboard implementation.

## Limitations and transparency

- This is a **practice/educational dataset**, not a representative sample of a verified store's current customers.
- There are no prices, sale dates, advertising costs, revenue, profit, or repeat-customer records. **Sales revenue, time-series trends, campaign ROI, and profitability cannot be calculated**.
- Differences between groups are **associations**, not evidence that commuting distance, age, or car ownership *caused* a purchase.
- Small categories such as owners of four cars should be interpreted carefully.
- Age group boundaries were inherited from and clarified within the supplied analysis; they are not universal standards.
- Income currency is unspecified, so the report deliberately does not attach a currency symbol.

## Data acknowledgement and project context

Dataset link: [AlexTheAnalyst/Excel-Tutorial — Excel Project Dataset.xlsx](https://github.com/AlexTheAnalyst/Excel-Tutorial/blob/main/Excel%20Project%20Dataset.xlsx).

This portfolio was expanded from a pre-existing workbook supplied for review. The enhanced outputs add customer-level QA, corrected labeling, formula-driven segment metrics, regional interaction, extended visualizations, and decision-focused documentation. Any tutorial assistance involved in producing the original workbook should be credited when describing the project publicly.