import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("Data/social_media_processed.csv")

# Features for anomaly detection
features = [
    "daily_usage_hours",
    "sessions_per_day",
    "avg_session_duration_min",
    "sleep_score",
    "screen_score",
    "break_score"
]

X = df[features]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Isolation Forest
model = IsolationForest(
    contamination=0.05,   # 5% anomalies
    random_state=42
)

df["anomaly"] = model.fit_predict(X_scaled)

# Convert labels
df["anomaly"] = df["anomaly"].map({
    1: "Normal",
   -1: "Anomaly"
})

# Results
print(df["anomaly"].value_counts())

# Show anomaly samples
print("\nSample Anomalies:\n")

print(
    df[df["anomaly"] == "Anomaly"][
        [
            "daily_usage_hours",
            "sessions_per_day",
            "avg_session_duration_min",
            "sleep_score",
            "screen_score",
            "break_score"
        ]
    ].head(10)
)