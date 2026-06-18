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
    page_title="User Segmentation",
    layout="wide"
)

load_css()

st.markdown("""
<div class="main-title">
👥 User Segmentation (K-Means)
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="banner">
User Behavior Clustering Analysis
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Cluster counts from your results

cluster_df = pd.DataFrame({
    "Cluster": ["Cluster 0", "Cluster 1", "Cluster 2", "Cluster 3"],
    "Users": [687, 637, 231, 445]
})

fig = px.pie(
    cluster_df,
    values="Users",
    names="Cluster",
    title="Cluster Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

cluster_summary = pd.DataFrame({

    "Cluster": [
        "Cluster 0",
        "Cluster 1",
        "Cluster 2",
        "Cluster 3"
    ],

    "Description": [
        "Concerned Users",
        "Casual Users",
        "High-Risk Users",
        "Sleep-Affected Users"
    ],

    "Users": [
        687,
        637,
        231,
        445
    ]
})

st.subheader("Cluster Profiles")

st.dataframe(
    cluster_summary,
    use_container_width=True
)

st.success(
    """
    Cluster 2 represents High-Risk Users with
    the highest daily usage hours and longest sessions.

    Cluster 1 represents Casual Users with
    the lowest sleep disruption and screen-time concern.
    """
)