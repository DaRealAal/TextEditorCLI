import os

current_dir = os.getcwd()
user = os.getlogin()

def check_file_same():
    file_path = os.path.join(user_saved_dir, user_txt_name + ".txt")
    
    if os.path.exists(file_path):
        print("This file already exists, Try another name or directory.")
        user_saved_dir = input(f"Where do you want to save this file? Current: ({current_dir}): ")
        check_file_same()
    else:
        write_txt_file(file_path)
        print("File Saved")

def write_txt_file(file_path):

    if not os.path.exists(user_saved_dir):
        os.makedirs(user_saved_dir)
    with open(file_path, 'w') as file:
        file.write(user_txt)

user_txt = input("Enter the text you want: ")
user_txt_name = input("What do you name this file: ")
user_saved_dir = input(f"Where do you want to save this file? Current: ({current_dir}): ")

check_file_same()