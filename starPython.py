def many_arguments_in_func():
    def f(*args):
        print(args)


    f(1, 2, 3)

    numbers = [666, 777, 808]
    groups = ['metallica', 'megadeth', 'slayer']

    f(*numbers)
    f(*groups)

# many_arguments_in_func()
