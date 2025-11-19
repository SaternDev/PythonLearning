#Pista: index/find y [:] 

#Dado el email 'admin.redes@centro.edu', extrae el usuario (antes de '@'), el dominio (entre '@' y primer '.') y el tld (después del '.').
#No uses bucles.

emails = 'admin.redes@centro.edu'

usuario = emails[:emails.find('@')]

print(f'Usuario: {usuario}')

dominio1 = emails[emails.find('@') + 1:]
dominio2 = dominio1[:dominio1.find('.')]
print(f'El dominio es: {dominio2}')

tld = dominio1[dominio1.find('.') + 1:]
print(f'El tld es: {tld}')