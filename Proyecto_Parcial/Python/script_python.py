import os  #OS ES SITEMA OPERATIVO

location = "C:/Users/Irving/Documents/Ruta para Analista de Data/CERTUS/DEVOPS/Proyecto_Parcial/Python/script_python.py"

###Validar que la carpeta exista###
if not os.path.exists(location):
    ##En caso mi carpeta no exista, voy a crear una nueva##
    os.mkdir(location) ##mkdir -> make directory
else:
    ##Si la carpeta ya existe, entonces borramos el contenido##
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) ##elimino todos los archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name)) ##rmdir -> remove directory / elimino todas mis carpetas

from kaggle.api.kaggle_api_extended import KaggleApi

##Con este codigo autenticamos la cuenta. Y poner el archivo json descargado de kaggle en la ruta indicada
api = KaggleApi()
api.authenticate()

#Lo que hace es descargar los diferentes dataset disponibles que hay en kaggle
#print(api.dataset_list())  

#CON ESTO DESCARGAMOS EL CSV ELEGIO Y LO GUARDAMOS EN  LA CARPETA QUE QUEREMOS
#(PRIMERO NOMBRE DE LA RUTA DEL DATA SET, LUEGO EL NOMBRE DEL DATA SET (LO UBICCAMOS EN KAGGLE) 
#Y POR ULTIMO LA RUTA DE LA CARPETA EN DONDE QUEREMOS GUARDAR)
api.dataset_download_file("sudarshan24byte/online-food-dataset","onlinefoods.csv",path="Proyecto_Parcial/Python/dataset")
