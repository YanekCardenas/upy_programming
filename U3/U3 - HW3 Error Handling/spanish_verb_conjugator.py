# PROCESS
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

verbo_valido = False

# INPUT
while verbo_valido == False:
    try:
        verbo = input("Ingrese verbo: ").strip().lower()

        if verbo == "":
            raise ValueError("no escribiste nada.")

        if len(verbo) < 3:
            raise ValueError("el verbo es demasiado corto.")

        if verbo.isalpha() == False:
            raise ValueError("el verbo solo debe tener letras.")

        raiz = verbo[:-2]
        final = verbo[-2:]
        lista_terminaciones = terminaciones[final]
        verbo_valido = True

    except ValueError as error:
        print("Error:", error)

    except KeyError:
        print("Error: el verbo debe terminar en -ar, -er o -ir.")

    except (EOFError, KeyboardInterrupt):
        print()
        print("Programa cancelado por el usuario.")
        verbo_valido = True
        lista_terminaciones = []

# OUTPUT
for i in range(len(lista_terminaciones)):
    print(pronombres[i] + " " + raiz + lista_terminaciones[i])
