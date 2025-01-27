'''Question- Password Generator.
hints-->
Welcome to the Password Generator!
How many letter would you like in your password?
How many symbols would you like?
How many nummbers would you like?
output:-9eSn)n'''
# methode-1 hard level
import random
list=[]
password=''
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
    'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols=['!','@','#','$','%','^','&','*','(',')','+','=']
numbers=[1,2,3,4,5,6,7,8,9,0]
print("Welcome to the password Generator!")
letter=int(input('How many letter would you like in your Passwword:'))
number=int(input('How many number would you like in your password: '))
symbol=int(input('How many symbols would you like in your password:'))
for i in range(letter):
    a=random.choice(letters)
    # password+=a
    list.append(a)
print(list)
for i in range(symbol):
    b=random.choice(symbols)
    list.append(b)
# print(list)
for i in range(number):
    c=random.choice(numbers)
    list.append(c)
    random.shuffle(list)
print(list)
for i in list:
    password+=str(i)
print(password)

# methode-2 eassy level
# import random
# # list=[]
# password=''
# letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
#     'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# symbols=['!','@','#','$','%','^','&','*','(',')','+']
# numbers=[1,2,3,4,5,6,7,8,9,0]
# print("Welcome to the password Generator!")
# letter=int(input('How many letter would you like in your Passwword:'))
# number=int(input('How many number would you like in your password: '))
# symbol=int(input('How many symbols would you like in your password:'))
# for i in range(letter):
#     a=random.choice(letters)
#     password+=a
#     # list.append(a)
# # print(list)

# for i in range(symbol):
#     b=random.choice(symbols)
#     # list.append(b)
#     password+=b
# # print(list)
# for i in range(number):
#     c=random.choice(numbers)
#     password+=str(c)
#     # list.append(c)
#     # random.shuffle(list)
# # print(list)
# print(password)
# # for i in list:
# #     password+=str(i)
# # print(password)
