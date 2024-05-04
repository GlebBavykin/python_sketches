class Cat:
    pass

class Dog:
    pass

cat = Cat()
dog = Dog()


def mew(): print("Mew!")

def woof(): print("Woof!")

example = dict()
example.update({cat: dog, dog: cat})

cat.go_mew = mew
dog.go_woof = woof

print(example)
example[cat].go_woof()
example[dog].go_mew()


