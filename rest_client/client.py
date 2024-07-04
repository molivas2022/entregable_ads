# client.py
import requests
import json

url = 'http://api:5000/message'
message = {'message': 'Hello, World!'}

response = requests.post(url, json=message)
print(response.json())
