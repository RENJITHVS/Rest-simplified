import requests
import json

url = 'http://127.0.0.1:8000/hello-w/'

def post_data():
    data = {
        'name': "manohar",
        'roll': 31,
        "city": "Thirupathi"
    }
    headers = {
        'content-Type':'application/json'
    }
    # data = {
    #     'name':"kiran vargeese45",
    #     'roll': 50,
    #     'city': "Kannur"
    # }
    json_data = json.dumps(data)
    r = requests.post(url=url,headers=headers, data = json_data)
    data = r.json()
    print(data)

post_data()

def get_data():
    data = {
        'name': "manohar",
        'roll': 31,
        "city": "Thirupathi"
    }
    headers = {
        'content-Type':'application/json'
    }

    json_data = json.dumps(data)
    r = requests.get(url=url,headers=headers, data = json_data)
    data = r.json()
    print(data)

# get_data()