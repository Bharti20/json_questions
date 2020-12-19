dic={
    "a":  1, 
    "a":  2, 
    "a":  3, 
    "a": 4, 
    "b": 1, 
    "b": 2
}
dic2={}
for key in dic:
    if key not in dic2:
        dic2.update(dic)
print(dic2)