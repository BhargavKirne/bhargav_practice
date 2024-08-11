# Single Inheritance -- B(A)
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


class B(A):
    def __init__(self, a):
        super().__init__(a)
        self.va = a
        print("bhargav1")

    def m1(self):
        print("python1")


obj = B(4)
obj.m1()
obj.m2()
obj.m3()
# obj.m4()
