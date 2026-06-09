#fuction
''' fuction is a block of code which only runs when it is called. you can pass data, known as parameters, into a function. a function can return data as a result.'''   

def greet(name):
    print("Hello, " + name + ". How are you?")
greet("Alice")

#types of function
''' there are two types of function in python. they are built-in function and user-defined function
built-in function is a function that is already defined in python.
user-defined function is a function that is defined by the user. '''

#built-in function
''' built-in function is a function that is already defined in python. it is used to perform a specific task. it is used to perform a specific task. it is used to perform a specific task. it is used to perform a specific task. it is used to perform a specific task.

some of the built-in function in python are print(), input(), len(), type(), etc. '''
print("Hello, World!")
name = input("Enter your name: ")
print("Hello, " + name + ". How are you?")
length = len(name)
print("The length of your name is: " + str(length))
print("The type of your name is: " + str(type(name)))

#user-defined function
''' user-defined function is a function that is defined by the user. it is used to perform a specific task. it is used to perform a specific task. it is used to perform a specific task. it is used to perform a specific task. it is used to perform a specific task.
to define a function in python, we use the def keyword. the syntax of a function is as follows:
def function_name(parameters):
    """docstring"""
    statement(s)
to call a function, we use the function name followed by parentheses. if the function has parameters, we pass the arguments inside the parentheses. ''' 

def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b
result = add(5, 10)
print("The sum of 5 and 10 is: " + str(result))

