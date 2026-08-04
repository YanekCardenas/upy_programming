import os

archivo = "foto.png"

nombre, ext = os.path.splitext(archivo)
respaldo = os.path.join("respaldos", nombre + ".bak")

print("respaldo:", respaldo)
print("existe el origen:", os.path.exists(archivo))

