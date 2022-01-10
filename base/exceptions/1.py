import sys


class WrongOSError(Exception):
    pass


# if not sys.platform.startswith("linux"):
#     raise AssertionError("Wrong OS!")


assert sys.platform.startswith("linux"), "Wrong OS!"
print(" hello")