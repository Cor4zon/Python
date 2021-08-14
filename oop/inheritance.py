class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self, age):
        if age < 1:
            return
        self.__age = age


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        self.__name = name


    def display(self):
        print(f"age: {self.__age}, name:{self.__name}")



class Employee(Person):
    def details(self, company):
        print(self.name, 'work in', company)



obj = Employee("Tom", 22)
obj.details('Microsoft')

print(obj.name)
print(obj.age)















