class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def getInfo(self):
        return f"{self.name}s age is {self.age}"

person = Person("John", 34)
print(person.getInfo) 
