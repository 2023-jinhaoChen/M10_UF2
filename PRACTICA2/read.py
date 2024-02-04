# Imprimir todos los registros de la tabla users
def read(connection):
    read_query = "SELECT * FROM public.users;"

    try:
        with connection.cursor() as cursor:
            cursor.execute(read_query)
            for user in cursor:
                print(user)

    except Exception as e:
        print(e)