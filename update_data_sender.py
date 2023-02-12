import requests
import json

url = 'http://127.0.0.1:8000/studentapi/'
cls_url = 'http://127.0.0.1:8000/student-cls-api/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {
            'id': id
        }
    json_data = json.dumps(data)
    r = requests.get(url=cls_url, data = json_data)
    data = r.json()
    print(data)

# get_data()

def post_data():
    val_data1 = {
        'name': "ruryaodanan",
        'roll': 30,
        "city": "Manglore"
    }
    data = {
        'name':"kiran vargeese45",
        'roll': 50,
        'city': "Kannur"
    }
    json_data = json.dumps(val_data1)
    r = requests.post(url=cls_url, data = json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id': 5,
        'name': "Mohit Kumar",
        'roll': 45,
        "city": "Elavally"
    }
    json_data = json.dumps(data)
    r = requests.put(url=cls_url, data = json_data)
    data = r.json()
    print(data)

update_data()

def delete_data():
    data = {
        'id': 2,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=url, data = json_data)
    data = r.json()
    print(data)

# delete_data()