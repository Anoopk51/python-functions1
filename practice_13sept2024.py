'''--------Question no-1----------->'''
# topice-list
# l=[1,2,3,4,5,6,7,8]
# l.insert(2,3)
# print(l)
# # print(len(l))
# # print(l[0])
# print(l[1:7:2])

'''--------Question no-2----------->'''
                # topic-tuple
# tuple=(3)
# print(type(tuple))
# tuple=(3,)
# print(tuple)
# print(type(tuple))
# tuple1=(10,1,-10,15,20,'jenny','ram','shyam',10.2)
# print(tuple1)
# print(tuple1[0])
# print(tuple1[-1])
# print(tuple1[1:4])
# print(tuple1[0:9:2])

'''--------Question no-3----------->'''
        # topic-sets
# set={1,2,3,'true','jenny',1.11,-10,531,}
# print(set)
# set={1,2,3,'true','jenny',1.11,-10,531,1}
# print(set)
# print(type(set))
# print(len(set))
# print(set[1])
# set1={18,56,89,98,'jenny','Ture'}
# print(set1)
# print(type(set1))
# set1.add(99)
# set1.remove(89)
# set1.pop()
# print(set1)
# set2={}
# print(set2)
# print(type(set2))
# set1[2]=99
# print(set)


'''--------Question no-4----------->'''
        # topic--sets oprators
# set={1,2,3,'true','jenny',1.11,-10,531,}
# set.add((13,14,15))
# print(set)

# set1={1,2,3,4,5}
# set2={4,5,6,10,11}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1&(set2))
# print(set1|(set2))
# set1.update(['Jenny','Mohan'])
# print(set1)
# set2.intersection_update(set1)
# print(set1)
# set2.intersection_update(['Mohan','Jiya'])
# print(set2)

# print(set1.difference(set2))
# print(set1-set2)
# print(set1.symmetric_difference(set2))

# set1={1,2,3,4,5}
# set2={4,10,7,8,-10,5,1,2,3}
# print(set1.isdisjoint(set2))
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# set2.clear()
# del.set2
# print(set2)

'''                             -------topic- for loop-----                     '''
'''--------Question no-5----------->'''
    
# name='Anoop Kushwaha'
# sequence=[]
# for i in name:
#     sequence.append(name)
# print(name)


'''--------Question no-6----------->'''

# names=['Jenny','Ram','Shyam']
# for i in names:
#     if i=='Jenny':
#         print(f"{i},it's me!")


'''--------Question no-7----------->'''
# numbers=[2,3,5,-1,0,53]
# for i in numbers:
#     print(i)
# else:
#     print("Sucessfully complleted!!")

            # or
# numbers=[2,3,5,-1,0,53]
# for i in numbers:
#     # pass
#     print(i)
#     break
# else:
#     print("Sucessfully complleted!!")


'''--------Question no-8----------->'''
# tuple=(2,56,34,3,5,-1)
# for i in tuple:
#     if i%6==0:
#         print(f'{i},is divisible by 6.')
#     else:
#         print('There is no number divisible by 6 in this sequence!!')

# else:
#     print('loop successfully completed and we are in else block now!!')


'''--------Question no-9----------->'''
                        # topic-while loop
# count=1
# while count<=5:
#     print(count)
#     count+=1


# list1=[1,2,0,5,6,7,8,9,6,5,4,3,2,1]
# while list1:
#     print("Hi Jenny")
#     list1.pop()



# count=1
# while count<=5:
#     print(count)
#     count+=1
# else:
#     print("in else block")
# print("out from loop")


# count=1
# while count<=1:
#     print(count)
#     count+=1
# else:
#     print("in else block.")
# print("out from loop")


# count=1
# while count<=5:
#     print(count)
#     count+=1
#     if count==4:
#         break
# else:
#     print("in else block.")
# print("out from loop.")


# number=int(input('enter a number (-1 to quit)'))
# while number!=-1:
#     print(number)
#     number=int(input('Enter a number(-1 to quit)'))
# else:
#     print('in else block')
# print('out form loop')

'''--------Question no-10----------->'''
                # topic- break,continue & pass.
#Question-WAP to write Hi words till 6 times.
# count=1
# while count<=10:
#     print(count)
#     count+=1
#     if count==7:
#         break
#     print('Hi')
# print('out from loop')

'''--------Question no-11----------->'''
# Question-WAP to print some combined value.
# list1=['Hi','Hello','Welcome']
# names=['krishn','Ram','Madhav'] 
# for item in list1:
#     for name in names:
#         print(item,name)
#         if item=='Hello' and name=='Ram':
#             break
#     print('out from inner loop.')
# print('out from outerloop.')

'''--------Question no-12----------->'''
# WAP to print 7 times number and gap then again print number and Hi.
# count=1
# while count<=10:
#     print(count)
#     count+=1
#     if count==7:
#         continue
#     print('Hi')
# print('out from loop.')

# for i in range(5):
#     pass
# def fun():
#     pass

# count=1
# while count<=10:
#     print(count)
#     count+=1
#     if count==7:
#         pass
#     print('Hi')
# print('out from loop')

'''--------Question no-13----------->'''
# topic-function
# def geet():
#     print("Hi")
#     print("Jenny")
# geet()s