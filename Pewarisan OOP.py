# class OOP
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# membuat objek
my_dog = Dog("Fido")
my_cat = Cat("Whiskers")

# memanggil method objek
print(my_dog.speak()) # output: Woof!
print(my_cat.speak()) # output: Meow!
