import pandas as pd

df = pd.read_csv("Data/social_media_user_behavior.csv")

sleep_map = {
    "No impact": 0,
    "Mild impact": 1,
    "Moderate impact": 2,
    "Severe impact": 3
}

screen_map = {
    "No": 0,
    "Somewhat": 1,
    "Yes": 2
}

break_map = {
    "Yes": 0,
    "Occasionally": 1,
    "No": 2
}

df["sleep_score"] = df["sleep_disruption"].map(sleep_map)
df["screen_score"] = df["screen_time_concern"].map(screen_map)
df["break_score"] = df["takes_social_media_breaks"].map(break_map)

df["addiction_score"] = (
    df["daily_usage_hours"] * 20 +
    df["sessions_per_day"] * 1.5 +
    df["avg_session_duration_min"] * 0.2 +
    df["sleep_score"] * 10 +
    df["screen_score"] * 10 +
    df["break_score"] * 10
)

df["addiction_score"] = (
    (df["addiction_score"] - df["addiction_score"].min())
    /
    (df["addiction_score"].max() - df["addiction_score"].min())
) * 100

def risk_level(score):
    if score < 25:
        return "Low"
    elif score < 50:
        return "Medium"
    elif score < 75:
        return "High"
    else:
        return "Severe"

df["risk_level"] = df["addiction_score"].apply(risk_level)

df.to_csv("Data/social_media_processed.csv", index=False)

print("Processed dataset saved successfully!")