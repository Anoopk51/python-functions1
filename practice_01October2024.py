## WAP to guess a number.
print('''
-----                           ----- -             -    -                    -
| --  \                        |_   _| |           | \  | |                  | |
| |  \/_   _   __   ___ ___      | | | |__    __   |  \ | |_   _ _  _ _  _ _ | |_ _    _ _ _ _ _
| | __| | | |/ _ \/ __/  __|     | | | `- \ / _ \  |  '   | | | |  '-  ' -  \| |-   \ / _ \  '__|
| |_\ \ |_| |  __/\__ \__  \     | | | | | |  __/  | | \  | |_| | |  | |  | || |_ )  | _ _/   |
\_____/\____|\___||___/____/     \_/ |_| |_|\___|  \_|  \_/\__'_|_|  |_|  |_||_'_ _ / \___|  _|
      
      ''')
import random
print("let me think of a number between 1 to 50.")
random_number=random.randint(1,50)
# print(random_number)
choice=input("Choose level of difficulty...Type 'easy' or 'hard':").lower()
if choice=='easy':
    # print(f"You have 10 attempts remaining to guess the number!")
    live=10
    continue_guess=True
    while continue_guess:
            print(f"You have {live} attempt remaining to guess the number!")
            guess_number=int(input("Make a guess:"))
            if random_number==guess_number:
                print(f"Your guess right,The answer was {guess_number}.")
                continue_guess=False
            else:
                print("Your Guess is too low.")
                live-=1
            if live==0:
                continue_guess=False
                print("You lose!")
if choice=='hard':
    # print(f"You have 10 attempts remaining to guess the number!")
    live=5
    continue_guess=True
    while continue_guess:
            print(f"You have {live} attempt remaining to guess the number!")
            guess_number=int(input("Make a guess:"))
            if random_number==guess_number:
                print(f"Your guess right,The answer was {guess_number}.")
                continue_guess=False
            else:
                print("Your Guess is too low.")
                live-=1
            if live==0:
                continue_guess=False
                print("You lose!")
                          