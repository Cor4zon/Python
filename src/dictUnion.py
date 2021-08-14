dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

dict4 = {**dict1, **dict2}
print(dict4)

def func():
    """
    this is docstring
    :return: nothing
    """
    # print(help(func))
    # dir(func)
    a = 10
    b = 7
    def azz():
        pass


print(dir(func))
# func()