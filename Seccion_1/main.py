import psycopg2
from database_setup import connect_db
from data_loader import load_data
from data_extractor import extract_data

def main():

    # Verificar la conexión con la base de datos
    try:
        # Conectarse con la base de datos
        conn = connect_db()
        cur = conn.cursor()

        # Terminar conexió para evitar errores
        cur.close()
        conn.close()

        # ** Carga de información **
        # Ruta del archivo
        file_path = 'data_prueba_tecnica.csv'

        # Cargar los datos a la base de datos
        load_data(file_path)

        # ** Extracción de la información de la base de datos
        extract_data()

    except psycopg2.Error as e:
        print(f"Error al conectar con la base de datos")


    # Conectarse a la base de datos
    conn = connect_db()

    # Cargar los datos del archivo csv
    file_path = 'data_prueba_tecnica.csv'
    df = load_data(file_path)






