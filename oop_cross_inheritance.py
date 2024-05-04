class First(object):
    def __init__(self):
        print("First(): entering")
        super(First, self).__init__()
        print("First(): exiting")


class Second(object):
    def __init__(self):
        print("Second(): entering")
        super(Second, self).__init__()
        print("Second(): exiting")


class Third(First, Second):
    def __init__(self):
        print("Third(): entering")
        super(Third, self).__init__()
        print("Third(): exiting")


ls = Third()
