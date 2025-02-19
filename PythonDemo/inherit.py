class A:
    def __init__(self):
        print("A constructor")

    def private(self):
        print("private method")


class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")


class C(A):
    def __init__(self):
        super().__init__()
        print("C constructor")

class D(C,B):
    def __init__(self):
        super().__init__()
        print("D constructor")


D = D()
D.private()