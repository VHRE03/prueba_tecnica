import psycopg2
from database_setup import connect_db
from data_loader import load_data
from data_extractor import extract_data
from data_distribution import disrupt_data

def main():
    try:
        # Conectarse con la base de datos
        conn = connect_db()
        cur = conn.cursor()
        
        print("Conexión con la base de datos exitosa.")

        # ** Carga de información **
        print("Carga de información y Transformación de datos")
        # Ruta del archivo
        file_path = 'data_prueba_tecnica.csv'

        # Cargar los datos a la base de datos
        load_data(file_path)
        print("\n")

        # ** Extracción de la información de la base de datos
        print("Extraccion de la información")
        extract_data()
        print("\n")

        # ** Dispersión de la información **
        print("Dispersión de la infromación")
        disrupt_data()
        print("\n")

    except psycopg2.Error as e:
        print(f"Error al conectar con la base de datos: {e}")

    finally:
        # Asegurarse de cerrar el cursor y la conexión
        cur.close()
        conn.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()
