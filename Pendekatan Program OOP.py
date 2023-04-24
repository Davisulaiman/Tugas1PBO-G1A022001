# class OOP
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

# membuat objek
my_dog = Dog("Fido", "Golden Retriever")

# memanggil method objek
print(my_dog.name) # output: Fido
my_dog.bark() # output: Woof!

