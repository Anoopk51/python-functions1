'''                     <----------Question no--1------------>                          '''
                # My Attempt or my solution
# student_marks={'Jenny':92,'Harry':78,'Dimpy':56,'Rahul':41,'Aniket':99,'Pream':34}
# student_grade={}
# for i in student_marks:
#     if student_marks[i]>=91 and student_marks[i]<=100:
#         student_grade[i]='A+'
#         # print(student_grade)
#     elif student_marks[i]>=81 and student_marks[i]<=90:
#         student_grade[i]='A'
#     elif student_marks[i]>=71 and student_marks[i]<=80:
#         student_grade[i]='B+'
#     elif student_marks[i]>=61 and student_marks[i]<=70:
#         student_grade[i]='B'
#     elif student_marks[i]>=51 and student_marks[i]<=60:
#         student_grade[i]='c'
#     elif student_marks[i]>=41 and student_marks[i]<=50:
#         student_grade[i]='D'
#     elif student_marks[i]<=40:
#         student_grade[i]='F'
# print(student_grade)


'''             <------------Ma'am Solution--------------->'''
student_marks={
    "Jenny":92,
    "Harry":78,
    "Dimpy":56,
    "Rahul":41,
    "Aniket":99,
    "Prem":34
}
student_grade={}
for student in student_marks:
    marks=student_marks[student]    #92
    if marks>90:
        student_grade[student]="A+"
    elif marks>80:
        student_grade[student]="A"
    elif marks>70:
        student_grade[student]="B+"
    elif marks>60:
        student_grade[student]="B"
    elif marks>50:
        student_grade[student]="C"
    elif marks>40:
        student_grade[student]="D"
    else:
        student_grade[student]="F"
print(student_grade)        
    
     