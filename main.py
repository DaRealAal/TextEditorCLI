# Importing os module library
import os
import random


bye_message = ['Have a nice day!', 
               'Have a Wonderful day!',
               'Be safe:)',
               'Thanks for using this Py file!']

random_bye_message = random.choice(bye_message)
   

while True:

    user_txt = input("Enter: ")
    user_name_txt = input("What do you want to name this file: ")
    user_saved_dir = input("Where do you want to save '{}': ".format(user_name_txt))

    text_name = user_name_txt
    file = open(user_saved_dir+'/'+user_name_txt+'.txt', 'w')

    if os.path.exists(user_name_txt+'.txt'):
        print("This file already exists, Try another directory")
        user_saved_dir = input("Where do you want to save {}?: ".format(user_name_txt))    
    else:
        file.write(user_txt)
        file.close()
        
        print(f"File created to {user_saved_dir}")
        break

print('\n{}'.format(random_bye_message))