import streamlit as st
import pandas as pd
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="AI Job Market Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Job Market Intelligence Dashboard")
st.markdown("---")

# =====================================================
# LOAD DATA
# =====================================================
BASE_DIR = Path(__file__).resolve().parent.parent

jobs = pd.read_csv(
    BASE_DIR / "data" / "raw" / "job_postings.csv"
)

companies = pd.read_csv(
    BASE_DIR / "data" / "raw" / "companies.csv"
)

skills = pd.read_csv(
    BASE_DIR / "data" / "raw" / "job_skills.csv"
)

# =====================================================
# SIDEBAR FILTERS
# =====================================================
st.sidebar.header("🔍 Dashboard Filters")

selected_location = st.sidebar.selectbox(
    "Select Location",
    ["All"] + sorted(
        jobs["location"].dropna().unique().tolist()
    )
)

if selected_location != "All":
    jobs = jobs[
        jobs["location"] == selected_location
    ]

# =====================================================
# KPI METRICS
# =====================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Jobs",
        f"{len(jobs):,}"
    )

with col2:
    st.metric(
        "Total Companies",
        f"{companies['company_id'].nunique():,}"
    )

with col3:
    remote_percent = round(
        jobs["remote_allowed"]
        .fillna(0)
        .mean() * 100,
        2
    )

    st.metric(
        "Remote Jobs %",
        f"{remote_percent}%"
    )

with col4:
    st.metric(
        "Locations",
        jobs["location"].nunique()
    )

st.markdown("---")

# =====================================================
# TOP HIRING LOCATIONS
# =====================================================
st.subheader("📍 Top Hiring Locations")

location_counts = (
    jobs["location"]
    .value_counts()
    .head(10)
)

st.bar_chart(location_counts)

# =====================================================
# WORK TYPE DISTRIBUTION
# =====================================================
st.subheader("💼 Work Type Distribution")

work_type = (
    jobs["formatted_work_type"]
    .value_counts()
)

st.bar_chart(work_type)

# =====================================================
# TOP HIRING COMPANIES
# =====================================================
st.subheader("🏢 Top Hiring Companies")

merged = jobs.merge(
    companies[["company_id", "name"]],
    on="company_id",
    how="left"
)

company_counts = (
    merged["name"]
    .value_counts()
    .head(10)
)

st.bar_chart(company_counts)

# =====================================================
# REMOTE VS ONSITE
# =====================================================
st.subheader("🏠 Remote vs On-Site Jobs")

remote_data = (
    jobs["remote_allowed"]
    .fillna(0)
    .replace({
        0: "On-Site",
        1: "Remote"
    })
    .value_counts()
)

st.bar_chart(remote_data)

# =====================================================
# AI / ANALYTICS JOBS
# =====================================================
st.subheader("🤖 AI & Analytics Jobs")

ai_jobs = jobs[
    jobs["title"].str.contains(
        "Data Scientist|Data Analyst|Business Analyst|Machine Learning|Data Engineer|AI Engineer",
        case=False,
        na=False
    )
]

st.metric(
    "AI / Analytics Openings",
    f"{len(ai_jobs):,}"
)

# =====================================================
# TOP AI JOB LOCATIONS
# =====================================================
st.subheader("🌎 Top AI Hiring Locations")

ai_locations = (
    ai_jobs["location"]
    .value_counts()
    .head(10)
)

st.bar_chart(ai_locations)

# =====================================================
# TOP AI JOB TITLES
# =====================================================
st.subheader("🧠 Most Common AI Job Titles")

ai_titles = (
    ai_jobs["title"]
    .value_counts()
    .head(10)
)

st.bar_chart(ai_titles)

# =====================================================
# TOP AI HIRING COMPANIES
# =====================================================
st.subheader("🏆 Top AI Hiring Companies")

ai_merged = ai_jobs.merge(
    companies[["company_id", "name"]],
    on="company_id",
    how="left"
)

ai_company_counts = (
    ai_merged["name"]
    .value_counts()
    .head(10)
)

st.bar_chart(ai_company_counts)

# =====================================================
# AI JOBS VS OTHER JOBS
# =====================================================
st.subheader("📊 AI Jobs vs Other Jobs")

comparison = pd.Series({
    "AI Jobs": len(ai_jobs),
    "Other Jobs": len(jobs) - len(ai_jobs)
})

st.bar_chart(comparison)

# =====================================================
# SALARY ANALYSIS
# =====================================================
st.subheader("💰 Salary Analysis")

salary_data = jobs["max_salary"].dropna()

if len(salary_data) > 0:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Salary",
            f"${salary_data.mean():,.0f}"
        )

    with col2:
        st.metric(
            "Highest Salary",
            f"${salary_data.max():,.0f}"
        )

    with col3:
        st.metric(
            "Lowest Salary",
            f"${salary_data.min():,.0f}"
        )

else:
    st.warning("No salary information available.")

# =====================================================
# TOP SKILLS DEMAND
# =====================================================
st.subheader("🧠 Top Skills Categories")

skill_counts = (
    skills["skill_abr"]
    .value_counts()
    .head(15)
)

st.bar_chart(skill_counts)

# =====================================================
# JOB TITLE SEARCH
# =====================================================
st.subheader("🔎 Search Jobs")

search_term = st.text_input(
    "Enter Job Title"
)

if search_term:

    filtered_jobs = jobs[
        jobs["title"].str.contains(
            search_term,
            case=False,
            na=False
        )
    ]

    st.write(
        f"Found {len(filtered_jobs)} matching jobs"
    )

    st.dataframe(
        filtered_jobs[
            [
                "title",
                "location",
                "formatted_work_type"
            ]
        ].head(50),
        use_container_width=True
    )

# =====================================================
# DATA PREVIEW
# =====================================================
st.subheader("📄 Sample Job Records")

st.dataframe(
    jobs[
        [
            "title",
            "location",
            "formatted_work_type"
        ]
    ].head(20),
    use_container_width=True
)

st.markdown("---")
st.success("Dashboard Loaded Successfully ✅")