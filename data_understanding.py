import pandas as pd

df1 = pd.read_csv("Data/social_media_user_behavior.csv")
df2 = pd.read_csv("Data/social_media_addiction.csv")

print("\n===== DATASET 1 INFO =====")
print(df1.info())

print("\n===== DATASET 1 MISSING VALUES =====")
print(df1.isnull().sum())

print("\n===== DATASET 2 INFO =====")
print(df2.info())

print("\n===== DATASET 2 MISSING VALUES =====")
print(df2.isnull().sum())