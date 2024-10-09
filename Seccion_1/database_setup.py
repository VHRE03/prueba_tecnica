import psycopg2

"""
    Función para establecer la conexión con una base de datos PostgreSQL.
    
    Parámetros: Ninguno.
    
    Devuelve: Un Objeto de conexión a la base de datos.
"""
def connect_db():
    conn = psycopg2.connect(
        dbname='company_transactions_db',   # Nombre de la base de datos
        user='vhre',                        # Nombre del usuario
        password='12345',                   # Contraseña
        host='localhost',                   # Host o dirección IP de la base de datos
        port='5432'                         # Puerto del servidor de la base de datos
    )

    return conn
