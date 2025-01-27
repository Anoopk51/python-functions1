#Question-1  print matrix
order=input('Enter the order of matrix suprated by comma:')
list=[]
index=0
row_number=int(order[0])
column_number=int(order[1])
total_element=row_number*column_number
print('total element is',total_element)
element=input('Enter the element suprated by comma:')
matrix_element=element.split(',')
if len(matrix_element)==total_element:
    print(matrix_element)
    for i in  matrix_element:
        list.append(int(i))
    print(list)
    print(type(list[0]))
    for i in range(row_number):
        for j in range(column_number):
            print(list[index],end=' ')
            index+=1
        print()
else:
    print('Sorry,number of matrix element is invailed!!')