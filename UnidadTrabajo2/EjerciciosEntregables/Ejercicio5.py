#Pista: find, [:] y replace

#Dado un nombre de archivo llamado 'backup_2025_09_03.tar.gz' extrae la fecha en formato '03-09-2025' 
# (puedes extraer el año, mes y día y luego unirlos con guiones) e imprímela.
#  Luego cambia a '.zip' el nombre del archivo original y muéstralo.

archivo = 'backup_2025_09_03.tar.gz'
res = archivo[archivo.find('_') + 1:]
año = res[:res.find('_')]
print(año)

print(res)

mes1 = res[res.find('_') + 1:]
mes2 = mes1[:mes1.find('_')]

print(mes2)

dia = mes1[mes1.find('_') + 1:]
print(dia)
dia2 = dia[:dia.find('.')]

print(dia2)

#Archivo Final

extensionarchivo = '.zip'

print(f'El archivo es: {dia2}-{mes2}-{año}-{extensionarchivo}')