'''<------My attempt---------------->'''


'''

print('''
# *    *      *    *      *       *       *       *       *       *       *       *     *      *     *
#                                      Welcome to My Quiz Game!
# *    *      *    *      *       *       *       *       *       *       *       *     *      *     *
# ''')
'''
def question_1():
    correct_answer=0
    print('The ability of one class to accurige methods & attributes from another class is ___')
    print('A. Inheritance\nB. Abstraction\nC. Polymorphism\nD. Objects')
    correct=input('Enter your answer(A/B/C/D):__')
    if correct=='A' or correct=='a':
        print('Correct Answer')
        correct_answer+=1
        print(f'Your current score is {correct_answer}/5\n')
    else:
        print('Incrrect Answer')
        print('The correct answer is: A')
        print(f'Your current score is {correct_answer}/5\n')

# def question_2():
    print('Which of the following is a type of inheritance?')
    print('A. Single\nB. Double\nC. Multiple\nD. Both A&C')
    correct=input('Enter your answer(A/B/C/D):__')
    if correct=='D' or correct=='d':
        print('Correct Answer')
        correct_answer=correct_answer+1
        print(f'Your current score is {correct_answer}/5\n')
    else:
        print('Incrrect Answer')
        print('The correct answer is: D')
        print(f'Your current score is {correct_answer}/5\n')


# def question_3():
    print('What type of inheritance has multiple subclasses to a single superclass?')
    print('A. Multiple Inheritance\n B.Multilevel Inheritance\n C.Hierarchical Inheritace\n D.None of these.')
    correct=input('Enter the your answer(A/B/C/D):__')
    if correct=='C' or correct=='c':
        print('Correct Answer')
        correct_answer=correct_answer+1
        print(f'Your current score is {correct_answer}/5\n')
    else:
        print('Incrrect Answer')
        print('The correct answer is: C')
        print(f'Your current score is {correct_answer}/5\n')
# def question_4():
    print('What is the depth of multilevel inheritace in Python?')
    print('A. Two level\nB. Three level\nC. Any level\nD. None of these')
    correct=input('Enter the your answer(A/B/C/D):__')
    if correct=='C' or correct=='c':
        print('Correct Answer')
        correct_answer=correct_answer+1
        print(f'Your current score is {correct_answer}/5\n')
    else:
        print('Incrrect Answer')
        print('The correct answer is: C')
        print(f'Your current score is {correct_answer}/5\n')
    
# def question_5():
    print('What does MRO stand for?')
    print('A. Method Recursive object\nB. Method Resolution order\nC. Main Resolution order\nD. Method Resolution object.')
    correct=input('Enter the your answer(A/B/C/D):__')
    if correct=='B' or correct=='b':
        print('Correct Answer')
        correct_answer=correct_answer+1
        print(f'Your current score is {correct_answer}/5\n')
    else:
        print('Incrrect Answer')
        print('The correct answer is: B')
        print(f'Your current score is {correct_answer}/5\n')

    print(f'You have given {correct_answer}/5 correct answers. ')
    percent=float((correct_answer/5)*100)
    print(f'Your score is {percent}%')

# for i in (question_1(),question_2(),question_3(),question_4(),question_5()): 
    # print(i)
question_1()
# question_2()
# question_3()
# question_4()
# question_5()
# print(f'You have given {correct_answer} correct answers. ')
# percent=float((correct_answer/5)*100)
# print(f'Your score is {percent}%')


'''
'''<-----------------------Ma'am Attempt----------------------------------------->'''

from  quiz_database import question_bank
from quiz_database import options
print("************************************")
print("Welcome to My Quiz Game!")
# question_bank=[{'text':'The ability of one class to accurige methods & attributes from another class is called',
#                 'answer':'A'},
#                {'text':'Which of the following is a type of inheritance?','answer':'D'},
#                {'text':'What type of inheritance has multiple subclasses to a single superclass?','answer':'C'},
#                {'text':'What is the depth of multilevel inheritace in Python?','answer':'C'},
#                {'text':'What does MRO stand for?','answer':'B'}
#                ]
# options=[["A. Inheritance","B. Abstraction","C. Polymorphism","D. Objects"],
#          ["A. Single","B. Double","C. Multiple","D. Both A & C"],
#          ["A. Multiple Inheritance","B.Multilevel Inheritance","C.Hierarchical Inheritace","D.None of these."],
#          ["A. Two level","B. Three level","C. Any level","D. None of these"],
#          ["A. Method Recursive object","B. Method Resolution order","C. Main Resolution order","D. Method Resolution object."]
#         ]

# for question in question_back:
#     # print(question_back[question])
#     print()

score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
for question_num in range(len(question_bank)): #0,1,2,3
    print('**************************')
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    
    guess=input("Enter your answer(A/B/C/D)").upper()
    is_correct=check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print('Correct Answer')
        score+=1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {question_bank[question_num]["answer"]}")
    print(f"Your current score is {score}/{question_num+1}")
print(f'Your have given {score} correct answers')
print(f"Your score is {(score/len(question_bank))*100}%")