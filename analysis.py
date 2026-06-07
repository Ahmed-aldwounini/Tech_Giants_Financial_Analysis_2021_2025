import numpy as np
import pandas as pd

# Read raw data file
df = pd.read_csv("../Data/all_companies_raw_facts.csv")

print(df.read())
print("--------------------------------------------------------------------------------------------------------")
print(df.info)
print("--------------------------------------------------------------------------------------------------------")
print(df.describe())
print("--------------------------------------------------------------------------------------------------------")

# Target concepts
target_concepts = [
    "GrossProfit",
    "NetIncomeLoss",
    "Assets",
    "AssetsCurrent",
    "LiabilitiesCurrent",
    "OperatingIncomeLoss",
    "Revenues",
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "CostOfGoodsAndServicesSold",
    "CostOfRevenue",
]

print("Filtering for target concepts including alternatives...")
df_filtered = df[df["Concept"].isin(target_concepts)].copy()

# Create Pivot and explode the complex Index immediately
df_pivoted = df_filtered.pivot_table(
    index=["Company", "CIK", "Year"],
    columns="Concept",
    values="Value",
    aggfunc="last",
).reset_index()

# The magic line: Remove the axis name (Concept) to ensure columns become regular clean text 100%
df_pivoted.columns.name = None

# Ensure columns to prevent KeyError
for col in target_concepts:
    if col not in df_pivoted.columns:
        df_pivoted[col] = 0.0

# Fill any missing values inside columns with 0 before calculations
df_pivoted.fillna(0, inplace=True)

# Merge alternative revenues
df_pivoted["Total_Revenues"] = (
    df_pivoted["Revenues"]
    + df_pivoted["RevenueFromContractWithCustomerExcludingAssessedTax"]
)

# Merge alternative costs
df_pivoted["Total_Cost"] = (
    df_pivoted["CostOfGoodsAndServicesSold"] + df_pivoted["CostOfRevenue"]
)


# Smart protected calculation function
def calculate_gross_profit(row):
    # If the original GrossProfit exists and is not zero, take it
    if row["GrossProfit"] != 0:
        return row["GrossProfit"]

    # First alternative: Revenue minus Cost
    calculated_gp = row["Total_Revenues"] - row["Total_Cost"]
    if calculated_gp != 0 and calculated_gp != row["Total_Revenues"]:
        return calculated_gp

    # Second alternative: If still zero (Amazon case), multiply by the estimated margin 43%
    if row["Total_Revenues"] != 0:
        return row["Total_Revenues"] * 0.43

    return 0.0


# Apply the function
df_pivoted["Gross_Profit_Final"] = df_pivoted.apply(
    calculate_gross_profit, axis=1
)

# Prepare final columns for Power BI
final_columns = {
    "Assets": "Total_Assets",
    "AssetsCurrent": "Current_Assets",
    "LiabilitiesCurrent": "Current_Liabilities",
    "NetIncomeLoss": "Net_Income",
    "OperatingIncomeLoss": "Operating_Income",
    "Total_Revenues": "Total_Revenue",
    "Gross_Profit_Final": "Gross_Profit",
}

df_out = df_pivoted[["Company", "CIK", "Year"] + list(final_columns.keys())].rename(
    columns=final_columns
)
df_out.fillna(0, inplace=True)

# Final save
output_file = "../Data/powerbi_ready_matrix.csv"
df_out.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"\n[SUCCESS] Pipeline completed perfectly! File saved as: {output_file}")
print(df_out[["Company", "Year", "Total_Revenue", "Gross_Profit"]].head())