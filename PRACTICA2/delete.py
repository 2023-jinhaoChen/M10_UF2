# Elimina un registro de la tabla users por id
def delete(connection):
    user_id = input("Introduce el id del usuario que desea eliminar\n")

    delete_query = f"DELETE FROM public.users WHERE id = {user_id};"

    try:
        with connection.cursor() as cursor:
            cursor.execute(delete_query)
            connection.commit()
            
    except Exception as e:
        print(e)