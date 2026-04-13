import requests

BASE_URL = "http://127.0.0.1:8000"

def analyze_location(lat, lon):
    try:
        response = requests.post(
            f"{BASE_URL}/analyze-location",
            json={
                "lat": lat,
                "lon": lon
            }
        )
        return response.json()
    except Exception as e:
        print(e)
        return None
    
def get_dashboard_data():
    try:
        response = requests.get(f"{BASE_URL}/dashboard-data")
        return response.json()
    except:
        return None