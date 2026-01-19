
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calcularemos el BMI = WEIGHT/(HEIGHT)2
    """

    if len(height) != len(weight):
        raise ValueError("Las listas no contienen los mismos elementos")

    bmi_list = []
    """
    Combinamos las dos listas mediante la función "zip" y asignamos a
    cada elemento de height un h y lo mismo para weight, para manejarlos
    con índices.
    Así obtenemos una tupla de listas: [(h[1]w[1]),(h[2], w[2]),.....]
    """
    for h, w in zip(height, weight):
        # comprobamos que cada elemento de height y weight sea int o float
        if not isinstance(h, (int | float)) or not isinstance(
                          w, (int | float)):
            raise TypeError("Sólo se admiten valores int o float")
        # comprobamos que los datos pasados de height no sean cero
        if h <= 0 or w <= 0:
            raise ValueError("No puede haber datos <= cero")
        bmi = w / (h**2)
        # añadimos a la lista de bmi cada valor calculado
        bmi_list.append(bmi)

    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not isinstance(limit, int) or limit < 0:
        raise TypeError("Límite debe ser un número entero mayor que cero.")
    result = []

    for i in bmi:
        result.append(i > limit)
    return result
