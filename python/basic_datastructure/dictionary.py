#dict
''' dictionary is a collection which is ordered, changeable and does not allow duplicates. '''
#creating a dictionary
mydict = {"name": "John", "age": 30, "city": "New York"}
print(mydict)
#accessing dictionary items
print(mydict["name"])
print(mydict["age"])
print(mydict["city"])
#changing dictionary items
mydict["age"] = 31
print(mydict)
#looping through a dictionary
for x in mydict:
    print(x)
for x in mydict:    print(mydict[x])
for x in mydict.values():
    print(x)
for x, y in mydict.items():
    print(x, y)
#checking if a key exists in a dictionary
print("name" in mydict)
print("country" in mydict)  
