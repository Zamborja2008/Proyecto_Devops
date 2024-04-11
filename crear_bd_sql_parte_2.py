import os
import pyodbc
import sqlalchemy
import pandas as pd

def conexion():
    username = 'DESKTOP-DRB2I0R\\SQLEXPRESS'  # Utiliza doble barra invertida para escapar el carácter '\'
    database = 'master'
    connection = 'DRIVER={ODBC Driver 17 for SQL Server};' \
                 f'SERVER={username};' \
                 f'DATABASE={database};' \
                 'Trusted_Connection=yes'
    return connection

# Intentamos establecer la conexión
conn = pyodbc.connect(conexion(),autocommit=True)

# Cursor para ejecutar consultas SQL
cursor = conn.cursor()
print("Conexión exitosa")

# Nombre de la nueva base de datos
new_database = 'ProyectoPar'

# Consulta SQL para verificar si la base de datos ya existe
check_database_query = f"SELECT database_id FROM sys.databases WHERE name = '{new_database}'"

# Ejecutar la consulta para verificar si la base de datos ya existe
cursor.execute(check_database_query)
result = cursor.fetchone()

# Si la base de datos no existe, crearla
if not result:
    # Cambiamos a la base de datos master
    cursor.execute('USE master;')

    # Consulta SQL para crear la base de datos
    create_database_query = f'CREATE DATABASE {new_database};'

    # Ejecutar la consulta para crear la base de datos
    cursor.execute(create_database_query)

    print(f'Se ha creado la base de datos {new_database} correctamente.')
else:
    print(f'La base de datos {new_database} ya existe.')


def extract_from_csv(file_to_process):  
    dataframe = pd.read_csv(file_to_process, encoding='ISO-8859-1')
    return dataframe

ruta_del_archivo_csv = 'C:\\Users\\Irving\\Documents\\Ruta para Analista de Data\\CERTUS\\DEVOPS\\Proyecto_Parcial\\Python\\dataset'

dataframe = extract_from_csv(ruta_del_archivo_csv) 

# Intentamos establecer la conexión
conn = sqlalchemy.create_engine(conexion())

# Visualizamos la Lista de todos los archivos en el directorio de descargas o en la carpeta
archivos_descargados = os.listdir(ruta_del_archivo_csv)

# Busca el archivo CSV en la lista de archivos descargados
for archivo in archivos_descargados:
    if archivo.endswith('.csv'):
        ruta_del_archivo_csv = os.path.join(ruta_del_archivo_csv, archivo)
        break
else:
    raise FileNotFoundError("No se encontró ningún archivo CSV en el directorio de descargas.")

create_tabla_sql = f'CREATE TABLE {"REPORTE"};'

#INSERTAMOS LOS DATOS DE CSV A LA TABLA
cursor.executemany(f"INSERT INTO {create_tabla_sql,archivo}")

print("Datos insertados correctamente en una nueva tabla llamada reporte en SQLSERVER.")

# Cerrar la conexión
cursor.close()
conn.close()