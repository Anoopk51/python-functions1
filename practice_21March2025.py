'''1.  My Incorrect Attempt of printing pattern using Class methode .'''
# class Pattern:
#     def func(base):
       
#         for i in range(1,base+1):
#             print('* '*i)
# base=int("Enter the base of tringle:")
# print(Pattern(base))



'''<-------------------My Correct Attempt of printing pattern using class methode.-------------->'''

'''2.<------- Tringle pattern i use class and methode. ------->'''


# class Pattern:
#     def func(base):
#         # base=int(input("Enter the base of tringle:"))
#         for i in range(1,base+1):
#             print('* '*i)
#             # return '* '*i
#     base=int(input("Enter the base of tringle:"))
#     func(base)

# p=Pattern()
# # print(p.func(base))
# print(p)





'''3.  Tringle Pattern using class and in class i use attribute and methode.'''

# class Pattern:
# #     def __init__(self):
# #         pass
#     def func(self):
#         # base=int(input('Enter the base of tringle:'))
#         for i in range(1,base+1):
#             print('* '*i)
#             # return '* '*i
# base=int(input('Enter the base of tringle:'))
# Pattern.func(base)


'''4. '''

# <-----------x-----------------x-----------------x----------------------x---------------x--------------->

'''             Print various python pattern of tringle using class and simple inheritance methode.'''

'''

class Pattern:
    # base=int(input("Enter the base of tringle:"))
    def tringle1(base):
        for i in range(1,base+1):
            print('* '*i)
        print('\n')
    def tringle2(base):
        for i in range(1,base+1):
            number=base+1-i
            print('* '*number)
        print('\n')
    def tringle3(base):
        for i in range(1,base+1):
            for j in range(1,base+1):
                if j<base+1-i:
                    print(' ',end=' ')
                else:
                    print('* ',end='')
            print()
        print('\n')

    def tringle4(base):
        for i in range(1,base+1):
            for j in range(1,base+1):
                if j>=i:
                    print('* ',end='')
                else:
                    print(' ',end=' ')
            print()
        print('\n')

    def tringle5(base):
        for i in range(1,base+1):
            for j in range(1,base+1):
                if j>=i:
                    print('* ',end='')
                else:
                    print(' ',end='')
            print()
        print('\n')

    def tringle6(base):
        for i in range(1,base+1):
            for j in range(1,base+1):
                if j<base+1-i:
                    print(' ',end='')
                else:
                    print('* ',end=' ')
            print()
        print('\n')
    
class final(Pattern):
    pass
base=int(input("Enter the base of tringle:"))
# final.display(base)
final.tringle1(base)
final.tringle2(base)
final.tringle3(base)
final.tringle4(base)
final.tringle5(base)
final.tringle6(base)

'''