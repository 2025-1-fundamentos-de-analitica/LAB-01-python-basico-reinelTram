"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """


    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    sumaPorLetra = {}

    for linea in lineas:
        partes = linea.strip().split('\t')
        if len(partes) >= 5:
            letra = partes[0]
            campo = partes[4]
            pares = campo.split(',')

            sumaFila = 0
            for par in pares:
                if ':' in par:
                    try:
                        _, valor = par.split(':')
                        sumaFila += int(valor)
                    except ValueError:
                        continue

            if letra in sumaPorLetra:
                sumaPorLetra[letra] += sumaFila
            else:
                sumaPorLetra[letra] = sumaFila

    return dict(sorted(sumaPorLetra.items()))
