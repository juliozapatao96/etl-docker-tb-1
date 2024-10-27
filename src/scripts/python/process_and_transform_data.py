
import os
from .connection_to_database_postgreSQL import connect_to_posgreSQL, close_connection

# Función para dividir el script en declaraciones individuales
def split_sql_script(script: any) -> list:
    statements = []
    current_statement = []
    for line in script.splitlines():
        line = line.strip()
        # Ignora líneas vacías y comentarios
        if not line or line.startswith('--'):
            continue  
        current_statement.append(line)
        if line.endswith(';'):
            statements.append(' '.join(current_statement))
            current_statement = []
    # Añade cualquier declaración restante            
    if current_statement:
        statements.append(' '.join(current_statement))  
    return statements


def process_sql_script(sql_script_filename):
    # Leer el contenido del archivo SQL
    path = os.path.join(".","src","scripts","sql",sql_script_filename)

    with open(path, 'r') as file:
        sql_script = file.read()

    # Dividir el script en declaraciones individuales
    sql_statements = split_sql_script(sql_script)

    connection = connect_to_posgreSQL()

    cursor = connection.cursor()

    try:
        # Ejecutar cada declaración individualmente
        for statement in sql_statements:
            cursor.execute(statement)

        # Confirmar los cambios en la base de datos de forma permanente
        connection.commit()

        print(f"Se ha ejecutado el script '{sql_script_filename}' de forma exitosa.")
    except Exception as e:
        # Si ocurre un error, revertir los cambios
        connection.rollback()
        print(f"Ocurrió un error al intentar procesar el script : {e}")

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        close_connection(connection)
