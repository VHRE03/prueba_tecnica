import psycopg2
import pandas as pd
from database_setup import connect_db

def extract_data():
    
    try:
        # Conectarse con la base de datos
        conn = connect_db()
        cur = conn.cursor()
        
        print("Conexión con la base de datos exitosa")
        
        # Verificar si la tabla 'Cargo' existe
        cur.execute("""
            SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'cargo');
        """)
        
        table_exist = cur.fetchone()[0]
        
        if not table_exist:
            print("La tabla 'Cargo' no existe en la base de datos")
        else:
            # Verificar si la tabla 'Cargo' tiene datos
            cur.execute("SELECT COUNT(*) FROM Cargo")
            row_count = cur.fetchone()[0]
            
            if row_count == 0:
                print("La tabla 'Cargo' está vacía. No hay datos para extraer")
            else:
                print(f"La tabla 'Cargo' contiene {row_count} registros. Extrayendo datos...")
                
                # Ejecutar la extracción de los datos
                cur.execute("SELECT * FROM Cargo")
                
                # Obtener los datos de la consulta
                rows = cur.fetchall()

                # Obtener los nombres de las columnas
                colnames = [desc[0] for desc in cur.description]

                # Convertir los datos a un DataFrame
                df = pd.DataFrame(rows, columns=colnames)

                # Exportar en formato CSV
                df.to_csv('extracted_data.csv', index=False)
                print("Datos exportados exitosamente a 'extracted_data.csv'")
                
    except psycopg2.Error as e:
        print(f"Error en la base de datos: {e}")
    
    finally:
        # Cerrar el cursor y la conexión:
        cur.close()
        conn.close()