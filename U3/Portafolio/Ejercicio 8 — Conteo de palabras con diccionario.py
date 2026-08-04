"""
Ejercicio 8 - Conteo de palabras con diccionario
Cuenta cuantas veces se repite cada palabra en una oracion
y muestra el resultado.
"""

oracion = "el perro corre y el gato duerme y el perro ladra"

conteo = {}
for palabra in oracion.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)

