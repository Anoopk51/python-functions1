# # WAP to find maximum number from a list of number,without use max() in build function.
'''--- my wrong attemmpt------>'''
# number=input('Enter the number suprated by comma:') 
# list=[]
# index=0
# # j=0
# number_list=number.split(',')
# print(number_list)
# for j in  number_list:
#     list.append(int(j))
# print(list)
# print(type(list[1]))
# for i in list:
#     # for j in list:
#     #     if i<j:
#     #         pass
#     #     print(j)
#     #         break
#     #     elif i==j:
#     #         print(i)
#     # else:
#     #     print('Greastesd')

# list=['Anoop','Kushwaha',1,2,3,4]
# print(len(list))

'''<-------------------------2nd attempt------------------------------------------------->'''

# number=input('Enter the number suprated by comma:')
# list=[]
# number_list=number.split(',')
# for i in number_list:
#     list.append(int(i))
# print(list)
# # print(type(list[0]))
# maximum_number=list[0]
# for number in list:
#     if number>maximum_number:
#         maximum_number=number
# print(f'maximun_nuber is',maximum_number)


'''<-------------------------ma'am aproch------------------------------------------------->'''
# number=input('Enter the number suprated by comma:')
# number_list=number.split(',')
# count=0
# for number in number_list:
#     count+=1
# print(count)
# for i in range(count):
#     number_list[i]=int(number_list[i])
# print(number_list)
# maximum_number=number_list[0]
# for number in number_list:
#     if number> maximum_number:
#         maximum_number=number
# print(f'The maxium number is:{maximum_number}')