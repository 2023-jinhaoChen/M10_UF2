import psycopg2

conn = psycopg2.connect(
    database = "postgres",
    user = "jinhao",
    password = "postgres",
    host = "localhost",
    port = "5432"
)

connection = conn.cursor()
