import random
import hangman_file
import words_file
# from hangman_file import stages
# stage=['''
#          ------+--------+
#                |        |
#                O        |
#               /|\       |
#               / \       |  
#                         |
#                         |
#          ===============+=
# ''','''
#          -------+--------+
#                |        |
#                O        |
#               /|\       |
#               /         |  
#                         |
#                         |
#          ===============+=
# ''','''
#          -------+--------+
#                |        |
#                O        |
#               /|\       |
#                         |  
#                         |
#                         |
#          ===============+=
# ''','''
#          ------+--------+
#                |        |
#                O        |
#                |\       |
#                         |  
#                         |
#                         |
#          ===============+=
# ''','''
#          ------+--------+
#                |        |
#                O        |
#                |        |
#                         |  
#                         |
#                         |
#          ===============+=
# ''','''
#          ------+--------+
#                |        |
#                O        |
#                         |
#                         |  
#                         |
#                         |
#          ===============+=
# ''','''
#          ------+--------+
#                |        |
#                         |
#                         |
#                         |  
#                         |
#                         |
#          ===============+=
# ''']
print("let's pay Hangman game.")
print('You have only 6 lives so try to gues the word within 6 attempts! Good luck!!')
# words=['apple','egg','elephant','cat','dog','boat']
words=words_file.words_dictionary
word=random.choice(words)
print(word)
list=[]
lives=6
for i in word:
    list+='-'
print(list)
# for i in range(len(word)):
game_over=False
while not game_over:
    letter=input("Guess a letter:").lower()
    for position in range(len(word)):
        if letter==word[position]:
            list[position]=letter
    print(list)
    if '-' not in list:
        game_over=True
        print('You win!')
    if letter not in word:
        lives-=1
        if lives==0:
            game_over=True
            print('You Lose the match!')
            
    # print(stage[lives])
    print(hangman_file.stages[lives])
