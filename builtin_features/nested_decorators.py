# Python code to illustrate
# Decorators with parameters in Python  (Multi-level Decorators)

def my_decorator(func):
    print('Before call message 1')

    def wrapper(*args, **kwargs):
        print('Before call message 2')
        return func(*args, **kwargs)

    print('After call message 1')
    return wrapper


@my_decorator
def print_number(number):
    print(number)
    return number

ls = print_number(2)


# def decodecorator(dataType, message1, message2):
#     def decorator(func):
#         print(message1)
#
#         def wrapper(*args, **kwargs):
#             print(message2)
#             if all([type(arg) == dataType for arg in args]):
#                 return func(*args, **kwargs)
#             return "Invalid Input"
#
#         return wrapper
#
#     return decorator
#
#
# @decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
# def stringJoin(*args):
#     st = ''
#     for i in args:
#         st += i
#     return st
#
#
# @decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
# def summation(*args):
#     summ = 0
#     for arg in args:
#         summ += arg
#     return summ
#
#
# print(stringJoin("I ", 'like ', "Geeks", 'for', "geeks"))
# print()
# print(summation(19, 2, 8, 533, 67, 981, 119))
