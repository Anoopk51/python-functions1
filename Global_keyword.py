# a=10    #global
# def display():
#     print(a)
# display()


# a=10    #global
# def display():
#     # a=15
#     print(a)
# display()
# print(a)


# a=10    #global
# def display():
#     global a
#     # a=15
#     a=a+1
#     print(a)
# display()


# # a=10    #global
# def display():
#     a=20
#     def show():
#         global a 
#         a=30
#     print(f"value of a Before calling show() function is {a}")
#     show()
#     print(f"value of a After calling show() function is {a}")
# display()
# print(a) 


# name="Jenny's"
# def display():
#     global name
#     name=name+" Lectures"
# print(name)
# display()
# print(name)


name="Jenny's"
def display():
    global name
    name=name+" Lectures"
# print(name)
print(name)
display()
print(name)



