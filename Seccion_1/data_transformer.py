import pandas as pd
import numpy as np

"""
    Esta función carga los datos de un archivo SCV, realiza la validación de sus datos
    y regresa datos validos.
    
    Parámetros: La ruta del archivo CSV.
    
    Devuelve: Un DataFrame de Pandas con los datos corregidos.
"""
def validate_data(file_path):

    # Cargar los datos del archivo CSV
    df = pd.read_csv(file_path)

    """
        ** Correcciones de la columna 'id' **
        
        - Trunca los ID existentes a un maximo de 24 caracteres
        - Genera ID unico para los valores que no existen
    """
    df['id'] = df['id'].str[:24]
    df['id'] = np.where(df['id'].isna(), np.arange(len(df)) + 1, df['id'])


    """
        ** Correcciones de la columna 'name'
        
        - Trunca los ID existentes a un maximo de 130 caracteres
        - Coloca 'UNKNOWN_COMPANY' para los valores que no existen
    """
    df['name'] = df['name'].fillna('UNKNOWN_COMPANY').str[:130]


    """
        ** Correcciones de la columna 'company_id' **
        
        - Trunca los ID existentes a un maximo de 24 caracteres
        - Genera ID unico para los valores que no existen
    """
    df['company_id'] = df['company_id'].str[:24]
    df['company_id'] = np.where(df['company_id'].isna(), np.arange(len(df)) + 1, df['company_id'])


    """
        ** Correcciones en la columna 'amount' **
        
        - Convertir a numérico
        - Rellenar valores faltantes con 0
        - Asegurar que el tipo de dato sea float64 para operaciones numéricas
        - Calcular el valor máximo permitido basado en la precisión (asumiendo DECIMAL(16,2)) valor_maximo_permitido = 10 ** 14 - 1
        - Identificar y truncar valores excesivamente grandes
    """
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df['amount'].fillna(0)
    df['amount'] = df['amount'].astype('float64')

    max_allowed_value = 10 ** 14 - 1
    oversized_rows = df[df['amount'].abs() > max_allowed_value]
    df.loc[oversized_rows.index, 'amount'] = df.loc[oversized_rows.index, 'amount'].clip(upper=max_allowed_value)


    """
        ** orrecciones en la columna 'status' **
        
        - Trunca los ID existentes a un maximo de 30 caracteres
        - Coloca 'UNKNOWN' para los valores que no existen
    """
    df['status'] = df['status'].fillna('UNKNOWN').str[:30]


    """
        ** Correcciones en las columnas 'created_at' y 'paid_at' **
        
        - Convertir a formato datetime con formato específico ('%Y-%m-%d')
        - Rellenar fechas faltantes con la fecha actual (sin hora)
    """
    df['created_at'] = pd.to_datetime(df['created_at'], format='%Y-%m-%d', errors='coerce')
    df['paid_at'] = pd.to_datetime(df['paid_at'], format='%Y-%m-%d', errors='coerce')

    df['created_at'] = df['created_at'].fillna(pd.Timestamp.today().normalize())
    df['paid_at'] = df['paid_at'].fillna(pd.Timestamp.today().normalize())


    return df
