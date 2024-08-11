# Multiple Inheritance  -- A(B, C)


class A:
    def __init__(self, a):
        print("bhargav")
        self.va = a

    def m2(self):
        print("python")

    def m1(self):
        print("class")

    def m3(self):
        print("learning")


class B:
    def __init__(self):
        print("bhargav1")

    def m1(self):
        print("class1")

    def m2(self):
        print("python1")


class C:
    def __init__(self):
        print("bhargav2")

    def m1(self):
        print("class2")

    def m3(self):
        print("python2")


class D(C, A, B):
    def __init__(self):
        print("bhargav3")

    def m1(self):
        print("python3")


obj = D()
obj.m1()
obj.m3()
obj.m2()