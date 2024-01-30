from connection import *

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

salir = False
while not salir:
    option = get_user_option()
    match option:
        case 1:
            create()
        case 2:
            read()
        case 3:
            update()
        case 4:
            delete()
        case 5:
            create_table()