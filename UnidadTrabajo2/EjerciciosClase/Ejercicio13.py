#Solicita al usuario que ingrese una frase. Luego:

#1. Extrae e imprime los primeros 10 caracteres de la frase.
#2. Extrae e imprime los últimos 10 caracteres.
#3. Muestra todos los caracteres desde la posición 5 hasta la posición 15.
#4. Imprime la frase en orden inverso

frase = str(input('Dime una frase: '))

print(f'Los primeros 10 caracteres de tu frase son: {frase[0:10]}')
print(f'Los ultimos 10 caracteres de tu frase son: {frase[-11:-1]}')
print(f'Los caracteres desde la posición 5 hasta la 15 son: {frase[5:15]}')
print(f'Tu frase invertida: {frase[::-1]}')