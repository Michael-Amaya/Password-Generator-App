import sys
import os
from .database_connection import CONNECTION as connection, CURSOR as cursor

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import UserDifferenceException


def get_user_passwords(email):
    prepared_query = '''SELECT user_passwords.password_id,
                        user_passwords.user_id, user_passwords.name,
                        user_passwords.password from user_passwords LEFT JOIN
                        users ON user_passwords.user_id = users.user_id WHERE
                        users.email = %s;
                    '''
    prepared_tuple = (email,)
    cursor.execute(prepared_query, prepared_tuple)
    passwords_found = cursor.fetchall()
    if len(passwords_found) != 0:
        user_passwords = [{'password_id': i[0], 'user_id': i[1], 'name': i[2],
                           'password': i[3]} for i in passwords_found]

        # Check to be sure that all passwords belong to same person
        belongs_userid = user_passwords[0]['user_id']
        check_list = [belongs_userid == i['user_id'] for i in user_passwords]
        if False in check_list:
            raise UserDifferenceException('User data got mixed somewhere')
    else:
        user_passwords = None

    return user_passwords


def insert_user_password(email, name, password, key, nonce, tag):
    prepared_query1 = 'SELECT user_id from users where email = %s;'
    prepared_tuple1 = (email,)

    cursor.execute(prepared_query1, prepared_tuple1)
    record_found = cursor.fetchone()
    if record_found is None:
        return False

    user_id = record_found[0]

    prepared_query2 = '''INSERT INTO user_passwords (user_id, name, password)
                         VALUES (%s, %s, %s) RETURNING password_id;
                      '''
    prepared_tuple2 = (user_id, name, password)
    prepared_query3 = '''INSERT INTO password_aes (password_id, key, nonce,
                         tag) VALUES (%s, %s, %s, %s);
                      '''
    prepared_tuple3 = [0, key, nonce, tag]
    cursor.execute(prepared_query2, prepared_tuple2)
    password_id_inserted = cursor.fetchone()[0]
    prepared_tuple3[0] = password_id_inserted
    cursor.execute(prepared_query3, tuple(prepared_tuple3))

    connection.commit()
    return True


def get_individual_user_password(user_id, password_id):
    prepared_query = '''SELECT user_passwords.password_id, 
                        user_passwords.user_id, user_passwords.password,
                        password_aes.key, password_aes.nonce, password_aes.tag
                        FROM user_passwords LEFT JOIN password_aes ON 
                        user_passwords.password_id = password_aes.password_id
                        WHERE user_passwords.user_id = %s AND
                        user_passwords.password_id = %s;
                     '''
    prepared_tuple = (user_id, password_id)
    cursor.execute(prepared_query, prepared_tuple)
    records_found = cursor.fetchone()
    if records_found:
        password_info = {
            'password_id': records_found[0],
            'user_id': records_found[1],
            'password': records_found[2],
            'key': records_found[3],
            'nonce': records_found[4],
            'tag': records_found[5]
        }
    else:
        password_info = None

    return password_info
