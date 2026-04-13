import streamlit as st

def show_footer():

    st.markdown("---")

    col1, col2, col3 = st.columns([2, 2, 2])

    with col1:
        st.markdown("### 🌿 GreenGuard")
        st.caption("Smart monitoring system for urban green cover")

    with col2:
        st.markdown("📧 greenguard.project@gmail.com")
        st.markdown("📞 +91 98765 43210")

    with col3:
        st.markdown("🔗 [LinkedIn](https://linkedin.com/in/your-profile)")

    st.markdown(
        "<p style='text-align:center; font-size:13px; color:#9ca3af;'>© 2026 GreenGuard • Built for Sustainable Cities 🌍</p>",
        unsafe_allow_html=True
    )