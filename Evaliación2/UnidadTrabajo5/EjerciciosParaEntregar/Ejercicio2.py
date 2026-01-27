# Ejercicio 2: Solicita por teclado 3 nombres de usuario mediante un bucle y almacénalos en una lista.
# A continuación, almacena sus home directory en un diccionario usando os.path.expanduser.
# Muestra el contenido del diccionario recorriendo sus elementos.

import os

nombres = []

usurHome = {

}

for i in range(3):
    usu = input('Dime el nombre del usuario: ')
    nombres.append(usu)

    usurHome[usu] = os.path.expanduser(f'/home/{usu}')

print(usurHome)