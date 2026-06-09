#class
#syntax
'''
class ClassName:
    """docstring"""
    statement(s)
to create an object of a class, we use the class name followed by parentheses. if the class has an __init__() method, we pass the arguments inside the parentheses. ''' 

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
employee1 = Employee("John", 30, 50000)
employee1.display() 