import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# LOAD CSS
# ==========================================

def load_css():
    try:
        with open("Dashboard/styles/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Anomaly Detection",
    page_icon="🚨",
    layout="wide"
)

load_css()

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="main-title">
🚨 Anomaly Detection
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="banner">
Isolation Forest Based User Behavior Analysis
</div>
""", unsafe_allow_html=True)

st.markdown(
    "<div style='height:30px;'></div>",
    unsafe_allow_html=True
)

# ==========================================
# KPI SECTION
# ==========================================

col1, gap, col2 = st.columns([1, 0.08, 1])

normal_users = 1900
anomalies = 100

with col1:

    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">✅</div>
        <div class="kpi-title">Normal Users</div>
        <div class="kpi-value">{normal_users:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">🚨</div>
        <div class="kpi-title">Anomalous Users</div>
        <div class="kpi-value">{anomalies:,}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# COMMON CHART STYLE
# ==========================================

chart_layout = dict(

    paper_bgcolor="#1E2538",

    plot_bgcolor="#1E2538",

    font=dict(
        color="#E5E7EB",
        family="Inter",
        size=14
    ),

    margin=dict(
        l=30,
        r=30,
        t=50,
        b=30
    ),

    xaxis=dict(
        showgrid=False,
        zeroline=False
    ),

    yaxis=dict(
        gridcolor="rgba(255,255,255,0.08)",
        zeroline=False
    )
)

# ==========================================
# PIE CHART
# ==========================================

st.markdown("## 📊 Normal vs Anomalous Users")

anomaly_df = pd.DataFrame({
    "Category": ["Normal", "Anomaly"],
    "Count": [1900, 100]
})

fig = px.pie(
    anomaly_df,
    values="Count",
    names="Category",
    hole=0.45,
    color="Category",
    color_discrete_map={
        "Normal": "#3B82F6",
        "Anomaly": "#EF4444"
    }
)

fig.update_traces(
    marker_line_width=2,
    marker_line_color="#0A0F1C",
    textfont_color="white"
)

fig.update_layout(

    **chart_layout,

    legend=dict(
        orientation="v",
        yanchor="middle",
        y=0.5,
        xanchor="right",
        x=0.98,
        font=dict(
            color="white"
        )
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# BAR CHART
# ==========================================

st.markdown("## 📈 User Category Distribution")

fig = px.bar(
    anomaly_df,
    x="Category",
    y="Count",
    color="Category",
    text="Count",
    color_discrete_map={
        "Normal": "#3B82F6",
        "Anomaly": "#EF4444"
    }
)

fig.update_traces(
    marker_line_width=1,
    marker_line_color="#0A0F1C",
    textposition="outside"
)

fig.update_layout(
    **chart_layout,
    showlegend=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# INSIGHTS
# ==========================================

st.markdown("## 📌 Anomaly Insights")

st.warning(
    """
🚨 Isolation Forest identified **100 anomalous users**.

### Common Patterns

• Extremely high daily usage hours

• Longer than average session duration

• Unusual engagement frequency

• Elevated addiction risk indicators

• Abnormal platform interaction behavior

### Recommendation

These users should be prioritized for intervention,
behavioral monitoring and addiction prevention programs.
"""
)

st.markdown("---")

# ==========================================
# BUSINESS IMPACT
# ==========================================

st.markdown("## 💡 Business Impact")

st.info(
    """
This anomaly detection system helps identify unusual user behavior patterns.

Potential applications:

• Digital Wellbeing Platforms

• Mental Health Monitoring

• User Risk Profiling

• Addiction Prevention Systems

• Real-Time Behavioral Alerts

Isolation Forest enables scalable unsupervised detection
without requiring labeled anomaly data.
"""
)

st.markdown("---")

# ==========================================
# FOOTER
# ==========================================

st.caption(
    "🚨 Anomaly Detection Module | Isolation Forest Analytics"
)