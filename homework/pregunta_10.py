"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    resultado = []

    for linea in lineas:
        partes = linea.strip().split('\t')
        if len(partes) >= 5:
            letra = partes[0]
            columna4 = partes[3]
            columna5 = partes[4]

            numCol4 = len(columna4.split(',')) if columna4 else 0
            numCol5 = len(columna5.split(',')) if columna5 else 0

            resultado.append((letra, numCol4, numCol5))

    return resultado


