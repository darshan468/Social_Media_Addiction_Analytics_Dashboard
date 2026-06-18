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

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Machine Learning Insights",
    page_icon="🤖",
    layout="wide"
)

load_css()

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="main-title">
🤖 Machine Learning Insights
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="banner">
Model Performance & Feature Analysis
</div>
""", unsafe_allow_html=True)

# Space between Banner and KPI Cards

st.markdown(
    "<div style='height:40px;'></div>",
    unsafe_allow_html=True
)

# ==========================================
# KPI SECTION
# ==========================================

st.markdown("<div style='height:25px;'></div>", unsafe_allow_html=True)

col1, gap1, col2, gap2, col3, gap3, col4 = st.columns(
    [1,0.08,1,0.08,1,0.08,1]
)

with col1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-icon">🌲</div>
        <div class="kpi-title">Random Forest</div>
        <div class="kpi-value">87.75%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-icon">🚀</div>
        <div class="kpi-title">XGBoost</div>
        <div class="kpi-value">93.25%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-icon">📈</div>
        <div class="kpi-title">Accuracy Gain</div>
        <div class="kpi-value">+5.5%</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-icon">🎯</div>
        <div class="kpi-title">Best Model</div>
        <div class="kpi-value">XGBoost</div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# MODEL COMPARISON
# ==========================================

st.subheader("📊 Model Performance Comparison")

comparison_df = pd.DataFrame({
    "Model": [
        "Random Forest",
        "XGBoost"
    ],
    "Accuracy": [
        87.75,
        93.25
    ]
})

fig = px.bar(
    comparison_df,
    x="Model",
    y="Accuracy",
    text="Accuracy",
    color="Model"
)

fig.update_traces(
    textposition="outside"
)

fig.update_layout(
    showlegend=False,
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# FEATURE IMPORTANCE
# ==========================================

st.subheader("🔥 Top Features Influencing Addiction Risk")

importance_df = pd.DataFrame({
    "Feature": [
        "daily_usage_hours",
        "avg_session_duration_min",
        "sessions_per_day",
        "ad_click_rate",
        "followers_count",
        "sleep_score"
    ],
    "Importance": [
        0.379913,
        0.182539,
        0.034905,
        0.022136,
        0.021968,
        0.020474
    ]
})

fig = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance"
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# MODEL INSIGHTS
# ==========================================

st.subheader("📌 Key Findings")

st.success("""
✅ Daily Usage Hours is the strongest predictor of addiction risk.

✅ Longer Session Duration significantly increases addiction probability.

✅ Sleep Disruption is strongly associated with higher addiction levels.

✅ XGBoost achieved the highest accuracy (93.25%).

✅ Behavioral features outperform demographic features in prediction.
""")

st.markdown("---")

# ==========================================
# BUSINESS IMPACT
# ==========================================

st.subheader("💡 Analytics Impact")

st.info("""
This machine learning pipeline helps identify users at risk of social media addiction.

The model can be integrated into:
- Social media wellness tools
- Digital wellbeing applications
- Mental health monitoring systems
- Educational awareness platforms

The explainable AI framework ensures prediction transparency and trust.
""")