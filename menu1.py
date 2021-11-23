# This starts the code
def start():
    print('''Welcome to the Group 4 app\n
    This app is for getting your digital vaccination certificate
    1. Next page
    2. Exit the app\n''')
    menu = input('Please enter your option: ')
    if menu == '1':
        main()
    elif menu == '2':
        quit()
    else:
        print('Wrong input, please try again')
        start()

# Login and registration
def main():
    print('LOGIN')
    print('\nPlease choose an option')
    print('1. Login')
    print('2. Register')
    print('3. Back')

    user_choice = input('Please choose an option: ')
    if user_choice == "1":
        login()
    elif user_choice == '2':
        Register()
    elif user_choice == '3':
        start()
    else:
        print('\nPLEASE ENTER A VALID INPUT')
        main()



def Register():
    while True:
        username = input('Create a username: ')
        if username != '':    # If username is not empty break out of the loop
            break

    while True:
        password = input('Create password: ')
        if password != '':
            break
    while True:
        confirm_password = input('Confirm your password: ')
        if confirm_password == password:      # if the passwords are the same break out of the loop
            break
        else:
            print('Password does not match')
            print()
    if user_exist(username, password):
        while True:
            print()
            error = input('User already exists. \n\nPress (T) to try again or (L) to login: ').lower()
            if error == 't':
                Register()

            elif error == 'l':
                login()

    Add_user_info([username, password])

    print('\nYour account has been created\n')
    print('You can now login')
    login()


def login():
    print('LOGIN \n')

    user_info = {}
    with open('userinfo.txt', 'r') as file:
        for line in file:
            line = line.split()
            user_info.update({line[0]: line[1]})          # Updates the dictionary with key and value

    while True:
        username = input('Enter your username: ')

        if username not in user_info:
            error = input('You are not registered \nEnter (R) to register '
                          '\n(L) to login correct username or (Q) to go back: ').lower()
            if error == 'r':
                Register()
            elif error == 'q':
                main()
            elif error == 'l':
                login()
        else:
            break

    while True:
        password = input('Enter password: ')
        if check_password(password) != user_info[username]:    # checks if the password matches the username
            print('Incorrect password')
        else:
            break

    print('\nLogin successful')


def check_password(password):
    return password


def Add_user_info(user_info: list):
    with open('userinfo.txt', 'a') as file:        # to add/append new users details to out text file
        for info in user_info:
            file.write(info)
            file.write(' ')
        file.write('\n')

# verifies the username and password and stores in a dictionary
def user_exist(username, password):
    user_info = {}
    with open('userinfo.txt', 'r') as file:
        for line in file:
            line = line.split()
            if line[0] == username and line[1] == password:
                user_info.update({line[0]: line[1]})
    if user_info == {}:
        return False
    return user_info[username] == password





start()