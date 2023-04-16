import socket
import json
import requests

PORT = 10100
SIZE = 1024

IP = socket.gethostbyname(socket.gethostname())
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SOCKET.bind((IP, PORT))

API_ENDPOINT = "https://udpproxycarspeedapi.azurewebsites.net/api/Sensors"
response = requests.get(API_ENDPOINT)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
    data = []

while True:
    data, addr = SOCKET.recvfrom(SIZE)
    JSON_DATA = json.loads(data.decode())

    sensor_name = JSON_DATA['SensorName']
    speed = JSON_DATA['Speed']
    timestamp = JSON_DATA['Timestamp']

    payload = {"name": sensor_name, "speed": speed, "timestamp": timestamp}
    response = requests.post(API_ENDPOINT, json=payload)

    print(response.text)
