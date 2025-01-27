'''<---------------------My First attempt-1------------------------>'''
# # print(ord('a'))
# # print(chr(98))
# def fun_name(choice):
#     # letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     if choice=='encrypt':
#         decrypt=''
#         message=input('Type your messsage.\n')
#         shift_key=int(input('Type the shift number.\n'))
#         for i in message:
#             # if i is chr:
#             incrypt=int((ord(i)+shift_key) )
#             decrypt+=(chr(incrypt))
#             # else:
#             #      decrypt+=' '
#         print(decrypt)
    
#     elif choice=='decrypt':
#             pass
# c=input("Type 'encrypt' for encryption ,type 'decrypt' for decryption.\n").lower()
# fun_name(c)

'''<---------------------My First attempt-2------------------------>'''

# def fun_name(choice):
#     chrecter=''
#     if choice=='encrypt':
#         message=input('Type your message:\n')
#         shift_key=int(input('Type the shift number:\n'))
#         for i in message:
#             encrpt_message=chr(ord(i)+shift_key)
#             chrecter+=encrpt_message
#         print(f"Here's the encrypt result:\n{chrecter}")
#     else:
#         message=input('Type your message:\n')
#         shift_key=int(input('Type the shift number:\n'))
#         for i in message:
#             decrypt_message=chr(ord(i)-shift_key)
#             chrecter+=decrypt_message
#         print(f"Here's the decrypt result:\n{chrecter}")
# def fun_name1():
#     open=False
#     c=input("Type 'encrypt' for encryption , type 'decrypt' for decryption.\n")
#     fun_name(c)
#     while not open:
        
#         salect=input("Type 'yes' if you want to go again , otherwise type 'no'.\n")
#         if salect=='yes':
#             c=input("Type 'encrypt' for encryption , type 'decrypt' for decryption.\n")
#             fun_name(c)
#         if salect=='no':
#             print('Good bye!')
#             open=True
       
# fun_name1()

'''<---------|---------------------|----nor upper attempt is correcct----|-----------------------|----------->'''
'''<-----------Ma'am solution----------------->'''
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

def encrytion(plain_text,shift_key): #hello h=7
    cipher_text=''
    for char in plain_text:                 #if shift_key=shift_key*-1
        if char in alphabet:
            position=alphabet.index(char )
            new_position=(position+shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char
    print(f"Here is the text after encryption:{cipher_text}")

def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)
            plain_text+=alphabet[new_position]
        else:
            plain_text+=char
    print(f"Here's is the text after encryption:{plain_text}")
wanna_end=False
while not wanna_end:
    What_to_do=input("Type 'encrypt' for encryption, type 'decrypt' for decryption.\n")
    text=input("Type your message:\n")
    shift=int(input("Enter shift key:\n"))
    if What_to_do=='encrypt':
        encrytion(plain_text=text,shift_key=shift)
    elif What_to_do=='decrypt':
        decryption(text,shift)
    play_again=input("Type 'yes' to continue,type 'no' to exit.\n")
    if play_again=='no':
        wanna_end=True
        print("Have a nice day!")