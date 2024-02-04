def create(connection):
    user_name = input("Introduce el nombre del usuario nuevo\n")
    surname = input("Introduce el primer apellido del usuario nuevo\n")
    surname2 = input("Introduce el segundo apellido del usuario nuevo\n")
    age = input("Introduce la edad del usuario nuevo\n")
    email = input("Introduce el email del usuario nuevo\n")

    create_query = (
        f"INSERT INTO public.users (name, surname, surname2, age, email) " 
        f"VALUES ('{user_name}', '{surname}', '{surname2}', {age}, '{email}');"
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(create_query)
            connection.commit()
            
    except Exception as e:
        print(e)