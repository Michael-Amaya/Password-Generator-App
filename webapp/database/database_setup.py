from database_connection import CONNECTION as connection, CURSOR as cursor


queries = [
    '''
    CREATE TABLE IF NOT EXISTS users (
        user_id BIGSERIAL PRIMARY KEY,
        name varchar(50) NOT NULL,
        birthday date NOT NULL,
        email varchar(100) UNIQUE NOT NULL,
        password varchar(255) NOT NULL,
        pin VARCHAR(15) NOT NULL,
        created_on TIMESTAMP NOT NULL DEFAULT NOW(),
        last_login TIMESTAMP NOT NULL DEFAULT NOW()
    );
    ''',
]

for query in queries:
    print(f'Running sql query {query[:20].strip()}...')
    cursor.execute(query)

connection.commit()
connection.close()
