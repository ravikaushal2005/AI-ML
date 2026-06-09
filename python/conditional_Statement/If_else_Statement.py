# conditonal statement
''' conditional statement is used to perform different actions based on different conditions. it is used to execute a block of code if a specified condition is true. if the condition is false, another block of code can be executed. '''

a = 10
if a > 5:
    print("a is greater than 5")
else:    print("a is less than or equal to 5")


# nested if statement
''' nested if statement is used to check multiple conditions. it is used to execute a block of code if a specified condition is true. if the condition is false, another block of code can be executed. '''


b = 20
if b > 10:
    if b < 30:
        print("b is between 10 and 30")
    else:
        print("b is greater than or equal to 30")
else:    print("b is less than or equal to 10")


# if elif else statement

''' if elif else statement is used to check multiple conditions. it is used to execute a block of code if a specified condition is true. if the condition is false, another block of code can be executed. '''  

c = 15
if c > 20:
    print("c is greater than 20")
elif c > 10:
    print("c is greater than 10 but less than or equal to 20")
else:    print("c is less than or equal to 10")

