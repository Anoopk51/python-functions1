'''Question:- WAP to make calculator with the help of function.'''

                            # My Attempt.
'''     <----------My correct attempt but without the using function.------->'''
# first_number=int(input('Enter the first number:'))
# print("+\n-\n*\n/")
# operators=input('Pick an operation:')
# second_number=int(input('Enter the next number:'))
# if operators=='+':
#     total=first_number+second_number
#     print(f'{first_number}+{second_number}={total}')
# elif operators=='-':
#     total=first_number-second_number
#     print(f'{first_number}-{second_number}={total}')
# elif operators=='*':
#     total=first_number*second_number
#     print(f'{first_number}*{second_number}={total}')
# elif operators=='/':
#     total=first_number/second_number
#     print(f'{first_number}/{second_number}={total}')
# condition=False
# while not condition:
#     choice=input(f"Enter 'Y' to continue calculation with {total} or 'n' to start new calculation or 'x' to exit:").lower()
#     if choice=='y':
#         operators=input('Pick an operation:')
#         second_number=int(input('Enter the next number:'))
#         if operators=='+':
#             total=total+second_number
#             print(f'{total}+{second_number}={total}')
#         elif operators=='-':
#             total=total-second_number
#             print(f'{total}-{second_number}={total}')
#         elif operators=='*':
#             total=total*second_number
#             print(f'{total}*{second_number}={total}')
#         elif operators=='/':
#             total=total/second_number
#             print(f'{total}/{second_number}={total}')
#     elif choice=='n':
#         first_number=int(input('Enter the first number:'))
#         print("+\n-\n*\n/")
#         operators=input('Pick an operation:')
#         second_number=int(input('Enter the next number:'))
#         if operators=='+':
#             total=first_number+second_number
#             print(f'{first_number}+{second_number}={total}')
#         elif operators=='-':
#             total=first_number-second_number
#             print(f'{first_number}-{second_number}={total}')
#         elif operators=='*':
#             total=first_number*second_number
#             print(f'{first_number}*{second_number}={total}')
#         elif operators=='/':
#             total=first_number/second_number
#             print(f'{first_number}/{second_number}={total}')
#     elif choice=='x':
#         condition=True


'''     <-----------Attempt with function----------->'''
# def fun():
#     first_number=int(input('Enter the first number:'))
#     print("+\n-\n*\n/")
#     operators=input('Pick an operation:')
#     second_number=int(input('Enter the next number:'))
#     if operators=='+':
#         total=first_number+second_number
#         print(f'{first_number}+{second_number}={total}')
#     elif operators=='-':
#         total=first_number-second_number
#         print(f'{first_number}-{second_number}={total}')
#     elif operators=='*':
#         total=first_number*second_number
#         print(f'{first_number}*{second_number}={total}')
#     elif operators=='/':
#         total=first_number/second_number
#         print(f'{first_number}/{second_number}={total}')
#     condition=False
#     while not condition:
#         choice=input(f"Enter 'Y' to continue calculation with {total} or 'n' to start new calculation or 'x' to exit:").lower()
#         if choice=='y':
#             operators=input('Pick an operation:')
#             second_number=int(input('Enter the next number:'))
#             if operators=='+':
#                 total=total+second_number
#                 print(f'{total}+{second_number}={total}')
#             elif operators=='-':
#                 total=total-second_number
#                 print(f'{total}-{second_number}={total}')
#             elif operators=='*':
#                 total=total*second_number
#                 print(f'{total}*{second_number}={total}')
#             elif operators=='/':
#                 total=total/second_number
#                 print(f'{total}/{second_number}={total}')
#         elif choice=='n':
#             first_number=int(input('Enter the first number:'))
#             print("+\n-\n*\n/")
#             operators=input('Pick an operation:')
#             second_number=int(input('Enter the next number:'))
#             if operators=='+':
#                 total=first_number+second_number
#                 print(f'{first_number}+{second_number}={total}')
#             elif operators=='-':
#                 total=first_number-second_number
#                 print(f'{first_number}-{second_number}={total}')
#             elif operators=='*':
#                 total=first_number*second_number
#                 print(f'{first_number}*{second_number}={total}')
#             elif operators=='/':
#                 total=first_number/second_number
#                 print(f'{first_number}/{second_number}={total}')
#         elif choice=='x':
#             condition=True
# fun()

'''<-----Ma'am Solution---------------->'''

import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    number1=float(input("Enter first number:"))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an operation:")   #+
        number2=float(input("Enter next number:"))
        calculator_function=operations_dict[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2}={output}")
        should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n'to new calculation or 'x' to exit." ).lower()
        if should_continue=='y':
            number1=output
        elif should_continue=='n':
            continue_flag=False
            os.system("cls")
            calculator()
        else:
            continue_flag=False
            print("Bye")
calculator()