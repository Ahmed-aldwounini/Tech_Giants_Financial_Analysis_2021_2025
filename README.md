# Tech Giants Financial Analysis 2021-2025

## Financial Performance & Liquidity Analysis of Amazon, Apple, Google, Meta, and Microsoft

---

## Introduction

This project represents a deep dive into the financial health of the "Big Five"—Amazon, Apple, Google (Alphabet), Meta, and Microsoft. The goal was to move beyond top-line numbers and unpack the financial mechanics that separate a hardware-heavy giant like Amazon from a pure software powerhouse like Microsoft.

The analysis focused on three core questions:

1. How does each company's business model dictate its liquidity risk?
2. How efficiently are they converting assets into actual profit?
3. What do these numbers tell us about their resilience through 2025?

The findings reveal distinct strategic architectures: Amazon's logistics-driven model versus Microsoft's software-centric approach.

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Data Processing** | Python (Pandas/NumPy) | Cleaning and normalizing financial data |
| **Notebook** | Jupyter Notebook | Interactive data processing pipeline |
| **Visualization** | Power BI | Interactive dashboard for insight discovery |
| **Documentation** | MS Word | Deep-dive qualitative analysis per company |

---

## Key Financial Insights

### 1. On Scale vs. Margin
Amazon's high-volume e-commerce model yields a net profit margin of ~6.8%, contrasting sharply with Microsoft's software-driven 35%+ margins, demonstrating that business model architecture is the primary driver of profitability.

### 2. On Liquidity
Alphabet and Meta maintain conservative liquidity profiles with current ratios exceeding 200%, significantly outperforming the industry baseline and providing unmatched strategic agility for R&D investment.

### 3. On Asset Efficiency
Asset-heavy giants like Amazon utilize physical logistics networks as a sustainable competitive moat, whereas Meta prioritizes an asset-light digital model to maximize Return on Assets (ROA).

---

## How to Run the Pipeline

### Using the Jupyter Notebook

The `financial_facts_pipeline.ipynb` notebook provides an interactive, step-by-step data processing pipeline:

```bash
# Navigate to the project directory
cd "K:/Tech Giants Financial Analytics"

# Execute the notebook
jupyter nbconvert --to notebook --execute financial_facts_pipeline.ipynb --output financial_facts_pipeline_executed.ipynb
```

The notebook will:
1. Load raw financial data from `Data/all_companies_raw_facts.csv`
2. Filter important accounting concepts
3. Create a pivot table for each company/year combination
4. Merge alternative revenue and cost columns
5. Calculate gross profit with intelligent fallback logic
6. Save the processed data to `Data/powerbi_ready_matrix.csv`

---

## How to Explore

You can navigate the repository as follows:

| Folder | Contents |
|--------|----------|
| **Data/** | Raw dataset (`all_companies_raw_facts.csv`) and processed matrix (`powerbi_ready_matrix.csv`) |
| **Dashboard/** | Power BI dashboard (`Tech_Giants_Performance_Analysis.pbix`) with visual analysis |
| **Reports/** | Individual deep-dive qualitative reports in MS Word for each company |
| **financial_facts_pipeline.ipynb** | Jupyter Notebook for interactive data processing |

---

## Data Methodology

My approach was simple: I started by cleaning raw financial facts. I used Python to handle outliers and ensure that metrics like Gross Profit and Current Ratios were comparable across different reporting standards. The `powerbi_ready_matrix.csv` was created as the final, clean output that fed directly into my visualization layers.

The pipeline handles:
- Multiple revenue reporting standards (Revenues vs RevenueFromContractWithCustomerExcludingAssessedTax)
- Multiple cost reporting standards (CostOfGoodsAndServicesSold vs CostOfRevenue)
- Missing gross profit values (e.g., Amazon) with a 43% estimated margin fallback
- Consistent column naming for Power BI compatibility

---

## Future Scope

This analysis provides a solid foundation. In the next phase, I aim to:

- Integrate real-time financial APIs for automated trend tracking
- Develop a predictive model to forecast future profitability based on historical data

*Note: This repository is a personal data analysis project aimed at demonstrating proficiency in financial modeling, data cleaning, and business intelligence.*

---

## Author

Senior Data Analyst | Financial Performance & Liquidity Analysis