import json

# checks a json file[like a database that contains vaccinated individuals] to get vaccinated users
def userInfo():
    print('Welcome user,')
    with open('new.json') as file:
        data = json.load(file)

    while True:
        ssn_no1 = input('Please enter your SSN: ')

        if ssn_no1 not in data:
            print('\nWrong SSN or You have not been vaccinated.')

        else:
            print('''\nCongratulations, you have been vaccinated.
            \nWould you like to print your certificate?
            1. Yes
            2. No''')
            choice = input('Please enter your option: ')
            if choice == '1':
                Cert(ssn_no1)
                break
            elif choice == '2':
                print('Thank you for caring for the environment')
                exit()


''''
def user():
    with open('new.json', 'r') as file:
        data = json.load(file)
    ssn_no = input('Enter SSN: ')
    if ssn_no not in data:
        print('Wrong input')
        user()
    else:
        Cert(ssn_no)
'''

def Cert(ssn_no):
    with open('new.json', 'r') as file:
        data = json.load(file)
        # store the values of the key in an object
        a = data[ssn_no]

    print('\t\tVACCINATION CERTIFICATE\n', '------' * 7)
    print(a['firstName'], a['lastName'], ' Sex:', a['gender'], ' Age:', a['age'])
    print('Vaccine taken:', a['vaccine'])
    print('Medical Centre:', a['hospital'])
    print('Vaccination Date:', a['Vac_date'])
    print('------' * 7, '\n')


def exit_app():
    print('Thank you ')
    exit_appl = input('To exit the app enter (Q): ').lower()
    if exit_appl == 'q':
        quit()
    else:
        print('Please enter valid input')
        exit_app()


userInfo()
#user()
exit_app()



