
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project paths
project_folder = Path(__file__).resolve().parent.parent
input_file = project_folder / "data" / "processed" / "telco_customer_churn_cleaned.csv"
output_folder = project_folder / "reports"

output_folder.mkdir(parents=True, exist_ok=True)

# Load cleaned data
df = pd.read_csv(input_file)

sns.set_theme(style="whitegrid")

# 1. Overall customer churn
print("\n========== OVERALL CHURN ANALYSIS ==========")
print(df["Churn"].value_counts())

churn_percentage = df["Churn"].value_counts(normalize=True) * 100
print("\nChurn percentage:")
print(churn_percentage.round(2))

# 2. Churn by contract type
print("\n========== CHURN BY CONTRACT ==========")
contract_analysis = pd.crosstab(
    df["Contract"], df["Churn"], normalize="index"
) * 100

print(contract_analysis.round(2))

# 3. Average tenure by churn status
print("\n========== AVERAGE TENURE ==========")
print(df.groupby("Churn")["tenure"].mean().round(2))

# 4. Average monthly charges by churn status
print("\n========== AVERAGE MONTHLY CHARGES ==========")
print(df.groupby("Churn")["MonthlyCharges"].mean().round(2))

# 5. Churn by contract chart
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Contract", hue="Churn")
plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(output_folder / "churn_by_contract.png")
plt.show()

# 6. Customer tenure chart
plt.figure(figsize=(8, 5))
sns.histplot(
    data=df, x="tenure", hue="Churn",
    bins=20, multiple="stack"
)
plt.title("Customer Tenure Distribution by Churn")
plt.xlabel("Tenure (Months)")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(output_folder / "tenure_distribution.png")
plt.show()

# 7. Monthly charges chart
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
plt.title("Monthly Charges by Churn Status")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.savefig(output_folder / "monthly_charges_by_churn.png")
plt.show()

print("\nEDA completed successfully!")
print("Charts saved inside the reports folder.")
