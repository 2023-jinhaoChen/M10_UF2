# La creación de la tabla users
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
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()

    except Exception as e:
        print(e)