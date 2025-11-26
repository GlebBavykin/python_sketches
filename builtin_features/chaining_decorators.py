def closure(x):
    """
        Inner function example
    :param x:
    :return:
    """

    def inner(y):
        return x + y

    return inner


add_five = closure(5)
print(add_five)
result = add_five(6)
print(result)


def add(x, y):
    return x + y


def calculate(func, x, y):
    """
        Pass a function as an argument
    :param func:
    :param x:
    :param y:
    :return:
    """
    return func(x, y)


result = calculate(add, 4, 6)
print(result)


def greeting(name):
    """
        Return function as a value
    :param name:
    :return:
    """

    def hello():
        return "Hello, " + name + "!"

    return hello


greet = greeting("Gleb")
print(greet)
print(greet())


def make_pretty(func):
    """
        The decorator exmaple
    :param func:
    :return:
    """

    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated before call")
        # call original function
        func()
        print("I gor decorated after call")

    # return the inner function
    return inner


def ordinary():
    print("I am ordinary")


ordinary()


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide ", a, "and ", b)
        if b == 0:
            raise ZeroDivisionError
        result = func(a, b)
        print("I'v divided ", a, "and ", b, "= ", result)
        return result

    return inner


@smart_divide
def divide(a, b):
    return a / b


print(divide(8, 2))


# print(divide(8, 0))


def star(func):
    def inner(*args, **kwargs):
        print("*" * 17)
        func(*args, **kwargs)
        print("*" * 17)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 17)
        func(*args, **kwargs)
        print("%" * 17)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
