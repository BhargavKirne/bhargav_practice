# Hybrid Inheritance  -- B(A), C(A), D(B, C, A)


class A:
    def __init__(self):
        print("bhargav")

    def m1(self):
        print("python")

    def m3(self):
        print(f"class")

    def m6(self):
        print("learning")


class B(A):
    def __init__(self):
        print("bhargav1")

    def m1(self):
        print("python1")

    def m5(self):
        print("class1")


class C(A):
    def __init__(self):
        print("bhargav2")

    def m1(self):
        print("python2")

    def m3(self):
        print("class2")

    def m6(self):
        print("learning2")


class D(B, C, A):
    def __init__(self):
        print("bhargav3")

    def m1(self):
        print("python3")

    def m3(self):
        print("class3")


obj = D()
obj.m6()
