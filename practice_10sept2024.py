'''------Question-1--------->'''
# two number  you can from the user what is first number and what is second then add those two number.
# first_number=int(input('Enter the first number:'))
# secend_number=int(input('Enter the first number:'))
# sum=first_number+secend_number
# print(sum)

'''-----------Question-2--------------->'''
# add digits of number.
# number=int(input('Enter the number:'))
# sum=0
# while number>0:
#     remender=number%10
#     sum+=remender
#     number=int(number/10)
# print(sum)

'''-----------Question-3--------------->'''
# product the digits of number.

# number=int(input('Enter the number:'))
# product=1
# while number>0:
#     remender=number%10
#     product*=remender
#     number=int(number/10)
# print(product)


'''-----------Question-4--------------->'''
# reverse digits of a number.

# number=int(input('Enter the number:'))
# reversed=0
# while number>0:
#     remender=number%10
#     reversed=reversed*10+remender
#     number=number//10
# print(reversed)


'''-----------Question-5--------------->'''
# a=2
# b=5
# print(a>3 or b<6)
# print(a>3 or b>6)
# print(a<3 or b<6)
# print(a<3 or b>6)
# print(a>3 and b<6)
# print(a>3 and b>6)
# print(a<3 and b<6)
# print(a<3 and b>6)
# print(a^b)


'''-----------Question-6--------------->'''
# name='Anoop Kushwaha'
# print( 'a' in name)


'''-----------Question-7--------------->'''
# To find  mass body index.
# weight=int(input('Enter the weight in kg:'))
# height=float(input('Enter the height in meter:'))
# b_m_i=int(weight/(height)**2)
# print('Your body mass index is',b_m_i)


'''-----------Question-8--------------->'''
# To find round function.
# print(round(674,2))
# print(round(674,-1))
# print(round(674.1012,-1))


'''-----------Question-9--------------->'''
# Find out how many day ,weeks,months.we have left if we live until 90 year old.

# present_age=int(input('Enter the your present age.'))
# year_left=90-present_age
# day_left=year_left*365
# months_left=year_left*12
# weeks_left=year_left*52
# print(f'You have {day_left} days,{weeks_left} weeks, and {months_left} months left.')


'''-----------Question-10--------------->'''
#  WAP for visiting red fort if human age is less then 3 then not rewaire token, otherwaise buy.
# age=int(input('Enter the age :'))
# if age<=3:
#     print('token is not requare.')
# else:
#     print('token is requare.')


'''-----------Question-11--------------->'''
# WAP check the  number is even or odd.

# number=int(input('Enter the number:'))
# if number%2==0:
#     print('number is even.')
# else:
#     print('number is odd.')


'''-----------Question-12--------------->'''

# WAP for ride if person height is greter then or equal 3 feet then allow for ride,and if age is less then or eqaul
#  18 year then pay only 50 rs otherwaise pay 500rs.
# height=int(input('What is your height in feet?'))
# if height>=3:
#     print("you can ride.")
#     age=int(input('What is your age?'))
#     if age<=18:
#         print('pay to 50 rs')
#     else:
#         print('pay 100 rs')
# else:
#     print("you can't ride.")
# print('Bye')


'''-----------Question-13--------------->'''

# WAP to print number in english language.
# number=int(input('Enter the number:'))
# if number==1:
#     print('One')
# elif number==2:
#     print('two')
# elif number==3:
#     print('three')
# elif number==4:
#     print('four')
# elif number==5:
#     print('five')
# elif number==6:
#     print('six')
# else:
#     print('Wrong input!')
# print("Bye")


'''-----------Question-14--------------->'''
# Qestion:-WAP  for ride the roller coaster ,if your height is >=3 then allow for ride & and your age is < 12
#  then pay 150rs and if age is <=18 then pay 250rs and if >18 then pay 500rs.

# height=int(input('Enter the height:'))
# if height>=3:
#     print('Allow for ride.')
#     age=int(input('Enter the age:'))
#     if age<12:
#         print('Please pay 150rs.')
#     elif age<=18:
#         print('Please pay 250rs.')
#     else:
#         print('Please pay 500rs. ')
#     # else:
#     #     print('Sorry you can not ride!')
# else:
#     print("can't allow for ride.")
# print('Good luck!!')



'''-----------Question-15--------------->'''

# WAP find BMI with range of under weight & overweight. if bmi is < 18.5 then you are under weight,if bmi < 25 then
# you have a normal weight,if bmi is <30 then you are overweight , if bmi is <35 then you are obese and bellow 35 
# then you are clinically obese.

# weight=int(input('Enter your weight in kg:'))
# height=float(input('Enter you height in meter:'))
# b_m_i=int(weight/(height*height))
# if b_m_i<18.5:
#     print(f'You bmi is {b_m_i} and you are under weight.')
# elif b_m_i<25:
#     print(f'Your bmi is {b_m_i} and you have a normal weight.')
# elif b_m_i<30:
#     print(f'Your bim is {b_m_i} and you are overweight.')
# elif b_m_i<35:
#     print(f'Your bim is {b_m_i} and you are obese.')
# else:
#     print(f'your bim is {b_m_i} and you are clinically obese.')
# print('God bless you!')



'''-----------Question-16--------------->'''
# WAP to check given year is leap year:

# year=int(input('Enter the year:'))
# if year%4==0:
#     if year%100==0:
#         if  year%400==0:
#             print(f'Year {year} is a leap year.')
#         else:
#             print(f'Year {year} is not a leap year.')
#     else:
#         print(f'Year {year} is a leap year.')
# else:
#     print(f'Year {year} is not a leap year.')


'''-----------Question-17--------------->'''
# Qestion:-WAP  for ride the roller coaster ,if your height is >=3 then allow for ride & and your age is < 12
#  then pay 150rs and if age is <=18 then pay 250rs and if >18 then pay 500rs. if you want a photo during ride
#  then pay extra 50rs,if you need to pay for photo then no matter of what's your age.

# height=int(input('Enter the your height:'))
# bill=0
# if height>=3:
#     print('Allow for ride.')  
#     age=int(input('Enter your age:'))
#     if age<12:
#         print('Please pay 150rs.')
#         bill+=150
#     elif age<=18:
#         print("please pay 250rs.")
#         bill+=250
#     else:
#         print("please pay 500rs")
#         bill+=500
#     photo=input("Do you want take photo (Y/N)?")
#     if photo=='y' or photo=='Y':
#         print('Please pay 50rs extra:')
#         bill+=50
#         print('Your total bill is',bill)
#     else:
#         print(f'Please pay only {bill}rs')
# else:
#     print("Sorry,can't allow for ride.")
# print("Best of luck!")

'''-----------Question-18--------------->'''
# pizza order program,small pizza=100,mediumm pizza=200,large pizza=300,pepperoni for small pizza=30,
# pepperoni for medium or large pizza=50,extra cheese for any size pizza=20.
size=input('Enter the size of pizza (small,medium,and large).')
bill=0
# total=0
if size=='small':
    print('Please pay 100rs:')
    bill+=100
elif size=='medium':
    print('Please pay 200rs:')
    bill+=200
elif size=='large':
    print('Please pay 300rs:')
    bill+=300
# else:
#     print()
want_pepperoni=input('Do you want pepperoni (Y/N):')
if want_pepperoni=='y' or want_pepperoni=='Y':
    pepperoni_size=input('Enter the size of pepperoni small/medium/large:')
    if pepperoni_size=='small':
        print('Please pay 30rs:')
        bill+=30
    elif pepperoni_size=='medium' or pepperoni_size=='large':
        print('Please pay 50rs:') 
        bill+=50
want_cheese=input('want extra cheese(Y/N):')
if want_cheese=='y' or want_cheese=='Y':
    print('Please pay 20rs:')
    bill+=20
    print('Your tatal bill is',bill)
else:
    print('Your tatal bill is',bill)