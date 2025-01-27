# WAP to calculate average height from a list of heights,without useing sum() and len() in build function.
height=input('Enter the height suprated by comma:')
total=0
sum=0
height_list=[]
list=height.split(',')
print(list)
for j in list:
    height_list.append(int(j))
print(height_list)
# print(type(height_list[2]))
for i in height_list:
    total+=1
    sum+=i
print('total number if height is',total)
print('sum of total number of height is',sum)
average=sum/total
print('average height is',average)