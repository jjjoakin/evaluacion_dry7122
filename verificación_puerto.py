numero_puerto = int(input("Ingrese el número de puerto (0-65535): "))

if 0 <= numero_puerto <= 1023:
    print("Puerto bien conocido")
elif 1024 <= numero_puerto <= 49151:
    print("Puerto registrado")
elif 49152 <= numero_puerto <= 65535:
    print("Puerto dinámico o privado")
else:
    print("No corresponde a un puerto válido")