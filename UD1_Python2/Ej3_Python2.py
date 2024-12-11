nombreUsuario = input("Introduce tu nombre: ")
nombreSinEspacios = nombreUsuario.strip()
numeroLetras = len(nombreSinEspacios)

print(nombreUsuario.upper(), " tiene ", numeroLetras, " letras")