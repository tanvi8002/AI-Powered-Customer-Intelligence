
import pandas as pd
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Dataset location
file_path = project_folder / "data" / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

# Check whether the file exists
if not file_path.exists():
    print("Dataset file not found!")
    print("Expected location:", file_path)
else:
    # Load dataset
    df = pd.read_csv(file_path)

    print("\n========== FIRST 5 RECORDS ==========")
    print(df.head())

    print("\n========== DATASET SIZE ==========")
    print("Rows and Columns:", df.shape)

    print("\n========== COLUMN NAMES ==========")
    print(df.columns.tolist())

    print("\n========== DATA INFORMATION ==========")
    df.info()

    print("\n========== MISSING VALUES ==========")
    print(df.isnull().sum())

    print("\n========== DUPLICATE RECORDS ==========")
    print("Duplicates:", df.duplicated().sum())

    print("\n========== CHURN DISTRIBUTION ==========")
    print(df["Churn"].value_counts())

    print("\n========== TOTAL CHARGES DATA TYPE ==========")
    print(df["TotalCharges"].dtype)

    print("\n========== DATA INSPECTION COMPLETED ==========")
