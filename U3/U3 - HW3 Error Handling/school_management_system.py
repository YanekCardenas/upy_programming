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
usuario = ""

# INPUT
while acceso == False:
    try:
        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()

        if usuarios[usuario]['password'] != contrasena:
            raise ValueError("la contraseña no es correcta.")

        acceso = True

    except KeyError:
        print("Error: ese usuario no está registrado.")

    except ValueError as error:
        print("Error:", error)

    except (EOFError, KeyboardInterrupt):
        print()
        print("Programa cancelado por el usuario.")
        acceso = True
        usuario = ""

# PROCESS
if usuario == "":
    rol = "ninguno"
    nombre = ""
else:
    nombre = usuarios[usuario]['nombre']
    rol = usuarios[usuario]['rol']

    # OUTPUT
    print("Bienvenido, " + nombre + " (" + rol + ")")
    print()

if rol == 'alumno':
    print("Boleta de " + nombre)

    aprobadas = set()

    for materia in materias:
        try:
            print(materia + ": " + str(calificaciones[usuario][materia]))

            if calificaciones[usuario][materia] >= 8.0:
                aprobadas.add(materia)

        except KeyError:
            print(materia + ": sin calificación registrada")

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

    capturado = False

    # INPUT
    while capturado == False:
        try:
            alumno = input("Alumno: ").strip()

            if usuarios[alumno]['rol'] != 'alumno':
                raise ValueError("ese usuario no es un alumno.")

            materia = input("Materia: ").strip()

            if materia not in materias:
                raise ValueError("esa materia no existe.")

            texto = input("Nueva calificación: ").strip()

            try:
                nueva = float(texto)
            except ValueError:
                raise ValueError("la calificación debe ser un número.")

            if nueva < 0 or nueva > 10:
                raise ValueError("la calificación debe estar entre 0 y 10.")

            # PROCESS
            calificaciones[alumno][materia] = nueva
            capturado = True

            # OUTPUT
            print("Calificación actualizada.")

        except KeyError:
            print("Error: ese alumno no está registrado.")

        except ValueError as error:
            print("Error:", error)

        except (EOFError, KeyboardInterrupt):
            print()
            print("Captura cancelada por el usuario.")
            capturado = True

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
        try:
            print(usuarios[a]['nombre'])
        except KeyError:
            print(a + " (alumno sin registro en usuarios)")

        for materia in materias:
            try:
                print("   " + materia + ": " + str(calificaciones[a][materia]))
            except KeyError:
                print("   " + materia + ": sin calificación registrada")

elif rol == 'ninguno':
    print("No se inició sesión.")

else:
    print("Error: el rol '" + rol + "' no tiene un menú asignado.")
