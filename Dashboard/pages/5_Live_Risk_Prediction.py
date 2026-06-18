import streamlit as st
import pandas as pd
import joblib

# ==========================
# Page Configuration
# ==========================

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
    page_title="Live Risk Prediction",
    layout="wide"
)

load_css()

st.markdown("""
<div class="main-title">
⚡ Live Risk Prediction
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================
# Load Model
# ==========================

model = joblib.load("Models/xgboost_model.pkl")

# ==========================
# User Inputs
# ==========================

st.subheader("Enter User Behavior Data")

daily_usage_hours = st.slider(
    "Daily Usage Hours",
    0.0, 12.0, 3.0
)

sessions_per_day = st.slider(
    "Sessions Per Day",
    1, 20, 5
)

avg_session_duration_min = st.slider(
    "Average Session Duration (Minutes)",
    1, 300, 30
)

sleep_score = st.slider(
    "Sleep Disruption Score",
    0, 3, 1
)

screen_score = st.slider(
    "Screen Time Concern Score",
    0, 2, 1
)

break_score = st.slider(
    "Social Media Break Score",
    0, 2, 1
)

# ==========================
# Predict Button
# ==========================

if st.button("Predict Risk Level"):

    # Create input row
    input_data = pd.DataFrame([{
        "daily_usage_hours": daily_usage_hours,
        "sessions_per_day": sessions_per_day,
        "avg_session_duration_min": avg_session_duration_min,
        "sleep_score": sleep_score,
        "screen_score": screen_score,
        "break_score": break_score
    }])

    # IMPORTANT:
    # The saved model expects all training features.
    # We add missing columns with default values.

    expected_features = model.feature_names_in_

    for col in expected_features:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[expected_features]

    prediction = model.predict(input_data)[0]

    st.markdown("---")

    if prediction == 0:
        st.success("🟢 LOW RISK USER")

    elif prediction == 1:
        st.info("🟡 MEDIUM RISK USER")

    elif prediction == 2:
        st.warning("🟠 HIGH RISK USER")

    else:
        st.error("🔴 SEVERE RISK USER")