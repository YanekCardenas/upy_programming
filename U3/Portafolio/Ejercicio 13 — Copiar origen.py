"""
Ejercicio 13 - Copiar origen
Crea un archivo con 3 lineas, copia su contenido a otro archivo
y muestra lo que quedo en la copia.
"""

with open("origen.txt", "w") as f:
    f.write("linea uno\nlinea dos\nlinea tres\n")

with open("origen.txt", "r") as origen, open("copia.txt", "w") as destino:
    for linea in origen:
        destino.write(linea)

with open("copia.txt", "r") as f:
    print(f.read())

