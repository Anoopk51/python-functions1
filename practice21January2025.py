# Question-1

# def myfunc(n):
#     return lambda a:a*n
# mydoubler=myfunc(2)
# print(mydoubler(11))

# class myclass:
#     x=5
# p1=myclass()
# print(p1.x)

# class myclass:
#     x1=4
#     x2=5
#     x3=6
#     x4=7
# p1=myclass()
# p2=myclass()
# p3=myclass()
# p4=myclass()
# print(p1.x1)
# print(p2.x2)
# print(p3.x3)
# print(p4.x4)

# class myfunc():
#     x1=3
#     x2=5
#     x3=6
#     x4=7
#     x5=8
# p1=myfunc()
# print(p1.x1)
# print(p1.x2)
# print(p1.x3)
# print(p1.x4)
# print(p1.x5)



# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person('Anoop',22)
# print(p1.name)
# print(p1.age)


# class name:
#     def __init__(self,name,age,height):
#         self.name=name
#         self.age=age
#         self.height=height
# per1=name('Anoop',22,1.68)
# # per2=name(22)
# # per3=name(1.68)
# print(f'{per1.name}\n{per1.age}\n{per1.height}')
    

# class number():
#     def __init__(self,roll_no,mob_no,room_no):
#         self.roll_no=roll_no
#         self.mob_no=mob_no
#         self.room_no=room_no
# per1=number(100230157,9369914437,str(51)+'B')
# print(f'My Roll Number is {per1.roll_no}\nMy Mobile Number is {per1.mob_no}\nMy Room Number is {per1.room_no}')


# class number():
#     room_no=51
#     mob_no=9369914437
#     roll_no=100230517
# num=number()
# print(f'My Room number is {num.room_no}\nMy Mobile number is {num.mob_no}\nMy Roll no is {num.roll_no}')


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"My name is {self.name} and my age is {self.age}"
# p1=person('Anoop',22)
# print(p1)


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}({self.age})"
# p1=person('Anoop',36)
# print(p1)


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print('Hello my name is '+ self.name)
# p1=person('John',36)
# p1.myfunc()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(abc):
        print('Hello my name is' +abc.name)
p1=person(' Jhon' , 36)
p1.myfunc()