# '''<---------Public-------------------------->'''
# # class Student:
# #     def __init__(self,name):
# #         self.name=name
# #     def display(self):
# #         print(f'Hi my self {self.name} from student class')
# # s1=Student("Rahul")
# # print(s1.name)
# # s1.display()  


# '''<----------------------Protected----------------------->'''
# # # So  having dravid class
# # class Student:
# #     def __init__(self,name,rollno):
# #         self.name=name      #public instance variable
# #         self._rollno=rollno     #protected instance variable
# #     def display(self):
# #         # print(f'Hi my self {self.name} from Student class')
# #         print(f"Hi myself {self.name} with rollno {self._rollno} from Student class")
# # class Branch(Student):
# #     pass
# # def showData():
    
# #     b1=Branch("Nisha",22)
# #     print(b1.name)
# #     print(b1._rollno)
# #     # b1.display()
# # showData()

# # s1=Student("Rahul",23)
# # # s1.name="Raunak"
# # # s1._rollno=45 
# # print(s1.name)
# # print(s1._rollno)
# # # s1.display()  


# '''<-----------------------Private---------------------->'''

# class Student:
#     def __init__(self,name,rollno,age):
#         self.name=name      #public instance variable
#         self._rollno=rollno     #protected instance variable
#         self._age=age
#     def display(self):
#         # print(f'Hi my self {self.name} from Student class')
#         print(f"Hi myself {self.name} with rollno {self._rollno} from Student class")
# class Branch(Student):
#     def show(self):
#         print(f'My age is {self._age}')
#         print(f'My rollno is{self._rollno}')
# b1=Branch("Nisha",45,23)
# # print(b1.__age)
# b1.show()
# # s1=Student("Rahul",23,20)
# # # s1.name="Raunak"
# # # s1._rollno=45 
# # print(s1.name) 
# # print(s1._rollno)
# # print(s1.__age)
# # # s1.display()  






# # class Student:
# #     def __init__(self,name,rollno,age):
# #         self.name=name      #public instance variable
# #         self._rollno=rollno     #protected instance variable
# #         self.__age=age
# #     def __display(self):
# #         # print(f'Hi my self {self.name} from Student class')
# #         print(f"Hi myself {self.name} with rollno {self._rollno} from Student class")
# #     def displayPrivateData(self):
# #         self.__display()
# # class Branch(Student):
# #     def show(self):
# #         # print(f'My age is {self.__age}')
# #         print(f'My rollno is{self._rollno}')
# # # b1=Branch("Nisha",45,23)
# # # print(b1.__age)
# # # b1.show()
# # s1=Student("Rahul",23,20)
# # # s1.name="Raunak"
# # # s1._rollno=45 
# # # print(s1.name) 
# # # print(s1.__age)
# # # s1.display()  
# # # s1.displayPrivateData()
# # # print(dir(s1))
# # print(s1.__Student__age)
# # s1._Student__display()


'''<------------x--------------------x-------------------------x-------------------->'''
    # Public specifiers

'''
class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Hi myself {self.name} from Student class")
s1=Student("Rahul")
print(s1.name)
s1.display( )  ## By default all attribute and methode is publical using

 '''




    # Protected Specifiers

'''
class Student:
    def __init__(self,name,rollno):
        self.name=name      #Public instance variable
        self._rollno=rollno #Protected instace variable
    def display(self):
        print(f"Hi myself {self.name} with rollno {self._rollno} from Student class")
class Branch(Student):
    pass
# def showData():
#     b1=Branch("Nisha",22)
#     print(b1.name)
#     print(b1._rollno)
# showData()
s1=Student("Rahul",23)
s1.name='Raunak'
s1._rollno=45
# print(s1.name)
s1.display( )  

'''

# Private Specifiers

'''
class Student:
    def __init__(self,name,rollno,age):
        self.name=name      #Public instance variable
        self._rollno=rollno #Protected instace variable
        self.__age=age
    def __display(self):
        # print(f"Hi myself {self.name} with rollno {self._rollno} from Student class")
        print(f'Hi myself {self.name} {self.__age} years old with rollno {self._rollno}')
    def displayPrivateData(self):
        self.__display()
class Branch(Student):
    def show(self):
        # print(f"My age is {self.__age}")
        print(f"My rollno is {self._rollno}")
# b1=Branch("Nisha",45,23)
# b1.show()
# print(b1.__age)
s1=Student("Rahul",23,20)
# s1.name=''
# s1._rollno=45
# print(s1.__age) # Aap __age ko accese nahi ker sakte because can't private methode or attribute out side of class.
# s1.__display()    # But __age accese ko ker sakte hai that is colled Name Mangling class. 
s1.displayPrivateData()

'''
# Private methode useing name mangling

class Student:
    def __init__(self,name,rollno,age):
        self.name=name      #Public instance variable
        self._rollno=rollno #Protected instace variable
        self.__age=age
    def __display(self):
        # print(f"Hi myself {self.name} with rollno {self._rollno} from Student class")
        print(f'Hi myself {self.name} {self.__age} years old with rollno {self._rollno} from Student class.')
    def displayPrivateData(self):
        self.__display()
class Branch(Student):
    def show(self):
        # print(f"My age is {self.__age}")
        print(f"My rollno is {self._rollno}")

s1=Student("Rahul",23,20)
# print(dir(s1))
print(s1._Student__age)
s1._Student__age=45

s1._Student__display() # this methode is name mangling.
# s1.displayPrivateData()
