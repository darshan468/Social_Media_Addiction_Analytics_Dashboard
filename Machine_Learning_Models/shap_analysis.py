import pandas as pd
import shap
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier

# =========================
# Load Dataset
# =========================

df = pd.read_csv("Data/social_media_processed.csv")

# Remove leakage columns
df = df.drop(columns=[
    "user_id",
    "account_join_date",
    "addiction_score"
])

# =========================
# Encode Categorical Columns
# =========================

for col in df.select_dtypes(include="object").columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# =========================
# Features and Target
# =========================

X = df.drop(columns=["risk_level"])
y = df["risk_level"]

# =========================
# Train Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# SMOTE
# =========================

smote = SMOTE(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(
    X_train,
    y_train
)

# =========================
# XGBoost Model
# =========================

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

print("Model trained successfully.")

# =========================
# SHAP DEBUG INFO
# =========================

print("\nModel Type:")
print(type(model))

print("\nX_test Shape:")
print(X_test.shape)

# =========================
# SHAP EXPLAINER
# =========================

try:

    explainer = shap.Explainer(
        model.predict,
        X_train_smote
    )

    shap_values = explainer(
        X_test.iloc[:100]
    )

    print("\nSHAP Values Generated Successfully!")

    shap.plots.beeswarm(
        shap_values,
        max_display=15
    )

    plt.show()

except Exception as e:

    print("\nSHAP ERROR:")
    print(e)