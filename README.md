# Prueba técnica

## Sección 1: Procesamiento y transferencia de datos

### Objetivo
El objetivo de este proyecto es crear un proceso para el manejo de datos utilizando herramientas disponibles, que incluye la carga, extracción, transformación y dispersión de información. El proceso se puede realizar utilizando tecnologías como Docker y lenguajes de programación adecuados. 

**Nota:** Este proyecto incluye un dataset con información sobre las compras de dos compañías ficticias.

### Proceso realizado
El proceso que se siguio fue el siguiente:
1. Modificacion y correcion de los datos para que la informacion cumpla con el esquema dado
2. Carga de los datos desde el archivo CSV
3. Extaccion de los datos ya modificados y corregidos a un nuevo archivo CSV
4.   Dispersion de la infromacion (Creacion de dos nuevas tablas)
Cada seccion se describira con mas adelante

### 1.1. Carga de Información

La información proporcionada debe cargarse en una base de datos, ya sea estructurada o no estructurada. Para este proyecto, se ha elegido **PostgreSQL** como base de datos. La elección se basa en su robustez, capacidad de manejar datos complejos y soporte para consultas avanzadas.

Para todo el proeycto se elegio python y las librerias Panda y psycopg2. Panda se utilizo para el manejo del archivo CSV y psycopg2 para la conexion con la base de datos antes mencionada

Antes de realizar esta seccion se tomo encuneta el punto 1.3 ya que antes de insertar la infromacion en la base de datos se relizaron los ajustes necesarios para que se cumpliera con el siguiente esquema

| Cargo          | Tipo                | Restricción   |
|----------------|---------------------|---------------|
| id             | varchar(24)        | NOT NULL      |
| company_name   | varchar(130)       | NULL          |
| company_id     | varchar(24)        | NOT NULL      |
| amount         | decimal(16,2)      | NOT NULL      |
| status         | varchar(30)        | NOT NULL      |
| created_at     | timestamp           | NOT NULL      |
| updated_at     | timestamp           | NULL          |

una vez realizada la correcion de los datos se proecedio a cargar la informacion a la base de dartos obteniendo esrte resultado:
![image](https://github.com/user-attachments/assets/0ef90f67-1c27-4fdc-9a3f-2d3749f20813)

