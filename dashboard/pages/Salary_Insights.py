import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Salary Intelligence",
    page_icon="💰",
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

salary_data = jobs["max_salary"].dropna()

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
# 💰 Salary Intelligence

Explore salary benchmarks,
high-paying opportunities,
and compensation trends.

---
""")

# =====================================================
# KPI CARDS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💵 Average Salary",
        f"${salary_data.mean():,.0f}"
    )

with col2:
    st.metric(
        "🚀 Highest Salary",
        f"${salary_data.max():,.0f}"
    )

with col3:
    st.metric(
        "📉 Lowest Salary",
        f"${salary_data.min():,.0f}"
    )

st.markdown("---")

# =====================================================
# SALARY DISTRIBUTION
# =====================================================

sample_salary = (
    salary_data
    .head(300)
    .reset_index(drop=True)
)

salary_df = pd.DataFrame({
    "Job Index": range(len(sample_salary)),
    "Salary": sample_salary
})

fig_salary = px.line(
    salary_df,
    x="Job Index",
    y="Salary",
    title="📈 Salary Distribution",
    template="plotly_dark"
)

fig_salary.update_layout(
    height=500
)

st.plotly_chart(
    fig_salary,
    use_container_width=True
)

# =====================================================
# SALARY HISTOGRAM
# =====================================================

fig_hist = px.histogram(
    salary_data,
    nbins=30,
    title="💰 Salary Frequency Distribution",
    template="plotly_dark"
)

fig_hist.update_layout(
    height=500
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

# =====================================================
# TOP 20 SALARIES
# =====================================================

top_salary = (
    salary_data
    .sort_values(ascending=False)
    .head(20)
    .reset_index(drop=True)
)

top_salary_df = pd.DataFrame({
    "Rank": range(1, 21),
    "Salary": top_salary
})

fig_top = px.bar(
    top_salary_df,
    x="Rank",
    y="Salary",
    title="🏆 Top 20 Highest Salaries",
    template="plotly_dark"
)

fig_top.update_layout(
    height=500
)

st.plotly_chart(
    fig_top,
    use_container_width=True
)

# =====================================================
# INSIGHTS
# =====================================================

st.markdown("---")

st.success(
    f"""
📊 Salary Insights

• Average salary: ${salary_data.mean():,.0f}

• Highest recorded salary: ${salary_data.max():,.0f}

• Lowest recorded salary: ${salary_data.min():,.0f}

• Total salary records analyzed: {len(salary_data):,}
"""
)