def read(connection):
    read_query = "SELECT * FROM TABLE users;"
    try:
        connection.execute(read_query)
        for user in connection:
            print(user)
    except Exception as e:
        print(e)
