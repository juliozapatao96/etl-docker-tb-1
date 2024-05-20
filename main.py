from scripts.python.store_data_csv_to_postgresql import *
from scripts.python.connection_to_database_postgreSQL import *
import os

table_names = ["cat_perfil_riesgo", "catalogo_activos", "catalogo_banca", "historico_aba_macroactivos"]
connection = None

# Etapa - Almacenamiento de datos en PostgreSQL
connection = connect_to_posgreSQL()

for table_name in table_names:
    insert_data_csv_to_table(table_name,os.path.join(".","..","data", table_name) + ".csv",connection)

close_connection(connection)








