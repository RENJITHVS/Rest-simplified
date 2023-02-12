import requests
import json

URL = "http://127.0.0.1:8000/studentcreate/"

data = {
    'name': "Maheesh K",
    'roll': 31,
    "city": "Thrissur"
}

json_data= json.dumps(data)
r =requests.post(url = URL, data = json_data)

new_data = r.json()

print(new_data)