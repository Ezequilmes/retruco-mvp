import cv2
import numpy as np
import random
import os

# Colocar las 3 cartas en una sola imagen
def superponerImagenes(background, overlay, x, y):
    background_width = background.shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay = overlay[:, :w]

    if y + h > background_height:
        h = background_height - y
        overlay = overlay[:h]

    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [
                overlay,
                np.ones((overlay.shape[0], overlay.shape[1], 1), dtype=overlay.dtype) * 255
            ],
            axis=2,
        )

    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0

    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_image

    return background 

# Elegir aleatoriamente las 3 cartas
def elegirCarta():
    return random.choice(palo) + random.choice(numero)

# Crear una mano con 3 cartas distintas
path = "./Cartas/"
formato = ".png"

# Verificar que la carpeta de resultados exista
if not os.path.exists("./Resultados/"):
    os.makedirs("./Resultados/")

# Cargar imagen de fondo
fondo = cv2.imread(path + "Fondo" + formato)
if fondo is None:
    raise FileNotFoundError(f"No se encontró la imagen de fondo en la ruta: {path}Fondo{formato}")

palo = ["B", "C", "E", "O"]
numero = ["1", "2", "3", "4", "5", "6", "7", "10", "11", "12"]

# Seleccionar cartas únicas
cartas = set()
while len(cartas) < 3:
    cartas.add(elegirCarta())
nombre1, nombre2, nombre3 = list(cartas)

# Cargar imágenes de las cartas
img1 = cv2.imread(path + nombre1 + formato)
img2 = cv2.imread(path + nombre2 + formato)
img3 = cv2.imread(path + nombre3 + formato)

# Verificar que las imágenes de las cartas se cargaron correctamente
if img1 is None:
    raise FileNotFoundError(f"No se encontró la imagen de la carta: {path}{nombre1}{formato}")
if img2 is None:
    raise FileNotFoundError(f"No se encontró la imagen de la carta: {path}{nombre2}{formato}")
if img3 is None:
    raise FileNotFoundError(f"No se encontró la imagen de la carta: {path}{nombre3}{formato}")

# Superponer las imágenes de las cartas en el fondo
aux = superponerImagenes(fondo, img1, 7, 15)
aux = superponerImagenes(aux, img2, 217, 15)
aux = superponerImagenes(aux, img3, 427, 15)

# Guardar la imagen generada
cv2.imwrite("./Resultados/photo0.png", aux)

# Guardar una lista en un archivo .txt
vector = [nombre1, nombre2, nombre3]

try:
    with open("cartas.txt", "w") as fp:
        for line in vector:
            fp.write(line + "\n")
except IOError as e:
    raise IOError(f"Error al escribir el archivo 'cartas.txt': {e}")