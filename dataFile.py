import json
dic={"bharti":1, "kumari":2}
my_data=open("dataFilejson.json",'w')
json.dump(dic, my_data)