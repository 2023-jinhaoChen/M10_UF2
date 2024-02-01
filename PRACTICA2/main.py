from connection import connection

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
            create_table(connection)