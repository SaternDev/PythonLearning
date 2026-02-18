# Crea commands.txt con comandos típicos (texto).
# Por ejemplo ls -la, df -h, uname -a, etc.
# Luego lee el fichero y genera commands_numbered.txt numerando cada línea (usa enumerate).

def crear(num, command):
    with open('commands_numbered.txt', 'a') as l:
        l.write(f'{num}, {command}')

with open('commands.txt', 'r') as f:
    for line_n, line in enumerate(f,start=1):
        crear(line_n, line)