# WAP to find how many day in any months.
'''             <------My Attempt-------------->        '''
# year=int(input('Enter the year:'))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             is_leap_year=True
#         else:
#             is_leap_year=False
#     else:
#         is_leap_year=True
# else:
#     is_leap_year=False
# if is_leap_year==True:
#     months={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#     i=int(input('Enter the months:'))
#     day=months[i]
#     print(f'total day in {i}/{year} is {day}.')
# else:
#     months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#     i=int(input('Enter the months:'))
#     day=months[i]
#     print(f'total day in {i}/{year} is {day}.')

'''<----------Ma'am solution----------------->'''
def leap_year(year):
    if year % 4==0:
        if year % 100==0:
            if year % 400==0:
               return True
            else:
                return False
        else:
            return True
    else:
        return  False

def day_in_month(year,month):
    day_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month==2:
        return 29
    else:
        return day_list[month-1]
year=int(input("Enter a year:"))
month=int(input("Enter a month:"))
days=day_in_month(year,month)
print(days)