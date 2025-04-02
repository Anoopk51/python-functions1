class Student:
    def __init__(self,name,rollno,age):
        self.name=name      #Public instance variable
        self._rollno=rollno #Protected instace variable
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>35:
            print("Invalid age given..Age should be less than 35")
        self.__age=age

#     def __display(self):
#         # print(f"Hi myself {self.name} with rollno {self._rollno} from Student class")
#         print(f'Hi myself {self.name} {self.__age} years old with rollno {self._rollno} from Student class.')
#     def displayPrivateData(self):
#         self.__display()
# class Branch(Student):
#     def show(self):
#         # print(f"My age is {self.__age}")
#         print(f"My rollno is {self._rollno}")


s1=Student("Rahul",23,20)
print(s1.get_age())
s1.set_age(34)
print(s1.get_age())