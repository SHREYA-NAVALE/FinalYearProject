from db import get_connection
import random

from services.image_fetch import fetch_images
from utils.image_utils import convert_to_png
import base64

def encode_image(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")

def analyze_area(lat, lon):

    # 🔥 MODULE 1 (REAL)
    images = fetch_images(lat, lon)

    # 🔥 Convert to PNG
    before_img = convert_to_png(images["previous"])
    after_img = convert_to_png(images["current"])

    # 🔥 Dummy detection (for now)
    polygon_wkt = f"POLYGON(({lon} {lat}, {lon+0.01} {lat}, {lon+0.01} {lat+0.01}, {lon} {lat+0.01}, {lon} {lat}))"

    save_detection(polygon_wkt)

    return {
    "green_cover_loss": 12.5,
    "illegal_area_loss": 3.2,
    "legal_deforestation": 6.8,
    "ndvi_loss": -0.21,
    "before_image": encode_image(before_img),
    "after_image": encode_image(after_img),
    "illegal_polygons": [
        {"id": "P1", "area": 2.5, "centroid": [lon, lat]}
        ]
    }


def save_detection(polygon_wkt):
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
        INSERT INTO detected_deforestation (geometry, detected_at)
        VALUES (ST_GeomFromText(%s, 4326), CURRENT_DATE)
        """

        cur.execute(query, (polygon_wkt,))
        conn.commit()

        cur.close()
        conn.close()

    except Exception as e:
        print("DB Error:", e)