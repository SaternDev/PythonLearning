# Un administrador de sistemas quiere automatizar la instalación de paquetes con un
# comando tipo: apt install paquete1 paquete2 paquete3.
# Crea una lista con varios nombres de paquetes, por ejemplo, ["vim", "curl", "htop"],
# simula que el usuario añade uno más por teclado, y construye la cadena completa
# del comando apt install ... a partir de la lista.

paquetes = ["vim", "curl", "htop"]

paqueteAnadir = input('Dime el paquete que quieres añadir: ')
paqueteAnadir = paqueteAnadir.lower()

if paqueteAnadir not in paquetes:
    paquetes.append(paqueteAnadir)

paquetes = ' '.join(paquetes)

print(f'apt install {paquetes}')