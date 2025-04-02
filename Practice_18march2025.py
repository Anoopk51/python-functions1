'''1.'''

# base=int(input("Enter the length of tringle:"))
# symbols='*'
# for i in range(1,base+1):
#     for j in range(1,base+1):
#         if j<=(base-i):
#             print(' ',end=' ')
#         else:
#             print(symbols,end=' ')
#     print() 


'''2.'''

# def func():
#     base=int(input("Enter the length of tringle:"))
#     symbols='*'
#     for i in  range(1,base+1):
#         print((' '+symbols)*i)
# func()


# '''3.'''

# def func():
#     base=int(input("Enter the length of tringle:"))
#     symbols='*'
#     for i in range(1,base+1):
#         length=base+1-i
#         print((' '+symbols)*length)
# func()


# ''' 4.'''
# def  func():
#     base=int(input("Enter the length of tringle:"))
#     symbols='*'
#     for i in range(1,base+1):
#         for j in range(1,base+1):
#             if j<=(base-i):
#                 print(' ',end=' ')
#             else:
#                 print(symbols,end=' ')
#         print()
# func()

''' 5.'''

# def  func():
#     base=int(input("Enter the length of tringle:"))
#     symbols='*'
#     for i in range(1,base+1):
#         for j in range(1,base+1):
#             lenght=base+1-i
#             if j>(base-i):
#                 print(' ',end=' ')
#             else:
#                 print(symbols,end=' ')
#         print()
# func()


'''<---------------Pattern Pratice--------------------------------->'''
'''1.'''

# base=int(input("Enter the base of tringle:"))
# for i in range(1,base+1):
#     print('* '*i)


'''2.'''

# base=int(input("Enter the base of tringle:"))
# for i in range(1,base+1):
#     number=base+1-i
#     print('* '*number)


'''3.'''

# base=int(input("Enter the base of tringle:"))
# for i in range(1,base+1):
#     for j in range(1,base+1):
#         if j<=(base-i):
#             print(' ',end='  ')
#         else:
#             print('* ',end=' ')
#     print()


'''4.'''
base=int(input("Enter the base of tringle:"))
for i in range(1,base+1):
    for j in range(1,base+1):
        if j<=(base+1-i):
            print('* ',end=' ')
        else:
            print(' ',end=' ')
    print()