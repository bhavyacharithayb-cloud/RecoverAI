import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("payment_failures.csv")

# Features and target
X = data.drop(
    columns=[
        "transaction_id",
        "recovery_probability",
        "recovered"
    ]
)

y = data["recovered"]

# Define categorical and numerical columns
categorical_features = [
    "payment_method",
    "failure_reason"
]

numerical_features = [
    "amount",
    "customer_attempts",
    "hour"
]

# Preprocess categorical data
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "num",
            "passthrough",
            numerical_features
        )
    ]
)

# Create ML pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=200,
                random_state=42
            )
        )
    ]
)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel trained successfully!")
print(f"Accuracy: {accuracy:.2%}\n")

print("Classification Report:")
print(classification_report(y_test, predictions))

# Save trained model
joblib.dump(model, "recovery_model.pkl")

print("\nModel saved as recovery_model.pkl")