import requests
import json

gj_srv_response = requests.get('http://127.0.0.1:8841/fan_sensor')
response = gj_srv_response.content
signal_json = json.loads(response)
signal_state = signal_json['signal']['state']
print(signal_state)
