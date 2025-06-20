import time
import torch
import numpy as np
import cv2
from collections import deque
import http_data

# Configuración
record_duration = 15
frame_rate = 5
max_frames = int(record_duration * frame_rate)

# Inicializa el búfer de frames
frame_buffer = deque(maxlen=max_frames)

# Carga el modelo
model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='C:/xampp/htdocs/Proyecto_BullingRDS/rds-ia-video/acoso.pt')

# Inicia la captura de la cámara
cap = cv2.VideoCapture(0)

last_time = time.time() - 15
send_report = False

# Captura inicial para llenar el búfer
while len(frame_buffer) < max_frames:
    ret, frame = cap.read()
    if not ret:
        break
    frame_buffer.append(frame)
    cv2.imshow('Detector', frame)
    if cv2.waitKey(5) == 27:  # Salir con tecla ESC
        break

# Bucle principal
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Agrega el fotograma al búfer
    frame_buffer.append(frame)

    # Realizamos detecciones
    detect = model(frame)
    info = detect.pandas().xyxy[0]

    # Detectar evento
    if not info.empty and time.time() - last_time > 15:
        print("¡Se ha detectado un posible acoso!, se generará un video.")
        send_report = True
        last_time = time.time()

        # Crear un nuevo archivo de video para el evento detectado
        video_name = f'video_evento_{int(time.time())}.avi'
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(video_name, fourcc, frame_rate, (640, 480))

        # Escribir los frames del búfer en el archivo
        for f in frame_buffer:
            out.write(f)
        out.release()

        # Enviar el video al servidor
        evento = http_data.crear_evento(descripcion='Video de posible acoso')
        if evento:
            id_evento = evento['data']['id']
            http_data.crear_evidencia_video(video_path=video_name, id_evento=id_evento)
            print(f'Video registrado para el evento ID: {id_evento}')

    # Mostrar la detección en tiempo real
    cv2.imshow('Detector', np.squeeze(detect.render()))

    if cv2.waitKey(5) == 27:  # Salir con tecla ESC
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
