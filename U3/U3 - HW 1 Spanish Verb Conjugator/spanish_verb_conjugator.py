# INPUT
verbo = input("Ingrese verbo: ")

# PROCESS
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

verbo = verbo.strip().lower()
raiz = verbo[:-2]
final = verbo[-2:]

# OUTPUT
if final in terminaciones:
    lista_terminaciones = terminaciones[final]

    for i in range(len(pronombres)):
        print(pronombres[i] + " " + raiz + lista_terminaciones[i])
else:
    print("Verbo no valido. Debe terminar en -ar, -er o -ir.")
