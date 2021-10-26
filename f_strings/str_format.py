name = "Eric"
surname = "Clapton"
age = 19
company = "Roga and Copita"
position = "Master of coin"

print("My name is {}, I am {}".format(name, age))
print("My name is {1}, I am {0}".format(age, name))
print("My name is {name}, I am {age}".format(name=name, age=age))

person = {"name": name, "age": age}
print("My name is {name}. I am {age}".format(name=person["name"], age=person["age"]))


# unpacking arguments
print("My name is {name}. I am {age}".format(**person))

"""
Это лучше, чем %-formating, так как тут можно давать имя переменным, 
но проблема остается.
Если много аргументов - unreadable
"""