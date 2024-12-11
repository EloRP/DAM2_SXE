fraseUser = input("Introduce una frase: ")
palabrasFrase = fraseUser.split()
palabrasFraseInvertidas = palabrasFrase[::-1]
fraseInvertida = ' '.join(palabrasFraseInvertidas)
print(fraseInvertida)
