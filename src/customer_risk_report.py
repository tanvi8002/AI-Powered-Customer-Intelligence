
import pandas as pd
import joblib
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Load cleaned dataset
data_path = project_folder / "data" / "processed" / "telco_customer_churn_cleaned.csv"
df = pd.read_csv(data_path)

# Load trained model
model_path = project_folder / "models" / "churn_prediction_model.joblib"
model = joblib.load(model_path)

# Prepare customer features
X = df.drop(columns=["customerID", "Churn"])

# Predict churn probability
probabilities = model.predict_proba(X)[:, 1]

# Predict churn status
predictions = model.predict(X)

# Create risk report
risk_report = pd.DataFrame({
    "CustomerID": df["customerID"],
    "Actual_Churn": df["Churn"],
    "Churn_Probability": probabilities,
    "Predicted_Churn": ["Yes" if p == 1 else "No" for p in predictions]
})

# Classify customer risk
def risk_category(probability):
    if probability >= 0.70:
        return "High Risk"
    elif probability >= 0.40:
        return "Medium Risk"
    else:
        return "Low Risk"

risk_report["Risk_Category"] = risk_report["Churn_Probability"].apply(risk_category)

# Format probability as percentage
risk_report["Churn_Probability"] = (
    risk_report["Churn_Probability"] * 100
).round(2)

# Save report
output_path = project_folder / "data" / "processed" / "customer_risk_report.csv"

risk_report.to_csv(output_path, index=False)

# Display summary
print("\n--- CUSTOMER RISK REPORT ---")

print("Total customers:", len(risk_report))

print("\nRisk category distribution:")
print(risk_report["Risk_Category"].value_counts())

print("\nPredicted churn distribution:")
print(risk_report["Predicted_Churn"].value_counts())

print("\nFirst 10 customer records:")
print(risk_report.head(10).to_string(index=False))

print("\nReport saved successfully!")
print("Saved location:", output_path)
