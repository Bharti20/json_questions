import json 

dic={"name": "David","class":"I","age": 6}

data=open('data2.json','w')

json.dump(dic, data, indent =3)
data.close()