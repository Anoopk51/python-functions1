#Question_1.To check whether given year is leap year or not.

year=int(input('Enter the year:'))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,'must be a leap year.') 
        else:
            print(year,'is not a leap year.')
    else:
        print(year,'must be a leap year.') 
       
else:
    print(year,',is not a leap year.')