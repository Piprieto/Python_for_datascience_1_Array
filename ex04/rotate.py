import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from load_image import ft_load


def rotate(image):
    h, w, c = image.shape
    # inicializamos con ceros una matriz de dimensiones traspuesta
    transposed = np.zeros((w, h, c), dtype=image.dtype)

    for i in range(h):   # rellenamos con cada elemento traspuesto
        for j in range(w):
            for k in range(c):  # Para cada canal: R, G, B trasponemos
                transposed[j][i][k] = image[i][j][k]
    # de una matriz 3D (400, 400, 1) pasamos a una 2D (400, 400)
    transposed = transposed[:, :, 0]
    return transposed


def ft_zoom(image_data: np.ndarray, size: int = 400):
    """
    Calculo y coloco el centro de la imagen y después recortarla
    """
    try:
        height, width, _ = image_data.shape
        # Corte desde el centro de la imagen
        center_x, center_y = (width // 2), (height // 2)
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

        # Convertir de nuevo a NumPy array
        gray = np.array(gray_pil)

        # Agregar dimensión de canal si se necesita formato (H, W, 1)
        gray_3d = gray[:, :, np.newaxis]

        return gray_3d

    except Exception as e:
        print(f"Error while zooming: {e}")
        return None


def main():
    path = "animal.jpeg"
    original = ft_load(path)
    cropped = ft_zoom(original)
    if cropped is None:
        return

    print(f"The shape of image is: {cropped.shape}")
    print(cropped)

    transposed = rotate(cropped)
    print("New shape after Transpose:", transposed.shape)
    print(transposed)

    # Mostrar imagen transpuesta
    plt.imshow(transposed, cmap='gray')
    plt.title("Transposed image")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
