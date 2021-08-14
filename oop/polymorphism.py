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
    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self.__company = company

    # переопределние метода
    def display(self):
        print(f"age: {self.age}, name:{self.name}, company:{self.__company}")



class Student(Person):
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.__university = university


    # переопределение метода
    def display(self):
        Person.display(self)
        print(f"university:{self.__university}")




class Doctor(Person):
    def __init__(self, name, age, hospital):
        Person.__init__(self, name, age)
        self.__hospital = hospital

    # переопределение метода
    def display(self):
        print(f"age: {self.age}, name:{self.name}, hospital:{self.__hospital}")


lst_obj = [Person('Tom', 22), Doctor('Boris', 18, 'Moscow central'), Student('Oleg', 18, 'MSU'), Employee('John', 28, 'Spotify')]

for obj in lst_obj:
    obj.display()

