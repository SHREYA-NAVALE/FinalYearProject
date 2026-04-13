import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import Draw
import datetime

from components.navbar import show_navbar
from components.footer import show_footer

# -------------------------------
# 🔐 SECURITY
# -------------------------------
if st.session_state.get("role") != "authority":
    st.error("Access Denied 🚫")
    st.stop()

# -------------------------------
# NAVBAR
# -------------------------------
show_navbar(st.session_state.role)

# -------------------------------
# TITLE
# -------------------------------
st.title("📄 Add Permit")

st.markdown("### 🏗 Register Authorized Land Use / Construction")

st.markdown("---")

# -------------------------------
# SESSION INIT
# -------------------------------
if "permit_polygon" not in st.session_state:
    st.session_state.permit_polygon = None

# -------------------------------
# 🗺 MAP FOR POLYGON
# -------------------------------
st.markdown("### 🗺 Draw Permit Area")

m = folium.Map(location=[22.5937, 78.9629], zoom_start=5)

Draw(
    draw_options={
        "polygon": True,
        "rectangle": True,
        "circle": False,
        "marker": False,
        "polyline": False,
        "circlemarker": False,
    }
).add_to(m)

map_data = st_folium(m, height=500)

# Capture polygon
if map_data and map_data.get("all_drawings"):
    shape = map_data["all_drawings"][-1]
    st.session_state.permit_polygon = shape["geometry"]

    st.success("✅ Area selected")

# -------------------------------
# 📋 FORM
# -------------------------------
st.markdown("### 📋 Permit Details")

col1, col2 = st.columns(2)

with col1:
    permit_id = st.text_input("Permit ID")
    project_name = st.text_input("Project Name")
    permit_type = st.selectbox(
        "Permit Type",
        ["Construction", "Road Work", "Commercial", "Residential"]
    )

with col2:
    authority = st.text_input("Issuing Authority")
    issue_date = st.date_input("Issue Date", datetime.date.today())
    status = st.selectbox(
        "Status",
        ["Approved", "Pending", "Rejected"]
    )

st.markdown("---")

# -------------------------------
# 🚀 SUBMIT
# -------------------------------
if st.button("Submit Permit", width="stretch"):

    if not permit_id or not project_name or not authority:
        st.error("❌ Please fill all required fields")

    elif st.session_state.permit_polygon is None:
        st.error("❌ Please draw permit area on map")

    else:
        permit_data = {
            "permit_id": permit_id,
            "geometry": st.session_state.permit_polygon,
            "issue_date": str(issue_date),
            "permit_type": permit_type,
            "authority": authority,
            "project_name": project_name,
            "status": status
        }

        # 🔥 Backend call placeholder
        st.success("✅ Permit added successfully!")

        st.json(permit_data)  # debug view (remove later)

# -------------------------------
# FOOTER
# -------------------------------
show_footer()