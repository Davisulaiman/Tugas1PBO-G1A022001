# class OOP
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# membuat objek
john = Person("John", 25)
print(john.age) # output: 25

# mengubah nilai atribut objek
john.age = 30
print(john.age) # output: 30
