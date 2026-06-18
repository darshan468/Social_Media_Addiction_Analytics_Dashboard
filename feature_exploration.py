import pandas as pd

df = pd.read_csv("Data/social_media_user_behavior.csv")

columns = [
    "sleep_disruption",
    "screen_time_concern",
    "mood_while_scrolling",
    "takes_social_media_breaks",
    "scroll_speed",
    "notification_frequency"
]

for col in columns:
    print(f"\n===== {col.upper()} =====")
    print(df[col].value_counts())