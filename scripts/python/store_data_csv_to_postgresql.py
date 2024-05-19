import pandas as pd
import psycopg2


def insert_data_csv_to_table(table_name, csv_path, connection):
    try:
        df = pd.read_csv(csv_path)

        cursor = connection.cursor()

        columns = ', '.join(df.columns)

        values = ', '.join(['%s'] * len(df.columns))

        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

        for index, row in df.iterrows():
            try:
                cursor.execute(query, tuple(row))
            except Exception as e:
                print(f"Error al intentar insertar la fila {index +1}: {e}")
                # print("Registro con problemas: \n", row)

        connection.commit()

        cursor.close()

        print(f"Se ha ingresado la información a la tabla '{table_name}' de manera exitosa")
    except (Exception, psycopg2.Error) as error:
        print(f"Error al intentar insertar información en '{table_name}' : {error}")
        if cursor is not None:
            cursor.close()

