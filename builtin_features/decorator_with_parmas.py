import time


def counter(iteration):

    def inner(fun):

        print(f"{iteration} iteration has been set")

        def wrapper(*args, **kwargs):
            start_time = time.time()
            for _ in range(iteration):
                fun(*args, **kwargs)
            end_time = time.time()
            print(
                f"{iteration} calls elapsed {round((end_time - start_time) / iteration, 10)}s"
            )

        return wrapper

    return inner


@counter(5)
def print_shit():
    print("shit")


ls = print_shit.__closure__[1].cell_contents

print_shit()
print(print_shit.__closure__[1].cell_contents)
