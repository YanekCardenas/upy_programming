# PROCESS
usuarios = {
    'jperez':   {'password': '1234', 'rol': 'alumno',      'nombre': 'Juan Pérez'},
    'amartin':  {'password': '1234', 'rol': 'alumno',      'nombre': 'Ana Martín'},
    'lgomez':   {'password': '1234', 'rol': 'alumno',      'nombre': 'Luis Gómez'},
    'sramirez': {'password': '1234', 'rol': 'alumno',      'nombre': 'Sofía Ramírez'},
    'dtorres':  {'password': '1234', 'rol': 'alumno',      'nombre': 'Diego Torres'},
    'cvargas':  {'password': '1234', 'rol': 'alumno',      'nombre': 'Carla Vargas'},
    'mlopez':   {'password': '1234', 'rol': 'maestro',     'nombre': 'María López'},
    'rgarcia':  {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}

materias = ('Matemáticas', 'Programación', 'Inglés')

calificaciones = {
    'jperez':   {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin':  {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'lgomez':   {'Matemáticas': 7.0, 'Programación': 8.5, 'Inglés': 9.0},
    'sramirez': {'Matemáticas': 9.5, 'Programación': 9.0, 'Inglés': 8.0},
    'dtorres':  {'Matemáticas': 6.5, 'Programación': 7.0, 'Inglés': 8.5},
    'cvargas':  {'Matemáticas': 8.0, 'Programación': 7.5, 'Inglés': 9.5}
}

acceso = False

# INPUT
while acceso == False:
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario]['password'] == contrasena:
        acceso = True
    else:
        print("Usuario o contraseña incorrectos.")

# PROCESS
nombre = usuarios[usuario]['nombre']
rol = usuarios[usuario]['rol']

# OUTPUT
print("Bienvenido, " + nombre + " (" + rol + ")")
print()

if rol == 'alumno':
    print("Boleta de " + nombre)

    aprobadas = set()

    for materia in materias:
        print(materia + ": " + str(calificaciones[usuario][materia]))

        if calificaciones[usuario][materia] >= 8.0:
            aprobadas.add(materia)

    pendientes = set(materias) - aprobadas

    print()
    print("Materias aprobadas:", aprobadas)
    print("Materias pendientes:", pendientes)

elif rol == 'maestro':
    print("Alumnos del grupo:")

    for u in usuarios:
        if usuarios[u]['rol'] == 'alumno':
            print(u + " - " + usuarios[u]['nombre'])

    print()

    # INPUT
    alumno = input("Alumno: ")

    while alumno not in calificaciones:
        print("Ese alumno no existe.")
        alumno = input("Alumno: ")

    materia = input("Materia: ")

    while materia not in materias:
        print("Esa materia no existe.")
        materia = input("Materia: ")

    nueva = float(input("Nueva calificación: "))

    # PROCESS
    calificaciones[alumno][materia] = nueva

    # OUTPUT
    print("Calificación actualizada.")

elif rol == 'coordinador':
    print("Maestros:")

    for u in usuarios:
        if usuarios[u]['rol'] == 'maestro':
            print(u + " - " + usuarios[u]['nombre'])

    print()
    print("Materias:")

    for materia in materias:
        print(materia)

    print()
    print("Alumnos y calificaciones:")

    for a in calificaciones:
        print(usuarios[a]['nombre'])

        for materia in materias:
            print("   " + materia + ": " + str(calificaciones[a][materia]))
