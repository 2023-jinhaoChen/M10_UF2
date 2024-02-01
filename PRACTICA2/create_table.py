def create_table(connection):
    create_table_query = """
    CREATE TABLE users(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL,
        surname2 VARCHAR(255),
        age INT NOT NULL,
        email VARCHAR(255) NOT NULL
    );
    """
    try:
        connection.execute(create_table_query)
    except Exception as e:
        print(e)
    finally:
        connection.execute("COMMIT;")