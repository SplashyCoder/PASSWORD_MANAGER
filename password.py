
from connection import *

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

def show ():
    connection = connect()
    cursor = connection.cursor()
    sql_sentence = '''SELECT * password'''
    cursor.execute(sql_sentence)
    data = cursor.fetchall()
    connection.close()
    return data

def search (id):

    connection = connect()
    cursor = connection.cursor()
    sql_sentence = '''SELECT * password WHERE id = ?'''
    cursor.execute(sql_sentence,(id))
    data = cursor.fetchall()
    connection.close()
    return data

def modify (id, name, url, user_name, password, description):

    connection = connect()
    cursor = connection.cursor()
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
    cursor.execute(sql_sentence)
    connection.commit()
    connection.close()
    return'password delete'
