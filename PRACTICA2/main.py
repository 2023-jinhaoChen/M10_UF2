from connection import connection
from create import create
from read import read
from update import update
from delete import delete
from create_table import create_table

menu = """
-------------------------------------MENÚ----------------------------------
1. Crear un nuevo registro(create)
2. Mostrar los registros(read)
3. Actualizar un registro con ID(update)
4. Eliminar un registro con ID(delete)
5. Crear la tabla users(con campo id, name, surname, surname2, age, email)
6. Salir
"""

# Return True cuando el usuario introduce 6 False en contrario
def get_user_option():
    option = get_valid_input(6, menu)

    match option:
        case 1:
            create(connection)
            return False
        case 2:
            read(connection)
            return False
        case 3:
            update(connection)
            return False
        case 4:
            delete(connection)
            return False
        case 5:
            create_table(connection)
            return False
        case 6:
            print("BYE")
            return True

# Validar el input del usuario, tiene que eligir entre 1 hasta el 6 
def get_valid_input(input_range = int, text = str):
    valid = False
    valid_input = list(range(1, input_range + 1))

    # Pedir un valor hasta que el valor es uno de la lista
    while not valid:
        try:
            user_input = int(input(text))
            if user_input in valid_input:
                valid = True
            else:
                print(f"El valor introducido es invalido, tiene que ser uno de estos: {valid_input}")

        except:
            print(f"No es un número, tiene que ser un numero de estos: {valid_input}")

    return user_input

if __name__ == "__main__":
    try:
        salir = False
        # entra el loop infinito hasta que el usuario elige la opción de salir
        while (not salir):
            salir = get_user_option()

    except Exception as e:
        print(e)

    # Cerrar la conexion siempre al salir del programa
    finally:
        if connection:
            connection.close()
