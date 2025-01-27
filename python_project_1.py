# rules- 0 for Rock ,1 for Paper and 2 for Scissors.
'''- Rock wins against Scissors
Scissors win against paper
Paper wins against Rock
--'''
#(((hint----> if computer choices >user choices
# You lose
# if user choices>computer choices
# You win
# if Equal then
# drow.)))
rock='''
        ------------
    ---'             )
            --------
           (---------)
           (--------)
    ---,   (------)
        ---(----)
    '''
paper='''
     ---------
----'         )
        -------
            --------)
            --------)
_______   ----------)
       '--------)
    '''
scissors='''
        ---------
    ---'      ---)-----
                -------)
              ----------)
              (----)
    ---,______(--)
        '''
gmae_images=[rock,paper,scissors]
import random
user_choice=int(input('Enter the your choice ,0 for rock,1 for paper and 2 for scissors:'))
if user_choice==0 or user_choice==1 or user_choice==2:
    print(gmae_images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer choice:")
    print(computer_choice)
    print(gmae_images[computer_choice])
    if user_choice==2 and computer_choice==0:
        print('You lose')
    elif user_choice==0 and computer_choice==2:
        print('You Win')
    elif user_choice==computer_choice:
        print('Match drow')
    elif user_choice>computer_choice:
        print('You win')
    elif user_choice<computer_choice:
        print('You lose')
else:
    print('Please enter vailed input.')