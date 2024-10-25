import psycopg2
import os
import time
from dotenv import load_dotenv

# Función para realizar la conexión con la base de datos
def connect_to_posgreSQL():
    # Cargar las variables de entorno
    load_dotenv(dotenv_path='config/config.env')
    DB_NAME = os.getenv("DB_NAME")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")

    connection = None
    retries = 5  # Número de intentos
    while retries > 0:
        try:
            # Establecer conexión
            connection = psycopg2.connect(
                user=DB_USERNAME,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME
            )
            print("La conexión a PostgreSQL ha sido establecida.")
            return connection
        except (Exception, psycopg2.Error) as error:
            print("Error al conectar a PostgreSQL:", error)
            retries -= 1
            print(f"Reintentando en 5 segundos... ({retries} intentos restantes)")
            time.sleep(5)  # Espera 5 segundos antes de reintentar

    print("No se pudo conectar a la base de datos después de varios intentos.")
    return None  # Devolver None si no se pudo conectar

# Función para cerrar la conexión con la base de datos
def close_connection(connection):
    if connection is not None:
        connection.close()
        print("La conexión a PostgreSQL ha sido cerrada. \n")

if __name__ == "__main__":
    connection = connect_to_posgreSQL()
    if connection is not None:
        # Aquí puedes realizar operaciones con la conexión
        close_connection(connection)
