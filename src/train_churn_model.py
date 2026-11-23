import joblib
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Load dataset
file_path = project_folder / "data" / "processed" / "telco_customer_churn_cleaned.csv"
df = pd.read_csv(file_path)

# Separate features and target
X = df.drop(columns=["customerID", "Churn"])
y = df["Churn"].map({"No": 0, "Yes": 1})

# Identify feature types
numerical_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Preprocessing for Logistic Regression
lr_preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Preprocessing for Random Forest
rf_preprocessor = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numerical_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Create models
models = {
    "Logistic Regression": Pipeline([
        ("preprocessor", lr_preprocessor),
        ("classifier", LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42
        ))
    ]),

    "Random Forest": Pipeline([
        ("preprocessor", rf_preprocessor),
        ("classifier", RandomForestClassifier(
            n_estimators=300,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        ))
    ])
}

# Train and evaluate both models
results = []

for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_probability = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    roc_auc = roc_auc_score(y_test, y_probability)

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC-AUC": roc_auc
    })

    print(f"{name} training completed!")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# Display comparison
comparison = pd.DataFrame(results)

print("\n--- MODEL PERFORMANCE COMPARISON ---")
print(comparison.to_string(index=False, formatters={
    "Accuracy": "{:.4f}".format,
    "Precision": "{:.4f}".format,
    "Recall": "{:.4f}".format,
    "F1 Score": "{:.4f}".format,
    "ROC-AUC": "{:.4f}".format
}))

print("\nBoth models trained and evaluated successfully!")
# Save selected Logistic Regression model
model_path = project_folder / "models" / "churn_prediction_model.joblib"

joblib.dump(models["Logistic Regression"], model_path)

print("\nSelected model saved successfully!")
print("Saved location:", model_path)

