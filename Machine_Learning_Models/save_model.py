import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier

# =====================================
# Load Dataset
# =====================================

df = pd.read_csv("Data/social_media_processed.csv")

# =====================================
# Remove Leakage Columns
# =====================================

df = df.drop(
    columns=[
        "user_id",
        "account_join_date",
        "addiction_score"
    ]
)

# =====================================
# Encode Categorical Columns
# =====================================

for col in df.select_dtypes(include="object").columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# =====================================
# Features and Target
# =====================================

X = df.drop(columns=["risk_level"])
y = df["risk_level"]

# =====================================
# Train-Test Split
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================
# Apply SMOTE
# =====================================

smote = SMOTE(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(
    X_train,
    y_train
)

print("Before SMOTE:")
print(y_train.value_counts())

print("\nAfter SMOTE:")
print(pd.Series(y_train_smote).value_counts())

# =====================================
# Train XGBoost Model
# =====================================

model = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    random_state=42,
    eval_metric="mlogloss"
)

model.fit(
    X_train_smote,
    y_train_smote
)

# =====================================
# Evaluate Model
# =====================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(f"\nModel Accuracy: {accuracy:.4f}")

# =====================================
# Create Models Folder
# =====================================

os.makedirs(
    "Models",
    exist_ok=True
)

# =====================================
# Save Model
# =====================================

model_path = "Models/xgboost_model.pkl"

joblib.dump(
    model,
    model_path
)

print("\n✅ Model saved successfully!")
print(f"📁 Saved Location: {model_path}")