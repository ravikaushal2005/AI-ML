#type casting
''' type casting is the process of converting a value from one data type to another data type.'''
a = 10
b = 3.0
c = "5"
print(float(a)) # 10.0
print(int(b)) # 3
print(int(c)) # 5

# type of type casting
''' there are two types of type casting in python.
1. implicit type casting   
2. explicit type casting'''

#implicit type casting
''' implicit type casting is the process of converting a value from one data type to another data type without the programmer's intervention.'''
a = 10
b = 3.0
c = a + b
print(c) # 13.0
print(type(c)) # <class 'float'>

#explicit type casting
''' explicit type casting is the process of converting a value from one data type to another data type with the programmer's intervention.'''
a = 10
b = 3.0
c = int(a) + int(b)
print(c) # 13
print(type(c)) # <class 'int'>  