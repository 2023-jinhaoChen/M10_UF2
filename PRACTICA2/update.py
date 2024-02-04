# Actualiza un registro de la tabla users por id
def update(connection):
    user_id = input("Introduce el id del usuario que desea actualizar\n")
    user_name = input("Introduce el nombre del usuario\n")
    surname = input("Introduce el primer apellido del usuario\n")
    surname2 = input("Introduce el segundo apellido del usuario\n")
    age = input("Introduce la edad del usuario\n")
    email = input("Introduce el email del usuario\n")

    update_query = (
        f"UPDATE public.users SET name = '{user_name}', surname = '{surname}', "
        f"surname2 = '{surname2}', age = {age}, email = '{email}' " 
        f"WHERE id = {user_id};"
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(update_query)
            connection.commit()
            
    except Exception as e:
        print(e)