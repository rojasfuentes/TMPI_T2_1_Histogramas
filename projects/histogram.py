import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargar la imagen
img = cv2.imread('C:/Users/JFROJAS/Documents/sample/src/image.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calcular el histograma
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Visualizar el histograma
plt.hist(gray.ravel(), 256, [0, 256])
plt.show()