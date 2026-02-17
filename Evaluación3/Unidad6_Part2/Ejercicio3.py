# Lee admin_log.txt y muestra cuántas líneas contiene y cuál es la última línea (si existe).

with open('admin_log.txt', 'r') as f:
    for line_no, line in enumerate(f, start=1):
        pass
    print(f'El número de líneas es: {line_no} y la última línea contiene: {line}')