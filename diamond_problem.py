class A:
    def display(self):
        print('display from A class')
class B(A):
    pass
    # def display(self):
    #     print('display from B class')
class C(A):
    
    def show(self):
        print("Hi from C class")
    # def display(self):
    #     print('display from C class ')
class D(B,C): # this is single + multiple inheritance
    pass
    # def display(self):
    #     print("display from D class")
d1=D()
d1.display()
# print(D.mro())
print(D.__mro__)