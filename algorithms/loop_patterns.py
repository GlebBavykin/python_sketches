n = 16

for i in range(0, n):
    print(" " * (n - i), "* " * i)

print("\n\n\n\n")

for i in range(1, n - 1):
    print(" " * (n - i), "* " * i)

for i in range(1, n):
    print(" " * i, "* " * (n - i))

print("\n\n\n\n")

for i in range(0, n):
    print(" " * n, "* " * n)

print("\n\n\n\n")

for i in range(1, n):
    print(" " * (2 * i), " *" * (n - i), "* " * n)

print("\n\n\n\n")

for i in range(0, n):
    print(" " * i, " *" * (n - i), "* " * n)

print("\n\n\n\n")

for i in range(1, n):
    print(" " * i, " *" * (n - i), "* " * i)


print("\n\n\n\n")
from math import sqrt

radius = 64

for horizontal in range((2 * radius) + 1):
    for vertical in range((2 * radius) + 1):

        distance = sqrt((horizontal - radius) ** 2 + (vertical - radius) ** 2)

        if distance >= radius:
            print("*", end="")
        else:
            print(" ", end="")
    print()
