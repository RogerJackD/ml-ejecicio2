Este script utiliza OpenCV y los clasificadores Haar Cascade para detectar ojos en tiempo real desde la cámara web y enmarcarlos con rectángulos o círculos azules.

Configuración Inicial
-cv2 (OpenCV): Biblioteca principal para procesamiento de imágenes.
-datetime: Usado para registrar la hora exacta de las capturas.
-os: Para manejar la creación de la carpeta de evidencias.

2. Clasificadores Haar Cascade
haarcascade_frontalface_default.xml: Detecta rostros frontales.

haarcascade_eye.xml: Detecta ojos dentro de los rostros.


Inicializar la cámara (cv2.VideoCapture(0)).


Al presionar 's', se guardará una imagen como:
📂 evidencias/deteccion_20230701_143022.png
