'''         <------------Question No.1--------------------->        '''
# def fun1(X):
#     return X+1
# def fun2(a,b):
#     c=a+b
#     return c
# output=fun2(3,4)
# result=fun1(output)
# print(result)

'''         <------------Question No.2--------------------->        '''
# WAP to find how many day in any months.
                # M-1
# def leap_year(year):
#     if year%4==0:
#         if year%100==0:
#             if  year%400==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# def days_in_month(year,month):
#     days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
#     if leap_year(year) and month==2:
#         return 29
#     else:
#         return days_list[month-1]
# year=int(input('Enter a year:'))
# month=int(input('Enter a month:'))
# day=days_in_month(year,month)
# print(day)

        # M-2
# year=int(input('Enter a year:'))       
# if year%4==0:
#     if year%100==0:
#         if  year%400==0:
#             a_leap_year = True
#         else:
#             a_leap_year = False
#     else:
#         a_leap_year = True
# else:
#     a_leap_year = False
# if a_leap_year==True:
#     months={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#     month=int(input('Enter a month:'))
#     day=months[month]
#     print(f'Total day in {month}/{year} is {day}. ')
# else:
#     months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#     month=int(input('Enter a month:'))
#     day=months[month]
#     print(f'Total day in {month}/{year} is {day}. ')

        # M-3
# year=int(input('Enter a year:'))       
# if year%4==0:
#     if year%100==0:
#         if  year%400==0:
#             a_leap_year = True
#         else:
#             a_leap_year = False
#     else:
#         a_leap_year = True
# else:
#     a_leap_year = False
# if a_leap_year==True:
#     days_list=[31,29,31,30,31,30,31,31,30,31,30,31]
#     month=int(input('Enter a month:'))
#     day=days_list[month-1]
#     print(f'Total day in {month}/{year} is {day}. ')
# else:
#     # months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#     days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
#     month=int(input('Enter a month:'))
#     day=days_list[month-1]
#     print(f'Total day in {month}/{year} is {day}. ')
