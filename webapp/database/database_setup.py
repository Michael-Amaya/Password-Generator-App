import os
import sys
import psycopg2

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from settings import SETTINGS


connection = psycopg2.connect(database=SETTINGS['database_name'],
                              host=SETTINGS['database_host'],
                              user=SETTINGS['database_user'],
                              password=SETTINGS['database_password'],
                              port=SETTINGS['database_port'])

cursor = connection.cursor()
queries = [
    '''
    CREATE TABLE IF NOT EXISTS users (
        user_id BIGSERIAL PRIMARY KEY,
        name varchar(50) NOT NULL,
        birthday date NOT NULL,
        email varchar(100) UNIQUE NOT NULL,
        password varchar(255) NOT NULL,
        pin VARCHAR(15) NOT NULL,
        created_on TIMESTAMP NOT NULL,
        last_login TIMESTAMP NOT NULL DEFAULT NOW()
    );
    ''',
]

for query in queries:
    print(f'Running sql query {query[:20].strip()}...')
    cursor.execute(query)

connection.commit()
connection.close()
