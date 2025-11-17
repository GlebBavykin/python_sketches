from dataclasses import dataclass, asdict


@dataclass
class Book:
    title: str
    author: str
    price: float


book = Book('Onegin', 'Pushkin', 14.3)
other_book = Book('Hamlet', 'Shakespeare', 20.0)

print(book)
print(other_book)
print(asdict(other_book))
assert book != other_book


class Author:
    name: str = 'anonymous'
    age: str = '1000'
    gender: str = 'male'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

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

    @property
    # Getter method
    def age(self):
        return self.__age

    # Setter method
    @age.setter
    def age(self, val):
        self.__age = val

    # Deleter method
    @age.deleter
    def age(self):
        del self.__age


my_author = Author('Gleb', 31)
print(my_author.name)
print((my_author.age))
print(my_author.gender)
print(Author.gender)
Author.gender = 'female'
print(my_author.name)
print((my_author.age))
print(my_author.gender)
another_author = Author('Kaleb', 25)
print(another_author.name)
print((another_author.age))
print(another_author.gender)