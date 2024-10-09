import psycopg2
import pandas as pd
from database_setup import connect_db

def disrupt_data():
    # Verificación conexión con la base de datos
    try:
        # Conectarse con la base de datos
        conn = connect_db()
        cur = conn.cursor()
        
        print("Conexión con la base de datos exitosa.")

        # Crear las tablas en la base de datos si es que no existen
        cur.execute("""
            CREATE TABLE IF NOT EXISTS companies (
                company_id VARCHAR(24) PRIMARY KEY,
                company_name VARCHAR(130)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS charges (
                id SERIAL PRIMARY KEY,
                company_id VARCHAR(24) REFERENCES companies(company_id),
                amount DECIMAL(16,2),
                status VARCHAR(30),
                created_at TIMESTAMP,
                updated_at TIMESTAMP
            );
        """)
        
        # Verificar si ya existe información en las tablas 'companies' y 'charges'
        cur.execute("SELECT COUNT(*) FROM companies")
        row_count_1 = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(*) FROM charges")
        row_count_2 = cur.fetchone()[0]
        
        if row_count_1 == 0 and row_count_2 == 0:
            print("Las tablas 'companies' y 'charges' están vacías. Cargando datos...")
            
            # Cargar los datos del archivo CSV
            file_path = 'extracted_data.csv'
            df = pd.read_csv(file_path)
            
            for _, row in df.iterrows():
                cur.execute("""
                    INSERT INTO companies (company_id, company_name)
                    VALUES (%s, %s) ON CONFLICT (company_id) DO NOTHING;
                """, (row['company_id'], row['company_name']))
                
                cur.execute("""
                    INSERT INTO charges (company_id, amount, status, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s);
                """, (row['company_id'], row['amount'], row['status'], row['created_at'], row['updated_at']))
                
            conn.commit()
            print("Datos cargados exitosamente.")
        else:
            print("Las tablas ya contienen datos. NO se pueden cargar datos.")

    except psycopg2.Error as e:
        print(f"Error en la base de datos: {e}")

    finally:
        # Asegurarse de cerrar el cursor y la conexión
        cur.close()
        conn.close()

disrupt_data()