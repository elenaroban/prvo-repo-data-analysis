import requests
import json


num_params = {
    "num1":15,
    "num2":4,
    "operation":"add"
}


response = requests.get(
    url="https://feed-77-28-29-255.ngrok-free.app/math",
    params=num_params
)

if response.status_code == 200:
    print(response.status_code)
    rezultat = json.loads(response.text)
    print(type(rezultat))
    print(rezultat)
else:
    print("nastana greska")
    print(response.text)