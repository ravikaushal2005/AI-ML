#oops concept in python
''' OOPs stands for Object Oriented Programming. it is a programming paradigm that uses objects and classes to design and program applications. it is a way of organizing code in a way that is easy to understand and maintain. it is a way of thinking about programming in terms of objects and their interactions. '''  
#class
''' class is a blueprint for creating objects. it is a user-defined data type that contains data members and member functions. it is used to create objects that have the same properties and behaviors. '''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
person1 = Person("John", 30)
person1.display()

#object
''' object is an instance of a class. it is a real-world entity that has properties and behaviors. it is created from a class and can be used to access the properties and behaviors of the class. '''
person2 = Person("Alice", 25)
person2.display()   



#oops concept in python is based on the following principles:
''' 1. Encapsulation: it is the process of hiding the internal details of an object
2. Inheritance: it is the process of creating a new class from an existing class
3. Polymorphism: it is the process of using a single interface to represent different types of objects
4. Abstraction: it is the process of hiding the implementation details of an object and only exposing the necessary details to the user '''
