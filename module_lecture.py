# import my_module 
# print(my_module.a)

# print(my_module.area_of_square(4))

# import my_module as m
# print(m.a)
# print(m.area_of_square(2))


# from my_module import calculator
# calculator(3,2)

# from my_module import calculator as c
# c(3,2)




# from my_module import *  

# print('Value of a from another module is:',a)
# print(area_of_square(4))
# calculator(3,2)




# from my_module import a
# a,b=4,5             #here a value use of this module but not use my_module file
#                     # If you try to import that(my_module) module then you write my_module with value
# sum=a+b
# print('Value of a from another module is:',a)
# print(area_of_square(4))
# calculator(3,2)


import my_module
a,b=4,5             #here a value use of this module but not use my_module file
                    # If you try to import that(my_module) module then you write my_module with value
sum=a+b
print('sum is :',sum)
print('Value of a from another module is:',my_module.a)
