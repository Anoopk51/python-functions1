# def add(*numbbers):
#     c=0
#     for i in numbbers:
#         c+=i
#     print(f'sum is {c}')
# add(1,2)
# add(6,5,6)
# add(1,2,3,4,56,8)

# def add(*numbers,name):
#     c=0
#     print(numbers)
#     print(name)
#     for i in numbers:
#         c+=i
#     print(f'sum is {c}')
# add(1,2,name='Jenny')
# # add(6,5,6)
# # add(1,2,3,4,56,8)


# def info_person(**kwargs):
#     for key ,value in kwargs.items():
#         print(key,value)
# info_person(name="Ram",age=30,dept="CSE")
# info_person(name="Shyam",dept="CSE")

# def info_person(**kwargs,*args)
'''<-1.------------------Revew----Topic-*args------------------>'''

# def add(*numbers):  #(1,2,3,4,56,8)
#     c=0
#     for i in numbers:
#         c+=i
#     print(f'Sum is {c}')
# add(1,2)
# add(6,5,6)
# add(1,2,3,4,5,6,8)

'''<--------Question-2---------->'''
# def add(*numbers):  #(1,2,3,4,56,8)
#     c=0
#     print(numbers[0])
#     numbers[0]=4
#     for i in numbers:
#         c+=i
#     print(f'Sum is {c}')      #///TypeError: 'tuple' object does not support item assignment

# add(1,2)



'''<--------Question-3---------->'''
# def add(*numbers,name):  #(1,2,3,4,56,8)
#     c=0
#     print(numbers)
#     print(name)
#     for i in numbers:
#         c+=i
#     print(f'Sum is {c}')
# add(1,2,name='Jenny')

'''<--------Question-4---------->'''
'''-----------------topic-arbitary keyword argument------->'''

# def info_person(**kwarge):
#     for key,value in kwarge.items():
#         print(key,value)
# info_person(name='Ram',age='30',dept='IT')
# info_person(name="shyam",dept="IT")


# def fun_name(**kwarge):
#     for key,value in kwarge.items():
#         print(key,value)
# fun_name(name='Anoop Kushwaha',branch='IT',age=21)
# fun_name(name='Rahul Yadav',brach='IT',age=62)



'''<--------Question-5---------->'''

# def info_person(*args,**kwarge):
#     for key,value in kwarge.items():
#         print(key,value)
#     print(args)  
# info_person(3,4,name='Ram',age='30',dept='IT')
# info_person(7,8,9,name="shyam",dept="IT")


'''<------------Ma'am--------Assignment argument--------->'''
# def multiply(*numbers):
#     c=1
#     print(numbers)
#     print(type(numbers))
#     for i in numbers:
#         c*=i
#     print(f'Multiplication is {c}')
# multiply(2,3,-6,8)
# multiply(2,5,8,9,0,6)


