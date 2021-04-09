# Extract Auth Token

import json

with open("user_info.json", "r") as read_file:
    data = json.load(read_file)

auth_token = data["user"]["auth_token"]

print(auth_token)

