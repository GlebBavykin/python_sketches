class Human(object):

    def __init__(self, name, age):
        print('Start Human.__init__()')
        self._name = name
        self._age = age
        print('End Human.__init__()')

    def __repr__(self):
        return f"name={self._name}, age={self._age}"

    def who_are_you(self):
        print(f"I'm {self.name}, {self.age} years old")

    def greeting(self):
        print(f"Hello there!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @age.deleter
    def age(self):
        del self._age


class CommitteeMember(Human):

    def __init__(self, name, age, committee_name, rank):
        print('Start CommitteeMember.__init__()')
        super().__init__(name, age)
        self._committee_name = committee_name
        self._rank = rank
        print('End CommitteeMember.__init__()')

    def who_are_you(self):
        print(f"I am a member of the committee with {self.rank} rank")

    def make_a_decision(self):
        print("I'm against that")

    @property
    def committee_name(self):
        return self._committee_name

    @committee_name.setter
    def committee_name(self, value):
        self._committee_name = value

    @committee_name.deleter
    def committee_name(self):
        del self._committee_name

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    @rank.deleter
    def rank(self):
        del self._rank


class Student(CommitteeMember, Human):

    def __init__(self, name, age, university, degree, committee_name=None, rank=None):
        print('Start Student.__init__()')
        super().__init__(name, age, committee_name, rank)
        self._university = university
        self._degree = degree
        print('End Student.__init__()')

    def __repr__(self):
        return f"name={self.name}, age={self.age}, university={self.university}, degree={self.degree}, committee_name={self.committee_name}, rank={self.rank}"

    def who_are_you(self):
        Human.who_are_you(self)
        CommitteeMember.who_are_you(self)
        print(f"but also I'm a {self.degree} from {self.university} university")

    def pass_the_test(self):
        print('I have passed this tests')

    @property
    def university(self):
        return self._university

    @university.setter
    def university(self, value):
        self._university = value

    @university.deleter
    def university(self):
        del self._university

    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        self._degree = value

    @degree.deleter
    def degree(self):
        del self._degree


gleb = Student('Gleb', 31, 'ITMO', 'master', 'child protection', '1')
print(gleb.name)
print(gleb.age)
gleb.greeting()
print(gleb.university)
print(gleb.degree)
gleb.pass_the_test()
print(gleb.committee_name)
print(gleb.rank)
gleb.make_a_decision()
print(gleb)
gleb.who_are_you()
print(Student.mro())
