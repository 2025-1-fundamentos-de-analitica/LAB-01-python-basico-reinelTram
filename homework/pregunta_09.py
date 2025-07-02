"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    conteoClaves = {}

    for linea in lineas:
        partes = linea.strip().split('\t')
        if len(partes) > 4:
            campo = partes[4]
            pares = campo.split(',')
            clavesEnFila = set()
            for par in pares:
                if ':' in par:
                    clave = par.split(':')[0]
                    clavesEnFila.add(clave)
            for clave in clavesEnFila:
                if clave in conteoClaves:
                    conteoClaves[clave] += 1
                else:
                    conteoClaves[clave] = 1

    return dict(sorted(conteoClaves.items()))

