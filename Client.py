import socket
import json
import requests
import random
from time import sleep
from datetime import datetime

IP = socket.gethostbyname(socket.gethostname())
PORT = 10100
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

sensor_name = "Mortens speedtrap"
speed = random.randint(40, 100)
timestamp = datetime.now().strftime("%Y-%m-%d")
JSON_DATA = json.dumps({"SensorName": sensor_name, "Speed": speed, "Timestamp": timestamp}).encode()
print(JSON_DATA)
SOCKET.sendto(JSON_DATA, (IP, PORT))
SOCKET.close()
