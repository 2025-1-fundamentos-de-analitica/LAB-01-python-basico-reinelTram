"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    valoresPorClave = {}

    for linea in lineas:
        partes = linea.strip().split('\t')
        if len(partes) > 4:
            campo = partes[4]
            pares = campo.split(',')
            for par in pares:
                if ':' in par:
                    clave, valor = par.split(':')
                    try:
                        valor = int(valor)
                        if clave not in valoresPorClave:
                            valoresPorClave[clave] = [valor]
                        else:
                            valoresPorClave[clave].append(valor)
                    except ValueError:
                        continue

    resultado = []
    for clave in sorted(valoresPorClave):
        valores = valoresPorClave[clave]
        resultado.append((clave, min(valores), max(valores)))

    return resultado
