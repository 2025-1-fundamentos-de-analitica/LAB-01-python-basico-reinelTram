"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    sumaPorLetra = {}

    for linea in lineas:
        partes = linea.strip().split('\t')
        if len(partes) > 3:
            try:
                valorCol2 = int(partes[1])
                letrasCol4 = partes[3].split(',')
                for letra in letrasCol4:
                    letra = letra.strip()
                    if letra in sumaPorLetra:
                        sumaPorLetra[letra] += valorCol2
                    else:
                        sumaPorLetra[letra] = valorCol2
            except ValueError:
                continue

    return dict(sorted(sumaPorLetra.items()))
