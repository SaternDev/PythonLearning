# Ejercicio 7: Usa la librería pathlib para listar los usuarios en /home.
# Crea un diccionario con los nombres de cada usuario y cuántos archivos tienen en su carpeta
# de usuario.
# Muestra el contenido del diccionario recorriendo sus elementos.

from pathlib import Path

users = {

}

usersDir = Path('/Users')
sumUserDir = 0

for i in usersDir.iterdir():
    print(i)
    for j in i.iterdir():
        sumUserDir +=1
    users[str(i)] = sumUserDir

print(users)