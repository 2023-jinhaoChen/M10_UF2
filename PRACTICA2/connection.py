import psycopg2

connection = psycopg2.connect(
    database = "postgres",
    user = "jinhao",
    password = "postgres",
    host = "localhost",
    port = "5432"
)

cursor = connection.cursor()
