# class Instructor:
#     pass
# instructor_1=Instructor() 
# instructor_1.name='Payal' # name is atrribute of this instructor
# instructor_1.address='Delhi'
# # print(name)  # NameError: name 'name' is not defined

# # if is asinge value then
# print(instructor_1.name)


# class Instructor:
#     pass


# instructor_2=Instructor() #name,address ,id,phone_no,has_camera,has_laptop
# instructor_2.name='Jenny'
# instructor_2.address='Delhi'
# print(instructor_2.name)

# class Instructor:
#     def __init__(self):
#         print("Creating a new object")
# instructor_1=Instructor() 
# instructor_1.name='Payal' # name is atrribute of this instructor
# instructor_1.address='Delhi'
# print(instructor_1.name)

# instructor_2=Instructor() #name,address ,id,phone_no,has_camera,has_laptop
# instructor_2.name='Jenny'
# instructor_2.address='Delhi'
# print(instructor_2.name)


# class Instructor:
#     def __init__(self,instructor_name,address):
#         self.name=instructor_name
#         self.address=address
#         self.followers=0
# instructor_1=Instructor('Jenny','Gurugaon')

# print(instructor_1.name)
# print(instructor_1.followers)
# instructor_2=Instructor('Payal','Delhi')



# class Instructor:
#     pass
# instructo1_1=Instructor()
# instructo1_1.name='Anoop'
# instructo1_1.address='Belwania,Chhitauni,kushinagar'
# print(instructo1_1.name)
# print(instructo1_1.address)

# class Instructor:
#     def __init__(self,name,address):
#         self.name='Anoop'
#         self.address='Belwania,Chhita uni,Kushinagar'
    
# instructor_1=Instructor(self.name)
# print(instructor_1)


# class Instructor():
#     def __init__(self):
#         print("Creating a new object")

# instructor_1=Instructor() #name,address,id,phone_no,has_camera,has_laptop
# instructor_1.name='Anoop'
# instructor_1.address='Delhi'
# print(instructor_1.name)

# instructor_2=Instructor()
# instructor_2.name='Payal'
# instructor_2.address='Delhi'
# print(instructor_2.name)


# class Instructor():
#     def __init__(self,instructor_name,address):
#         # print("Creating a new object")
#         self.name=instructor_name
#         self.address=address
# instructor_1=Instructor('Jenny','Gurgaon') #name,address,id,phone_no,has_camera,has_laptop
# # instructor_1.name='Anoop'
# # instructor_1.address='Delhi'
# print(instructor_1.name)

# instructor_2=Instructor()
# # instructor_2.name='Payal'
# # instructor_2.address='Delhi'
# # print(instructor_2.name)




# class Instructor():
#     def __init__(self,instructor_name,address):
#         # print("Creating a new object")
#         self.name=instructor_name
#         self.address=address
#         self.followers=0
# instructor_1=Instructor('Jenny','Gurgaon') #name,address,id,phone_no,has_camera,has_laptop
# # instructor_1.name='Anoop'
# # instructor_1.address='Delhi'
# print(instructor_1.name)
# print(instructor_1.followers)
# instructor_2=Instructor('Payal','Delhi')
# # instructor_2.name='Payal'
# # instructor_2.address='Delhi'
# # print(instructor_2.name)


# <---------Assingment------->
# create two instructor name and address and print information.
class instructor:
    def __init__(self,name,address):
        self.name1=name
        self.address1=address
instructor_1=instructor('Anoop Kushwaha','Belwania Chhitauni Kushinagar')
# print(instructor_1.name1)
# print(instructor_1.address1)
print(f"{instructor_1.name1}\n{instructor_1.address1}")