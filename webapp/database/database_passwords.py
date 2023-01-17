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
