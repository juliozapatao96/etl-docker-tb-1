from scripts.python.store_data_csv_to_postgresql import *
from scripts.python.connection_to_database_postgreSQL import *
from scripts.python.process_and_transform_data import process_sql_script

import os

# Reiniciar tablas para efectos prácticos

process_sql_script("drop_tables.sql")
process_sql_script("create_tables.sql")


# Etapa - Almacenamiento de datos en PostgreSQL

table_names = ["cat_perfil_riesgo", "catalogo_activos", "catalogo_banca", "historico_aba_macroactivos"]
connection = None

connection = connect_to_posgreSQL()

for table_name in table_names:
    insert_data_csv_to_table(table_name,os.path.join(".","..","data", table_name) + ".csv",connection)

close_connection(connection)


# Etapa - Procesar y transformar datos en las tablas psql


# Script que se encarga de limpiar valores nulos y valores duplicados
process_sql_script("data_cleaning_miss_dupl.sql")

# Script que limpia los valores no deseados y valores atípicos
process_sql_script("data_cleaning_invalid_outliers.sql")

# Script que modifica los tipos de datos correctos en algunos campos
process_sql_script("data_cleaning_data_type.sql")








