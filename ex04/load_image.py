
from PIL import Image
import numpy as np


def ft_load(path: str):   # str será la cadena de texto con la ruta al archivo
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

        # Imprimir la forma de la imagen. Muestra por pantalla las
        # dimensiones del array.
        print(f"The shape of image is: {data.shape}")
        return data

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
