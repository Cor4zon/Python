"""
    this is main module
"""
def test_local(a=None, b=None):
    x = 777
    print("LOCAL")
    l = locals()
    print(l)
    x = 666
    print(l)
    print("locals return copy :(")
    print("this is very important difference")



print("GLOBAL:")
g = globals()
print(g)
x = 66
print(g)
print("globals return link")

test_local()