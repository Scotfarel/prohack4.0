import requests
import json

url = 'http://127.0.0.1:5500'
data = {"command": "enable"}
serialized_data = json.dumps(data)

requests.post(url, json=serialized_data)
