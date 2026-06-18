import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import os

# =====================================
# Page Configuration
# =====================================

def load_css():
    try:
        with open("Dashboard/styles/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass

load_css()

st.set_page_config(
    page_title="Live AI Predictions",
    layout="wide"
)

load_css()

st.markdown("""
<div class="main-title">
🤖 Live AI Predictions
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =====================================
# Check Required Files
# =====================================

MODEL_PATH = "Models/xgboost_model.pkl"
STREAM_PATH = "Streaming/live_predictions.csv"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found!")
    st.stop()

if not os.path.exists(STREAM_PATH):
    st.error("❌ Streaming file not found!")
    st.stop()

# =====================================
# Load Model
# =====================================

model = joblib.load(MODEL_PATH)

# =====================================
# Load Streaming Data
# =====================================

df = pd.read_csv(STREAM_PATH)

if df.empty:
    st.warning("⚠️ No streaming data available yet.")
    st.stop()

# =====================================
# Use Latest 50 Users
# =====================================

latest_users = df.tail(50).copy()

# =====================================
# Features Used For Prediction
# =====================================

prediction_features = [
    "daily_usage_hours",
    "sessions_per_day",
    "avg_session_duration_min",
    "sleep_score",
    "screen_score",
    "break_score"
]

prediction_df = latest_users[prediction_features].copy()

# =====================================
# Match Model Features
# =====================================

expected_features = model.feature_names_in_

for col in expected_features:
    if col not in prediction_df.columns:
        prediction_df[col] = 0

prediction_df = prediction_df[expected_features]

# =====================================
# Predictions
# =====================================

predictions = model.predict(prediction_df)

risk_map = {
    0: "Low Risk",
    1: "Medium Risk",
    2: "High Risk",
    3: "Severe Risk"
}

latest_users["Predicted Risk"] = [
    risk_map.get(pred, "Unknown")
    for pred in predictions
]

# =====================================
# KPIs
# =====================================

total_users = len(df)

high_risk_count = len(
    latest_users[
        latest_users["Predicted Risk"].isin(
            ["High Risk", "Severe Risk"]
        )
    ]
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Streamed Users",
    total_users
)

col2.metric(
    "Latest Users Analyzed",
    len(latest_users)
)

col3.metric(
    "High / Severe Risk Users",
    high_risk_count
)

st.markdown("---")

# =====================================
# Risk Distribution Chart
# =====================================

st.subheader("📊 Risk Distribution")

risk_counts = latest_users["Predicted Risk"].value_counts()

fig = px.pie(
    values=risk_counts.values,
    names=risk_counts.index,
    title="Predicted Risk Levels"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================
# Prediction Table
# =====================================

st.subheader("📋 Latest User Predictions")

display_cols = [
    "user_id",
    "daily_usage_hours",
    "sessions_per_day",
    "avg_session_duration_min",
    "Predicted Risk"
]

st.dataframe(
    latest_users[display_cols],
    use_container_width=True
)

st.markdown("---")

# =====================================
# Insights
# =====================================

st.success(
    """
    Live AI Prediction Engine

    • Uses trained XGBoost model

    • Predicts addiction risk in real time

    • Monitors recent user behavior

    • Identifies High-Risk and Severe-Risk users
    """
)