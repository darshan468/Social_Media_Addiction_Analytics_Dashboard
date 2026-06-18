import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("Data/social_media_processed.csv")

# Features for clustering
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

# KMeans with K=4
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["cluster"] = kmeans.fit_predict(X_scaled)

# Cluster counts
print(df["cluster"].value_counts())

# Cluster centers
cluster_summary = df.groupby("cluster")[features].mean()

print("\nCluster Summary:")
print(cluster_summary)