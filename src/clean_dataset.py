
import pandas as pd
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# File paths
input_file = project_folder / "data" / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
output_file = project_folder / "data" / "processed" / "telco_customer_churn_cleaned.csv"

# Load original dataset
df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)

# 1. Remove unnecessary spaces from text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# 2. Convert TotalCharges into numeric values
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

print("\nMissing TotalCharges after conversion:")
print(df["TotalCharges"].isnull().sum())

# 3. Check rows with missing TotalCharges
print("\nRows with missing TotalCharges:")
print(df[df["TotalCharges"].isnull()][["customerID", "tenure", "TotalCharges"]])

# 4. Fill missing TotalCharges with 0
# These records represent customers with zero tenure
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# 5. Check duplicate customer IDs
print("\nDuplicate customer IDs:", df["customerID"].duplicated().sum())

# 6. Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# 7. Check corrected data types
print("\nCorrected TotalCharges data type:")
print(df["TotalCharges"].dtype)

# 8. Save cleaned dataset
output_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_file, index=False)

print("\nCleaned dataset shape:", df.shape)
print("Cleaned dataset saved successfully!")
print("Saved location:", output_file)
