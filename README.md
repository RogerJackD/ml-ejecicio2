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



📦 Versiones utilizadas
Para garantizar el correcto funcionamiento del script, se utilizaron las siguientes versiones:

text
Python: 3.8.10
OpenCV (cv2): 4.5.5
numpy: 1.21.5 (dependencia de OpenCV)
🛠️ Configuración del entorno virtual
1. Crear el entorno virtual
Recomiendo usar venv (incluido en Python) para aislar las dependencias:

bash
python -m venv venv_eye_detection
2. Activar el entorno virtual
Windows (CMD/PowerShell):

bash
.\venv_eye_detection\Scripts\activate
Linux/MacOS:

bash
source venv_eye_detection/bin/activate
3. Instalar las dependencias
Con el entorno virtual activado, instala los paquetes necesarios:

bash
pip install opencv-python==4.5.5.64 numpy==1.21.5
