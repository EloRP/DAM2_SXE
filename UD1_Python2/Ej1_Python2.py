#Escribir un programa que pregunte el nombre del usuario en la consola
# y un número entero e imprima por pantalla en líneas distintas
# el nombre del usuario tantas veces como el número introducido.

print("Introduce tu nombre: ")
nombre = input()
print("Introduce un número entero: ")
numero = int(input())

for i in range(numero):
    print(nombre)