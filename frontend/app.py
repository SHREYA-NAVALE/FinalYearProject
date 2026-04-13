import streamlit as st

st.set_page_config(page_title="GreenGuard", layout="wide")

# -------------------------------
# SESSION STATE
# -------------------------------
if "role" not in st.session_state:
    st.session_state.role = "public"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------------
# LOAD CSS
# -------------------------------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------
# NAVBAR
# -------------------------------
from components.navbar import show_navbar
show_navbar(st.session_state.role)

# -------------------------------
# HERO SECTION
# -------------------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🌱 Track. Detect. Protect.")

    st.markdown("## Save Green Cover")
    st.markdown(
        "<h1 style='color:#16a34a'>SEE THE CHANGE</h1>",
        unsafe_allow_html=True
    )

    st.write(
        "Monitor urban deforestation, analyze tree cover, and protect green spaces using satellite data."
    )

    # 🔥 UPDATED BUTTON
    if st.button("Get Started"):
        st.switch_page("pages/2_Analytics.py")

with col2:
    st.image(
        "assets/slider.png",
        width="stretch"
    )

# -------------------------------
# METRICS
# -------------------------------
st.markdown("###")

c1, c2, c3 = st.columns(3)

c1.metric("1", "A")
c2.metric("2", "B")
c3.metric("3", "C")

# -------------------------------
# INFO SECTION
# -------------------------------
st.markdown("## How GreenGuard Works")

st.write(
    "Combining satellite imagery, AI analysis, and urban monitoring to track green cover changes."
)

col1, col2 = st.columns([1, 0.5])

with col1:
    st.markdown("### 🌳 Urban Tree Analysis")

    st.markdown(
        """
        <p style="font-size:26px; line-height:1.8; color:#4b5563;">
        
        <span style="font-size:20px; font-weight:600; color:#111827;">
        Urban Tree Analysis helps understand how cities are evolving and how these changes impact 
        <span style="color:#16a34a;">green spaces</span>.
        </span>
        
        By tracking patterns over time, the system identifies areas where vegetation is gradually shrinking and highlights regions at risk.
        
        This enables early awareness and supports timely action to protect and preserve urban greenery.
        
        </p>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.image(
        "assets/satellite.png",
        width="stretch"
    )

# -------------------------------
# SECOND SECTION
# -------------------------------
col1, col2 = st.columns([0.5, 1])

with col1:
    st.image(
        "assets/permit.png",
        width=350
    )

with col2:
    st.markdown("### 🧑‍🤝‍🧑 Permit Verification")

    st.markdown(
        """
        <p style="font-size:18px; line-height:1.8; color:#4b5563;">
        
        <span style="font-size:22px; font-weight:600; color:#111827;">
        Permit Verification ensures that changes in green cover are legitimate.
        </span>

        It checks whether detected changes align with approved permissions, helping distinguish between authorized development and potential illegal deforestation.

        This improves accuracy, reduces false alerts, and supports responsible urban planning.

        </p>
        """,
        unsafe_allow_html=True
    )

# -------------------------------
# FOOTER
# -------------------------------
from components.footer import show_footer
show_footer()