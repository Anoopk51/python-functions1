# class Instructor:
#     followers=0     #CLASS OBJECT VARIABLE
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#         # self.followers=0
#     def display(self):
#         print(f"Hi, I am {self.name}")

# instructor_1=Instructor('Jenny','Gurugaon')
# print(instructor_1.name)
# # print(instructor_1.followers)
# # instructor_2=Instructor('Jiya','Gurugaon')
# instructor_1.display()


# class Instructor:
#     followers=0     #CLASS OBJECT VARIABLE
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#         # self.followers=0
#     def display(self,subject_name):
#         print(f"Hi, I am {self.name} and I teach {subject_name}")

# instructor_1=Instructor('Jenny','Gurugaon')
# print(instructor_1.name)
# # print(instructor_1.followers)
# # instructor_2=Instructor('Jiya','Gurugaon')
# instructor_1.display('Python')


# class Instructor:
#     followers=0     #CLASS OBJECT VARIABLE
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#         # self.followers=0
#     def display(self,subject_name):
#         print(f"Hi, I am {self.name} and I teach {self.subject_name}")
#         # AttributeError: 'Instructor' object has no attribute 'subject_name'
#     def update_followers(self):
#         self.followers +=1



# instructor_1=Instructor('Jenny','Gurugaon')
# print(instructor_1.name)
# # print(instructor_1.followers)
# # instructor_2=Instructor('Jiya','Gurugaon')
# instructor_1.display('Python')
# print(instructor_1.fllowers)
# instructor_2=Instructor('Jiya','Gurugaon')



# 06/02/2025 Practice----->

# class Instructor:
#     pass
# instructor_1=Instructor()
# instructor_1.name='Anoop'
# print(instructor_1.name)

# class Instructor:
#     def __init__(self):
#         pass



# class Instructor:
#     followers=0     #This is class object variable.
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#         # self.followers=0
# instructor_1=Instructor('Anoop','Gurugaon')
# print(instructor_1.name)
# print(instructor_1.followers)
# instructor_2=Instructor('Jiya','Gurugaon')
# print(instructor_2.name)



# class Instructor:
#     followers=0     #This is class object variable.
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#         # self.followers=0
#     def display(self,subject_name):
#         # print('Hi')
#         print(f'Hi, I am {instructor_1.name} and I teach {subject_name}')

# instructor_1=Instructor('Anoop','Gurugaon')
# print(instructor_1.name)
# print(instructor_1.followers)
# print(instructor_1.display())
# instructor_1.display("Python")
# instructor_2=Instructor('Jiya','Gurugaon')
# print(instructor_2.name)




# class Instructor:
#     followers=0     #This is class object variable.
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#         # self.followers=0
#     def display(self,subject_name):
#         # print('Hi')
#         print(f'Hi, I am {instructor_1.name} and I teach {subject_name}')
#     def update_followers(self,follower_name):
#          self.followers+=1  
# instructor_1=Instructor('Anoop','Gurugaon')

# print(instructor_1.name)
# instructor_1.display("Python")
# instructor_1.update_followers('Payal')
# print(instructor_1.followers)
# instructor_2=Instructor("Jiya","Gurugaon")
# # print(instructor_2.followers)
# instructor_2.update_followers('Anoop')
# print(instructor_2.followers)