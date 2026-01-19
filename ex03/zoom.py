from PIL import Image            # módulo para manipular imágenes
import numpy as np               # módulo para convertir y trabajar con arrays
import matplotlib.pyplot as plt  # módulo para mostrar gráficas, ejes,...
from load_image import ft_load


def ft_zoom(image_data: np.ndarray, size: int = 400):
    """
    Función para calcular el centro de la imagen y recortarla
    """
    try:
        height, width, _ = image_data.shape
        # image_data es una matriz (porque lo hemos hecho con np)
        # en NumPy, con shape podemos obtener una tupla con las dimensiones
        # de la matriz así, en este caso, los índices se guardaŕan
        # en height(altura) y width(anchura)

        # Corte desde el centro de la imagen
        center_x, center_y = (width // 2), (height // 2)
        # calculamos el centro de la imagen y lo movemos un poco para que la
        # imagen final se parezca más a la dada en el enunciado
        center_x = center_x + 150
        center_y = center_y - 90
        half = size // 2
        cropped = image_data[
            center_y - half:center_y + half,
            center_x - half:center_x + half
        ]

        # Convertir el recorte a imagen PIL
        cropped_pil = Image.fromarray(cropped)
        # Convertir a escala de grises usando PIL
        gray_pil = cropped_pil.convert("L")

        # Convertir de nuevo a NumPy array. Ahora será un array 2D(alto, ancho)
        gray = np.array(gray_pil)

        # Agregar dimensión de canal si se necesita formato 3D(alto,ancho, 1)
        gray_3d = gray[:, :, np.newaxis]

        print(f"New shape after slicing: {gray_3d.shape}")
        print(gray_3d[:1])      # sólo primera columna

        return gray

    except Exception as e:
        print(f"Error while zooming: {e}")
        return None


def show_image(image: np.ndarray):  # mostramos imagen resultante
    try:
        plt.imshow(image, cmap='gray')  # cmap='gray'para que salga en grises
        plt.title("Zoomed Image with Axes")
        plt.xlabel("X-axis (pixels)")
        plt.ylabel("Y-axis (pixels)")
        plt.show()
    except Exception as e:
        print(f"Error displaying image: {e}")


def main():
    path = "animal.jpeg"
    image_loaded = ft_load(path)
    print(image_loaded)
    zoomed = ft_zoom(image_loaded)
    # original = ft_load(path)
    if zoomed is not None:
        # show_image(original)
        show_image(zoomed)


"""
# Para ver las dos imagenes con los titulos correctos:
def show_image(image, title="Image"):
    # Muestra una imagen usando matplotlib.
    # Detecta automáticamente si es RGB o grayscale.

    import matplotlib.pyplot as plt

    plt.figure(title)  # Cada imagen en una ventana separada
    if len(image.shape) == 2:  # Escala de grises
        plt.imshow(image, cmap='gray')
    else:  # Imagen RGB
        plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()

def main():
    path = "animal.jpeg"
    original = ft_load(path)
    zoomed = ft_zoom(original)

    if zoomed is not None:
        # Cada imagen en su propia ventana
        show_image(original, title="Original")
        show_image(zoomed, title="Zoomed")
"""


if __name__ == "__main__":
    main()
