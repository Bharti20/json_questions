import json
dic={1:2, 3:4, 4:7}
# data_covert=json.dumps(dic)
with open("sample.json","w") as data:
    json.dump(dic, data)
    

