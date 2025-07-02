"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    valoresPorLetra = {}

    for linea in lineas:
        partes = linea.strip().split('\t')
        if len(partes) > 1:
            letra = partes[0]
            try:
                valor = int(partes[1])
                if letra not in valoresPorLetra:
                    valoresPorLetra[letra] = [valor]
                else:
                    valoresPorLetra[letra].append(valor)
            except ValueError:
                continue

    resultado = []
    for letra in sorted(valoresPorLetra):
        valores = valoresPorLetra[letra]
        resultado.append((letra, max(valores), min(valores)))

    return resultado
