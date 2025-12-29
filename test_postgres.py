import psycopg2
try:
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="rft3055",
        host="db",
        port="5432"
    )
    print("Connection to PostgreSQL database established successfully.")
    conn.close()
except Exception as e:
    print(f"An error occurred while connecting to the PostgreSQL database: {e}")