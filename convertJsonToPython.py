import json
data=open("data.json")
my_data=json.load(data)
print(my_data)
data.close()