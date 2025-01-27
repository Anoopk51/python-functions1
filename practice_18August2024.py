# # Question-1 print the matrix of a order mXn

order=input('Enter the order of a matrix(mXn):')
row_number=int(order[0])
column_number=int(order[1])
total_element=row_number*column_number
print('total element is',total_element)
element=input('Enter the element suprated by comma:')
element_list=element.split(',')
print(element_list)

