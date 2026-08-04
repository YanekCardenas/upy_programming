with open("notas.txt", "w") as f:
    f.write("Ana 9\nLuis 9\nDaniel 7\nJesus 10\nJaen 4\n")

with open("notas.txt", "r") as f:
    for linea in f:
        nombre, calif = linea.split()
        if int(calif) >= 8:
            print(nombre)

