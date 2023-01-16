from database_connection import CONNECTION as connection, CURSOR as cursor


queries = [
    '''
    CREATE TABLE IF NOT EXISTS users (
        user_id BIGSERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        birthday DATE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        pin VARCHAR(255) NOT NULL,
        created_on TIMESTAMP NOT NULL DEFAULT NOW(),
        last_login TIMESTAMP NOT NULL DEFAULT NOW()
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS user_passwords (
        password_id BIGSERIAL PRIMARY KEY,
        user_id BIGINT NOT NULL,
        name VARCHAR(100) NOT NULL,
        password VARCHAR(255) NOT NULL,
        created_on TIMESTAMP NOT NULL DEFAULT NOW(),
        last_viewed TIMESTAMP NOT NULL DEFAULT NOW(),
        last_copied TIMESTAMP NOT NULL DEFAULT NOW(),
        CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
    '''
]

for query in queries:
    print(f'Running sql query {query[:20].strip()}...')
    cursor.execute(query)

connection.commit()
connection.close()
