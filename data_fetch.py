import requests


def get_live_data():
    """Fetch real-time rainfall and humidity from Open-Meteo API for Kakinada, AP."""
    lat = 15.9129
    lon = 79.7400
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current=rain,relative_humidity_2m"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        rainfall = data["current"].get("rain", 0) or 0
        humidity = data["current"].get("relative_humidity_2m", 0) or 0
        water_level = round(rainfall * 0.2, 2)
        return {
            "rainfall": rainfall,
            "humidity": humidity,
            "water_level": water_level
        }
    except Exception as e:
        print(f"[data_fetch] Live API error: {e}. Returning fallback data.")
        return {
            "rainfall": 8.0,
            "humidity": 72,
            "water_level": 1.6
        }


def simulate_flood():
    """Return simulated extreme flood conditions for demo purposes."""
    return {
        "rainfall": 250,
        "humidity": 95,
        "water_level": 15.0
    }
