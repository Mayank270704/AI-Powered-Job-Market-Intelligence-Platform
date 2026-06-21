import streamlit as st
import pandas as pd
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Job Market Intelligence",
    page_icon="🚀",
    layout="wide"
)

with open("dashboard/assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

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
<div style='text-align:center;padding-top:20px;padding-bottom:20px;'>

<h1 style='
font-size:72px;
font-weight:900;
margin-bottom:10px;
background:linear-gradient(90deg,#38bdf8,#818cf8,#ec4899);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
'>
🚀 AI Job Market Intelligence
</h1>

<p style='
font-size:22px;
color:#cbd5e1;
max-width:1000px;
margin:auto;
'>
Analyze hiring trends, salary benchmarks, company demand,
AI opportunities and skill intelligence using real-world job market data.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# KPI CARDS
# =====================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "💼 Total Jobs",
        f"{len(jobs):,}"
    )

with c2:
    st.metric(
        "🏢 Companies",
        f"{companies['company_id'].nunique():,}"
    )

with c3:
    st.metric(
        "🌎 Locations",
        jobs["location"].nunique()
    )

with c4:
    st.metric(
        "🤖 AI Openings",
        f"{len(ai_jobs):,}"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# MODULES
# =====================================================

st.markdown("""
<h2 style='color:white;margin-bottom:25px;'>
⚡ Intelligence Modules
</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 📈 Job Trends

Analyze hiring demand, work types,
remote jobs and location patterns.
""")

with col2:
    st.info("""
### 💰 Salary Insights

Explore compensation trends,
salary benchmarks and top salaries.
""")

with col3:
    st.info("""
### 🤖 AI Jobs

Track AI hiring activity,
roles and recruiters.
""")

col4, col5, col6 = st.columns(3)

with col4:
    st.info("""
### 🏢 Company Analysis

Discover top recruiters,
company demand and market leaders.
""")

with col5:
    st.info("""
### 🧠 Skills Intelligence

Identify the most demanded skills
across the job market.
""")

with col6:
    st.info("""
### 🚀 Career Growth

Use insights to plan your career,
skills and opportunities.
""")

# =====================================================
# DASHBOARD OVERVIEW
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns([2, 1])

with left:

    st.subheader("📊 Platform Overview")

    st.write(
        """
        This platform helps students, job seekers,
        analysts and recruiters understand:

        - Hiring demand
        - Salary trends
        - AI opportunities
        - Skill requirements
        - Company hiring behavior
        """
    )

with right:

    st.subheader("🔥 Quick Stats")

    st.metric(
        "Skill Records",
        f"{len(skills):,}"
    )

    st.metric(
        "Unique Skills",
        skills["skill_abr"].nunique()
    )

# =====================================================
# NAVIGATION
# =====================================================

st.markdown("---")

st.success("""
👈 Use the sidebar to explore:

• Job Trends

• Salary Insights

• AI Jobs Intelligence

• Company Analysis

• Skills Intelligence
""")

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<br><br>

<div style='text-align:center;color:#94a3b8;'>

Built by <b>Mayank Swaroop Nandan</b>

<br><br>

AI Engineering • Data Analytics • Machine Learning

</div>
""", unsafe_allow_html=True)