import pandas as pd

df = pd.read_csv("Data/social_media_processed.csv")

correlation_columns = [
    "daily_usage_hours",
    "sessions_per_day",
    "avg_session_duration_min",
    "sleep_score",
    "screen_score",
    "break_score",
    "self_reported_mental_health_score",
    "addiction_score"
]

print(
    df[correlation_columns]
    .corr()["addiction_score"]
    .sort_values(ascending=False)
)