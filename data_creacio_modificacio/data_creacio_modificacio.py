# coding:utf-8
import os, time
 
ruta_a_explorar="./test/"
 
 
for ruta, directorios, archivos in os.walk(ruta_a_explorar):
    for nombre in archivos:
        ruta_completa=os.path.join(ruta, nombre)
        print(ruta_completa)
 
        #Data últim accés
        print time.ctime(os.path.getatime(ruta_completa))
 
        #Data última modificació
        print time.ctime(os.path.getmtime(ruta_completa))
 
 
 
    for nombre in directorios:            
        ruta_completa=os.path.join(ruta, nombre)
        print(ruta_completa)
