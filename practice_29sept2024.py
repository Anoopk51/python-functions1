'''Question-1 WAP for calculator-------------->'''
import os
def add(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
operation_dict={"+":add,
                    "-":subtraction,
                    "*":multiplication,
                    "/":division
                    }
def calculator():
    number1=int(input("Enter first number:"))
   
    for symbol in operation_dict:
        print(symbol)
    continue_fly=True

    while continue_fly:
        
        operator=input("Pick an operation:")
        number2=int(input("Enter the next number:"))
        op_choice=operation_dict[operator]
        output=op_choice(number1,number2)
        print(f"{number1} {operator} {number2}={output}")
        choice=input(f"Enter 'Y' to continue calculation with {output} or 'n' to start new calculation or 'x' to exit:").lower()
        # print(output)
        if choice=='y':
            number1=output
        elif choice=='n':
            continue_fly=False
            os.system("cls")
            calculator()
        else:
            continue_fly=False
            print("Bye")
calculator()