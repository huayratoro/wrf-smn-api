import os
import imageio

# Directorio donde se encuentran las imágenes
dir_path = "assets/pp/"

# Lista para almacenar las imágenes
images = []

# Obtiene una lista de todos los nombres de archivo en el directorio
filenames = os.listdir(dir_path)

# Ordena los nombres de archivo
filenames.sort()

# Lee todas las imágenes del directorio en orden
for filename in filenames:
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Asegúrate de que son imágenes
        img_path = os.path.join(dir_path, filename)
        images.append(imageio.imread(img_path))

# Crea un GIF a partir de las imágenes
# El parámetro 'duration' controla la duración de cada cuadro en segundos
# Un valor más pequeño hará que el GIF se reproduzca más rápido, y un valor 
# más grande hará que se reproduzca más lentamente.
imageio.mimsave('assets/pp.gif', images, duration=250)