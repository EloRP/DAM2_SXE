fraseInput = input("Introduce una frase: ")
vocalFrase = input("Introduce una vocal: ").lower()

frase_modificada = fraseInput.replace(vocalFrase, vocalFrase.upper())
print("Frase modificada:", frase_modificada)