import json
dic= {
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
sorted_dic =dict(sorted(dic.items()))
my_data = json.dumps(sorted_dic, indent=2)
with open ('sort.json', 'w') as openfile:
                openfile.write(my_data)
        
            