import requests


def obtener_clima(latitud, longitud):
    url = "https://api.open-meteo.com/v1/forecast"
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,wind_speed_10m",
    }
    r = requests.get(url, params=parametros, timeout=10)
    r.raise_for_status()
    return r.json()["current"]


ciudades = {
    "Querétaro": (20.59, -100.39),
    "Ciudad de México": (19.43, -99.13),
    "Guadalajara": (20.67, -103.35),
}

print(f"{'Ciudad':<18} | {'Temp (°C)':>9} | {'Viento (km/h)':>13}")
print("-" * 46)

for nombre, (lat, lon) in ciudades.items():
    try:
        clima = obtener_clima(lat, lon)
        print(f"{nombre:<18} | {clima['temperature_2m']:>9} | {clima['wind_speed_10m']:>13}")
    except requests.exceptions.RequestException as e:
        print(f"{nombre:<18} | Error: {e}")

print("Juan Antonio Salazar Mendez")
