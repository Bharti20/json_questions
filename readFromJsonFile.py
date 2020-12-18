import json
with open('file.json', 'r') as openfile:
    json_object= json.load(openfile)
print(json_object)
print(type(json_object))
