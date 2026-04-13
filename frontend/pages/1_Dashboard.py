import streamlit as st

st.set_page_config(layout="wide")
from components.navbar import show_navbar
# ensure role exists
if "role" not in st.session_state:
    st.session_state.role = "public"

show_navbar(st.session_state.role)

import streamlit as st

st.set_page_config(layout="wide")

st.write("")
st.write("")



# # ---------------- DATA FUNCTION ----------------
# # 👉 Later replace this with DB query
# def get_dashboard_data():
#     return {
#         "total_reports": 120,
#         "active_permits": 45,
#         "illegal_areas": 18,
#         "total_loss": 2300
#     }

# # ---------------- FETCH DATA ----------------
# data = get_dashboard_data()

from utils.api import get_dashboard_data

data = get_dashboard_data()

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
.card {
    background-color: #f1f8e9;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
}
.title {
    font-size: 16px;
    color: #2e7d32;
}
.value {
    font-size: 28px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- CARDS ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f'''
    <div class="card">
        <div class="title">Total Reports</div>
        <div class="value">{data["total_reports"]}</div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
    <div class="card">
        <div class="title">Total Active Permits</div>
        <div class="value">{data["active_permits"]}</div>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown(f'''
    <div class="card">
        <div class="title">Potentially Illegal Areas</div>
        <div class="value">{data["illegal_areas"]}</div>
    </div>
    ''', unsafe_allow_html=True)

with col4:
    st.markdown(f'''
    <div class="card">
        <div class="title">Total Loss (m²)</div>
        <div class="value">{data["total_loss"]}</div>
    </div>
    ''', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")


# ---------------- MAP SECTION ----------------
import folium
from streamlit_folium import st_folium

st.markdown("## 🗺 Monitored Regions")




# --------- DATA FUNCTION ----------
def get_monitored_locations():
    return [
        {"lat": 18.5204, "lon": 73.8567, "name": "Shivaji Nagar"},
        {"lat": 18.5300, "lon": 73.8600, "name": "Koregaon Park"},
        {"lat": 18.5100, "lon": 73.8500, "name": "Swargate"},
    ]


locations = get_monitored_locations()


# --------- MAP CENTER ----------
if locations:
    center_lat = sum(loc["lat"] for loc in locations) / len(locations)
    center_lon = sum(loc["lon"] for loc in locations) / len(locations)
else:
    center_lat, center_lon = 18.5204, 73.8567


# --------- CREATE SATELLITE MAP ----------
m = folium.Map(location=[center_lat, center_lon], zoom_start=13, tiles=None)

# 🔥 Satellite Layer (Google)
folium.TileLayer(
    tiles="https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
    attr="Google",
    name="Satellite",
    max_zoom=20,
    subdomains=["mt0", "mt1", "mt2", "mt3"],
).add_to(m)

# 🔥 Labels Layer (names of regions)
folium.TileLayer(
    tiles="https://{s}.google.com/vt/lyrs=h&x={x}&y={y}&z={z}",
    attr="Google",
    name="Labels",
    max_zoom=20,
    subdomains=["mt0", "mt1", "mt2", "mt3"],
).add_to(m)


# --------- ADD MARKERS ----------
for loc in locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=f"<b>{loc['name']}</b>",
        tooltip=loc["name"],
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(m)


# --------- LAYER CONTROL ----------
folium.LayerControl().add_to(m)


# --------- DISPLAY ----------
st_folium(m, width=1200, height=500)






# ---------------- SPACE ----------------
st.write("")
st.write("")


# ---------------- RECENT ANALYSIS ----------------
st.markdown("## 📊 Recent Analysis")


# --------- DATA FUNCTION (DB READY) ----------
def get_recent_analysis():
    return {
        "area_details": {
            "latitude": 18.5204,
            "longitude": 73.8567,
            "region": "Shivaji Nagar",
            "status": "Illegal",
            "loss": 120
        },
        "deforestation_map": [
            {"lat": 18.5204, "lon": 73.8567},
            {"lat": 18.5210, "lon": 73.8575}
        ],
        "illegal_polygons": [
            [
                [18.5204, 73.8567],
                [18.5210, 73.8575],
                [18.5195, 73.8580]
            ]
        ]
    }


analysis_data = get_recent_analysis()


# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs([
    "📍 Area Details",
    "🌳 Deforestation Map",
    "🚨 Illegal Polygons"
])


# ---------------- TAB 1: AREA DETAILS ----------------
with tab1:
    details = analysis_data["area_details"]

    st.write(f"**Region:** {details['region']}")
    st.write(f"**Latitude:** {details['latitude']}")
    st.write(f"**Longitude:** {details['longitude']}")
    st.write(f"**Loss (m²):** {details['loss']}")




# ---------------- TAB 2: DEFORESTATION MAP ----------------
with tab2:
    m2 = folium.Map(location=[18.5204, 73.8567], zoom_start=14)

    for point in analysis_data["deforestation_map"]:
        folium.CircleMarker(
            location=[point["lat"], point["lon"]],
            radius=5,
            color="green",
            fill=True,
            fill_color="green"
        ).add_to(m2)

    st_folium(m2, width=900, height=400)


# ---------------- TAB 3: ILLEGAL POLYGONS ----------------
with tab3:
    m3 = folium.Map(location=[18.5204, 73.8567], zoom_start=14)

    for polygon in analysis_data["illegal_polygons"]:
        folium.Polygon(
            locations=polygon,
            color="red",
            fill=True,
            fill_opacity=0.4
        ).add_to(m3)

    st_folium(m3, width=900, height=400)














    #footer
from components.footer import show_footer

show_footer()