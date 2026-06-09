#switch statement in python
''' switch statement is used to perform different actions based on different conditions. it is used to execute a block of code if a specified condition is true. if the condition is false, another block of code can be executed. '''

#Q. write a switch statement in python to check the day of the week.

day = input("Enter the day of the week: ")
switcher = {
    "Monday": "Today is Monday",
    "Tuesday": "Today is Tuesday",
    "Wednesday": "Today is Wednesday",
    "Thursday": "Today is Thursday",
    "Friday": "Today is Friday",
    "Saturday": "Today is Saturday",
    "Sunday": "Today is Sunday"
}
print(switcher.get(day, "Invalid day of the week")) 

