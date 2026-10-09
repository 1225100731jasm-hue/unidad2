import requests
response = requests.get(
  'https://api.restcountries.com/countries/v5?q=canada',
  headers={'Authorization': 'Bearer rc_live_962a94a9f4aa4b39aef461cd6d2086ce'}
)
data = response.json()
print(f"Nombre comun: {data["data"]["objects"][0]["names"]["common"]}")
print(f"Nombre oficial: {data["data"]["objects"][0]["names"]["official"]}")
print(f"Su descripcion: {data["data"]["objects"][0]["flag"]["description"]}")