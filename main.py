from scripts.python.store_data_csv_to_postgresql import *
from scripts.python.connection_to_database_postgreSQL import *

csv_path = ".\..\data\cat_perfil_riesgo.csv"
table_name = "cat_perfil_riesgo"
connection = None

connection = connect_to_posgreSQL()
insert_data_csv_to_table(table_name,csv_path,connection)

close_connection(connection)








