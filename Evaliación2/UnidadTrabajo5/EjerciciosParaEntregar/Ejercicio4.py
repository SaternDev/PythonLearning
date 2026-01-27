# Ejercicio 4: Usa pathlib para listar los archivos y carpetas del directorio actual y 
# guarda esa información (si son archivo o directorio) en un diccionario, tal y como se ha hecho en el ejercicio anterior.

from pathlib import Path

tipeDic = {
    
}

files = []

directory = []

for i in Path.iterdir(Path.cwd()):
    if i.is_dir():
        directory.append(i)
    elif i.is_file:
        files.append(i)

tipeDic["Files"] = files
tipeDic["Directoryes"] = directory

print(tipeDic)