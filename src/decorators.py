def my_shine_new_decorator(function_to_decorate):
    def the_wrapped_around_the_original_function():
        print("message before")
        function_to_decorate()
        print("message after")
    return the_wrapped_around_the_original_function


@my_shine_new_decorator
def alone_function():
    print("I am alone function. Don't touch me")


# alone_function = my_shine_new_decorator(alone_function)
# alone_function()
"""
Second decorator example
"""
def bread(func):
    def wrapper(arg1):
        print()
        func(arg1)
        print("\__________/")
    return wrapper


def ingredients(func):
    def wrapper(arg1):
        print("tomatos")
        func(arg1)
        print("cheese")
    return wrapper




@bread
@ingredients
def sandwich(food):
    print(food)


# foodForBurger = input("Input main ingredient: ")
# sandwich(foodForBurger)


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie -= 3
        return method_to_decorate(self, lie)        # don't forget about self
    return wrapper


class Lucy:
    def __init__(self):
        self.age = 30

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("I'm {}, and what do you think about it?".format(self.age + lie))

obj = Lucy()
obj.sayYourAge(-1000)









