import pandas as pd

df = pd.read_csv("Data/social_media_user_behavior.csv")

# Basic Addiction Score
df["addiction_score"] = (
    (df["daily_usage_hours"] * 25) +
    (df["sessions_per_day"] * 1.5) +
    (df["avg_session_duration_min"] * 0.2)
)

# Normalize score between 0 and 100
df["addiction_score"] = (
    (df["addiction_score"] - df["addiction_score"].min())
    / (df["addiction_score"].max() - df["addiction_score"].min())
) * 100

print(df["addiction_score"].describe())