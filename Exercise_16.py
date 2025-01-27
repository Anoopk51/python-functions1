# WAP to Calculate the sum of even number from 1 to 100 including 1 & 100:
total=0
for i in range(1,101):
    if i%2==0:
        total+=i
print(total)