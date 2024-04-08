import sqlalchemy
import os
from Crear_BD import conexion
import pandas as pd

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

tablanueva = conexion()  #Creamos una variable que contiene la conexion a la base de datos

# Insertamos la data y creamos una nueva tabla en la base de datos countries
dataframe.to_sql('Reporte_BD', con=tablanueva, if_exists='replace', index=False)

print("Datos insertados correctamente en una nueva tabla llamada reporte en SQLSERVER.")