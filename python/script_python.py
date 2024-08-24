import os


####Carpeta Dataset #####

location = "C:/Users/LEGION/Desktop/CERTUS/proyecto_parcial/dataset"

#### Validar si existe la carpeta ####

if not os.path.exists(location):
    os.mkdir(location)

else:
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove (os.path.join(root,name)) ## eliminar archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name)) ## eliminar carpeta


#### descargar dataset  ####
from kaggle.api.kaggle_api_extended import KaggleApi

### Autenticarnos ###
api= KaggleApi()
api.authenticate()

print(api.dataset_list(search=''))

api.dataset_download_files('youssefismail20/olympic-games-1994-2024',path=location,force=True, quiet=False, unzip=True)
