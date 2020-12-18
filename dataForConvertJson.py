import json
my_dict={'Name':['neha','ravina','rani'], 6:(10, 20, 30)}
my_string = json.dumps(my_dict, indent=2)
with open('dataFromPy.json','w') as outfile:
    outfile.write(my_string)
