# Procesamiento y Transferencia de Datos

## Objetivo
El objetivo de este proyecto es crear un proceso para el manejo de datos utilizando herramientas disponibles, que incluye la carga, extracción, transformación y dispersión de información. El proceso se puede realizar utilizando tecnologías como Docker y lenguajes de programación adecuados. 

Además, se proporcionan pruebas unitarias o de integración para garantizar la calidad del código. El proyecto se comparte a través de GitHub y puede ser descargado como un archivo ZIP.

**Nota:** Este proyecto incluye un dataset con información sobre las compras de dos compañías ficticias.

## 1. Carga de Información

La información proporcionada debe cargarse en una base de datos, ya sea estructurada o no estructurada. Para este proyecto, se ha elegido **PostgreSQL** como base de datos. La elección se basa en su robustez, capacidad de manejar datos complejos y soporte para consultas avanzadas.

### Instalación y Ejecución

1. **Instalar PostgreSQL**:
   - Sigue las [instrucciones oficiales](https://www.postgresql.org/download/) para instalar PostgreSQL en tu sistema.

2. **Configurar la Base de Datos**:
   - Crea una nueva base de datos usando el siguiente comando en la consola de PostgreSQL:
     ```sql
     CREATE DATABASE nombre_de_la_base_de_datos;
     ```

3. **Cargar Datos**:
   - Utiliza el script `load_data.py` para cargar la información del dataset en la base de datos.

```python
# Comentarios sobre el proceso de carga:
# Se eligió PostgreSQL debido a su capacidad para manejar transacciones y datos estructurados.
# Además, proporciona un buen rendimiento en consultas complejas.
