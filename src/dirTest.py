print(dir())

def localFunc():
    x = 10
    b = 11
    print(dir())


localFunc()
print(__name__)
print(__doc__)