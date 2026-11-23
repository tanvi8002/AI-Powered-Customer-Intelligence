
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Load cleaned dataset
file_path = project_folder / "data" / "processed" / "telco_customer_churn_cleaned.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# Separate features and target
X = df.drop(columns=["customerID", "Churn"])
y = df["Churn"].map({"No": 0, "Yes": 1})

print("\nFeatures shape:", X.shape)
print("Target shape:", y.shape)

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Display split results
print("\n--- Training and Testing Results ---")

print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)

print("Training target:", y_train.shape)
print("Testing target:", y_test.shape)

print("\nTraining churn distribution:")
print(y_train.value_counts())

print("\nTesting churn distribution:")
print(y_test.value_counts())

print("\nData splitting completed successfully!")
