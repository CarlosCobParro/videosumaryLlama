# transcriber.py
from faster_whisper import WhisperModel

# Forzamos GPU
model = WhisperModel("base", device="cpu")  # usa GPU device=cuda, CPU device=cpu

def transcribe(audio_file):
    """
    Transcribe un archivo de audio y devuelve todo el texto.
    
    Parámetros:
        audio_file (str): Ruta al archivo de audio (mp3, wav, etc.)
    
    Retorna:
        str: Transcripción completa del audio
    """
    print(f"Transcribiendo {audio_file}...")

    # La función transcribe devuelve los segmentos y el tiempo de procesamiento
    segments, _ = model.transcribe(audio_file)

    # Unir todos los segmentos en un solo texto
    text = ""
    for segment in segments:
        text += segment.text + " "

    print(f"Transcripción completada ({len(text.split())} palabras).")
    return text.strip()