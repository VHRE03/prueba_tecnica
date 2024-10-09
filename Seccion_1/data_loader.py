import psycopg2
from database_setup import connect_db
from data_transformer import validate_data

"""
    Esta función carga los datos de un archivo SCV una vez que los datos esten devidamente
    validados.
    
    Parámetros: La ruta del archivo CSV.
    
    Devuelve: Nada.
"""
def load_data(file_path):

    # Verificar conexion con la base de datos
    try:
        # Conectarse con la base de datos
        conn = connect_db()
        cur = conn.cursor()

        # Crear la tabla en la base de datos si es que no existe
        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS  Cargo(
                    id VARCHAR(24) NOT NULL,
                    company_name VARCHAR(130) NULL,
                    company_id VARCHAR(24) NOT NULL,
                    amount DECIMAL(16,2) NOT NULL,
                    status VARCHAR(30) NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    updated_at TIMESTAMP NULL,
                    PRIMARY KEY (id)
                )
            """
        )

        # Verificar si ya existe información en la tabla 'Cargo'
        try:
            cur.execute("SELECT COUNT(*) FROM Cargo")
            row_count = cur.fetchone()[0]

            if row_count == 0:
                print("La tabla 'Cargo' esta vacía. Cargando datos...")

                # Obtner la ruta del archivo para realizar las conversiones necesarias
                df = validate_data(file_path)

                # Guardar la información en la base de datos
                for i, row in df.iterrows():
                    cur.execute(
                        """
                        INSERT INTO Cargo (id, company_name, company_id, amount, status, created_at, updated_at)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """,
                        (row['id'], row['name'], row['company_id'], row['amount'], row['status'], row['created_at'],
                         row['paid_at'])
                    )
                    
                conn.commit()
            else:
                print("La tabla 'Cargo' ya contiene datos. NO se pueden cargar datos")
                cur.close()
                conn.close()
        except psycopg2.Error as e:
            print(f"Error al verificar los datos de la tabla: {e}")
        finally:
            cur.close()
            conn.close()
    except psycopg2.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
