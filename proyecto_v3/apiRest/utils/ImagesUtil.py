import platform
from pathlib import Path
from utils.settings import Settings

class ImagesUtil:
    def guardarArchivoFisico(file_name:str, ruta:str, file_content):
        try:
            file_name_fisic = file_name
            if(platform.system() == "Darwin" or platform.system() == "Linux"):
                archivo_ruta = Settings().main_path + ruta
                path = archivo_ruta.replace("\\","/")
                path = Path(path)
                path.mkdir(parents=True,exist_ok=True) 
                path = path / file_name_fisic
            else: 
                path = Path(path)
                path.mkdir(parents=True,exist_ok=True)
                path = ruta / file_name_fisic

            # graba en SO local                             
            with open(path,"wb") as f:
                f.write(file_content)
            
            return True
        except:
            return False
        
    
    def extraerArchivoFisico(ruta:str,idArchivo:int) -> bytes:
        archivo_ruta = ruta
        if(platform.system() == "Darwin" or platform.system() == "Linux"):
            archivo_ruta = archivo_ruta.replace("\\","/")
            path = Settings().main_path + archivo_ruta
        else:         
            #platform.system() == "Windows"
            path = archivo_ruta

        with open(path, "rb") as file:
            file_content = file.read()

        return file_content