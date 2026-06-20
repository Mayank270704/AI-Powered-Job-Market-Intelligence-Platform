import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Company Intelligence",
    page_icon="🏢",
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

companies = pd.read_csv(
    BASE_DIR / "data" / "raw" / "companies.csv"
)

merged = jobs.merge(
    companies[["company_id", "name", "city", "country"]],
    on="company_id",
    how="left"
)

# =====================================================
# TOP COMPANY
# =====================================================

top_company_series = merged["name"].value_counts()

top_company = top_company_series.index[0]
top_jobs = top_company_series.iloc[0]

# =====================================================
# HERO
# =====================================================

st.markdown(
    """
    <div class='hero-title'>
    🏢 Company Intelligence Center
    </div>

    <div class='hero-sub'>
    Analyze recruiters, hiring activity,
    company locations and market concentration.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# KPI CARDS
# =====================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{companies['company_id'].nunique():,}</h2>
        <p>Total Companies</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{len(jobs):,}</h2>
        <p>Total Jobs</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{companies['city'].nunique():,}</h2>
        <p>Cities</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{top_company[:15]}</h2>
        <p>Top Recruiter</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =====================================================
# SEARCH COMPANY
# =====================================================

st.markdown(
    "<div class='section-title'>🔎 Company Explorer</div>",
    unsafe_allow_html=True
)

search_company = st.text_input(
    "Search Company"
)

if search_company:

    filtered = merged[
        merged["name"].str.contains(
            search_company,
            case=False,
            na=False
        )
    ]

    st.metric(
        "Matching Jobs",
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
# TOP HIRING COMPANIES
# =====================================================

st.markdown(
    "<div class='section-title'>🏆 Top Hiring Companies</div>",
    unsafe_allow_html=True
)

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
    template="plotly_dark",
    title="Top Hiring Companies"
)

fig_companies.update_layout(
    height=550
)

st.plotly_chart(
    fig_companies,
    use_container_width=True
)

# =====================================================
# PIE CHART
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
    hole=.55,
    template="plotly_dark",
    title="Market Share of Top Recruiters"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

# =====================================================
# COMPANY TABLE
# =====================================================

st.markdown(
    "<div class='section-title'>📋 Recruiter Ranking</div>",
    unsafe_allow_html=True
)

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

ranking_df.index += 1

st.dataframe(
    ranking_df,
    use_container_width=True
)

# =====================================================
# COMPANY LOCATION ANALYSIS
# =====================================================

st.markdown(
    "<div class='section-title'>🌎 Company Locations</div>",
    unsafe_allow_html=True
)

city_counts = (
    companies["city"]
    .value_counts()
    .head(15)
    .reset_index()
)

city_counts.columns = [
    "City",
    "Companies"
]

fig_city = px.bar(
    city_counts,
    x="City",
    y="Companies",
    template="plotly_dark",
    title="Top Company Cities"
)

fig_city.update_layout(
    height=550
)

st.plotly_chart(
    fig_city,
    use_container_width=True
)

# =====================================================
# INSIGHTS
# =====================================================

st.markdown("---")

st.success(
    f"""
📈 Company Market Insights

• Top recruiter: {top_company}

• Job postings by top recruiter: {top_jobs:,}

• Total companies analyzed: {companies['company_id'].nunique():,}

• Total jobs analyzed: {len(jobs):,}

• Hiring activity is concentrated among a small number of dominant employers.
"""
)