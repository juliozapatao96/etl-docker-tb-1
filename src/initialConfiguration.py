from src.scripts.python.store_data_csv_to_postgresql import *
from src.scripts.python.connection_to_database_postgreSQL import *
from src.scripts.python.process_and_transform_data import process_sql_script

import os


def main():
    print("Ejecutando Configuración Inicial...")

    # Reiniciar tablas para efectos prácticos
    process_sql_script("drop_tables.sql")
    process_sql_script("create_tables.sql")


    # Etapa - Almacenamiento de datos en tablas iniales en PostgreSQL

    table_names = ["cat_perfil_riesgo", "catalogo_activos", "catalogo_banca"]
    connection = None

    connection = connect_to_posgreSQL()

    for table_name in table_names:
        insert_data_csv_to_table(table_name,os.path.join(".","data", table_name) + ".csv",connection)

    close_connection(connection)

    print("Configuración Inicial ha Finalizado...")


if __name__ == '__main__':
    main()
