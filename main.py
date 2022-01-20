import os 
from getpass import getpass
from tabulate import tabulate
from connection import *
import user
import password

connection = connect()
craft_table(connection)

def start ():

    os.system('cls')
    check = user.user_check()
    if len(check) == 0:
        print('Wellcome please enter your information')
        name = input('Please enter your name')
        last_name = input('Please enter your last name')
        password = getpass('Please enter your password')
        answer = user.register(name, last_name, password)
        if answer == 'succesfull register':
            print(f'Welcome{name}')
            menu()
        else:
            print(answer)
    else:
        master_password = getpass('Please enter your password')
        answer_2 = user.password_check(2,master_password)
        if answer_2 == 0:
            print('Incorrect password')
        else:
            print('Wellcome')
            menu()

def new_password():
    name = input('Please enter your name')
    url = input('Please enter your url')
    user_name = input('Please enter your user name')
    password_new = input('Please enter your password')
    description = input('Please enter your description')
    answer = password.register(name, url, user_name, password_new, description)
    print(answer)
    
def menu():
    while True:
        option = int(input('Please choice a option and enter it using the number \n 1) Add a new password \n 2) visualize all the password \n 4) Change a password \n 5) Delete a password \n 6) Exit'))
        if option == 1:
            new_password()
        elif option == 2:
            print("opc2")
        elif option == 3:
            print("opc3")
        elif option == 4:
            print("opc4")
        elif option == 5:
            print("opc5")
        elif option == 6:
            break
        else:
            print("No valid option")
start()

