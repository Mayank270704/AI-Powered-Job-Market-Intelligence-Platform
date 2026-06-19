import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Jobs Intelligence",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

h1,h2,h3 {
    color:white;
}

[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

jobs = pd.read_csv(
    BASE_DIR / "data" / "raw" / "job_postings.csv"
)

companies = pd.read_csv(
    BASE_DIR / "data" / "raw" / "companies.csv"
)

# =====================================================
# AI JOB FILTER
# =====================================================

ai_jobs = jobs[
    jobs["title"].str.contains(
        "Data Scientist|Data Analyst|Business Analyst|Machine Learning|Data Engineer|AI Engineer",
        case=False,
        na=False
    )
]

# =====================================================
# HERO
# =====================================================

st.markdown("""
# 🤖 AI Jobs Intelligence

Discover where AI hiring is happening,
which companies are recruiting,
and which AI roles dominate the market.

---
""")

# =====================================================
# KPI SECTION
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🤖 AI Openings",
        f"{len(ai_jobs):,}"
    )

with col2:
    st.metric(
        "🌎 AI Locations",
        ai_jobs["location"].nunique()
    )

with col3:
    st.metric(
        "🏢 AI Companies",
        ai_jobs["company_id"].nunique()
    )

st.markdown("---")

# =====================================================
# TOP AI LOCATIONS
# =====================================================

locations = (
    ai_jobs["location"]
    .value_counts()
    .head(10)
    .reset_index()
)

locations.columns = [
    "Location",
    "Jobs"
]

fig_locations = px.bar(
    locations,
    x="Location",
    y="Jobs",
    title="🌎 Top AI Hiring Locations",
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
# TOP AI JOB TITLES
# =====================================================

titles = (
    ai_jobs["title"]
    .value_counts()
    .head(10)
    .reset_index()
)

titles.columns = [
    "Role",
    "Count"
]

fig_titles = px.bar(
    titles,
    x="Role",
    y="Count",
    title="🧠 Most Common AI Job Titles",
    template="plotly_dark"
)

fig_titles.update_layout(
    height=500
)

st.plotly_chart(
    fig_titles,
    use_container_width=True
)

# =====================================================
# TOP AI COMPANIES
# =====================================================

ai_merged = ai_jobs.merge(
    companies[["company_id", "name"]],
    on="company_id",
    how="left"
)

top_companies = (
    ai_merged["name"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_companies.columns = [
    "Company",
    "Jobs"
]

fig_companies = px.bar(
    top_companies,
    x="Company",
    y="Jobs",
    title="🏆 Top AI Hiring Companies",
    template="plotly_dark"
)

fig_companies.update_layout(
    height=500
)

st.plotly_chart(
    fig_companies,
    use_container_width=True
)

# =====================================================
# AI VS OTHER JOBS
# =====================================================

comparison = pd.DataFrame({
    "Category": [
        "AI Jobs",
        "Other Jobs"
    ],
    "Count": [
        len(ai_jobs),
        len(jobs) - len(ai_jobs)
    ]
})

fig_compare = px.pie(
    comparison,
    names="Category",
    values="Count",
    title="📊 AI Jobs vs Other Jobs",
    hole=0.5,
    template="plotly_dark"
)

st.plotly_chart(
    fig_compare,
    use_container_width=True
)

# =====================================================
# INSIGHTS
# =====================================================

st.markdown("---")

top_role = titles.iloc[0]["Role"]
top_location = locations.iloc[0]["Location"]

st.success(
    f"""
📈 AI Market Insights

• Most demanded AI role: {top_role}

• Strongest hiring region: {top_location}

• Total AI opportunities: {len(ai_jobs):,}

• AI hiring is concentrated among a small group of companies.
"""
)