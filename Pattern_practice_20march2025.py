'''<-------Wring solution of 'A' pattern'''
# length=int(input("Enter the length of pattern:"))
# for i in range(1,length+1):
#     for j in range(1,length+1):
#         if length%2==0:
#             mid_point=length/2

#             if j<mid_point or j>mid_point:
#                 print(' ',end='')
#             else:
#                 print('* ',end='')
#         print()


'''1. '''

# base=int(input("Enter the length of tringle:"))
# for i in range(1,base+1):
#     print('* '*i)

'''2. '''

# base=int(input("Enter the length of tringle:"))
# for i in range(1,base+1):
#     number=base+1-i
#     print('* '*number)

'''3. '''
# base=int(input("Enter the length of tringle:"))
# for i in range(1,base+1):
#     for j in range(1,base+1):
#         if j<base+1-i:
#             print(' ',end='')
#         else:
#             print('* ',end='')
#     print()

'''4. '''

# base=int(input("Enter the length of tringle:"))
# for i in range(1,base+1):
#     for j in range(1,base+1):
#         if j<base+1-i:
#             print(' ',end=' ')
#         else:
#             print('* ',end='')
#     print()

'''5. '''

# base=int(input("Enter the length of tringle:"))
# for i in range(1,base+1):
#     for j in range(1,base+1):
#         if j>=i:
#             print('* ',end='')
#         else:
#             print(' ',end=' ')
#     print()


'''6. '''

'''<--------Wrong-solution-of 'A'---->'''
# base=int(input("Enter the length of tringle:"))
# for i in range(1,base+1):
#     for j in range(1,base+1):
#         if j<base+1-i:
#             print(' ',end=' ')
#         else:
#             print('* ',end=' ')
#             # if i>=(base-1):
#                 # if j>2 and j<5:
#                 # print(' ',end=' ')
#                 # else:
#                     # print('* ',end=' ')
#     print()


'''7.'''

'''<-----Worng attempt of E pattern.--------->'''

# base=int(input("Enter the base of pattern:"))
# for i in range(1,base+1):
#     for j in range(1,base+1):
#         if j>=base:
#             print('* ',end='')
#         if i<base-2 or i>base-2:
#             print('* ',end='\n')
#         if j==int(base/2):
#             print('* ',end='')

