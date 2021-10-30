

def odds(start, stop):
    """generator-function?"""
    for odd in range(start, stop+1, 2):
        yield odd


