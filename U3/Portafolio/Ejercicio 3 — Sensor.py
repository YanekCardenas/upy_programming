"""
Ejercicio 3 - Sensor
Un sensor registra 12 lecturas a lo largo del dia.
Separa las primeras 6 lecturas (manana) de las restantes (tarde),
y obten una muestra tomando una lectura de cada 3.
"""

lecturas = [30, 33, 38, 48, 27, 23, 32, 33, 35, 38, 12, 10]

manana = lecturas[:6]
tarde = lecturas[6:]
muestreo = lecturas[::3]

print("Manana:", manana)
print("Tarde:", tarde)
print("Muestreo cada 3:", muestreo)

