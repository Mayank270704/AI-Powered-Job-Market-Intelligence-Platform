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

skills = pd.read_csv(
    BASE_DIR / "data" / "raw" / "job_skills.csv"
)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
# 🧠 Skills Intelligence

Analyze the most demanded skills,
technology trends,
and market requirements.

---
""")

# =====================================================
# KPI CARDS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📚 Total Skill Records",
        f"{len(skills):,}"
    )

with col2:
    st.metric(
        "🏷 Unique Skills",
        skills["skill_abr"].nunique()
    )

with col3:
    top_skill = skills["skill_abr"].mode()[0]
    st.metric(
        "🔥 Most Demanded Skill",
        top_skill
    )

st.markdown("---")

# =====================================================
# TOP SKILLS
# =====================================================

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

fig_skills = px.bar(
    skill_counts,
    x="Skill",
    y="Count",
    title="🔥 Top 15 Most In-Demand Skills",
    template="plotly_dark"
)

fig_skills.update_layout(
    height=550
)

st.plotly_chart(
    fig_skills,
    use_container_width=True
)

# =====================================================
# TOP 10 SKILLS PIE CHART
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
    hole=0.45,
    title="📊 Skill Demand Share",
    template="plotly_dark"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

# =====================================================
# DEMAND RANKING
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

ranking_df.index = ranking_df.index + 1

st.dataframe(
    ranking_df,
    use_container_width=True
)

# =====================================================
# SEARCH SKILL
# =====================================================

st.subheader("🔍 Search Skill Demand")

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
# INSIGHTS
# =====================================================

st.markdown("---")

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