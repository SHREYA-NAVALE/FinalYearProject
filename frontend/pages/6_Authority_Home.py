import streamlit as st
from components.navbar import show_navbar

# -------------------------------
# SECURITY CHECK
# -------------------------------
if st.session_state.get("role") != "authority":
    st.error("Access Denied 🚫")
    st.stop()

# -------------------------------
# NAVBAR
# -------------------------------
show_navbar(st.session_state.role)
st.write("")
st.write("")

# -------------------------------
# HEADER
# -------------------------------
st.markdown("## 🛡 Authority Dashboard")
st.markdown("### 🌿 GreenGuard Control Center")

st.write(
    "Monitor urban environments, detect green cover changes, and verify development permits "
    "using satellite-based intelligence."
)

st.markdown("---")

# ===============================
# LIVE MONITORING SECTION
# ===============================
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("### 📡 Live Monitoring")

    st.markdown(
        """
        <p style="font-size:18px; line-height:1.7; color:#4b5563;">
        Live Monitoring provides real-time insights into urban green cover changes using satellite imagery.
        It helps identify areas where vegetation is decreasing and detects possible deforestation activities.
        <br><br>
        This system enables early alerts, allowing authorities to take timely action and prevent illegal developments.
        </p>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.image("assets/urbanarea1.png", width="stretch")

st.markdown("---")

# ===============================
# PERMIT VERIFICATION SECTION
# ===============================
col1, col2 = st.columns([1, 1.2])

with col1:
    st.image("assets/urbanarea2.png", width="stretch")

with col2:
    st.markdown("### 📄 Permit Verification")

    st.markdown(
        """
        <p style="font-size:18px; line-height:1.7; color:#4b5563;">
        Permit Verification ensures that detected changes in land use are authorized and legally approved.
        <br><br>
        By comparing satellite data with official permissions, the system distinguishes between 
        approved construction and potential illegal deforestation.
        <br><br>
        This improves monitoring accuracy and supports responsible urban planning.
        </p>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# ===============================
# SUMMARY STATS (CLEAN LOOK)
# ===============================
c1, c2, c3 = st.columns(3)

