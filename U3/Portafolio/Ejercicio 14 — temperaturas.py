"""
Ejercicio 14 - temperaturas
Un archivo contiene una temperatura por linea.
Imprime cuantas hay registradas y cual es la mas alta.
"""

with open("temperaturas.txt", "w") as f:
    f.write("19\n21\n29\n38\n33\n")

with open("temperaturas.txt", "r") as f:
    lineas = f.readlines()

temperaturas = [int(x) for x in lineas]

print("Cantidad de lecturas:", len(temperaturas))
print("Temperatura maxima:", max(temperaturas))

