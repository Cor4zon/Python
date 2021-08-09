# инкапсуляцию часто путают с сокрытием данных
# сокрытие данных есть во многих ЯП (С, например).
# инкапсуляция и сокрытие данных это не одно и то же

"""
    Инкапсуляция - механизм языка, позволяющий объединить данные и
    методы, работающие с этими данными, в единый объект. И!
    и скрыть детали реализации от пользователя.
"""

class Person:
    def __init__(self, name, age):
        # приватные атрибуты (начинаются с двух underline'ов
        self.__name = name
        self.__age = age

    # def display(self):
    #     print(f"Name is {self.__age}; age is {self.__name}")

    def set_age(self, age):
        self.__age = age

    def name(self, name):
        self.__name = name

    def display(self):
        print(f"age: {self.__age}, name:{self.__name}")



obj = Person("Jack", 30)
obj.display()
obj.name("Boris")
obj.display()


# свойства - специальные методы в python, ограничеващее доступ.
# геттеры/сеттеры - это свойства
# свойства нужны для доступа к приватным атрибутам из вне(не из класса)
