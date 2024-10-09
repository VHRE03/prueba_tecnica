import pandas as pd
from database_setup import connect_db

def extract_data():
    # Conectarse con la base de datos
    conn = connect_db()
    cur = conn.cursor()

    # Ejecutar la consulta
    cur.execute("SELECT * FROM Cargo")

    # Obtener los datos de la consulta
    rows = cur.fetchall()

    # Obtener los nombres de las columnas
    colnames = [desc[0] for desc in cur.description]

    # Convertir los datos a un DataFrame
    df = pd.DataFrame(rows, columns=colnames)

    # Exportar en formato CSV
    df.to_csv('extracted_data.csv', index=False)

    # Cerrar el cursor y la conexión
    cur.close()
    conn.close()

extract_data()