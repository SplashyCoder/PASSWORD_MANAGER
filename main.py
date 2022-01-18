import os 
from getpass import getpass
from tabulate import tabulate
from connection import *

connection = connect()
craft_table(connection)

def menu():
    while True:
        option = int(input('Please choice a option and enter it using the number \n 1) Add a new password \n 2) visualize all the password \n 4) Change a password \n 5) Delete a password \n 6) Exit'))
        if option == 1:
            print("opc1")
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
menu()
