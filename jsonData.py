import json
file_name = open("jsonData.json","r")
data= json.load(file_name)
print(data)
