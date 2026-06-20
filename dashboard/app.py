import streamlit as st

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
# CUSTOM CSS
# =====================================================

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🚀 AI Job Market Intelligence
</div>

<div class="hero-subtitle">
Discover hiring trends, AI opportunities, salary benchmarks,
skill demand and company insights using real-world job market data.
</div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# KPI SECTION
# =====================================================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">15,886</div>
        <div class="metric-label">Total Jobs</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">6,063</div>
        <div class="metric-label">Companies</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">3,010</div>
        <div class="metric-label">Locations</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">270+</div>
        <div class="metric-label">AI Openings</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# QUICK ACCESS
# =====================================================

st.markdown("""
<div class="section-title">
⚡ Explore Intelligence Modules
</div>
""", unsafe_allow_html=True)

row1 = st.columns(3)

with row1[0]:
    st.markdown("""
    <div class="module-card">
    <h2>📈 Job Trends</h2>
    <p>
    Analyze hiring patterns, work types,
    remote opportunities and location demand.
    </p>
    </div>
    """, unsafe_allow_html=True)

with row1[1]:
    st.markdown("""
    <div class="module-card">
    <h2>💰 Salary Insights</h2>
    <p>
    Discover compensation trends,
    salary benchmarks and top-paying roles.
    </p>
    </div>
    """, unsafe_allow_html=True)

with row1[2]:
    st.markdown("""
    <div class="module-card">
    <h2>🤖 AI Jobs</h2>
    <p>
    Explore AI hiring demand,
    recruiter activity and emerging roles.
    </p>
    </div>
    """, unsafe_allow_html=True)

row2 = st.columns(3)

with row2[0]:
    st.markdown("""
    <div class="module-card">
    <h2>🏢 Companies</h2>
    <p>
    Discover top recruiters,
    hiring concentration and market leaders.
    </p>
    </div>
    """, unsafe_allow_html=True)

with row2[1]:
    st.markdown("""
    <div class="module-card">
    <h2>🧠 Skills</h2>
    <p>
    Track the most demanded skills
    across thousands of job postings.
    </p>
    </div>
    """, unsafe_allow_html=True)

with row2[2]:
    st.markdown("""
    <div class="module-card">
    <h2>🚀 Career Growth</h2>
    <p>
    Use market intelligence to make
    smarter career decisions.
    </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# NAVIGATION
# =====================================================

st.markdown("""
<div class="section-title">
📚 Dashboard Navigation
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="nav-box">

<h3>👈 Use the sidebar to explore:</h3>

<ul>
<li>📈 Job Trends</li>
<li>💰 Salary Insights</li>
<li>🤖 AI Jobs Intelligence</li>
<li>🏢 Company Analysis</li>
<li>🧠 Skills Intelligence</li>
</ul>

</div>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">

<h4>Built by Mayank Swaroop Nandan</h4>

AI Engineering • Data Analytics • Machine Learning

</div>
""", unsafe_allow_html=True)