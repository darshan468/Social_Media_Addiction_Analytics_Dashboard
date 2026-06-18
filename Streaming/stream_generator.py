import pandas as pd
import time
import random

# Load original dataset
df = pd.read_csv("Data/social_media_processed.csv")

output_file = "Streaming/live_predictions.csv"

# Create empty file first
df.iloc[0:0].to_csv(output_file, index=False)

print("Streaming started...")

while True:

    random_row = df.sample(1)

    random_row.to_csv(
        output_file,
        mode="a",
        header=False,
        index=False
    )

    print(
        f"Streamed User: {random_row['user_id'].values[0]}"
    )

    time.sleep(2)