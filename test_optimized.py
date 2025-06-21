import time
import cv2
import numpy as np
from cvzone.PoseModule import PoseDetector
from datetime import datetime
import torch
import requests

# Leemos el modelo
model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/Christian Carrion/Documents/Documentos/UAGRM/Software2/proyectoFinal/Proyecto_BullingRDS/rds-ia-video/acoso.pt')
cap = cv2.VideoCapture(0)

# Configuración optimizada de cámara
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 15)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Reducir buffer

detector = PoseDetector()
last_time = time.time() - 60
nimg = 0
process_every_n_frames = 5  # Procesar solo cada 5 frames
frame_count = 0

print("Iniciando detector optimizado...")
print("Presiona ESC para salir")

while True:
    start_time = time.time()
    
    ret, frame = cap.read()
    if not ret:
        print("Error: No se puede leer de la cámara")
        break
    
    frame_count += 1
    
    # Mostrar siempre el frame original para fluidez visual
    display_frame = frame.copy()
    
    # Procesar IA solo cada N frames
    if frame_count % process_every_n_frames == 0:
        try:
            # Redimensionar frame para procesamiento más rápido
            small_frame = cv2.resize(frame, (320, 240))
            
            # Realizamos detecciones en frame pequeño
            detect = model(small_frame)
            img = detector.findPose(small_frame)
            lmlist, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
            
            # Filtrar resultados
            info = detect.pandas().xyxy[0]
            
            # Detectar evento
            if not info.empty and lmlist and time.time() - last_time > 60:
                print("¡Se ha detectado un posible acoso!")
                cv2.imwrite(f'nimg_{nimg}.png', frame)  # Guardar frame original
                print(f'Imagen guardada: nimg_{nimg}.png')
                nimg += 1
                last_time = time.time()
                
                # Mostrar detección en frame original
                cv2.putText(display_frame, "ACOSO DETECTADO!", (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            # Mostrar información de rendimiento
            fps = 1.0 / (time.time() - start_time)
            cv2.putText(display_frame, f"FPS: {fps:.1f}", (10, display_frame.shape[0] - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            
        except Exception as e:
            print(f"Error en procesamiento: {e}")
    
    # Mostrar frame
    cv2.imshow('Detector de Acoso Optimizado', display_frame)
    
    # Control de velocidad
    if cv2.waitKey(1) == 27:  # ESC para salir
        break

print("Cerrando detector...")
cap.release()
cv2.destroyAllWindows()