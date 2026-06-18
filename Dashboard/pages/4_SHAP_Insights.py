import streamlit as st
import pandas as pd
import plotly.express as px

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
    page_title="SHAP Insights",
    layout="wide"
)

load_css()

st.markdown("""
<div class="main-title">
🧠 Explainable AI (SHAP)
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="banner">
Explainable Artificial Intelligence
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.subheader("Top Features Influencing Addiction Risk")

shap_df = pd.DataFrame({
    "Feature": [
        "daily_usage_hours",
        "posts_per_week",
        "avg_session_duration_min",
        "screen_time_concern",
        "takes_social_media_breaks",
        "sleep_score"
    ],
    "Importance": [
        1.00,
        0.72,
        0.65,
        0.52,
        0.43,
        0.38
    ]
})

fig = px.bar(
    shap_df,
    x="Importance",
    y="Feature",
    orientation="h",
    title="SHAP Feature Importance"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.success("""
Key Findings:

• Daily usage hours is the strongest addiction predictor.

• Posting frequency significantly affects addiction behavior.

• Long session duration increases addiction risk.

• Screen-time concern is an important behavioral signal.

• Sleep-related factors contribute to addiction prediction.
""")

st.info("""
SHAP (SHapley Additive Explanations) was used to explain
why the XGBoost model classified users into different
addiction risk levels.
""")