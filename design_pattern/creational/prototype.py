from abc import ABC, abstractmethod
from enum import Enum, auto


class Course(Enum):
    Java = auto()
    Python = auto()
    HTML = auto()


class PersonPrototype(ABC):
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    @abstractmethod
    def clone(self) -> PersonPrototype:
        pass


class Teacher(PersonPrototype):
    def __init__(self, name: str, age: int, course: Course) -> None:
        super().__init__(name, age)
        self._course = course

    @property
    def course(self) -> Course:
        return self._course

    @course.setter
    def course(self, course) -> None:
        self._course = course

    def clone(self) -> Teacher:
        return Teacher(self._name, self._age, self._course)


class Student(PersonPrototype):
    def __init__(self, name: str, age: int, teacher: Teacher) -> None:
        super().__init__(name, age)
        self._teacher = teacher

    @property
    def teacher(self) -> Teacher:
        return self._teacher

    @teacher.setter
    def teacher(self, new_teacher: Teacher) -> None:
        self._teacher = new_teacher

    def clone(self) -> Student:
        return Student(self._name, self._age, self._teacher)


class Registry:
    def __init__(self) -> None:
        self.persons = {}

    def add_person(self, name: str, prototype: PersonPrototype) -> None:
        self.persons[name] = prototype

    def get_person(self, name: str) -> PersonPrototype | Teacher | Student:
        if name in self.persons:
            return self.persons[name].clone()
        else:
            raise ValueError(f"Prototype '{name}' not found.")
