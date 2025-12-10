#Dado el texto ' pc -- aula - 07 \n' debes convertirlo a 'PC-AULA-07' sin usar condicionales ni bucles. Imprime el resultado.
string = ' pc -- aula - 07 \n'
str_modified = string.strip()
str_modified = str_modified.replace(' ', '')
str_modified = str_modified.replace('--', '-')
str_modified = str_modified.upper()
print(str_modified)