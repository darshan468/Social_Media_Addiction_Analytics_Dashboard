import pandas as pd

df1 = pd.read_csv("Data/social_media_user_behavior.csv")
df2 = pd.read_csv("Data/social_media_addiction.csv")

print("Dataset 1 Shape:", df1.shape)
print("Dataset 2 Shape:", df2.shape)

print("\nDataset 1 Columns:")
print(df1.columns)

print("\nDataset 2 Columns:")
print(df2.columns)