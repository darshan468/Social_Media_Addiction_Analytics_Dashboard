import pandas as pd

df = pd.read_csv("Data/social_media_user_behavior.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nGender Distribution:")
print(df["gender"].value_counts())

print("\nTop 10 Countries:")
print(df["country"].value_counts().head(10))

print("\nPlatform Usage:")
print(df["primary_platform"].value_counts())

print("\nAverage Daily Usage Hours:")
print(df["daily_usage_hours"].mean())

print("\nAverage Mental Health Score:")
print(df["self_reported_mental_health_score"].mean())