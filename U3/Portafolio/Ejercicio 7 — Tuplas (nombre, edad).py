"""
Ejercicio 7 - Tuplas (nombre, edad)
Una lista de clientes llega como tuplas (nombre, edad).
Recorre la lista e imprime el nombre de cada cliente mayor
o igual a 20 anios.
"""

clientes = [("Mariana", 19), ("Diego", 25), ("Paola", 20), ("Hugo", 17)]

for nombre, edad in clientes:
    if edad >= 20:
        print(nombre)

