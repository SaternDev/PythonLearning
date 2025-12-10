#Pista: startswith, find y [:]

#Dada la etiqueta 'PC-AULA-23', verifica si empieza por 'PC-' (solo muestra True o False) y extrae 'AULA' y '23' usando find y [:] (troceado de cadenas).
#  No uses condicionales; solo imprime las partes obtenidas.

string = 'PC-AULA-23'
empieza_str = string.startswith('PC-')
print(empieza_str)
pos_first_str =  string.find('-')
rest_str = string[pos_first_str + 1:]
aula_str = rest_str[:rest_str.find('-')]
num_aula = rest_str[rest_str.find('-') + 1:]
print(f'La aula es: {aula_str} {num_aula}')