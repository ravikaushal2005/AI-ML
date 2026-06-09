#tuple
''' tuple is a collection which is ordered and unchangeable. Allows duplicate members.'''   
#creating a tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple)
#accessing tuple items
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
#negative indexing
print(mytuple[-1])
print(mytuple[-2])
print(mytuple[-3])
#slicing a tuple
print(mytuple[0:2])
print(mytuple[1:3])
print(mytuple[:2])
print(mytuple[1:])
#looping through a tuple
for x in mytuple:
    print(x)
#checking if an item exists in a tuple
print("banana" in mytuple)  

