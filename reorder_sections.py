import re

# Leer archivo
with open(r'c:\Users\McCopper\Desktop\3D-Ultra\05_3DUltra\page arquitectura _Mcco\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# Encontrar indices
scanner_start = None
twins_start = None
twins_end = None

for i, line in enumerate(lines):
    if 'id="scanner"' in line and scanner_start is None:
        scanner_start = i
    if 'id="twins"' in line and twins_start is None:
        twins_start = i
    if twins_start and 'id="concierge"' in line:
        twins_end = i
        break

print(f'scanner_start: {scanner_start}')
print(f'twins_start: {twins_start}')  
print(f'twins_end: {twins_end}')

# Extraer secciones
before_scanner = lines[:scanner_start]
scanner_to_before_twins = lines[scanner_start:twins_start]
twins_section = lines[twins_start:twins_end]
after_twins = lines[twins_end:]

# Reordenar: before_scanner + twins + scanner_to_arqui + after
new_content = before_scanner + twins_section + scanner_to_before_twins + after_twins

# Guardar
with open(r'c:\Users\McCopper\Desktop\3D-Ultra\05_3DUltra\page arquitectura _Mcco\index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_content))

print('Archivo actualizado correctamente')
print(f'Total lineas original: {len(lines)}')
print(f'Total lineas nuevo: {len(new_content)}')
