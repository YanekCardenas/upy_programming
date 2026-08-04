"""
Ejercicio 12 - registro
Crea un archivo en modo escritura con la linea "inicio de sesion",
luego agrega la linea "cierre de sesion" sin borrar lo anterior,
y muestra el contenido final.
"""

with open("registro.txt", "w") as f:
    f.write("inicio de sesion\n")

with open("registro.txt", "a") as f:
    f.write("cierre de sesion\n")

with open("registro.txt", "r") as f:
    print(f.read())

