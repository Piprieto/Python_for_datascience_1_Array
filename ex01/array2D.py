import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Trabajaremos con una lista de listas (es decir, una matriz 2D)
    y aplicaremos slicing para obtener una parte de esa matriz.
    El método slicing es una técnica que permite extraer partes de una lista,
    tupla, cadena o array utilizando una notación especial con
    corchetes y dos puntos: "lista[inicio:fin]"
    """
    if not isinstance(family, list):
        raise TypeError("Family no es de tipo lista")
    if not family:
        raise ValueError("Family está vacía")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("Cada elemento de family debe ser una lista")
    if not all(len(row) == len(family[0]) for row in family):
        raise AssertionError(
            "Todos los elementos de Family deben tener el mismo tamaño"
        )
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Comienzo y final deben ser números enteros")

    # Convertimos la lista a un array numpy
    array = np.array(family)

    # Imprimimos la forma de la matriz con la función array.shape
    print(f"My shape is : {array.shape}")

    # Aplicamos slicing
    sliced_array = array[start:end]

    # Mostramos la nueva forma
    print(f"My new shape is : {sliced_array.shape}")

    # Convertimos el array de vuelta a lista con la función tolist()
    return sliced_array.tolist()
