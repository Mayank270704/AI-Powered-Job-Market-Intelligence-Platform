import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Skills Intelligence",
    page_icon="🧠",
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

skills = pd.read_csv(
    BASE_DIR / "data" / "raw" / "job_skills.csv"
)

# =====================================================
# DATA PREP
# =====================================================

top_skill = skills["skill_abr"].mode()[0]

skill_counts = (
    skills["skill_abr"]
    .value_counts()
    .head(15)
    .reset_index()
)

skill_counts.columns = [
    "Skill",
    "Count"
]

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="hero-title">
🧠 Skills Intelligence Hub
</div>

<div class="hero-sub">
Analyze the most demanded skills,
technology trends and hiring requirements.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =====================================================
# KPI CARDS
# =====================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{len(skills):,}</h2>
        <p>Total Skill Records</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{skills['skill_abr'].nunique():,}</h2>
        <p>Unique Skills</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{top_skill}</h2>
        <p>Top Skill</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =====================================================
# SEARCH SKILL
# =====================================================

st.subheader("🔍 Skill Search")

search_skill = st.text_input(
    "Enter Skill Name"
)

if search_skill:

    filtered = skills[
        skills["skill_abr"]
        .str.contains(
            search_skill,
            case=False,
            na=False
        )
    ]

    st.metric(
        "Matching Records",
        len(filtered)
    )

    st.dataframe(
        filtered.head(100),
        use_container_width=True
    )

# =====================================================
# TOP SKILLS CHART
# =====================================================

fig_skills = px.bar(
    skill_counts,
    x="Skill",
    y="Count",
    color="Count",
    color_continuous_scale="plasma",
    template="plotly_dark",
    title="🔥 Top 15 Most In-Demand Skills"
)

fig_skills.update_layout(
    height=550
)

st.plotly_chart(
    fig_skills,
    use_container_width=True
)

# =====================================================
# SKILL SHARE
# =====================================================

top10 = (
    skills["skill_abr"]
    .value_counts()
    .head(10)
    .reset_index()
)

top10.columns = [
    "Skill",
    "Count"
]

fig_pie = px.pie(
    top10,
    names="Skill",
    values="Count",
    hole=0.55,
    template="plotly_dark",
    title="📊 Skill Demand Share"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

# =====================================================
# SKILL RANKING
# =====================================================

st.subheader("🏆 Top Skills Ranking")

ranking_df = (
    skills["skill_abr"]
    .value_counts()
    .head(20)
    .reset_index()
)

ranking_df.columns = [
    "Skill",
    "Demand Count"
]

ranking_df.index += 1

st.dataframe(
    ranking_df,
    use_container_width=True
)

# =====================================================
# INSIGHTS
# =====================================================

top_skill_name = skill_counts.iloc[0]["Skill"]
top_skill_count = skill_counts.iloc[0]["Count"]

st.success(
    f"""
📈 Skills Market Insights

• Most demanded skill: {top_skill_name}

• Demand count: {top_skill_count:,}

• Unique skills tracked: {skills['skill_abr'].nunique():,}

• Total skill records analyzed: {len(skills):,}

• Focus on top-ranked skills to maximize employability.
"""
)