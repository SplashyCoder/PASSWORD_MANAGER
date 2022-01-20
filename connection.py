# Module to create the data base and the tables that establish it

import sqlite3 #
from sqlite3 import Error

# Function wich connect and create the data base
def connect():
    try:
        connection = sqlite3.connect('password_database.db') #Create the data base and give it name
        return connection
    except:
        print('An error has ocurred')

# Function wich create the first the table with data(name, last_name, password)
def craft_table(connection):
    #Cursor its the way to send the information to the table
    cursor = connection.cursor() 
    #The sql_sentence is the instruction you give to the sqlite at the hour to create the data base 
        # usuario is the name of the table and the arguments inside of the paretheses is the spaces which you can use to save the information and the behaviour every single one of them has
    sql_sentence_1 = '''CREATE TABLE IF NOT EXISTS user( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_name  TEXT NOT NULL,
        password  TEXT NOT NULL
    )'''

    sql_sentence_2 = '''CREATE TABLE IF NOT EXISTS password(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        url  TEXT NOT NULL,
        user_name  TEXT NOT NULL,
        password  TEXT NOT NULL,
        description  TEXT
    )'''
    #Cursor sending the instruction to Sqlite
    cursor.execute(sql_sentence_1)
    cursor.execute(sql_sentence_2)
    #Its literally a commit to save the canges on the data base
    connection.commit()
    
    