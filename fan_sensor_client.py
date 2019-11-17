import time
import json
import requests

from.raspberry_admin import get_pollution_rate

# script settings
minimal_working_level = 10
url = '127.0.0.1:8841/fan_sensor/'


def send_sensor_info():
    working_state = False
    while True:
        pollution_rate = get_pollution_rate()

        if (pollution_rate > minimal_working_level) and not working_state:
            working_state = True
            serialized_data = json.dumps({'smoke': working_state})
            requests.post(url, json=serialized_data)
        elif (pollution_rate <= minimal_working_level) and working_state:
            working_state = False
            serialized_data = json.dumps({'smoke': working_state})
            requests.post(url, json=serialized_data)

        time.sleep(5.0)


if __name__ == "__main__":
    send_sensor_info()
