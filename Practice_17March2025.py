# # ## WAP to find prime number.
# number=int(input("Enter the number:\n"))
# prime='is prime'
# if number==1:
#     prime='is prime'
# elif number==2:
#     prime='is prime'
# for i in range(3,number+1):

#     if number%i==0:
#         prime='is not prime'
    
#     else:
#         # print(f"{number} is  prime number.")
#         prime='is prime'
# print(f"{number} ,{prime}.")
# # print('True')

'''
# number= int(input("Enter the number:"))
# prime='is prime'
# if number%1==0:
#     prime='is prime'
# if number%number==0:
#     prime='is prime'
# for i in range(2,number):
#     if number%i==0:
#         prime='is not a prime'
#     # # else:
#     # elif number!=0:
#     #     prime='is prime'
# print(f"{number} , {prime} number.")
'''
#### <----------------x----------------x----------------x--------------------x------------x----------->


# number=int(input("Enter the number:"))
# prime='is prime'
# if number%1==0:
#     prime=='is prime'
# if number%number==0:
#     prime='is prime'
# for i in range(2,number):
#     if number%i==0:
#         prime='is not a prime'
# print(f"{number} , {prime} number.")



'''<----------------x-----------------x----------------------x--------------------x--------------->'''

# base=int(input("Enter the base of tringle:"))
# symbols=input("Enter the symbols:")
# for i in range(1,base+1):
#     for j in range(1,i+1):
#         if i==j:
#             pattern=symbols*j
#         elif i>j:
#             pattern=symbols*j
#     print(pattern)



'''<-----------------x----------------------------x-----------------------x-------------------x--------------------------->'''
# base=int(input("Enter the base of tringle:"))
# symbols=input("Enter the symbols:")
# for i in range(1,base+1):
#     for j in range(1,base+1):
#         if i>=j:
#             pattern=symbols*i
      
#     print(pattern)


'''<---------------X-------------X-------------------X------------------->'''

# base=int(input("Enter the base of tringle:"))
# symbols=input("Enter the symbols:")
# # def fun():
# for i in range(1,base+1):
#     # return f'{symbols*i}'
#     print(('  '+symbols)*i)
# # pattern=fun()
# # print(pattern)


'''<-------------------x-------------------------x-----------------------x---------------->'''

# number=5
# for i in range(1,6):
#     print('*'*i)


'''<-------------------x-------------------------x-----------------------x----------------->'''

# number=int(input("Enter the number:"))
# # symbols=input("Enter the symbols:")
# symbols='*'
# for i in range(1,number+1):
#     for j in range(1,i+1):
#         if i>=j:
#            pattern=symbols*(number+1-j)
#     print(pattern)

'''<-------------------x-------------------------x-----------------------x----------------->'''

# number=int(input("Enter the number:"))
# symbol='*'
# for i in range(1,number+1):
#     # for j in  range(1,i+1):
#     #     if i>=j:
#     base=number-i
#     str=' '
#             # for k in range(1,base+1):
#             #     print(' ')
    
#     print((str+symbol)*base)


'''<-------------Question-1 WAP to find prime number.------------------------->'''
'''<-----Methode-1----------->'''
# number=int(input("Enter the number:"))
# if number%1==0:
#     prime='is prime'
# if number%number==0:
#     prime='is prime'
# for i in range(2,number):
#     if number%i==0:
#         prime='is not a prime'
#     elif number%2!=0:
#         prime='is prime'
# print(f"{number} , {prime} number.")


'''<------------------Methode-2---------->'''

# number=int(input("Enter the number:"))
# prime='is prime'
# for i in range(2,number):
#     if number%i==0:
#         prime='is not a prime'
# print(f"{number} , {prime} number.")

'''<----------------Methode-3---------------------->'''


# def funame(number,prime):
#     # number=int(input("Enter the number:"))
#     # prime='is prime'
#     for i in range(2,number):
#         # prime='is prime'
#         if number%i==0:
#             prime='is not a prime'
#     return f"{number} , {prime} number."
#     # print(f"{number} , {prime} number.")
# number=int(input("Enter the number:"))
# prime='is prime'

# value=funame(number,prime)
# print(value)

# def func(number,prime):
#     for i in range(2,number):
#         if number%i==0:
#             prime='is not a prime'
#     return f"{number}, {prime}"
# number=int(input("Enter the number."))
# prime='is prime'
# value=func(number,prime)
# print(value)

