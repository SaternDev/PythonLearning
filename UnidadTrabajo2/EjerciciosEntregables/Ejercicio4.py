#Pista: strip, count, find y [:]

#Dada la IP ' 192.168.001.010 ': limpia bordes, cuenta puntos, extrae el primer octeto (hasta primer '.') 
# y último octeto (desde último '.'). Imprime estos 2 octetos.

ip = ' 192.168.001.010 '
ip = ip.strip()
prim_parte = ip[:ip.find('.')]
rest = ip[ip.find('.') + 1:]
rest = rest[rest.find('.') + 1:]
rest = rest[rest.find('.') + 1:]
print(rest)
print(prim_parte)