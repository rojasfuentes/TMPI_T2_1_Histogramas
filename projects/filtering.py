import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargar la imagen
img = cv2.imread('C:/Users/JFROJAS/Documents/sample/src/image.jpg')

# Definir una máscara
mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# Aplicar la convolución a la imagen utilizando la máscara
filtered_img = cv2.filter2D(img, -1, mask)

# Mostrar la imagen original y la imagen filtrada
plt.subplot(121), plt.imshow(img), plt.title('Imagen Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(filtered_img), plt.title('Imagen Filtrada')
plt.xticks([]), plt.yticks([])
plt.show()