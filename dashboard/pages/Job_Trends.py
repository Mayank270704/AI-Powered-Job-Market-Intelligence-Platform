import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Job Trends",
    page_icon="📈",
    layout="wide"
)

with open("dashboard/assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =====================================================
# CUSTOM CSS
# =====================================================

# =====================================================
# LOAD DATA
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

jobs = pd.read_csv(
    BASE_DIR / "data" / "raw" / "job_postings.csv"
)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
# 📈 Job Market Trends

Explore hiring demand, work arrangements,
and geographic hiring patterns.

---
""")

# =====================================================
# KPI CARDS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💼 Total Jobs",
        f"{len(jobs):,}"
    )

with col2:
    st.metric(
        "🌎 Locations",
        jobs["location"].nunique()
    )

with col3:
    remote_pct = round(
        jobs["remote_allowed"]
        .fillna(0)
        .mean() * 100,
        2
    )

    st.metric(
        "🏠 Remote %",
        f"{remote_pct}%"
    )

st.markdown("---")

# =====================================================
# TOP HIRING LOCATIONS
# =====================================================

location_counts = (
    jobs["location"]
    .value_counts()
    .head(10)
    .reset_index()
)

location_counts.columns = [
    "Location",
    "Jobs"
]

fig_locations = px.bar(
    location_counts,
    x="Location",
    y="Jobs",
    title="📍 Top Hiring Locations",
    template="plotly_dark"
)

fig_locations.update_layout(
    height=500
)

st.plotly_chart(
    fig_locations,
    use_container_width=True
)

# =====================================================
# WORK TYPE DISTRIBUTION
# =====================================================

work_type = (
    jobs["formatted_work_type"]
    .value_counts()
    .reset_index()
)

work_type.columns = [
    "Work Type",
    "Count"
]

fig_work = px.pie(
    work_type,
    names="Work Type",
    values="Count",
    title="💼 Work Type Distribution",
    hole=0.45,
    template="plotly_dark"
)

st.plotly_chart(
    fig_work,
    use_container_width=True
)

# =====================================================
# REMOTE VS ONSITE
# =====================================================

remote_data = (
    jobs["remote_allowed"]
    .fillna(0)
    .replace({
        0: "On-Site",
        1: "Remote"
    })
    .value_counts()
    .reset_index()
)

remote_data.columns = [
    "Type",
    "Count"
]

fig_remote = px.pie(
    remote_data,
    names="Type",
    values="Count",
    title="🏠 Remote vs On-Site Jobs",
    hole=0.5,
    template="plotly_dark"
)

st.plotly_chart(
    fig_remote,
    use_container_width=True
)

# =====================================================
# INSIGHTS
# =====================================================

st.markdown("---")

top_location = location_counts.iloc[0]["Location"]

st.success(
    f"""
    📊 Key Insight

    • Top hiring location: {top_location}

    • Remote opportunities represent {remote_pct}% of all jobs

    • Total locations hiring: {jobs['location'].nunique()}
    """
)