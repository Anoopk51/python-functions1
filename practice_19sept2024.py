'''<-------------------Question-1------------------------------->''' # methode-1
# prime number
# number=int(input('Enter the numebr:'))
# is_prime=True
# if number==1:
#     is_prime=False
# for i in range(2,number):
#     if number%i==0:
#         is_prime=False
# if is_prime:
#     print('Number is prime.')
# else:
#     print('Number not a prime.')


                            # methode-2
# import math
# number=int(input('Enter a number:\n'))
# is_prime=True
# if number==1:
#     is_prime=False
# for i in range(2,math.ceil((number/2)+1)):
#     if number%i==0:
#         is_prime=False
# if is_prime:
#     print('number is prime')
# else:
#     print('number  not a prime.')



                            # Methode-3
# def prime_checker(number):
#     is_prime=True
#     if number==1:
#         is_prime=False
#     for i in range(2,number+1):
#         # print(i)
#         if number%i==0:
#             is_prime=False
#     if is_prime:
#         print('Number is  prime.')
#     else:
#         print('Number not a prime.')

# n=int(input('Enter the number.'))
# prime_checker(n)


                            # Methode-4
# def prime_checker(number):
#     import math
#     is_prime=True
#     if number==1:
#         is_prime=False
#     for i in range(2,math.ceil(number/2)+1):
#         if number%i==0:
#             is_prime=False
#     if is_prime:
#         print('Number is prime.')
#     else:
#         print('Number is not prime.')
# n=int(input('Enter a number:\n'))
# prime_checker(n)

                     #Methode-5   
# number=int(input('Enter the number:\n'))
# list=[2,3,4,5,6,7,8,9]
# for i in list:
#     if number==i:
#         list.remove(i) 
# # print(list)
# is_prime=True
# if number==1:
#     is_prime=False
# for i in range(len(list)):
#     # print(list[i])
#     if number%list[i]==0:
#         is_prime=False
# if is_prime:
#     print('Number is prime.')
# else:
#     print('Number not a prime.')



'''<-----------------Question-2----------------------->'''
'''<----------Hangman Game--------------->'''
# # stags=['''
# # -----+------+
# #      |      |
# #      O      |
# #     /|\     |
# #     / \     |
# #             |
# #             |
# #             |
# #             |
# # ============+===  
# # ''',
# # ''' 
# # ------+------+
# #       |      |
# #       O      |
# #      /|\     |
# #      /       |
# #              |
# #              |
# #              |
# # =============+===  
# # ''',
# # '''  
# # ----------+------+
# #           |      |
# #           O      |
# #          /|\     |
# #                  |
# #                  |
# #                  |
# #                  |
# #                  |
# # =================+===  
# # ''',
# # '''  
# # ----------+------+
# #           |      |
# #           O      |
# #          /|      |
# #                  |
# #                  |
# #                  |
# #                  |
# #                  |
# # =================+===  
# # ''',
# # '''
# # -----------+------+
# #            |      |
# #            O      |
# #            |      |
# #                   |
# #                   |
# #                   |
# #                   |
# #                   |
# # ======================+===  
# # ''',
# # '''
# # ----------+------+
# #           |      |
# #           O      |
# #                  |
# #                  |
# #                  |
# #                  |
# #                  |
# #                  |
# # =================+==  
# # ''',
# # '''
# # -------+------+
# #        |      |
# #               |
# #               |
# #               |
# #               |
# #               |
# #               |
# #               |
# # ==============+==  
# # ''',]
# # words=['Apple','egg','mango']
# import random
# import words_file
# import hangman_file
# list=[]
# print("let's play Hangman game!" )
# print('You have only 6 lives so try to gues the word within 6 attempts!!')
# words=words_file.words_dictionary
# word=random.choice(words)
# print(word)
# for i in word:
#     list.append('-')
#     # print(i)
# print(list)
# live=6
# game_over=False
# while not game_over:
#     letter=input('Guess a letter:').lower()
#     for i in range(len(list)):
#         if letter==word[i]:
#             list[i]=letter
#     print(list)
#     if '-' not in list:
#         game_over=True
#         print('You Win!')
#     if letter not in word:
#         live-=1
        
#         if live==0:
#             game_over=True
#             print('You lose the match!!')
#     print(hangman_file.stages[live])


'''     <-----------------------Question-3------------------------------------------>'''
# name='ANOOP KUSHWAHA'
# lower=' '
# list=[]
# for i in name:
#     list.append(chr(ord(i)+32))
# # print(list) 
# for i in list:
#     if i=='@':
#         lower+=' '
#     else:
#         lower+=i
# print(lower)

'''     <----------------------------Question-4------------------------------------------>'''

# name='Anoop kushwaha'
# chrecter=' '
# for i in name:
#     if 'A'<= i <='Z':
#         chrecter+=chr(ord(i)+32)
#     else:
#         chrecter+=' '
# print(chrecter)



def to_lowercase(input_string):
    result = ""
    for char in input_string:
        # Check if character is uppercase (between 'A' and 'Z')
        if 'A' <= char <= 'Z':
            # Convert to lowercase by adding the difference between 'a' and 'A' (which is 32)
            result += chr(ord(char) + 32)
        else:
            # If it's not an uppercase letter, just add it as is (for spaces, lowercase letters, etc.)
            result += char
    return result

# Test the function
input_string = "ANOOP KUSHWAHA"
lowercase_string = to_lowercase(input_string)
print(lowercase_string)


















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































