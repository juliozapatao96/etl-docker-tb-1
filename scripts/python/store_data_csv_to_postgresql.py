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
            cursor.execute(query, tuple(row))

        connection.commit()

        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error al intentar insertar información : ", error)

