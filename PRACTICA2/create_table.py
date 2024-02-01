def create_table(connection):
    create_table_query = """
    CREATE TABLE Users(
        User_id SERIAL PRIMARY KEY,
        User_name VARCHAR(255) NOT NULL,
        USER_surname VARCHAR(255) NOT NULL,
        USER_surname2 VARCHAR(255),
        User_age INT NOT NULL,
        User_email VARCHAR(255) NOT NULL
    );
    """

    connection.execute(create_table_query)
    connection.execute("COMMIT;")