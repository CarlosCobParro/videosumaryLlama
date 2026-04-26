# downloader.py
import yt_dlp
import os

def download_audio(url, output_filename="audio"):
    """
    Descarga el audio de un video de YouTube y lo guarda como MP3.
    
    Parámetros:
        url (str): URL del video de YouTube.
        output_filename (str): Nombre del archivo de salida (por defecto "audio.mp3").
    
    Retorna:
        str: Ruta del archivo descargado.
    """
    # Configuración de yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_filename,  # nombre del archivo de salida
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # convertir a mp3
            'preferredquality': '192',
        }],
        'quiet': False,  # True para no mostrar logs
        'no_warnings': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Descargando audio de: {url}")
        ydl.download([url])
    
    # Verificar que el archivo existe
    if os.path.exists(output_filename+'.mp3'):
        print(f"Audio descargado en: {output_filename}")
        return output_filename
    else:
        raise FileNotFoundError(f"No se pudo descargar el audio de {url}")