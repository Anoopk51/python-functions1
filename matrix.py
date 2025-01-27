# order_1=input('enter the order(mXn) of matix_1:')
# row_1=int(order_1[0])
# column_1=int(order_1[1])
# number_of_element_1=row_1*column_1
# print('Number of element 1 is',number_of_element_1)
# element_1=input('Number of element of matrix_1:')
# order_2=input('enter the order(mXn) of matix_2:')
# row_2=int(order_2[0])
# column_2=int(order_2[1])
# number_of_element_2=row_2*column_2
# print('Number of element 2 is',number_of_element_2)
# element_2=input('Number of element of matrix_1:')
# if number_of_element_1==element_1:
#     print('Error,re-enter the number of element of matix:')
    
# else:

order=input('enter the order of matrix(mXn):')
matrix=[]
index=0
row=int(order[0])
column=int(order[1])
total_element=row*column
print('total element is',total_element)
element=input('enter the element of a matrix:')
list=element.split( )
print(list)
for i in list:
    matrix.append(int(i))
print(matrix)
print(type(matrix[0]))
if total_element==len(matrix):
    for i in range(row):
        for j in range(column):
            print(matrix[index],end=' ')
            index+=1
        print()
else:
    print('Sorry,please enter right number of matrix element:')









