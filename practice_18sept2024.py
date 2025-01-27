'''<------------Ma'am solution--------------> '''
            # methode-1
# def prime_checker(number):            #6  #5   5%2==0 5%3   5%4
#     is_prime=True
#     if number==1:
#         is_prime=False
#     for i in range(2,number):   #2,3,4
#         if number%i==0:
#             is_prime=False
#     if is_prime:
#         print('It is a prime number.')
#     else:
#         print('Not a prime number.')
# n=int(input('Enter a number:\n'))
# prime_checker(n)
'''<-------------prime number checker---------------->'''
'''         <--methode-1-->             '''
# def prime_checker(number):
#     is_prime=True
#     if number==1:
#         is_prime=False
#     for i in range(2,number):
#         if number%i == 0:
#             is_prime=False
#     if is_prime==False:
#         print('Number is not prime.')
#     else:
#         print('Number is prime.')

# n=int(input('Enter the number:'))
# prime_checker(n)

'''         <--methode-2-->             '''
# number=int(input('Enter the number.'))
# is_prime=True
# if number==1:
#     is_prime=False
# for i in range(2,number):
#     if number%i==0:
#         is_prime=False
# if is_prime:
#     print('Number is prime.')
# else:
#     print('Not a prime number.')

'''<----Methode-3--------->'''
# import math
# def prime_checker(number):
#     is_prime=True
#     if number==1:
#         is_prime=False
#     for i in range(2,math.ceil(number/2)+1):
#         if number%i==0:
#             is_prime=False
#     if is_prime:
#         print('Number is prime.')
#     else:
#         print('Number is not prime.')
# n=int(input('Enter the number:'))
# prime_checker(n)
