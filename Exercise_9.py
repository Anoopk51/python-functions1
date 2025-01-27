#Question_1. Pizza order Program
# pirce-->small pizza=100,medium pizza=200,Large Pizza=300;
# Pepperoni for small Pizza=30;
# Pepperoni for medium or Large Pizza=50;
# Extra cheese for any size Pizza=20;


print("Hi,Welcome to join me!")
order=input('Do you want pizza,peppperoni and extra cheese(Y/N):')
if order=='y' or order=='Y':
    size=input('Enter the size of Pizza (large,medium,small):')
    bill=0
    if size=='large' or size=='Large':
        print('Please pay 300rs:')
        bill=bill+300
    elif size=='medium' or size=='Medium':
        print('Please pay 200rs:')
        bill=bill+200
    elif size=='small' or size=='Small':
        print('Please pay 100rs:')
        bill=bill+100
    else:
        print('Please enter the vaild size of pizza in between large,medium,small:')
    add_pepperoni=input('Do you want add pepperoni (Y/N):')
    if add_pepperoni=='Y' or add_pepperoni=='y':
        add_pepperoni=input('Enter the pepperoni for small,medium and large:')
        if add_pepperoni=='small' or add_pepperoni=='Small':
            print('Please pay 30rs:')
            bill=bill+30
        elif add_pepperoni=='medium' or add_pepperoni=='Medium':
            print('Please pay 50rs:')
            bill=bill+50
        elif add_pepperoni=='large' or add_pepperoni=='Large':
            print('Please pay 50rs:')
            bill=bill+50
        else:
            print('Please enter the vaild input for pepperoni in between (S/M/L):')   
    else:
        print('Your bill is',bill)
    extra_cheese=input('Do you want extra cheese (Y/N):')
    if extra_cheese=='y' or extra_cheese=='Y':
        print('Please pay 20rs:')
        total=bill+20
        print('Total bill is',total)
    else:
        print('Your total bill is',bill)
else:
    print('Sorry,you enter the wrong input or slection key:')
    print('Please enter the input or key:')
print('Thank You!')
