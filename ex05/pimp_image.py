import numpy as np
import matplotlib.pyplot as plt  # para mostrar imágenes en vez de los arrays
"""
En el array, 0 significa que el color es tan oscuro que se ve negro
mientras que 255 significa que el color está en su máxima intensidad.
De esta manera un pixel negro en una imagen será un pixel en el cual los tres
colores tengan intensidad 0, un pixel de color rojo puro será un pixel con
intensidad 255 en el rojo e intensidad 0 en verde y azul, y un pixel blanco
tendrá intensidad 255 en los tres componentes.
"""


def show_image(array, title):
    """
    Muestra una imagen con título.
    Cada array tiene forma (H, W, 3) y cada pixel tiene 3 valores [R, G, B]
    ej cada pixel: array[i][j] = [100, 150, 200]
    """
    plt.imshow(array)
    plt.title(title)
    plt.axis("off")  # sin que aparezcan los ejes
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:    # sólo permitidos =,+.-,*
    """Inverts the color of the image received."""
    result = 255 - array    # invertimos un color en su opuesto
    show_image(result, "Invert Filter")
    return result


def ft_red(array: np.ndarray) -> np.ndarray:        # sólo permitidos =,*
    """Applies a red filter to the image."""
    result = array * [1, 0, 0]               # usamos * para dejar sólo R
    show_image(result, "Red Filter")
    return result


def ft_green(array: np.ndarray) -> np.ndarray:  # sólo permitidos =,-
    """Applies a green filter to the image."""
    result = array.copy()
    # delete red channel
    result[:, :, 0] = 0
    # delete blue channel
    result[:, :, 2] = 0
    show_image(result, "Green Filter")
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:   # sólo permitido =
    """Applies a blue filter to the image."""
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    show_image(result, "Blue Filter")
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:   # sólo permitidos =, /
    """Converts the image to grayscale. """
    gray = (array[:, :, 0] / 3 + array[:, :, 1] / 3
            + array[:, :, 2] / 3).astype(np.uint8)
    """
    Para que una imagen sea gris, la intensidad de los tres canale en cada
    pixel debe ser igual. Primero calcula la media de los canales
    R, G y B → resultado es float64 (por defecto en operaciones con división)
    así que hacemos astype(np.uint8) que convierte ese resultado
    en entero sin signo de 8 bits, es decir, un número entre 0 y 255
    (lo que se usa para representar colores en imágenes)
    """
    result = np.zeros_like(array)
    result[:, :, 0] = gray
    result[:, :, 1] = gray
    result[:, :, 2] = gray
    show_image(result, "Grayscale Filter")
    return result
