import json
# checks a json file[like a database that contains vaccinated individuals] to get vaccinated users
def userInfo():
    print('Welcome user')
    with open('new.json') as file:
        data = json.load(file)

    while True:
        ssn_no = input('Please enter your SSN: ')

        if ssn_no not in data:
            print('Wrong SSN or You have not been vaccinated.')

        else:
            print('''\nCongratulations, you have been vaccinated.
            \nWould you like to print your certificate?
            1. Yes
            2. No''')
            choice = input('Please enter your option: ')
            if choice == '1':
                break
            elif choice == '2':
                print('Thank you for caring for the environment')
                exit()


def certificate(user):
    print('***'*11)
    print('VACCINATION CERTIFICATE\n')
    user.confirmation()
    print('\n')
    print('***'*11)


def user():
    cert = input('Please enter your SSN: ')
    if cert == '123':
        certificate(user1)
    elif cert == '456':
        certificate(user2)
    elif cert == '789':
        certificate(user3)
    else:
        print('User has no vaccination certificate')


def exit_app():
    print('Thank you ')
    exit_app = input('To exit the app enter (Q): ').lower()
    if exit_app == 'q':
        quit()
    else:
        exit()


userInfo()
user()
exit_app()
