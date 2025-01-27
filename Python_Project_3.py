# # 1st attempt------------------------>

# print("let's play hangman")
# print("You have only 6 lives so try to gues the word with in 6 attempt! Good luck!!")
# chioce=input("Enter the chioce of any name by first person:")
# # del.(chioce)
# list=[]
# lenght=len(chioce)
# for i in range(lenght):
#     list.append('-')
# print(list)
# digits=len(list)
# print(digits)
# for j in range(6):
#     for k in range(digits):
#         if letters==list[k]:
#             letters=input("Guess a letter:")
#         # symbolls=["O", "/", "\", "|", "/", "\"]
#         # print(f"------|{symbolls[j]}-------\n|\n|\n|\n|\n|\n|\n|")
#             print("You win the match:")
#         else:

#             break


## 2nd Attempt---------->

# print("let'sm pay Hangman")
# list=[]
# list2=[]
# world=input('Enter the world by first player:')
# for i in world:
#     list2+=i
# print(list2)
# length=len(list2)
# print(length)
# for i in world:
#     list+="-"
# print(list)
# print("You have only 6 lives so try to gues the word within 6 attempts! Good luck!!")
# for i in range(length):
#     letter=input('guess a letter:')
#     if letter==list2[i]:
#         list+=letter
#         print(list)
#         if len(list)==length:
#             print('You win')
#         break
#     else:
#         print("---------|\nO----------\n|\n|\n|\n|\n|\n|\n|")
#         break
# for i in range(length):
#     letter=input('guess a letter:')
#     if letter==list2[i]:
#         list+=letter
#         print(list)
#         if len(list)==length:
#             print('You win')
#             break
#     else:
#         print("---------|\nO\n/----------\n|\n|\n|\n|\n|\n|\n|")
#         break
# for i in range(length):
#     letter=input('guess a letter:')
#     if letter==list2[i]:
#         list+=letter
#         print(list)
#         if len(list)==length:
#             print('You win')
#             break
#     else:
#         print("---------|\nO\n/\n\----------\n|\n|\n|\n|\n|\n|\n|")
#         break
# for i in range(length):
#     letter=input('guess a letter:')
#     if letter==list2[i]:
#         list+=letter
#         print(list)
#         if len(list)==length:
#             print('You win')
#             break
#     else:
#         print("---------|\nO\n|\n/\n\\n|----------\n|\n|\n|\n|\n|\n|\n|")
#         break
# for i in range(length):
#     letter=input('guess a letter:')
#     if letter==list2[i]:
#         list+=letter
#         print(list)
#         if len(list)==length:
#             print('You win')
#             break
#     else:
#         print("---------|\nO\n|\n/\n\\n|\n/----------\n|\n|\n|\n|\n|\n|\n|")
#         break
# for i in range(length):
#     letter=input('guess a letter:')
#     if letter==list2[i]:
#         list+=letter
#         print(list)
#         if len(list)==length:
#             print('You win')
#             break
#     else:
#         print("---------|\nO\n|\n/\n\\n|\n/\n\----------\n|\n|\n|\n|\n|\n|\n|")
#         print('You lost match!')
#         break
       
"""""-----------Ma'am solution------------"""
import random
import hangman_file
stages=['''
        ----+-------+
            |       | 
            O       |
           /|\      |
           / \      |
                    |
                    |
        ============+=====
''','''
        -----+-------+
             |       | 
             O       |
            /|\      |
            /        |
                     |
                     |
        ================+=====
''',''' 
           -----+-------+
                |       | 
                O       |
               /|\      |
                        |
                        |
                        |
        ================+=====
''' ,'''
           -----+-------+
                |       | 
                O       |
               / \      |
                        |
                        |
                        |
        ================+=====
''',''' 
           -----+-------+
                |       | 
                O       |
               /        |
                        |
                        |
                        |
        ================+=====
''','''
           -----+-------+
                |       | 
                O       |
                        |
                        |
                        |
                        |
        ================+=====
''','''
        -----+-------+
             |       | 
                     |
                     |
                     |
                     |
                     |
        ==============+=====
''']
word_list=["apple","beautiful","potao"]
lives=6
chosen_word=random.choice(word_list)    #chosen_word=radom.chpice(word_file.word)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):   # 0 1 2 3 4 #apple
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter:").lower() # r
    for position in range(len(chosen_word)): # 0 1 2 3 4
        letter=chosen_word[position]
        if letter ==guessed_letter: #p == x
            display[position]=guessed_letter
    print(display)      
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives==0:
            game_over = True
            print("You Lose!")
    if '_' not in display:
        game_over=True
        print("You win")
    print(stages[lives])
    # print(hangman_file.stages[lives])
   