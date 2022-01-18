#Module to interact with the data base using the functions

#lybrary to encrypt the password
import hashlib
from connection import *

#function can 
def user_check():
    connection = connect()
    cursor = connection.cursor()
    sql_sentence = 'SELECT * FROM  usuario'
    cursor.execute(sql_sentence)
    user_found = cursor.fetchall()
    connection.close
    return user_found

def register (name, last_name, password):

        connection = connect()
        cursor = connection.cursor()
        sql_sentence = '''INSERT INTO usuario
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
    sql_sentence = '''SELECT * FROM usuario
    WHERE id = ? AND password = ?'''
    uncrypted_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute(sql_sentence, (id,uncrypted_password))
    data = cursor.fetchall()
    connection.close()
    return data

print(register('David','Pacheco', 'Python1033'))
print(password_check(1,'Python1033'))