'''         <-----------Question-1----------------->        '''
# phone_no={'Ram':1234,'Shyam':34567,'Mohan':8976}
# print(phone_no)
# print(phone_no['Ram'])

'''         <-----------Question-2----------------->        '''
# phone_no=dict({'Ram':1234,'Shyam':34567,'Mohan':8976})
# print(phone_no)
# print(type(phone_no))

'''         <-----------Question-3----------------->        '''
# phone_no={'Ram':1234,'Shyam':34567,'Mohan':8976}
# phone_no['Mohan']=11111
# phone_no['Madhav']={111,222,3333}
# print(phone_no)

'''         <-----------Question-4----------------->        '''
# phone_no={'Ram':1234,'Shyam':34567,'Mohan':8976}
# phone_no['Shyam']={'Shyam_Home':5555,'Shyam_work':4444}
# # print(phone_no)
# # print(phone_no['Shyam']['Shyam_Home'])
# # print(phone_no.pop('Ram'))
# # del phone_no['Ram']
# print(phone_no)
# # phone_no.clear()
# print(phone_no.keys())
# print(phone_no.values())


'''         <-----------Question-5----------------->        '''
# phone_no={'Ram':1234,'Shyam':34567,'Mohan':8976}
# for i in phone_no:
#     print(i)
#     print(phone_no[i])

'''         <-----------Question-6----------------->        '''
# student_marks={
#     'Jenny':92,
#     'Harry':78,
#     'Rahul':41,
#     'Aniket':99,
#     'Pream':34,
# }
# student_grade={}
# for student in student_marks:
#     mark=student_marks[student]
#     if mark>90:
#         student_grade[student]="A+"
#     elif mark>80:
#         student_grade[student]="A"
#     elif mark>70:
#         student_grade[student]="B+"
#     elif mark>60:
#         student_grade[student]="B"
#     elif mark>50:
#         student_grade[student]="C"
#     elif mark>40:
#         student_grade[student]="D"
#     else:
#         student_grade[student]="F"
# print(student_grade)


'''         <-----------Question-7----------------->        '''
                    # Topic:-Dictionaries
# student_data={"Ram":{"roll_no":10,"age":20,"course":"Python"},
#               "Mohan":{"roll_no":20,"age":22,"course":"Java"}}
# # print(student_data)
# # print(student_data["Ram"]["roll_no"])
# # del student_data["Mohan"]["roll_no"] 
# # print(student_data)  
# print(student_data["Mohan"].pop("course"))
# print(student_data)


'''         <-----------Question-8----------------->        '''
# travel_data={"Gujrat":["Dwarkadhish","Somnath","Statue of unity"],"Rajasthan":["Jaipur","Udaipur"]}
# print(travel_data)
# print(type(travel_data["Gujrat"]))

'''         <-----------Question-9----------------->        '''
# student_data=[{"Name":"Ram","roll_no":10,"age":20,"course":"Python"},{"Name":'Ram',"roll_no":10,"age":22,"course":"Java"}]
# print(student_data)
# print(student_data[0])
# print(type(student_data[0]))


'''         <-----------Question-10----------------->        '''
# student_marks={
#     'Jenny':92,
#     'Harry':78,
#     'Rahul':41,
#     'Aniket':99,
#     'Pream':34,
# }
# student_marks.clear()
# student_marks.keys()
# student_marks.values()

# print(student_marks)
# print(student_marks.keys())
# print(student_marks.values())
# print(type(student_marks.values()))

'''         <-----------Question-11----------------->        '''
student_data=[{"Name":"Ram",
               "roll_no":10,
               "age":20,
               "course":"Python"
               },{
                   "Name":'Ram',
                   "roll_no":10,
                   "age":22,
                   "course":"Java"
                   }]
# def add_new_student(name,rollno,age,course):
#     new_student={}
#     new_student["Name"]=name
#     new_student["roll_no"]=rollno
#     new_student["age"]=age
#     new_student["course"]=course
#     student_data.append(new_student)
# add_new_student("Shayam",22,13,"C++")
# print(student_data)
            #Methode-2
def add_new_student(name,rollno,age,course):
    student_data.append({"Name":name,"roll_no":rollno,"age":age,"course":course})
    print(student_data)
add_new_student("Shayam",22,18,"C++")