# WAP for fizz , Buzz job interview Question. take number till 1 to 100.
for i in range(101):
    if i%3==0 and i%5==0:
        print("Fizz Buzz!")
    elif i%3==0:
        print("Fizz!")
    elif i%5==0:
        print("Buzz!")
    else:
        print(i)
    