def fun_choice(choice):
    decrypt_massage=''
    incrypt_massage=''
    if choice=='encrypt':
        message=input('Type your message:\n')
        shift_key=int(input('Type the shift number:\n'))
        for i in message:
            
            incrypt=chr((ord(i)+shift_key))
            incrypt_massage+=incrypt
        print(f"Here's the  encrypt result:{incrypt_massage}")
    choice=input("Type 'encrypt' for encryption, type 'decrypt' for decryption.\n")
    if choice=='decrypt':
        message=input('Type your message:\n')
        shift_key=int(input('Type the shift number:\n'))
        for i in message:
            
            decrypt=chr((ord(i)-shift_key))
            decrypt_massage+=decrypt
        print(f"Here's the decrypted result:{decrypt_massage}.")
select_key=False
while not select_key:
        select_option=input("Type 'yes' if you want to go again,otherwise type 'no'.")
        if select_option=='yes':
            select_key=False
            option=input("Type 'encrypt' for encryption, type 'decrypt' for decryption.\n")
            fun_choice(option)
        else:
             select_key=True
             print('Good Bye!!')

