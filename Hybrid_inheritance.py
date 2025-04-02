class A:
    def display(self):
        print('display from A class')
class B(A):
    def display(self):
        print('display from B class')
class C:
    def show(self):
        print("Hi from C class")
class D(B,C): # this is single + multiple inheritance

    def display(self):
        print("display from D class")
d1=D()
d1.display()
print(D.mro())