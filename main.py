#library to interact with the operative system
import os 
#library to dont show the password in the console
from getpass import getpass
#library to make the representation of the table in the console
from tabulate import tabulate
from connection import *
import user
import password

connection = connect()
craft_table(connection)

#Function to start with the program
def start():
    #os,system('cls') can clear the console everytime the program starts
    os.system('cls')
    check = user.user_check()
    #len its to know the quantity of characters on a list
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
        #getpass make that the imput dont be shown in the console
        master_password = getpass('Please enter your password')
        answer_2 = user.password_check(2,master_password)
        if answer_2 == 0:
            print('Incorrect password')
        else:
            print('Wellcome')
            menu()


def menu():
    while True:
        option = int(input('Please choice a option and enter it using the number \n 1) Add a new password \n 2) visualize all the password \n 3) visualize one password \n 4) Change a password \n 5) Delete a password \n 6) Exit'))
        if option == 1:
            new_password()
        elif option == 2:
            show_password()
        elif option == 3:
            search_password()
        elif option == 4:
            modify_password()
        elif option == 5:
            delete_password()
        elif option == 6:
            break
        else:
            print("No valid option")


def new_password():
    name = input('Please enter your name')
    url = input('Please enter your url')
    user_name = input('Please enter your user name')
    password_new = input('Please enter your password')
    description = input('Please enter your description')
    answer = password.register(name, url, user_name, password_new, description)
    print(answer)


def show_password():
    data = password.show()
    new_data = []
    #its the way to create a header with the name of the data in every space of the table
    headers = ['ID', 'NAME', 'URL', 'USER NAME', 'PASSWORD', 'DESCRIPTION']
    #The for uses datas to go over the tuple data and to change the passwords to ***** 
    #And later append them to new_data list and show it in a table a
    for datas in data:
        converted = list(datas)
        converted [4] = '********'
        new_data.append(converted)
    #Tabulate is used to representate the table in console and the arguments its respectly the data inside(new_data, headers) and the way of how the table its phisicly represented
    table = tabulate(new_data, headers, tablefmt = 'fancy_grid')
    print('All the answers')
    print(table)

#Function able to show an especific entrance and show it but with out the "******"
def search_password():
    master_password = getpass("Please enter your master password")
    answer = user.password_check(1,master_password)
    if len(answer) == 0:
        print('Incorrect password')
    else:
        id = input('Please enter the password id')
        data = password.search(id)
        headers = ['ID', 'NAME', 'URL', 'USER NAME', 'PASSWORD', 'DESCRIPTION']
        table = tabulate(data, headers, tablefmt = 'fancy_grid')
        print('All the answers')
        print(table)
         
def modify_password():
    master_password = getpass("Please enter your master password")
    answer = user.password_check(1,master_password)
    if len(answer) == 0:
        print('Incorrect password')
    else:
        id = input('Please enter the password id')
        name = input('Please enter the new name')
        url = input('Please enter the new url')
        user_name = input('Please enter the new user_name')
        password_new = input('Please enter the new password')
        description = input('Please enter the new description')
        answer = password.modify(id, name, url, user_name, password_new, description)
        print(answer)



def delete_password():
    master_password = getpass("Please enter your master password")
    answer = user.password_check(1,master_password)
    if len(answer) == 0:
        print('Incorrect password')
    else:
        id = input('Please enter the password id')
        answer = password.delete(id)
        return answer    

start()

