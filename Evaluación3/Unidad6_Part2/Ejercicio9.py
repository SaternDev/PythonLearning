# Crea cleanup_plan.txt con una lista de carpetas temporales (una por línea).
# Por ejemplo, /tmp, /var/tmp, /noexiste, etc.
# Genera cleanup_report.txt indicando cuáles existen y cuántos elementos contienen (usa pathlib.iterdir() y recuento).
# Cada línea debería tener el siguiente formato: ruta -> existe -> elementos: 3 o ruta -> NO existe.

from pathlib import Path

rutas = []

if not Path('cleanup_plan.txt').exists():
    with open('cleanup_plan.txt', 'a') as l:
        l.write(f'/tmp\n/var/tmp\n/noexiste\nEjerciciosPracticar')

with open('cleanup_plan.txt', 'r') as p:
    for i in p.readlines():
        rutas.append(i.strip())

with open('cleanup_report.txt', 'a') as f:
    for j in rutas:
        sum = 0
        if Path(j).exists():
            for file in Path(j).iterdir():
                sum += 1
            f.write(f'{j} -> existe -> elementos: {sum}\n')
        else:
            f.write(f'{j} -> NO existe\n')