# youtube_summarize

## Resumen y utilidad
Proyecto para descargar/transcribir y resumir vídeos de YouTube (pipeline típico: descarga → transcripción → resumen). Útil para generar resúmenes automáticos, notas de clase o metadatos para búsquedas.

## Requisitos
- Python 3.8+
- pip
- (opcional) Docker
- Variables de entorno típicas: YOUTUBE_API_KEY, TRANSCRIBE_MODEL, OUTPUT_DIR

## Instalación
1. Clona el repo y entra en la carpeta:
```bash
git clone <repo-url> .
```
2. Crea y activa un entorno:
```bash
python -m venv venv
source venv/bin/activate
```
3. Instala dependencias (ajusta el fichero si no existe):
```bash
pip install -r requirements.txt
```

## Inicializar desde script
1. Supuesto: punto de entrada `main.py` o paquete `youtube_summarize.__main__`.
2. Ejemplo de ejecución directa:
```bash
# con variables de entorno en línea
YOUTUBE_API_KEY=xxx OUTPUT_DIR=./data python main.py --url "https://youtu.be/..." --mode summarize
```
3. Ejemplo de script `run.sh` (crear en la raíz):
```bash
#!/usr/bin/env bash
set -e
export YOUTUBE_API_KEY="tu_api_key"
export OUTPUT_DIR="./data"
python main.py "$@"
```
Hacer ejecutable: `chmod +x run.sh` y ejecutar `./run.sh --url "https://youtu.be/..."`.

## Inicializar desde Docker
1. Dockerfile mínimo (crear si no existe):
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV OUTPUT_DIR=/app/data
CMD ["python", "main.py"]
```
2. Build y run:
```bash
docker build -t youtube_summarize .
docker run --rm --env YOUTUBE_API_KEY=xxx -v "$(pwd)/data":/app/data youtube_summarize --url "https://youtu.be/..."
```
3. docker-compose (opcional):
```yaml
version: "3.8"
services:
    app:
        build: .
        environment:
            - YOUTUBE_API_KEY=${YOUTUBE_API_KEY}
        volumes:
            - ./data:/app/data
        command: ["--url", "https://youtu.be/..."]
```

## Notas
- Ajustar nombres de archivos/entrada según la implementación real (p. ej. `main.py`, `app.py` o paquete).
- Añadir `.env` y `.gitignore` para claves y datos grandes.
