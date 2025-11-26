def add_one(x):
    return x + 1


def multiply_by_two(x):
    return x * 2


def apply(fun, x):
    return fun(x)


sum_one = apply(add_one, 10)
product = apply(multiply_by_two, 10)

print(sum_one)
print(product)

add = lambda x: x + 1
multiply = lambda x: x * 2

print(apply(add, 3))
print(apply(multiply, 4))

data = [1, 2, 3, 4, 5]

# Using the map to apply a function to each element
# Lambda function returns the square of x
result1 = map(lambda x: x * 2, data)  # Result: [2, 4, 6, 8, 10]

for item in result1:
    print(item)

# print(list(result1))
