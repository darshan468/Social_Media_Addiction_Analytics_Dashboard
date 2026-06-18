import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Social Media Addiction Analytics Dashboard",
    page_icon="📱",
    layout="wide"
)

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
        st.warning("style.css file not found!")

load_css()

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown(
        """
        <div style='text-align:center;padding-top:10px;'>

        <h1 style='color:white;font-weight:700;'>
        📱 SMAD
        </h1>

        <p style='color:#9CA3AF;font-size:15px;'>
        Social Media Addiction Analytics Dashboard
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    
    st.markdown(
    """
    <div class="sidebar-footer">
        <p>Developed By</p>
        <h4>Darshan </h4>
    </div>
    """,
    unsafe_allow_html=True
    )
    
# ==========================================
# LOAD DATA
# ==========================================

try:
    df = pd.read_csv("Data/social_media_processed.csv")

except FileNotFoundError:

    st.error(
        "❌ Data/social_media_processed.csv not found!"
    )

    st.stop()

# ==========================================
# HEADER
# ==========================================

st.markdown(
    """
    <div class="main-title">
        📱 Social Media Addiction Analytics Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="banner">
        Real-Time Social Media Addiction Analytics & AI Risk Prediction Platform
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='height:15px;'></div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    ## 📈 Key Performance Indicators
    """
)

# ==========================================
# KPI SECTION
# ==========================================

col1, gap1, col2, gap2, col3, gap3, col4 = st.columns(
    [1, 0.08, 1, 0.08, 1, 0.08, 1]
)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">👥</div>
        <div class="kpi-title">Total Users</div>
        <div class="kpi-value">{len(df):,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">🎂</div>
        <div class="kpi-title">Average Age</div>
        <div class="kpi-value">{round(df['age'].mean(),1)}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">⏳</div>
        <div class="kpi-title">Avg Daily Usage</div>
        <div class="kpi-value">{round(df['daily_usage_hours'].mean(),2)}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">📊</div>
        <div class="kpi-title">Addiction Score</div>
        <div class="kpi-value">{round(df['addiction_score'].mean(),2)}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# PREMIUM DARK CHART THEME
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

    legend=dict(
        bgcolor="rgba(0,0,0,0)",
        font=dict(
            color="white",
            size=13
        ),
        orientation="v"
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
# FIRST ROW OF CHARTS
# ==========================================

col1, gap, col2 = st.columns([1, 0.12, 1])

# ------------------------------------------
# Risk Level Distribution
# ------------------------------------------

with col1:

    st.markdown("## 📊 Risk Level Distribution")

    risk_counts = df["risk_level"].value_counts()

    fig = px.pie(
        values=risk_counts.values,
        names=risk_counts.index,
        hole=0.45,
        color_discrete_sequence=px.colors.sequential.Blues_r
    )

    fig.update_traces(
        marker_line_width=2,
        marker_line_color="#0A0F1C",
        textfont_color="white"
    )

    fig.update_layout(
        **chart_layout,
        showlegend=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ------------------------------------------
# Platform Usage
# ------------------------------------------

with col2:

    st.markdown("## 📱 Platform Usage")

    platform_counts = df["primary_platform"].value_counts()

    fig = px.bar(
        x=platform_counts.index,
        y=platform_counts.values,
        color=platform_counts.values,
        color_continuous_scale="Blues"
    )

    fig.update_traces(
        marker_line_width=1,
        marker_line_color="#0A0F1C"
    )

    fig.update_layout(
        **chart_layout,
        coloraxis_showscale=False
    )

    fig.update_xaxes(
        tickangle=-30
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# SECOND ROW OF CHARTS
# ==========================================

col3, gap2, col4 = st.columns([1, 0.12, 1])

# ------------------------------------------
# Daily Usage Distribution
# ------------------------------------------

with col3:

    st.markdown("## ⏳ Daily Usage Hours")

    fig = px.histogram(
        df,
        x="daily_usage_hours",
        nbins=30,
        color_discrete_sequence=["#3B82F6"]
    )

    fig.update_traces(
        marker_line_width=1,
        marker_line_color="#0A0F1C"
    )

    fig.update_layout(
        **chart_layout,

        xaxis_title="Daily Usage Hours",

        yaxis_title="Users"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ------------------------------------------
# Risk Level Count
# ------------------------------------------

with col4:

    st.markdown("## 🚨 Risk Level Count")

    fig = px.bar(
        x=risk_counts.index,
        y=risk_counts.values,
        color=risk_counts.values,
        color_continuous_scale="Blues",
        labels={
            "x": "Risk Level",
            "y": "Users"
        }
    )

    fig.update_traces(
        marker_line_width=1,
        marker_line_color="#0A0F1C"
    )

    fig.update_layout(
        **chart_layout,

        coloraxis_showscale=False,

        xaxis_title="Risk Level",

        yaxis_title="Users"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# ==========================================
# CORRELATION HEATMAP
# ==========================================

st.markdown("## 🔥 Correlation Heatmap")

numeric_df = df.select_dtypes(
    include=["int64", "float64"]
)

corr = numeric_df.corr()

fig = px.imshow(
    corr,
    aspect="auto",
    text_auto=".2f",
    color_continuous_scale="Blues"
)

fig.update_layout(
    **chart_layout,

    coloraxis_colorbar=dict(
        tickfont=dict(
            color="#E5E7EB"
        )
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# DATASET PREVIEW
# ==========================================

st.markdown("## 📋 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.markdown("---")

# ==========================================
# PROJECT INSIGHTS
# ==========================================

st.markdown("## 📌 Project Insights")

high_risk_users = len(
    df[
        df["risk_level"].isin(
            ["High", "Severe"]
        )
    ]
)

st.info(
    f"""
    👥 Total Users Analyzed: {len(df)}

    🚨 High / Severe Risk Users: {high_risk_users}

    📊 Average Addiction Score: {round(df['addiction_score'].mean(), 2)}

    ⏳ Average Daily Usage: {round(df['daily_usage_hours'].mean(), 2)} hours

    📱 Most Used Platform: {df['primary_platform'].mode()[0]}
    """
)

st.markdown("---")

# ==========================================
# FOOTER
# ==========================================

st.caption(
    "📱 Social Media Addiction Analytics Dashboard | Built with Python, Streamlit, XGBoost, SHAP, K-Means & Isolation Forest"
)
