#Pide al usuario que escriba una frase. Luego, muestra:

#1. Los primeros 5 caracteres.

#2. Los últimos 5 caracteres.

#3. Todos los caracteres en posiciones pares.

frase = str(input('Dime una frase \n'))
longitudCadena = len(frase)
print(f'Los primeros 5 carcateres de tu frase son: {frase[0:5]}')
print(f'Los ultimos 5 carcateres de tu frase son: {frase[-6:-1]}')
print(f'Todas las letras en posiciones pares: {frase[0:longitudCadena:2]}')
