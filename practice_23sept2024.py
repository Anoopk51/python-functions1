def prime_checker(number):
    is_prime=True
    if number==1:
        is_prime=False
    for i in range(2,number):
        if  number%i==0:
            is_prime=False
        # print(i)
    if is_prime:
        print('Number is prime.')
    else:
        print('Number not a prime.')    
n=int(input('Enter the number:\n'))
prime_checker(n)