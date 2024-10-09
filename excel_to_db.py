import pandas as pd
import mysql.connector
from mysql.connector import Error

def actualizar_coordenadas_en_db(host, user, password, database, excel_file, port):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            df = pd.read_excel(excel_file)
            
            df['latitude'] = df['latitude'].fillna(0)
            df['longitude'] = df['longitude'].fillna(0)

            cursor = connection.cursor()

            for index, row in df.iterrows():
                id_tienda = row['id']
                latitude = row['latitude']
                longitude = row['longitude']

                sql_update_query = """UPDATE vlc_tienda SET latitude = %s, longitude = %s WHERE id = %s"""
                cursor.execute(sql_update_query, (latitude, longitude, id_tienda))
                connection.commit()

            print("Datos actualizados correctamente")

    except Error as e:
        print("Error al conectarse a MySQL:", e)
        return  # Añadido return para salir de la función en caso de error

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

# Parámetros de conexión
host = 'localhost'  # Asegúrate de que este es el nombre correcto del host
user = 'user'
password = 'pass'
database = 'database'
port = 8887  # Reemplaza XXXX con el puerto correcto

# Ruta al archivo Excel
excel_file = 'vlc_tienda.xlsx'

# Llamar a la función
actualizar_coordenadas_en_db(host, user, password, database, excel_file, port)

