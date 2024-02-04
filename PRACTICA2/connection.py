import psycopg2
# Datos de la conexion al base de datos 
connection = psycopg2.connect(
    database = "postgres",
    user = "jinhao",
    password = "postgres",
    host = "localhost",
    port = "5432"
)
