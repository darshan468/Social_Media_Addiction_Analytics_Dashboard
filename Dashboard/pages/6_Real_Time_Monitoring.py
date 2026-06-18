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
    page_title="Real-Time Monitoring",
    page_icon="📡",
    layout="wide"
)

load_css()

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="main-title">
📡 Real-Time Monitoring
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="banner">
Live User Activity & Streaming Analytics
</div>
""", unsafe_allow_html=True)

st.markdown(
    "<div style='height:30px;'></div>",
    unsafe_allow_html=True
)

# ==========================================
# LOAD STREAM DATA
# ==========================================

file_path = "Streaming/live_predictions.csv"

try:

    df = pd.read_csv(file_path)

    # ==========================================
    # KPI SECTION
    # ==========================================

    avg_usage = round(
        df["daily_usage_hours"].mean(),
        2
    )

    col1, gap, col2 = st.columns(
        [1, 0.08, 1]
    )

    with col1:

        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">👥</div>
            <div class="kpi-title">
                Streamed Users
            </div>
            <div class="kpi-value">
                {len(df):,}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">⏳</div>
            <div class="kpi-title">
                Average Daily Usage
            </div>
            <div class="kpi-value">
                {avg_usage}
            </div>
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
    # DATA PREVIEW
    # ==========================================

    st.markdown(
        "## 📋 Latest Streamed Records"
    )

    st.dataframe(
        df.tail(20),
        use_container_width=True
    )

    st.markdown("---")

    # ==========================================
    # LIVE USAGE TREND
    # ==========================================

    st.markdown(
        "## 📈 Live Usage Trend"
    )

    chart_data = (
        df[["daily_usage_hours"]]
        .reset_index()
    )

    fig = px.line(
        chart_data,
        x="index",
        y="daily_usage_hours",
        markers=True
    )

    fig.update_traces(
        line=dict(
            width=3,
            color="#3B82F6"
        )
    )

    fig.update_layout(
        **chart_layout,

        xaxis_title="Stream Index",

        yaxis_title="Daily Usage Hours",

        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================================
    # STREAM INSIGHTS
    # ==========================================

    st.markdown(
        "## 📌 Real-Time Insights"
    )

    st.info(
        f"""
👥 Total Streamed Users: {len(df)}

⏳ Average Daily Usage: {avg_usage} Hours

📈 Highest Usage:
{round(df['daily_usage_hours'].max(),2)} Hours

📉 Lowest Usage:
{round(df['daily_usage_hours'].min(),2)} Hours

📊 Monitoring live behavioral activity in real time.
        """
    )

    st.markdown("---")

    # ==========================================
    # FOOTER
    # ==========================================

    st.caption(
        "📡 Real-Time Monitoring Module | Live User Analytics"
    )

except Exception as e:

    st.warning(
        "⚠ Waiting for streaming data..."
    )

    st.write(e)