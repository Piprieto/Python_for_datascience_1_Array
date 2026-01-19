from PIL import Image
import numpy as np


def ft_load(path: str):  # str cadena de texto con la ruta al archivo
    """
    Este ejercicio pide crear un archivo load_image.py
    con una función ft_load(path: str) que:
    - Cargue una imagen desde la ruta dada.
    - Imprima su formato y contenido en píxeles (en formato RGB).
    - Maneje errores adecuadamente, como archivos no encontrados
    o formatos incorrectos.
    - Soporte al menos imágenes JPG y JPEG.

    Usaremos la libreria PIL para la manipulación de imágenes y
    Numpy para la manipulación de matrices ya que nos piden dar
    el shape (forma) de la imagen como (alto, ancho, 3) y
    los valores RGB de los píxeles como un array.
    Ejemplo: (257, 450, 3).
    - 257 píxeles de alto
    - 450 píxeles de ancho
    - 3 canales de color (R, G, B)

    Los pasos que seguiremos son:
    1. Leer una imagen.
    2. Verificar su formato.
    3. Convertirla a un array NumPy en RGB.
    4. Imprimir su forma (dimensiones).
    5. Devolver los datos de los píxeles.
    """
    try:
        # Cargar la imagen,si el archivo no existe o no es legible
        # ==> except FileNotFoundError
        img = Image.open(path)

        # Verificar formato
        if img.format not in ['JPEG', 'JPG', 'PNG']:
            raise ValueError(
                "Unsupported file format. Only JPG and JPEG are allowed."
                )

        # Convertir a RGB por si no lo está
        img = img.convert("RGB")

        # Convertir la imagen a un array de NumPy
        data = np.array(img)

        # Imprimir la forma de la imagen.
        # Muestra por pantalla las dimensiones del array.
        print(f"The shape of image is: {data.shape}")
        print(data)
        return data

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
