from src.scripts.python.store_data_csv_to_postgresql import *
from src.scripts.python.connection_to_database_postgreSQL import *
from src.scripts.python.process_and_transform_data import process_sql_script
from src.scripts.python.utils import list_csv_files, move_file

import os


def main():
    print("Ejecutando ETL...")

    path_input = os.path.join(".","data","input-data")
    path_move = os.path.join(".","data","historical-data")

    # Etapa - Almacenamiento de datos en PostgreSQL

    filenames = list_csv_files(path_input)
    
    
    if filenames:
        connection = None

        connection = connect_to_posgreSQL()
        for file in filenames:
            # Script sql que se encarga de crear la tabla temp
            process_sql_script("create_table_temp.sql")
            
            insert_data_csv_to_table(file,os.path.join(path_input, file) + ".csv",connection)
            move_file(file+".csv", path_input, path_move)

        close_connection(connection)
        
        # Etapa - Procesar y transformar datos en las tablas psql



        # Script que se encarga de limpiar valores nulos y valores duplicados
        process_sql_script("data_cleaning_miss_dupl.sql")

        # Script que limpia los valores no deseados y valores atípicos
        process_sql_script("data_cleaning_invalid_outliers.sql")

        # Script que modifica los tipos de datos correctos en algunos campos
        process_sql_script("data_cleaning_data_type.sql")

        # Script para agregar campo date y establece las pkey y fkey en la tabla historica
        process_sql_script("data_transform.sql")

        #Script sql que se encarga de migrar la información de temp-procesada a la original y luego elimina la temp-procesada
        process_sql_script("migrate_info_aba.sql")


        print("ETL ha Finalizado...")
        return True
    
    print(f"No hay archivos a procesar dentro de {path_input}")
    return False

if __name__ == '__main__':
    main()


