# Circular Inheritance  --  C(B), B(A), A(C) -- Not Supported

class A(D):
    def __init__(self):
        print("bhargav")

    def m1(self):
        print("python")

    def m3(self):
        print("class")


class B(A):
    def __init__(self):
        print("learning")

    def m1(self):
        print("kirne")

    def m5(self):
        print(f"bhargav1")


class C(B):
    def __init__(self):
        print("bhargav2")

    def m1(self):
        print("python1")

    def m3(self):
        print("class1")

class D(C):
    def __init__(self):
        print("python2")

    def m1(self):
        print("bhargav2")

    def m6(self):
        print("class2")


obj = D()
obj.m6()
obj.m3()
obj.m5()
