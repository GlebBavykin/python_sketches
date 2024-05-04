class SuperClass1:
    def info(self):
        print("Super Class 1 method called")


class SuperClass2:
    def info(self):
        print("Super Class 2 method called")


class Derived(SuperClass1, SuperClass2):
    pass


d1 = Derived()
d1.info()
