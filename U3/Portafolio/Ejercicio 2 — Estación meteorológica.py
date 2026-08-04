"""
Ejercicio 2 - Estacion meteorologica
Una estacion registra la temperatura de 10 dias.
Calcula el promedio entre el primer y el ultimo dia registrado,
e indica si el ultimo dia fue mas caluroso que el primero.
"""

temperaturas = [28, 30, 33, 45, 26, 22, 31, 33, 34, 36]

primero = temperaturas[0]
ultimo = temperaturas[-1]

print("Promedio entre primer y ultimo dia:", (primero + ultimo) / 2)
print("El ultimo dia fue mas caluroso que el primero:", ultimo > primero)

