'''             <---nested dictionary--------->'''
# # student_data={
# #     "name":"Ram"
# # }


# student_data={
#     "Ram":{"roll_no":10,"age":20,"course":"Python"},
#     "Mohan":{"roll_no":20,"age":22,"course":"Java"}
# }
# # print(student_data["Mohan"])
# # print(student_data["Mohan"]["roll_no"])
# student_data["Mohan"]["phone_no"]=987654
# print(student_data["Mohan"])
# print(student_data["Mohan"].pop("phone_no"))
# print(student_data["Mohan"])
# # del student_data["phone_no"]        # KeyError: 'phone_no'
# # del student_data["Mohan"]["phone_no"]
# # print(student_data["Mohan"])

'''         <--------list in nested dictionary--------> '''
# travel_data={
#     "Gujrat":["Dwarkadhish","Somnath","Statue of unity"],
#     "Rajasthan":["Jaipur","Udaipur"]
# }
# print(travel_data)
# print(travel_data["Rajasthan"])

# student_data=[
#    {"Name":"Ram","roll_no":10,"age":20,"course":"Python"},
#     {"Name":"Mohan","roll_no":20,"age":22,"course":"Java"}
# ] 
# print(student_data)  
# print(student_data[0])
# print(student_data[1])

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
# print(student_data)  
# print(student_data[0])
print(student_data[1])

