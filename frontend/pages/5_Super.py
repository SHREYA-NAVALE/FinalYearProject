import streamlit as st
import rasterio
import numpy as np
from components.navbar import show_navbar

# ensure role exists
if "role" not in st.session_state:
    st.session_state.role = "public"

show_navbar(st.session_state.role)

def load_tif(path):
    with rasterio.open(path) as src:
        img = src.read([1, 2, 3])
        img = np.transpose(img, (1, 2, 0))
    return img

def normalize(img):
    img = img.astype(float)
    img = (img - img.min()) / (img.max() - img.min())
    return img

img1 = normalize(load_tif("data/img1.tif"))
img2 = normalize(load_tif("data/img2.tif"))

col1, col2 = st.columns(2)

with col1:
    st.image(img1, caption="A")

with col2:
    st.image(img2, caption="B")




#footer
from components.footer import show_footer

show_footer()