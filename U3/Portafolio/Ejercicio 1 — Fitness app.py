"""
Ejercicio 1 - Fitness app
Una app de fitness registra los pasos diarios de una semana.
Imprime el primer dia registrado, el ultimo dia, el total de
pasos y el promedio diario.
"""

pasos = [5200, 7300, 2100, 8400, 6100, 9800, 4300]

print("Primer dia:", pasos[0])
print("Ultimo dia:", pasos[-1])
print("Total de pasos:", sum(pasos))
print("Promedio diario:", sum(pasos) / len(pasos))

