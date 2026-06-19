import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Job Market Intelligence",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.stApp{
    background:
    radial-gradient(circle at top left,#172554 0%,#0f172a 40%),
    radial-gradient(circle at top right,#312e81 0%,transparent 30%),
    #020617;
    color:white;
}

.block-container{
    max-width:1400px;
    padding-top:2rem;
}

/* HERO */

.hero{
    text-align:center;
    padding-top:30px;
    padding-bottom:30px;
}

.hero-title{
    font-size:5rem;
    font-weight:900;
    line-height:1;
    background:linear-gradient(
        90deg,
        #38bdf8,
        #818cf8,
        #ec4899
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-subtitle{
    font-size:1.3rem;
    color:#cbd5e1;
    margin-top:15px;
}

/* KPI CARDS */

.metric-card{
    background:rgba(255,255,255,0.06);
    border:1px solid rgba(255,255,255,0.12);
    border-radius:25px;
    padding:25px;
    text-align:center;
    backdrop-filter:blur(15px);
    transition:0.3s;
    color:white;
}

.metric-card:hover{
    transform:translateY(-8px);
    border:1px solid #60a5fa;
    box-shadow:0px 0px 30px rgba(96,165,250,.35);
}

.metric-number{
    font-size:2.8rem;
    font-weight:800;
    color:white;
}

.metric-label{
    color:#cbd5e1;
    font-size:1rem;
}

/* SECTION TITLE */

.section-title{
    font-size:2.4rem;
    font-weight:800;
    color:white;
    margin-top:50px;
    margin-bottom:25px;
}

/* MODULE CARDS */

.module-card{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.10);
    border-radius:25px;
    padding:30px;
    text-align:center;
    min-height:220px;
    backdrop-filter:blur(15px);
    transition:0.3s;
}

.module-card:hover{
    transform:translateY(-10px);
    border:1px solid #38bdf8;
    box-shadow:0px 0px 35px rgba(56,189,248,.25);
}

.module-card h2{
    color:white;
    font-size:2rem;
}

.module-card p{
    color:#cbd5e1;
    font-size:1.05rem;
}

/* NAVIGATION BOX */

.nav-box{
    background:rgba(56,189,248,.08);
    border:1px solid rgba(56,189,248,.15);
    border-radius:20px;
    padding:25px;
    color:white;
}

.nav-box li{
    margin-bottom:10px;
    color:#cbd5e1;
}

/* FOOTER */

.footer{
    text-align:center;
    color:#94a3b8;
    margin-top:60px;
    padding-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

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