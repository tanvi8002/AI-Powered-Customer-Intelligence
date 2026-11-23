
import pandas as pd
import joblib
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Load saved model
model_path = project_folder / "models" / "churn_prediction_model.joblib"

model = joblib.load(model_path)

# Create sample customer data
customer = pd.DataFrame([{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 2,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.70,
    "TotalCharges": 151.65
}])

# Predict churn
prediction = model.predict(customer)[0]
probability = model.predict_proba(customer)[0][1]

print("\n--- CUSTOMER CHURN PREDICTION ---")

print("Churn Probability:", round(probability * 100, 2), "%")

if prediction == 1:
    print("Prediction: Customer is at risk of churning.")
else:
    print("Prediction: Customer is likely to stay.")

print("\nPrediction completed successfully!")
