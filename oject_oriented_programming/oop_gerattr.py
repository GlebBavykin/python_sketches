# Python program to illustrate the use of
# @property decorator


# Defining class
class Portal:

    # Defining __init__ method
    def __init__(self):
        self.__name = ""

    # Using @property decorator
    @property
    # Getter method
    def name(self):
        return self.__name

    # Setter method
    @name.setter
    def name(self, val):
        self.__name = val

    # Deleter method
    @name.deleter
    def name(self):
        del self.__name


# Creating object
p = Portal()

# Setting name
p.name = "GeeksforGeeks"

# Prints name
print(getattr(p, "name"))

# # Deletes name
# del p.name
#
# # As name is deleted above this
# # will throw an error
# print(p.name)
