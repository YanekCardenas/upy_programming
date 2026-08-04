"""
Ejercicio 16 - precios
Una lista de productos con su precio se guarda en un archivo
de texto con un encabezado "producto precio".
"""

productos = [("pluma", 7), ("goma", 4), ("sacapuntas", 6), ("libreta", 12)]

with open("productos.txt", "w") as f:
    f.write("producto precio\n")
    for nombre, precio in productos:
        f.write(nombre + " " + str(precio) + "\n")

with open("productos.txt", "r") as f:
    print(f.read())

