#Module to interact with the data base using the functions

#lybrary to encrypt the password
import hashlib
from connection import *


def user_check():
    connection = connect()
    cursor = connection.cursor()
    sql_sentence = 'SELECT * FROM  user'
    cursor.execute(sql_sentence)
    user_found = cursor.fetchall()
    connection.close()
    return user_found 

def register (name, last_name, password):

        connection = connect()
        cursor = connection.cursor()
        sql_sentence = '''INSERT INTO user
        (name, last_name, password)
        VALUES (?, ?, ?)'''
        encrypted_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        data = (name, last_name, encrypted_password)
        cursor.execute(sql_sentence, data)
        connection.commit()
        connection.close()
        return 'succesfull register'

def password_check(id, password):
    connection = connect()
    cursor = connection.cursor()
    sql_sentence = '''SELECT * FROM user
    WHERE id = ? AND password = ?'''
    uncrypted_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute(sql_sentence, (id,uncrypted_password))
    data = cursor.fetchall()
    connection.close()
    return data
# user_check()
# print(register('David','Pacheco', 'Python1033'))
# print(password_check(2,'Python1033'))