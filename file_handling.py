# f1=open("file_1.txt",'r')
# data=f1.read()
# print(data)

'''<----------------------x---------------------------x---------------------------x---------------------->'''

# f1=open("file_1.txt")
# data=f1.read()
# print(data)

'''<----------------------x---------------------------x---------------------------x---------------------->'''

# f1=open("file_2.txt",'r')
# data=f1.read()
# print(data)

'''<----------------------x---------------------------x---------------------------x---------------------->'''

# f1=open("file_2.txt",'w')
# # data=f1.read()
# # print(data)  


'''<----------------------x---------------------------x---------------------------x---------------------->'''

# f1=open("file_1.txt",'w')
# f1.write("Welcome to jenny's lectures")
# # data=f1.read()
# # print(data)

'''<----------------------x---------------------------x---------------------------x---------------------->'''

# f1=open("file_1.txt",'w')
# f1.write("Welcome to jenny's lectures")
# # data=f1.read()
# # print(data)
# # print(f1.read())

'''<----------------------x---------------------------x---------------------------x---------------------->'''

# f1=open("file_3.txt",'r+')
# f1.write("Welcome to jenny's lectures")
# data=f1.read()
# print(data)

'''<----------------------x---------------------------x---------------------------x---------------------->'''

# f1=open("file_1.txt",'r+')
# f1.write("Welcome to jenny's lectures")
# print(f1.read()) 
# f1.write("This is python course.")
## print(data)

'''<----------------------x---------------------------x---------------------------x---------------------->'''

# f1=open("file_1.txt",'r+')
# f1.write("Hi")
# print(f1.read())
# # data=f1.read()
# # print(data)

'''<----------------------x---------------------------x---------------------------x---------------------->'''

# f1=open("file_1.txt",'r+')
# print(f1.tell())
# f1.write("Hi")
# print(f1.tell())
# print(f1.read())
# print(f1.tell())
# # data=f1.read()
# # print(data)

'''<----------------------x---------------------------x---------------------------x---------------------->'''

# f1=open("file_1.txt",'w+')
# f1.write('Hi welcome')

# f1.write("This is python course")
# data=f1.read()
# print(data)
# f1.close()

'''<----------------------x---------------------------x---------------------------x---------------------->'''

# f1=open("file_1.txt",'w+')
# print(f1.tell())
# f1.write('Hi welcome')
# print(f1.tell())
# f1.write("This is python course")
# print(f1.tell())
# f1.seek(0) # this is pointer option
# print(f1.read())
# data=f1.read()
# print(data)
# print(f1.tell())
# f1.close()


'''<---------------Append mode---------------->'''
# f1=open('file_1.txt','a')
# f1.write("Hello students")
# print(f1.read())


'''<------------x------------------x------------------x----------------->'''
# f1=open('file_1.txt','a+')
# print(f1.tell())
# f1.seek(0)
# # f1.write("Hello students")
# print(f1.read())


'''<-------------------x---------------x-------------x------------->'''

# f1=open('file_1.txt','a+')
# print(f1.tell())
# f1.seek(0)
# # f1.write("Hello students")
# print(f1.read())
# f1.write("jenny's lectures")



'''<-------------------x---------------x-------------x------------->'''

# f1=open("C:\Desktop\myfile_desk.txt","a+")
# print(f1.tell())
# f1.seek(0)
# print(f1.read())
# f1.write("jenny's lectures")
# # import os
# print(os.getcwd())

'''<-------------------x---------------x-------------x------------->'''
# f1=open("my_images1.jpg",'rb')
# f2=open("my_image2.jpg",'wb')
# for i in f1:
#     f2.write(i)
