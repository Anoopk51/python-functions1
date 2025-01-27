'''<---------My wrong attempt------>'''

# list=[2,3,4,5,6,7,8,9]
# number=int(input('Enter the number:'))
# print(number)
# for i in list:
#     if i==number:
#         list.remove(i)
# print(list)
#     # i==number
#     # list.remove(i)
#     # print(list)
# for j in list:
#     if number%j==0:
#         print(f'{number} is not prime.')
#         continue
#     elif number%j!=0:
#         print(f'{number} is prime.')
        
# def fun_name(*numbers):


# # numbers(2,3,4,5,6,7,8,9)
# # number=int(input('Enter the number:'))

'''<-----------Ma'am solution---------->'''
# import math
# def prime_checher(number):  #5 5%2==0 5%3 5%4
#     is_prime=True
#     if number==1:
#         is_prime=False
#     for i in range(2,math.ceil(number/2)+1):
#         if number%i==0:
#             is_prime=False
#     if is_prime==True:
#         print('It is a prime number')
#     else:
#         print("Not a prime number")
# n=int(input('Enter a number:\n'))
# prime_checher(n)



