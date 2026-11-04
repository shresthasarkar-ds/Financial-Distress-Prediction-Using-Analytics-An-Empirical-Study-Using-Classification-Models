# Financial-Distress-Prediction-Using-Analytics-An-Empirical-Study-Using-Classification-Models
An empirical financial analytics project focused on predicting corporate financial distress using classification models, including Logistic Regression, Decision Tree, and Random Forest. Analyzes financial ratios and key performance indicators using Python, R, and Excel to identify potential financial risks and evaluate model performance.
# Financial Distress Prediction Using Analytics

### An Empirical Study Using Classification Models (Logistic Regression, Decision Tree, Random Forest)

Dissertation project for the **PGDM (Finance & Business Analytics)**, ISBR Business School, Bangalore (2024-2026).
It uses financial ratios to classify companies as **distressed (1)** or **non-distressed (0)**, and finds which ratios matter most.

---

## Table of Contents
1. [Overview](#overview)
2. [Key Results](#key-results)
3. [Dataset](#dataset)
4. [Methodology](#methodology)
5. [Results in Detail](#results-in-detail)
6. [Power BI Dashboard](#power-bi-dashboard)
7. [Repository Structure](#repository-structure)
8. [How to Run](#how-to-run)
9. [Notes and Limitations](#notes-and-limitations)
10. [Future Scope](#future-scope)
11. [Author](#author)

---

## Overview

Financial distress develops gradually, and catching it early helps investors, lenders and managers act sooner. This project:

- Analyses **12 companies across 14 years** using liquidity, profitability, leverage and cash-flow ratios
- Builds **three classification models** and compares them
- Identifies the **most important predictors** of distress
- Tests whether **inflation** affects corporate profitability (Net Profit Margin vs US inflation)
- Presents the findings in an interactive **Power BI dashboard**

## Key Results

| Finding | Result |
|---|---|
| Most important predictors | **Current Ratio** and **ROA** (consistent across all three models) |
| Logistic Regression | Accuracy **87.58%**, **AUC 0.9393** |
| Decision Tree | **100%** accuracy on 49 test observations (see [Notes](#notes-and-limitations)) |
| Random Forest | **97.96%** accuracy on 49 test observations (48 of 49 correct) |
| Inflation vs Net Profit Margin | Weak positive correlation (**0.21**), and it varies by industry |

---

## Dataset

- **Source:** Kaggle (secondary data), financial statements and ratios
- **Coverage:** 12 companies, 14 years each

| Ticker | Company | Sector |
|---|---|---|
| AAPL | Apple Inc. | Information Technology |
| AIG | American International Group | Insurance / Financial Services |
| AMZN | Amazon.com Inc. | E-commerce / Technology |
| BCS | Barclays PLC | Investment Banking / Financial Services |
| GOOG | Alphabet Inc. | Technology / Internet Services |
| INTC | Intel Corporation | Semiconductor |
| MCD | McDonald's Corporation | Food & Restaurant |
| MSFT | Microsoft Corporation | Information Technology |
| NVDA | NVIDIA Corporation | Semiconductor |
| PCG | Pacific Gas and Electric | Utility / Energy |
| PYPL | PayPal Holdings | Financial Technology |
| SHLDQ | Sears Holdings Corporation | Retail |

**Original variables:** Market Cap, Revenue, Gross Profit, Net Income, EPS, EBITDA, Shareholder Equity, Cash Flow (Operating / Investing / Financing), Current Ratio, Debt/Equity, ROE, ROA, ROI, Tax Rate, Interest Expense, Net Profit Margin, Free Cash Flow per Share, Return on Tangible Equity, Number of Employees, US Inflation Rate.

**Derived variables**

| Variable | Formula |
|---|---|
| Total Debt | Debt/Equity Ratio x Shareholder Equity |
| Capital Employed | Shareholder Equity + Total Debt |
| ROCE | EBITDA / Capital Employed (EBITDA used as an EBIT proxy) |
| Interest Coverage Ratio | EBITDA / Interest Expense (EBITDA used as an EBIT proxy) |
| **Distress (target)** | `1` if Net Income < 0 **or** Current Ratio < 1, otherwise `0` |

## Methodology

1. **Data preparation** in Excel: missing-value checks, consistent naming, ratio calculation, target creation
2. **Exploratory analysis:** descriptive statistics, correlation and trend analysis, per company and overall
3. **Modelling**
   - Logistic Regression (**R**)
   - Decision Tree (**Python**)
   - Random Forest (**Python**)
4. **Predictors used:** Current Ratio, Debt/Equity Ratio, ROA, Interest Coverage Ratio, Operating Cash Flow, US Inflation Rate
5. **Evaluation:** accuracy, precision, recall, F1, confusion matrix, Kappa, ROC/AUC
6. **Visualisation:** Power BI dashboard

---

## Results in Detail

### 1. Logistic Regression (R)

Current Ratio (negative coefficient) and ROA were the statistically significant predictors. Higher liquidity and higher profitability both lower the probability of distress.

<img width="667" height="273" alt="logistic_regression_output" src="https://github.com/user-attachments/assets/2ef1e4b8-60b1-47d0-bc1d-5b3dddf90010" />


**Confusion matrix (161 observations)**

| Actual \ Predicted | Non-Distress (0) | Distress (1) |
|---|---|---|
| **Non-Distress (0)** | 103 | 13 |
| **Distress (1)** | 7 | 38 |

| Metric | Value |
|---|---|
| Accuracy | 87.58% |
| Sensitivity | 88.79% |
| Specificity | 84.44% |
| Precision (PPV) | 93.64% |
| Negative Predictive Value | 74.51% |
| Balanced Accuracy | 86.62% |
| Kappa | 0.7037 |
| No Information Rate | 0.7205 |
| P-value (Accuracy > NIR) | 1.81e-06 |
| McNemar's test p-value | 0.2636 |

> Sensitivity, specificity, PPV and NPV above are reported with **Non-Distress (0) as the positive class**. For the **Distress** class: recall = 38/45 = **84.4%** and precision = 38/51 = **74.5%**.

**ROC curve: AUC = 0.9393 (excellent discrimination)**

<img width="1128" height="708" alt="roc_curve_logistic" src="https://github.com/user-attachments/assets/57e0b35a-7e4f-47cc-a364-871b340b68fd" />


### 2. Decision Tree (Python)

The tree splits on **Current Ratio <= 0.996** first, then **ROA <= 0.149**, then **Interest Coverage <= 1.064**.

<img width="1337" height="730" alt="decision_tree_diagram" src="https://github.com/user-attachments/assets/063c08b8-1bb1-4713-b222-345235195cbd" />



| Actual \ Predicted | Non-Distress (0) | Distress (1) |
|---|---|---|
| **Non-Distress (0)** | 37 | 0 |
| **Distress (1)** | 0 | 12 |

Accuracy: **100%** on 49 test observations (precision, recall and F1 = 1.00 for both classes).


<img width="1291" height="603" alt="decision_tree_variable_importance" src="https://github.com/user-attachments/assets/0736f5df-a092-4f4f-8af5-1bc5c33e1d17" />


| Rank | Variable | Importance |
|---|---|---|
| 1 | Current Ratio | 0.6529 |
| 2 | ROA | 0.3084 |
| 3 | Interest Coverage Ratio | 0.0387 |
| 4-6 | Debt/Equity, Operating Cash Flow, Inflation | 0.0000 |

### 3. Random Forest (Python)

| Actual \ Predicted | Non-Distress (0) | Distress (1) |
|---|---|---|
| **Non-Distress (0)** | 36 | 1 |
| **Distress (1)** | 0 | 12 |

Accuracy: **97.96%** (48 of 49). Macro F1 = 0.97, weighted F1 = 0.98. All distressed firms were identified.

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Non-Distress (0) | 1.00 | 0.97 | 0.99 | 37 |
| Distress (1) | 0.92 | 1.00 | 0.96 | 12 |


<img width="1299" height="625" alt="random_forest_feature_importance" src="https://github.com/user-attachments/assets/9f3f16d4-4a91-40e4-869d-3e22d3470477" />


| Rank | Variable | Importance |
|---|---|---|
| 1 | Current Ratio | 0.4208 |
| 2 | ROA | 0.2309 |
| 3 | Interest Coverage Ratio | 0.2049 |
| 4 | Debt/Equity Ratio | 0.0690 |
| 5 | Operating Cash Flow | 0.0589 |
| 6 | Inflation Rate (US) | 0.0155 |

### Model comparison

| Model | Tool | Evaluation set | Accuracy |
|---|---|---|---|
| Logistic Regression | R | 161 observations | 87.58% (AUC 0.9393) |
| Decision Tree | Python | 49 test observations | 100% |
| Random Forest | Python | 49 test observations | 97.96% |

### 4. Exploratory analysis

**Correlation matrix** (ROE, ROA and ROI move together; operating cash flow is positively related to profitability; inflation shows weak correlations with company ratios)


  <img width="1060" height="393" alt="correlation_matrix" src="https://github.com/user-attachments/assets/648dde0f-05e6-4c5f-bf9b-a5aa6cc05da0" />


**Liquidity vs leverage, and profitability by company** (Apple, Microsoft and McDonald's lead on ROA; Sears Holdings is the clear negative outlier)


  <img width="1182" height="560" alt="liquidity_vs_leverage_and_roa" src="https://github.com/user-attachments/assets/4e56876b-bdb2-4316-8960-9d5877204887" />



### 5. Net Profit Margin vs Inflation

Overall correlation: **0.21** (weak positive). The effect depends on the industry:

| Stronger positive (pricing power) | Near zero / negative |
|---|---|
| AAPL 0.67, MSFT 0.63, AIG 0.58, MCD 0.57, NVDA 0.55, BCS 0.51 | GOOG 0.02, PCG 0.02, SHLDQ -0.07, AMZN -0.09, INTC -0.11, PYPL -0.24 |


  <img width="543" height="307" alt="npm_vs_inflation" src="https://github.com/user-attachments/assets/9ac5b135-62b0-4e15-b79d-e5999ad1db52" />


---

## Power BI Dashboard


`Financial_Distress_Dashboard.pbix` has 4 pages:

| Page | Visuals |
|---|---|
| **Dashboard** | KPI cards (Average ROA, Average Current Ratio, Distress Count), Net Profit Margin vs Inflation, Liquidity vs Leverage bubble chart, Distress by Industry Sector, Distress Trend Over Time, Feature Importance, slicers for Year, Category and Company |
| **Trend Analysis** | Profitability by Company, NPM vs Inflation, Distress Trend Over Time, Distress by Sector |
| **Liquidity vs Leverage** | Bubble chart sized by market cap |
| **Feature importance chart** | Important financial ratios |

> Add a screenshot of the main dashboard page as `Result/dashboard_overview.png` and uncomment the line below.

<!-- ![Dashboard](Result/dashboard_overview.png) -->

---

## Repository Structure

```
Financial-Distress-Prediction/
├── README.md
├── LICENSE
├── Secondary_Dataset(Kaggle)/        # raw Kaggle dataset (12 companies, 14 years)
├── Excel_Files/
│   ├── <company>.xlsx                # descriptive, correlation and trend analysis, company-wise
│   │                                 # (AAPL, AIG, AMZN, BCS, GOOG, INTC, MCD, MSFT, NVDA, PCG, PYPL, SHLDQ)
│   └── Analysis_Result/
│       └── Financial_Statements.xlsx # financial statements, ratios, overall analysis
├── Python_Notebook/
│   ├── decision_tree.py
│   └── random_forest.py
├── R_Script/
│   ├── Logistic Regression & Confusion Matrix.R
│   └── ROC curve (Rplot)             # ROC curve output
├── PowerBI_Dashboard/
│   └── Financial_Distress_Dashboard.pbix
├── Report/                           # full project report (PDF)
└── Result/                           # figures extracted from the report (used in this README)
    ├── roc_curve_logistic.png
    ├── decision_tree_diagram.png
    ├── decision_tree_variable_importance.png
    ├── random_forest_feature_importance.png
    ├── correlation_matrix.png
    ├── liquidity_vs_leverage_and_roa.jpeg
    ├── npm_vs_inflation.jpeg
    ├── logistic_regression_output.png
    └── dashboard_overview.png        # add a Power BI screenshot
```

## How to Run

**R (Logistic Regression)**
```r
install.packages(c("caret", "pROC", "ggplot2"))
source("R_Script/Logistic Regression & Confusion Matrix.R")
```

**Python (Decision Tree, Random Forest)**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl
python Python_Notebook/decision_tree.py
python Python_Notebook/random_forest.py
```

**Dashboard:** open `PowerBI_Dashboard/Financial_Distress_Dashboard.pbix` in Power BI Desktop.

> The dataset is in `Secondary_Dataset(Kaggle)/`. Check the file paths inside each script match that folder.

---

## Notes and Limitations

- **Target definition overlaps with a predictor.** Distress is defined partly by `Current Ratio < 1`, and Current Ratio is also an input feature. This explains why the tree's first split (Current Ratio <= 0.996) is almost the target rule itself, and why it scores 100%. Read the tree and forest accuracy as how well the models recover a rule-based label, not as proof of real-world early warning.
- **Small, unevenly sized sample.** 12 large, mostly US-listed companies over 14 years, with 49 test observations for the tree models.
- **Evaluation sets differ.** Logistic Regression is reported on 161 observations and the tree models on 49 test observations, so the accuracy figures are not a like-for-like comparison.
- **EBITDA is used as an approximation of EBIT** for ROCE and Interest Coverage.
- Findings are specific to the selected companies and period, and may not generalise across industries.

## Future Scope

- Larger multi-country, multi-industry samples
- Add cash-flow, market and governance indicators
- Gradient boosting, neural networks and other advanced models
- A distress label independent of the input ratios (e.g. actual bankruptcy or default events), plus cross-validation
- Macro variables such as interest rates, GDP growth and exchange rates

## Author

**Shrestha Sarkar**
PGDM (Finance & Business Analytics), ISBR Business School, Bangalore (2024-2026)
Guide: Prof. Jaswanth Singh G

- LinkedIn: www.linkedin.com/in/shrestha-sarkar
- Email: sarkarshrestha88@gmail.com

## References

- Altman, E. I. (1968). Financial ratios, discriminant analysis and the prediction of corporate bankruptcy. *The Journal of Finance*, 23(4), 589-609.
- Beaver, W. H. (1966). Financial ratios as predictors of failure. *Journal of Accounting Research*, 4, 71-111.
- Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5-32.
- Shumway, T. (2001). Forecasting bankruptcy more accurately: A simple hazard model. *The Journal of Business*, 74(1), 101-124.
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer.
