# 🛡️ Sistema de Detección de Acoso con IA

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.9.0-green)
![YOLOv5](https://img.shields.io/badge/YOLOv5-Custom-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

Sistema inteligente de detección de acoso en tiempo real utilizando visión por computadora y redes neuronales. Este proyecto implementa un modelo personalizado de YOLOv5 para identificar situaciones de acoso y generar alertas automáticas.

## 🚀 Características

- ✅ **Detección en tiempo real** de situaciones de acoso
- 🎥 **Grabación automática** de evidencia cuando se detecta un evento
- 📊 **Análisis de poses** utilizando MediaPipe y CVZone
- 🌐 **Envío de reportes** vía HTTP a servidor remoto
- 📱 **Interfaz visual** para monitoreo en vivo
- ⚡ **Optimización de rendimiento** con procesamiento selectivo de frames

## 📋 Requisitos del Sistema

- **Python**: 3.8 o superior
- **Sistema Operativo**: Windows, macOS, Linux
- **Cámara web**: Compatible con OpenCV
- **RAM**: Mínimo 4GB (recomendado 8GB)
- **GPU**: Opcional (CUDA compatible para mejor rendimiento)

## 🛠️ Instalación

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd rds-ia-video
```

### 2. Crear entorno virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Descargar el modelo de IA

**⚠️ IMPORTANTE**: Debes descargar el modelo personalizado `acoso.pt` desde el siguiente enlace:

📥 **[Descargar acoso.pt](https://drive.google.com/file/d/1lVreho8XVgqyOrARyb5iaz8VUfqO02Es/view?usp=sharing)**

1. Haz clic en el enlace anterior
2. Descarga el archivo `acoso.pt`
3. Coloca el archivo en la carpeta raíz del proyecto

```
rds-ia-video/
├── acoso.pt          ← Aquí debe estar el modelo
├── test.py
├── detect_video_http.py
└── ...
```

### 5. Instalar dependencias adicionales
```bash
pip install mediapipe cvzone
```

## 🎮 Uso

### Modo de Prueba Básico
Para probar la detección básica:
```bash
python test.py
```

### Modo de Prueba Optimizado
Para mejor rendimiento:
```bash
python test_optimized.py
```

### Modo Completo con HTTP
Para envío automático de reportes:
```bash
python detect_video_http.py
```

### Grabación de Video
Para grabar videos manualmente:
```bash
python video_record.py
```

## 📁 Estructura del Proyecto

```
rds-ia-video/
├── 📄 README.md                 # Este archivo
├── 🤖 acoso.pt                  # Modelo de IA (descargar por separado)
├── 🐍 test.py                   # Script de prueba básico
├── ⚡ test_optimized.py         # Script optimizado
├── 🌐 detect_video_http.py      # Detección con envío HTTP
├── 🎥 video_record.py           # Grabación de video
├── 📡 http_data.py              # Funciones HTTP
├── ⚙️ custom.yaml               # Configuración personalizada
├── 📦 requirements.txt          # Dependencias Python
├── 🚫 .gitignore               # Archivos ignorados por Git
└── 📊 yolov5s.pt               # Modelo YOLOv5 base
```

## ⚙️ Configuración

### Ajustar rutas del modelo
Si necesitas cambiar la ubicación del modelo, edita la línea en los archivos Python:
```python
model = torch.hub.load('ultralytics/yolov5', 'custom', path='./acoso.pt')
```

### Configurar cámara
Para usar una cámara diferente, modifica:
```python
cap = cv2.VideoCapture(0)  # 0 = cámara por defecto, 1 = segunda cámara
```

### Ajustar sensibilidad
Modifica el tiempo de cooldown entre detecciones:
```python
if time.time() - last_time > 60:  # 60 segundos entre detecciones
```

## 🔧 Solución de Problemas

### Error: "No module named 'mediapipe'"
```bash
pip install mediapipe cvzone
```

### Error: "No se puede encontrar acoso.pt"
- Verifica que descargaste el modelo desde el enlace proporcionado
- Asegúrate de que está en la carpeta raíz del proyecto
- Verifica que el nombre del archivo sea exactamente `acoso.pt`

### Cámara se congela o va lenta
- Usa `test_optimized.py` en lugar de `test.py`
- Reduce la resolución de la cámara
- Cierra otras aplicaciones que usen la cámara

### Error de dependencias en Python 3.12
```bash
pip install --upgrade gevent>=22.0.0 libsass>=0.22.0 lxml>=4.9.0
```

## 📊 Rendimiento

- **FPS promedio**: 15-30 (depende del hardware)
- **Tiempo de detección**: ~100-200ms por frame
- **Precisión del modelo**: ~85-90% (en condiciones óptimas)
- **Uso de RAM**: ~2-4GB durante ejecución

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request



## 🙏 Agradecimientos

- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5) por el framework de detección
- [CVZone](https://github.com/cvzone/cvzone) por las utilidades de visión por computadora
- [MediaPipe](https://mediapipe.dev/) por el análisis de poses
- UAGRM - Facultad de Ingeniería

---

⭐ **¡No olvides dar una estrella al proyecto si te fue útil!** ⭐