'''<----------------x-----------------x------------------x-----------------x--------------------->'''
'''1.'''
# base=int(input("Enter the base of tringle:"))
# symbols='*'
# for i in range(1,base+1):
#     print(symbols*i)

'''2.'''
# base=int(input("Enter the base of tringle:"))
# symbols='*'
# for i in range(1,base+1):
#     horizontal_side=base+1-i
#     print(symbols*horizontal_side)

'''3.'''

# base=int(input("Enter the base of tringle:"))
# symbols='*'
# # space=' '

# for i in range(1,base+1):
#     for j in range(1,base+1):
#         # horizontal_side=base+1-j
#         k=base+1-i
#         if j<k:
#             print(' ',end=' ')

#         elif j>=k:
#             print(symbols ,end=' ')
#     # break
#     print()


'''

base=int(input("Enter the length of tringle:"))
symbols='*'
for i in range(1,base+1):
    print(symbols*i)

base=int(input("Enter the length of tringle:"))
symbols="*"
space=' '
for i in range(1,base+1):
    number=base+1-i
    print((symbols+" ")*number)

'''

# base=int(input("Enter the number:"))
# symbols='*'
# for i in range(1,base+1):
#     for j in range(1,base+1):
#         if base>=j:
#             pattern=(' ' + symbols)*j
#         if base<j:
#             pattern=
#     print(pattern,end=' ')
#     break



# length=int(input('Enter the base of tringle length:'))
# pattern=''
# # star=
# for i in range(length):
#     pattern+='*'
#     print(pattern)


length=int(input('Enter the length of base of a tringle:'))
pattern=''
for i in range(1,length+1):
    for j  in range(1,length+1):
        if j<=(length-i):
            # pattern=pattern+'*'
        # pass
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()

# print(type(print()))



