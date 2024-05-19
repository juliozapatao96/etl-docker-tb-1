import psycopg2
import os
from dotenv import load_dotenv

# Función para realizar la conexión con la base de datos
def connect_to_posgreSQL():
    # Cargar las variables de entorno
    load_dotenv(dotenv_path='config.env')
    DB_NAME         =   os.getenv("DB_NAME")
    DB_USERNAME     =   os.getenv("DB_USERNAME")
    DB_PASSWORD     =   os.getenv("DB_PASSWORD")
    DB_HOST         =   os.getenv("DB_HOST")
    DB_PORT         =   os.getenv("DB_PORT")

    connection = None
    try:
        # establecer conexxión
        connection = psycopg2.connect(
            user=DB_USERNAME,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )

        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a PostgreSQL", error)

# Función para cerrar la conexión con la base de datos
def close_connection(connection):
    if (connection is not None):
        connection.close()
        print("La conexión a PostgreSQL ha sido cerrada.")

if __name__ == "__main__":
    connect_to_posgreSQL()