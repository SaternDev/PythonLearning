# Pide al usuario una palabra y guárdala en palabras.txt sin borrar el contenido anterior.
# Ejecuta varias veces y comprueba que funciona correctamente.

with open('palabras.txt', 'a') as f:
    palabra = input('Dime la palabra que quieras guardar: ')
    f.write(palabra + '\n')