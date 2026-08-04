import csv

with open("empleados.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["nombre", "sueldo"])
    w.writerow(["ana", 1500])
    w.writerow(["jaen", 67])
    w.writerow(["santiago", 8000])
    w.writerow(["sabrina", 4000])
    w.writerow(["leo", 67])

total = 0
with open("empleados.csv", "r") as f:
    for fila in csv.DictReader(f):
        total = total + int(fila["sueldo"])

print("Total de sueldos:", total)

