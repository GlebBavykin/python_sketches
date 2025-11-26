# Defining a decorator
def trace(f):
    counter = 0

    def wrap(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        print(f"[TRACE] counter: {counter}")
        return f(*args, **kwargs)

    return wrap


# Applying decorator to a function
@trace
def add_two(x):
    return x + 2


# Calling the decorated function
add_two(3)
add_two(3)
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x**2))(3))
print((trace(lambda x: x**2))(3))


def outer_func(x):
    y = 4

    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z

    return inner_func


for i in range(3):
    closure = outer_func(i)
    print(f"closure({i + 5}) = {closure(i + 5)}")
