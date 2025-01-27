# Question-1 Find out how many day,weaks,months. we have left if we live
# until 90 year old.
# Methode-1
from calendar import month

age=int(input('Enter the your present age:'))
save_day=(90-age)*365
save_weak=(90-age)*52
save_months=(90-age)*12
print(f'You have {save_day} day,{save_weak} weak and {save_months} months.')

#Methode-2

age=int(input('Enter the your age:'))
year_left=90-age
day_left=year_left*365
weak_left=year_left*52
month_left=year_left*12
print(f'You have {day_left} day,{weak_left} weak and {month_left} months left.')