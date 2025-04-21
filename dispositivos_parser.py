import json


with open('dispositivos.json', 'r') as file:
    dispositivos_data = json.load(file)

for dispositivo in dispositivos_data:
    nombre = dispositivo.get('nombre','sin nombre')
    direccion_ip = dispositivo.get('ip','sin direccion ip')
    estado = dispositivo.get('estado','desconocido')

    print(f"nombre del dispositivo: \n{nombre}")
    print(f"direccion ip: \n {direccion_ip}")
    print(f"estado: \n {estado}")