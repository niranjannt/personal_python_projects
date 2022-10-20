import requests

url = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyARDpKHpmorVp7UExo8AA5j0hvwXdI-Mus"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
