from scripts.python.store_data_csv_to_postgresql import *
from scripts.python.connection_to_database_postgreSQL import *
from scripts.python.process_and_transform_data import process_sql_script

import os

# Reiniciar tablas para efectos prácticos

process_sql_script("drop_tables.sql")
process_sql_script("create_tables.sql")


#########################################

table_names = ["cat_perfil_riesgo", "catalogo_activos", "catalogo_banca", "historico_aba_macroactivos"]
connection = None

# Etapa - Almacenamiento de datos en PostgreSQL
connection = connect_to_posgreSQL()

for table_name in table_names:
    insert_data_csv_to_table(table_name,os.path.join(".","..","data", table_name) + ".csv",connection)

close_connection(connection)


# Etapa - Procesar y transformar datos en las tablas psql

# Script que se encarga de limpiar valores nulos y valores duplicados
process_sql_script("data_cleaning_miss_dupl.sql")






