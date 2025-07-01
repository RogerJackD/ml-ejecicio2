import cv2
import datetime
import os

# 📂 Crear carpeta para guardar evidencias
if not os.path.exists('evidencias'):
    os.makedirs('evidencias')

# 🔍 Cargar clasificadores preentrenados de Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 🎥 Inicializar la cámara web (0 = cámara predeterminada)
cap = cv2.VideoCapture(0)

while True:
    # 📸 Capturar frame por frame
    ret, frame = cap.read()
    if not ret:
        break  # Si no hay frame, salir del bucle

    # 🔳 Convertir a escala de grises (mejor rendimiento para detección)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 👤 Detectar rostros en la imagen
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # 🟢 Dibujar rectángulo verde alrededor del rostro
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 👀 Definir Región de Interés (ROI) para los ojos dentro del rostro
        roi_gray = gray[y:y + h, x:x + w]  # ROI en escala de grises
        roi_color = frame[y:y + h, x:x + w]  # ROI en color (para dibujar)

        # 🔵 Detectar ojos dentro del ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            # 🔷 Opción 1: Dibujar rectángulo azul alrededor del ojo
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

            # 🔵 Opción 2: Dibujar círculo azul alrededor del ojo
            center = (ex + ew // 2, ey + eh // 2)  # Centro del ojo
            radius = int((ew + eh) / 4)  # Radio aproximado
            cv2.circle(roi_color, center, radius, (255, 0, 0), 2)

    # 🖥️ Mostrar el resultado en una ventana
    cv2.imshow('Detección de Ojos en Tiempo Real', frame)

    # 💾 Guardar evidencia al presionar 's' (Screenshot)
    key = cv2.waitKey(1)
    if key == ord('s'):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"evidencias/deteccion_{timestamp}.png"
        cv2.imwrite(filename, frame)
        print(f"✅ Evidencia guardada como: {filename}")

    # 🚪 Salir del programa al presionar 'q' (Quit)
    if key == ord('q'):
        break

# 🔌 Liberar recursos y cerrar ventanas
cap.release()
cv2.destroyAllWindows()