# WAP to determine the price of pizza if small size pizza price is 150rs and medium size is 200rs and large size 
# pizza is 250rs if you want take extra cheese then you pay 20rs and if you want papperoni then you pay 30rs for 
# small and medium and large for 45rs.
choice=input("Do you want pizza {yes or no}?\n") 
if choice=='yes' or choice=='YES':
    bill=0
    size=input('Enter the size of pizza{small,medium ,large}.\n')
    if size=='small' or size=='SMALL':
        print('small size pizza price is 150rs.')
        bill=bill+150
    elif size=='medium' or size=='MEDIUM':
        print('Medium size pizza price is 200rs.')
        bill=bill+200
    elif size=='large' or size=='LARGE':
        print('Large size pizza price is 250rs.')
        bill=bill+250
    else:
        print('Please enter the right word.')
        bill=+bill
    extra_cheese=input('Do you want extra cheese!!\n')
    if extra_cheese=='yes' or extra_cheese=='YES':
        print('Price of extra cheese is 20rs')
        bill=bill+20
    papperoni=input('Do you want papperoni?\n')
    if papperoni=='yes' or papperoni=='YES':
        papperoni_size=input('Enter the size of papperoni!\n')
        if papperoni_size=='small' or papperoni_size=='SMALL' or papperoni_size=='MEDIUM' or papperoni_size=='medium':
            print('Paperoni price is small and medium size pizza is 30rs.')
            bill=bill+30
        elif papperoni_size=='large' or papperoni_size=='LARGE':
            print('papperoni price for Large size pizza is 45rs.')
            bill=bill+45
        else:
            print('Please enter the vaild size!!\n')
    print(f'You total bill is {bill}rs.\n Please pay bill! \n Thank You!')
else:
    print(f'Best you luck!\n Try again with write key!')
    print('Thank You!!')

