import pandas as pd
import psycopg2


def insert_data_csv_to_table(table_name, csv_path, connection):
    try:
        # Leer el archivo csv
        df = pd.read_csv(csv_path)

        # Crear el cursor
        cursor = connection.cursor()

        # Crear un string con los campos del csv separados por comas
        columns = ', '.join(df.columns)

        # Crear un string de %s por cada campo del csv separados por comas
        values = ', '.join(['%s'] * len(df.columns))

        if table_name.startswith("historico_aba_macroactivos"):
            table_name = "temp_historico_aba_macroactivos"

        # Crear la consulta que guardará la información en la tabla
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

        # iterar el dataframe y ejecutar la query
        for index, row in df.iterrows():
            try:
                cursor.execute(query, tuple(row))
            except Exception as e:
                print(f"Error al intentar insertar la fila {index +1}: {e}")
                # print("Registro con problemas: \n", row)

        # confirmar la transacción en la base de datos para que los cambios sean permamentes
        connection.commit()

        # cerrar la conexión con el cursor
        cursor.close()

        print(f"Se ha ingresado la información a la tabla '{table_name}' de manera exitosa")
        
    except (Exception, psycopg2.Error) as error:
        print(f"Error al intentar insertar información en '{table_name}' : {error}")
        if cursor is not None:
            cursor.close()

