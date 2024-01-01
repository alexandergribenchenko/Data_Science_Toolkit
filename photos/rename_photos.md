```python

import os
from PIL import Image
import exifread
from datetime import datetime

# Ruta de la carpeta que contiene las imágenes
carpeta_imagenes = "C:\\Users\\User\\Pictures\\Descarga_Iphone\\"

# Función para obtener la fecha de la imagen desde los metadatos EXIF
def obtener_fecha_imagen(ruta_imagen):
    with open(ruta_imagen, 'rb') as imagen:
        tags = exifread.process_file(imagen)
        fecha = tags.get('EXIF DateTimeOriginal')
        if fecha is not None:
            fecha_str = str(fecha)
            fecha_formateada = datetime.strptime(fecha_str, '%Y:%m:%d %H:%M:%S')
            return fecha_formateada
        else:
            # Si no se puede obtener la fecha de los metadatos, obtener la fecha de la última modificación del archivo
            fecha_modificacion = os.path.getmtime(ruta_imagen)
            return datetime.fromtimestamp(fecha_modificacion)

# Recorremos cada archivo en la carpeta de imágenes
for archivo in os.listdir(carpeta_imagenes):
    ruta_archivo = os.path.join(carpeta_imagenes, archivo)
    if os.path.isfile(ruta_archivo):
        # Verificamos si el archivo es una imagen
        if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            fecha_imagen = obtener_fecha_imagen(ruta_archivo)
            if fecha_imagen:
                # Formateamos la fecha para usarla en el nombre del archivo
                fecha_nombre = fecha_imagen.strftime('%Y%m%d_%H%M%S')
                # Generamos el nuevo nombre del archivo
                nuevo_nombre = f"{fecha_nombre}_{archivo}"
                # Renombramos el archivo
                os.rename(ruta_archivo, os.path.join(carpeta_imagenes, nuevo_nombre))
                print(f"Archivo renombrado: {archivo} -> {nuevo_nombre}")
            else:
                print(f"No se pudo obtener la fecha de la imagen: {archivo}")
```
