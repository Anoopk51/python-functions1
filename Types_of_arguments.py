'''-----------------Question- Topic-positional argument--------------->'''
# def greet(name,dept):
#     print(f"Hi {name}")
#     print(f'Are you from {dept} department?')
# greet("CS","jenny")
        # correct is-->
# def greet(name,dept):
#     print(f"Hi {name}")
#     print(f'Are you from {dept} department?')
# greet("Jenny","CS")


'''---------------Question- Topic-Keyword argument---------------------->'''
# def greet(name,de 
# greet(name="Jenny",dept="CS")
            # or
# greet(dept="CS",name="Jenny")
# greet("Jenny",dept="CS")
            # or
# greet(dept="CS","Jenny")


'''---------------Question- Topic-default argument---------------------->'''
# def greet(name,subject,dept="CS"):
#     print(f"Hi {name}")
#     print(f'Do you tech {subject}?')
#     print(f'Are you from {dept} department?')
# greet('Jenny','python','ME') 


# def greet(name,subject,dept="CS"):
#     print(f"Hi {name}")
#     print(f'Do you tech {subject}?')
#     print(f'Are you from {dept} department?')
# greet('Jenny','ME') 

'''---------------Question- Topic-Arbitrary argument---------------------->'''


def add(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(f'Sum is {c}')
add(5,7,9)
add(1,2,3,4,5,6,9)