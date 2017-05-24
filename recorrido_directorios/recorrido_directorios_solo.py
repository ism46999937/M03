# coding:utf-8
import os
 
path_to_explore="./prueba/"

#De esta forma miramos solo la ruta de los directorios
for root, dirs, files in os.walk(path_to_explore):
    for name in dirs:
            
        name_path=os.path.join(root, name)
        print(name_path)
