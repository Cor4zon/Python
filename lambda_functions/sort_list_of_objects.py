class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}, {self.age}"


ben = Person("Ben", 10)
eddi = Person("Eddi", 15)
mike = Person("Mike", 11)
lst = [ben, eddi, mike]
print(lst)
lst.sort(key=lambda x: x.age)
print(lst)