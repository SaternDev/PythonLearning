# Crea un diccionario vacío. Luego, pide al usuario que introduzca por teclado 3 pares clave-valor para rellenarlo.
#  Finalmente, imprime el diccionario.

diccionario = {

}

for _ in range(3):
    clave = input('Dime la primera clave: ')
    valor = input('Dime el valor de esa clave: ')

    diccionario[clave] = valor

print(diccionario)