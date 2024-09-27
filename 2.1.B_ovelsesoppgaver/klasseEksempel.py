#!/bin/python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person opprettet")

    def greet(self):
        print(f"jeg heter {self.name}, og er {self.age} år")

person1 = Person("Cris", 18)
#person1.greet() #
print(person1.name)