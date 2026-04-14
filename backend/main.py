from fastapi import FastAPI
from services.analysis import analyze_area
from db import get_connection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GreenGuard Backend Running ✅"}


@app.post("/analyze-location")
def analyze(data: dict):
    lat = data["lat"]
    lon = data["lon"]

    result = analyze_area(lat, lon)
    return result

@app.get("/dashboard-data")
def dashboard():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM detected_deforestation")
    detections = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM permits")
    permits = cur.fetchone()[0]

    cur.close()
    conn.close()

    return {
        "total_reports": detections,
        "active_permits": permits,
        "illegal_areas": detections,
        "total_loss": detections * 100
    }