'''             <-------My attempt---------->           '''
def add_new_student(Name,roll_no,age,sub):
    # student_data.append({Name,roll_no,age,sub})
    student_data.append({"Name":Name,"roll_no":roll_no,"age":age,"course":sub})
    print(student_data)
student_data=[
   {"Name":"Ram",
    "roll_no":10,
    "age":20,
    "course":"Python"
    },
    {
        "Name":"Mohan",
        "roll_no":20,
        "age":22,
        "course":"Java",
        "Phone_no":[6757355244183]
        }
] 
add_new_student("Shyam",22,13,"C++")

'''             <-----Ma'am solution-------->'''
# student_data=[
#    {"Name":"Ram",
#     "roll_no":10,
#     "age":20,
#     "course":"Python"
#     },
#     {
#         "Name":"Mohan",
#         "roll_no":20,
#         "age":22,
#         "course":"Java",
#         "Phone_no":[6757355244183]
#         }
# ] 
# def add_new_student(name,rollno,age,course_opted):
#     new_student={}
#     new_student["Name"]=name
#     new_student["roll_no"]=rollno
#     new_student["age"]=age
#     new_student["course"]=course_opted
#     student_data.append(new_student)
# add_new_student("Shayam",22,18,"C++")
# print(student_data)