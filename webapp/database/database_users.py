from .database_connection import CONNECTION as connection, CURSOR as cursor


def create_user(name, birthday, email, password, pin):
    prepared_query = 'INSERT INTO users (name, birthday, email, password, ' + \
                     'pin) VALUES (%s, %s, %s, %s, %s)'
    prepared_tuple = (name, birthday, email, password, pin)
    cursor.execute(prepared_query, prepared_tuple)
    connection.commit()
    return True


def get_user_data(email):
    prepared_query = 'SELECT * FROM users WHERE email = %s'
    prepared_tuple = (email,)
    cursor.execute(prepared_query, prepared_tuple)
    user_record = cursor.fetchone()

    if user_record is None:
        return None
    else:
        to_return = {
            'user_id': user_record[0],
            'name': user_record[1],
            'birthday': user_record[2],
            'email': user_record[3],
            'password': user_record[4],
            'pin': user_record[5],
            'created_on': user_record[6],
            'last_login': user_record[7]
        }

        return to_return


def change_user_password(email, password):
    prepared_query = 'UPDATE users SET password = %s WHERE email = %s'
    prepared_tuple = (email, password)
    cursor.execute(prepared_query, prepared_tuple)
    connection.commit()
