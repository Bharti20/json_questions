import json

with open("usingLoad.json","r") as json_data:
    data=json.load(json_data)
print(type(data))
