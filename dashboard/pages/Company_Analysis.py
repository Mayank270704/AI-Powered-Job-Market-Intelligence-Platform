import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Company Analysis",
    page_icon="🏢",
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

merged = jobs.merge(
    companies[["company_id", "name"]],
    on="company_id",
    how="left"
)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
# 🏢 Company Analysis

Explore hiring activity,
top recruiters,
and company-level demand trends.

---
""")

# =====================================================
# KPI CARDS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🏢 Total Companies",
        f"{companies['company_id'].nunique():,}"
    )

with col2:
    st.metric(
        "💼 Total Jobs",
        f"{len(jobs):,}"
    )

with col3:
    st.metric(
        "🌎 Hiring Locations",
        jobs["location"].nunique()
    )

st.markdown("---")

# =====================================================
# TOP HIRING COMPANIES
# =====================================================

company_counts = (
    merged["name"]
    .value_counts()
    .head(15)
    .reset_index()
)

company_counts.columns = [
    "Company",
    "Jobs"
]

fig_companies = px.bar(
    company_counts,
    x="Company",
    y="Jobs",
    title="🏆 Top Hiring Companies",
    template="plotly_dark"
)

fig_companies.update_layout(
    height=550
)

st.plotly_chart(
    fig_companies,
    use_container_width=True
)

# =====================================================
# COMPANY HIRING SHARE
# =====================================================

top10 = (
    merged["name"]
    .value_counts()
    .head(10)
    .reset_index()
)

top10.columns = [
    "Company",
    "Jobs"
]

fig_pie = px.pie(
    top10,
    names="Company",
    values="Jobs",
    hole=0.45,
    title="📊 Hiring Share by Company",
    template="plotly_dark"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

# =====================================================
# TOP RECRUITERS TABLE
# =====================================================

st.subheader("📋 Top Recruiters")

ranking_df = (
    merged["name"]
    .value_counts()
    .head(20)
    .reset_index()
)

ranking_df.columns = [
    "Company",
    "Job Postings"
]

ranking_df.index = ranking_df.index + 1

st.dataframe(
    ranking_df,
    use_container_width=True
)

# =====================================================
# SEARCH COMPANY
# =====================================================

st.subheader("🔍 Search Company")

search_company = st.text_input(
    "Enter Company Name"
)

if search_company:

    filtered = merged[
        merged["name"]
        .str.contains(
            search_company,
            case=False,
            na=False
        )
    ]

    st.metric(
        "Matching Job Postings",
        len(filtered)
    )

    st.dataframe(
        filtered[
            [
                "name",
                "title",
                "location"
            ]
        ].head(100),
        use_container_width=True
    )

# =====================================================
# TOP COMPANY LOCATIONS
# =====================================================

st.subheader("🌎 Hiring Locations Distribution")

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
    title="Top Hiring Locations",
    template="plotly_dark"
)

st.plotly_chart(
    fig_locations,
    use_container_width=True
)

# =====================================================
# INSIGHTS
# =====================================================

st.markdown("---")

top_company = company_counts.iloc[0]["Company"]
top_jobs = company_counts.iloc[0]["Jobs"]

st.success(
    f"""
📈 Company Hiring Insights

• Top recruiter: {top_company}

• Job postings by top recruiter: {top_jobs:,}

• Companies analyzed: {companies['company_id'].nunique():,}

• Total jobs analyzed: {len(jobs):,}

• Hiring activity is concentrated among a small group of leading employers.
"""
)