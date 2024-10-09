import psycopg2
from database_setup import connect_db
from data_loader import load_data
from data_extractor import extract_data
from data_distribution import disrupt_data

"""
    Esta función es la principal y llama a las otras funciones en orden, para llevar una secuencia 
    correcta y evitar errores en el manejo de la infromación y la base de datos.
    
    Para verificar el funcionamiento de toda la sección 1 de la prueba técnia ejecute este archivo.
"""
def main():
    # ** Carga de información **
    print("1 CARGA DE INFORMACION Y TRANSFORMACION DE DATOS")
    # Ruta del archivo
    file_path = 'data_prueba_tecnica.csv'
    
    # Cargar la información a la base de datos
    load_data(file_path)
    print("\n")

    # ** Extracción de la información de la base de datos
    print("2 EXTRACCION DE LA INFORMACION")
    extract_data()
    print("\n")

    # ** Dispersión de la información **
    print("3 DISPERSION DE LA INFORMACION")
    disrupt_data()
    print("\n")

main()
