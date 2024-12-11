telefonoEmpresa = input("Escribe un número de teléfono con el formato +34-Número-Extensión: ")

partesNumeroTelefono = telefonoEmpresa.split("-")
numero = partesNumeroTelefono[1]

print("El número de teléfono sin prefijo ni extensión es: " + numero)
