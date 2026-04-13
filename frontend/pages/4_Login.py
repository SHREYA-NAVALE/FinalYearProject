import streamlit as st
from components.navbar import show_navbar

# ✅ MUST BE FIRST
st.set_page_config(page_title="Authority Access", layout="wide")

# -------------------------------
# SESSION STATE INIT
# -------------------------------
if "role" not in st.session_state:
    st.session_state.role = "public"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "login"

# -------------------------------
# 🔥 RESET FUNCTION
# -------------------------------
def reset_analysis():
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

# -------------------------------
# NAVBAR
# -------------------------------
show_navbar(st.session_state.role)

# -------------------------------
# TITLE
# -------------------------------
st.markdown(
    "<h2 style='text-align:center;'>🛡 Authority Access</h2>",
    unsafe_allow_html=True
)

# -------------------------------
# CENTER BOX
# -------------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    # -------------------------------
    # TOGGLE BUTTONS
    # -------------------------------
    c1, c2 = st.columns([1, 1], gap="small")

    with c1:
        if st.button("Login", width="stretch", key="login_toggle"):
            st.session_state.auth_mode = "login"

    with c2:
        if st.button("Register", width="stretch", key="register_toggle"):
            st.session_state.auth_mode = "register"

    st.markdown("---")

    # -------------------------------
    # LOGIN FORM
    # -------------------------------
    if st.session_state.auth_mode == "login":

        st.subheader("Admin Login")

        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login Now", width="stretch", key="login_submit"):

            # 🛡 ONLY AUTHORITY LOGIN
            if username == "admin" and password == "1234":
                reset_analysis()

                st.session_state.role = "authority"
                st.session_state.logged_in = True

                st.success("🛡 Logged in as Authority")
                st.switch_page("pages/6_Authority_Home.py")

            else:
                st.error("❌ Invalid Authority Credentials")

    # -------------------------------
    # REGISTER FORM
    # -------------------------------
    else:

        st.subheader("Register Authority")

        new_user = st.text_input("Username", key="register_username")
        new_email = st.text_input("Email", key="register_email")
        new_pass = st.text_input("Password", type="password", key="register_password")
        confirm_pass = st.text_input("Confirm Password", type="password", key="register_confirm")

        if st.button("Register Now", width="stretch", key="register_submit"):

            if new_pass != confirm_pass:
                st.error("❌ Passwords do not match")

            elif new_user == "" or new_email == "" or new_pass == "":
                st.error("❌ Please fill all fields")

            else:
                st.success("✅ Authority account created (demo)")
                st.info("Use admin / 1234 for now")

        st.markdown("Already registered?")
        if st.button("Go to Login", key="go_to_login"):
            st.session_state.auth_mode = "login"

# -------------------------------
# FOOTER
# -------------------------------
from components.footer import show_footer
show_footer()