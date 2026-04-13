from db import get_connection
import random

def analyze_area(lat, lon):

    polygon_wkt = f"POLYGON(({lon} {lat}, {lon+0.01} {lat}, {lon+0.01} {lat+0.01}, {lon} {lat+0.01}, {lon} {lat}))"

    # ✅ Save into PostGIS
    save_detection(polygon_wkt)

    return {
        "green_cover_loss": 12.5,
        "illegal_area_loss": 3.2,
        "legal_deforestation": 6.8,
        "ndvi_loss": -0.21,
        "before_image": "",
        "after_image": "",
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