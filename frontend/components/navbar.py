import streamlit as st

def show_navbar(role):

    logged_in = st.session_state.get("logged_in", False)

    st.markdown('<div class="navbar">', unsafe_allow_html=True)

    nav1, nav2 = st.columns([6, 6])

    # -------------------------------
    # LEFT (LOGO)
    # -------------------------------
    with nav1:
        st.markdown("## 🌿 GreenGuard")

    # -------------------------------
    # RIGHT (BUTTONS)
    # -------------------------------
    with nav2:

        # 🛡 AUTHORITY USER
        if logged_in and role == "authority":
            cols = st.columns(3)

            if cols[0].button("Home", width="stretch"):
                st.switch_page("pages/6_Authority_Home.py")

            if cols[1].button("Add Permit", width="stretch"):
                st.switch_page("pages/3_Report.py")

            if cols[2].button("Logout", width="stretch"):
                reset_session()
                st.session_state.logged_in = False
                st.session_state.role = "public"
                st.switch_page("app.py")

        # 👤 PUBLIC USER (LOGGED IN)
        elif logged_in and role == "public":
            cols = st.columns(4)

            if cols[0].button("Home", width="stretch"):
                st.switch_page("app.py")

            if cols[1].button("Dashboard", width="stretch"):
                st.switch_page("pages/1_Dashboard.py")

            if cols[2].button("Analytics", width="stretch"):
                st.switch_page("pages/2_Analytics.py")

            if cols[3].button("Logout", width="stretch"):
                reset_session()
                st.session_state.logged_in = False
                st.switch_page("app.py")

        # 👤 PUBLIC USER (NOT LOGGED IN)
        else:
            cols = st.columns(4)

            if cols[0].button("Home", width="stretch"):
                st.switch_page("app.py")

            if cols[1].button("Dashboard", width="stretch"):
                st.switch_page("pages/1_Dashboard.py")

            if cols[2].button("Analytics", width="stretch"):
                st.switch_page("pages/2_Analytics.py")

            if cols[3].button("Admin Login", width="stretch"):
                st.switch_page("pages/4_Login.py")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------
# 🔥 RESET FUNCTION
# -------------------------------
def reset_session():
    keys_to_clear = [
        "analysis_done",
        "analysis_result",
        "coords",
        "lat",
        "lon",
        "location_name"
    ]

    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]