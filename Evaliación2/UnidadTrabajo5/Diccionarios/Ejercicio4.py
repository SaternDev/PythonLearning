#  Escribe un programa que solicite al usuario una palabra y devuelva su significado usando el siguiente diccionario:

diccionario = {
    'python': 'Lenguaje de programación',
    'algoritmo': 'Conjunto de instrucciones',
    'variable': 'Espacio de memoria para almacenar datos'
}

palabra = input('Dime una palabra para decirte su significado: ')

if palabra in diccionario:
    print(f'El significado de {palabra} es: {diccionario[palabra]}')
else:
    print('La palabra indicada no está en el diccionario')
    palabra = input('Dime otra palabra que si esté en el diccionario: ')