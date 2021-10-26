name = "Eric"
print("My name is %s" % name)

age = 19
print("My name is %s and i am %s year old" % (name, age))

"""
В целом нормально, но если переменных будет много, то будет нечитаемо. 
"""
company = "Roga and Copita"
position = "Master of coin"
surname = "Clapton"
print("My name is %s %s. I work in %s on %s position"
        % (name, surname, company, position))
