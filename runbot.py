import json
import os

with open("config/json/config.json") as f:
    data = json.load(f)

room_id = data['room_id']
api_token = data['api_token']
file_name = data['file_name']

if not room_id or not api_token:
    print("Please set the room_id and api_token in config.yml.")
else:
    os.system(f"highrise {file_name}:Bot {room_id} {api_token}")
