# Ejercicio 5: Crea 3 nombres de carpeta que se situarán en el directorio actual en una lista y convierte a tipo Path.
# A continuación, para cada carpeta, si no existe, la creas y guarda en un diccionario si las carpetas fueron creadas o ya existían.
# Muestra el contenido del diccionario recorriendo sus elementos.

from pathlib import Path

folderNames = ['Test1', 'Test2', 'Test3']

folders = {
    
}

for i in range(0, len(folderNames)):
    if Path(folderNames[i]).is_dir():
        folders[folderNames[i]] = 'Ya existe la carpeta'
    else:
        Path.mkdir(folderNames[i])
        folders[folderNames[i]] = 'Se ha creado la carpeta'

print(folders)