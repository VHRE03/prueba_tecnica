# Prueba técnica

## Sección 1: Procesamiento y transferencia de datos

### Objetivo
El objetivo de este proyecto es crear un proceso para el manejo de datos utilizando herramientas disponibles, que incluye la carga, extracción, transformación y dispersión de información. El proceso se puede realizar utilizando tecnologías como Docker y lenguajes de programación adecuados.

**Nota:** Este proyecto incluye un dataset con información sobre las compras de dos compañías ficticias.

### Proceso realizado
El proceso que se siguió fue el siguiente:
1. Modificación y corrección de los datos para que la información cumpla con el esquema dado.
2. Carga de los datos desde el archivo CSV.
3. Extracción de los datos ya modificados y corregidos a un nuevo archivo CSV.
4. Dispersión de la información (creación de dos nuevas tablas).

Cada sección se describirá más adelante.

### 1.1 Carga de Información
La información proporcionada debe cargarse en una base de datos, ya sea estructurada o no estructurada. Para este proyecto, se ha elegido **PostgreSQL** como base de datos debido a su robustez, capacidad de manejar datos complejos y soporte para consultas avanzadas.

Para todo el proyecto se eligió Python junto con las librerías **pandas** y **psycopg2**. **pandas** se utilizó para el manejo del archivo CSV y **psycopg2** para la conexión con la base de datos.

Antes de realizar esta sección, se tomó en cuenta el punto 1.3, ya que antes de insertar la información en la base de datos, se realizaron los ajustes necesarios para que se cumpliera con el siguiente esquema:

| Campo          | Tipo                | Restricción   |
|----------------|---------------------|---------------|
| id             | varchar(24)          | NOT NULL      |
| company_name   | varchar(130)         | NULL          |
| company_id     | varchar(24)          | NOT NULL      |
| amount         | decimal(16,2)        | NOT NULL      |
| status         | varchar(30)          | NOT NULL      |
| created_at     | timestamp            | NOT NULL      |
| updated_at     | timestamp            | NULL          |

Una vez realizada la corrección de los datos, se procedió a cargarlos en la base de datos, obteniendo el siguiente resultado:

![image](https://github.com/user-attachments/assets/0ef90f67-1c27-4fdc-9a3f-2d3749f20813)

### 1.2 Extracción
Una vez teniendo los datos correctos en la base de datos, procedimos a guardar esta nueva información en un archivo CSV, presentado de la siguiente manera:

![image](https://github.com/user-attachments/assets/6a913f7b-f5ff-4d7d-a77e-543212785307)

### 1.3 Transformación
Este proceso fue el primero en realizarse. Las transformaciones que tuve que realizar fueron las siguientes:

- Los `id` no tenían la longitud requerida (24 caracteres) y algunos ni siquiera existían.
- Algunos valores del campo `amount` excedían el tamaño permitido, lo que causó varios problemas hasta que encontré una solución.
- Para los valores de tipo `timestamp`, muchas fechas faltaban en el archivo CSV, por lo que fue necesario reemplazar estos espacios vacíos.

Uno de los principales retos fue manejar correctamente los datos faltantes, decidir si truncarlos o reemplazarlos por valores por defecto.

### 1.4 Dispersión de la información
Finalmente, se realizó la dispersión de la información creando primero las tablas requeridas. Posteriormente, se cargó la información corregida en la base de datos utilizando el nuevo archivo CSV.

#### Diagrama entidad-relación

![image](https://github.com/user-attachments/assets/ede703b7-7cfe-427d-ac89-f0a7620907b0)

#### Resultados en la base de datos

![image](https://github.com/user-attachments/assets/1e2ff3f9-b622-4f33-a6d8-b938d17f3c14)
![image](https://github.com/user-attachments/assets/ed7959f2-f546-488e-87a2-6a8570361794)

### 1.5 Configuración de la base de datos
El proyecto fue realizado en una máquina virtual Ubuntu con los siguientes parámetros de conexión a PostgreSQL:

```python
dbname='company_transactions_db',   # Nombre de la base de datos
user='vhre',                        # Nombre del usuario
password='12345',                   # Contraseña
host='localhost',                   # Host o dirección IP de la base de datos
port='5432'                         # Puerto del servidor de la base de datos
