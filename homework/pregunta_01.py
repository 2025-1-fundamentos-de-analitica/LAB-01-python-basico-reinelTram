"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
   
    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    sumaSegundaColumna = 0

    for linea in lineas:
        partes = linea.strip().split('\t')
        if len(partes) > 1:
            try:
                numero = int(partes[1])
                sumaSegundaColumna += numero
            except ValueError:
                continue

    return sumaSegundaColumna

if __name__ == "__main__":
    print(pregunta_01())