#Module to can interact with the table password from the data base
from connection import *

#Function wich can register new entrances of passwords 
def register(name, url, user_name, password, description):
    connection = connect()
    cursor = connection.cursor()
    sql_sentence = '''INSERT INTO password(
    name, url, user_name, password, description)
    VALUES(?,?,?,?,?)'''
    data = (name, url, user_name, password, description)
    cursor.execute(sql_sentence, data)
    connection.commit()
    connection.close()

#Can show all the entrances from password
def show ():
    connection = connect()
    cursor = connection.cursor()
    #This sql_sentence select all the table and the data inside
    sql_sentence = '''SELECT * FROM password'''
    #With .execute you send the instruction to the data base and the table
    cursor.execute(sql_sentence)
    #.fetchall take all the data from the table and transform it in a list
    data = cursor.fetchall()
    connection.close()
    return data

# Function wich can show an exact entrance of the table
def search (id):
    connection = connect()
    cursor = connection.cursor()
    #sql_sentence take all the data from a exact entrance identificate with an id 
    # the 'WHERE id = ?' its the instruction wich search the id using an argument
    sql_sentence = '''SELECT * FROM password WHERE id = ?'''
    #With .execute you send the instruction(sql_sentence) to the data base and the table and the id 
    cursor.execute(sql_sentence,(id))
    #.fetchall take all the data from the table and transform it in a list
    data = cursor.fetchall()
    connection.close()
    return data

# Function wich can modify an entrance of the password table
def modify (id, name, url, user_name, password, description):
    connection = connect()
    cursor = connection.cursor()
    #UPDATE is the instruction to change data in the table
    #SET is for interact  and the argument = ? its to compare and change the data with the argument that the function asks for
    sql_sentence = ''' UPDATE password SET name = ?, url = ?, user_name = ?, password = ?, description = ? WHERE id = ?'''
    data = (name, url, user_name, password, description, id)
    cursor.execute(sql_sentence, data)
    connection.commit()
    connection.close()
    return 'password modify'

def delete(id):
    connection = connect()
    cursor = connection.cursor()
    sql_sentence = '''DELETE FROM password WHERE id = ?'''
    cursor.execute(sql_sentence, id)
    connection.commit()
    connection.close()
    return'password delete'
