import json
with open("usingLoads.json", 'r') as json_string:
    data_py=json.loads(json_string)
print(type(data_py))