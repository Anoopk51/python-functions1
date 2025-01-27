'''-----Question no-1----------->'''
# WAP to find love score of any coplus.

# first_persion=input('What is your name?')
# second_persion=input('What is his/her name?')
# add_name=(first_persion+second_persion).lower()
# # print(add_name)
# T=add_name.count('t')
# R=add_name.count('r')
# U=add_name.count('u')
# E=add_name.count('e')
# L=add_name.count('l')
# O=add_name.count('o')
# V=add_name.count('v')
# E=add_name.count('e')
# true=T+R+U+E
# love=L+O+V+E
# love_score=int(str(true)+str(love))
# if love_score<10 or love_score>90:
#     print(f'your love score is {love_score}%')
#     print('You got together like coke and mentors.')
# elif love_score>40 and love_score<50:
#     print(f'your love score is {love_score}%')
#     print('You are allright together.')
# else:
#     print(f'Your love score is these {love_score}%')


'''<-----Question no-2----------->'''
# based on list problems.
# numbers=[1,12,3,87,4,5,6,7,9,-56]
# numbers=[1,2,3,4,5,6,7,8,9]
# print(numbers)
# print(type(numbers))]
# print(numbers[0])
# print(numbers[-2])
# print(numbers[-1])
# print(numbers[1:7])
# print(numbers[0:7])
# print(numbers[:7])
# print(numbers[1:7:2])
# print(numbers[1:9:3])
# numbers.sort()
# print(type(numbers[7]))
# numbers.reverse()
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# numbers.append(-4)
# print(numbers)
# numbers.insert(2,34)
# print(numbers)
# numbers.extend([-12,-90,-34,-56])
# print(numbers)
# numbers.remove(-56)
# print(numbers)
# print(numbers.pop(1))
# print(numbers.pop(0))



'''<-----Question no-3----------->'''

# tuples=(1,2,3,4,5,6,7,1,1,1,1)
# print(tuples)
# print(type(tuples))


'''<-----Question no-4----------->'''

# tuples={1,2,3,4,5,6,7,1,1,1,1}
# print(tuples)
# print(type(tuples))


'''<-----Question no-5----------->'''

# WAP on random Module.
# import random
# list=[1,12,3,87,4,5,6,7,9,-56]
# a=random.randint(4,8)
# b=random.randrange(4,8)
# c=random.random()
# d=random.uniform(7,90)
# random.shuffle(list)
# print(list)
# print(type(list[0]))
# f=print(list)
# print(f)
# print(type(f))


'''<-----Question no-6----------->'''
# Vertical point or program like tons a coins and find either head or tails.same program write then,
# will tell the user head or tails.


# import random
# result=random.randint(0,1)
# # print(result)
# if result==1:
#     print('Head')
# else:
#     print('Tails')


'''<-----Question no-7----------->'''
# WAP which select a random name from a list of names & the person select will have to pay for everybody food bill.
'''                       <------- methode-1--------->with using choice methode'''

# import random
# names=input('Enter the name suprated by comma:')
# names_list=names.split(',')
# print(names_list)
# # print(type(names_list))
# name=random.choice(names_list)
# print(f'{name},will pay the bill.')

'''                       <------- methode-2--------->without using choice module'''
# import random
# names=input('Enter the name suprated by comma:')
# name_list=names.split(',')
# print(name_list)
# # print(len(name_list))
# index=random.randint(0,len(name_list)-1)
# print(f'{name_list[index]},will pay the bill.')
