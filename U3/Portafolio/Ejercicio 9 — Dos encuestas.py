"""
Ejercicio 9 - Dos encuestas
Dos encuestas preguntan que lenguaje de programacion prefieren
los estudiantes. Compara ambas listas e imprime lo que aparece
en las dos encuestas y lo que es unico de cada una.
"""

encuesta_a = ["python", "java", "c++", "javascript"]
encuesta_b = ["python", "c++", "kotlin", "swift"]

grupo_a = set(encuesta_a)
grupo_b = set(encuesta_b)

print("En ambas encuestas:", sorted(grupo_a & grupo_b))
print("Valores unicos:", sorted((grupo_a - grupo_b) | (grupo_b - grupo_a)))

