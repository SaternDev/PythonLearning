# Dado un diccionario con nombres de personas como claves y su edad como valores, muestra el nombre de la persona más joven.
# Crea tú mismo el diccionario con al menos 3 pares clave-valor.

personas = {
    'Juan' : 19,
    'Pedro' : 30,
    'Pepe' : 60,
    'Mauro' : 12
}

menor = ''

for i in personas:
    if menor == '':
        menor = i
    elif personas[i] < personas[menor]:
        menor = i

print(f'La persona menor es: {menor} con {personas[menor]} años')