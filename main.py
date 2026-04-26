from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles

from downloader import download_audio
from transcriber import transcribe
from chunker import split_text
from summarizer import summarize_chunk, final_summary

import os

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):

    await ws.accept()

    data = await ws.receive_json()
    url = data["url"]

    def log(msg):
        print(msg)
        return ws.send_text(msg)

    try:

        await log("📥 Descargando audio...")
        audio_file = download_audio(url)

        await log("🧠 Transcribiendo...")
        text = transcribe(audio_file + ".mp3")

        await log("✂️ Dividiendo texto...")
        chunks = split_text(text)

        summaries = []

        for i, chunk in enumerate(chunks, 1):
            await log(f"📝 Resumiendo fragmento {i}/{len(chunks)}")
            summaries.append(summarize_chunk(chunk))

        await log("📊 Generando resumen final...")
        summary = final_summary(summaries)

        await ws.send_json({
            "type": "result",
            "summary": summary
        })

    finally:

        if os.path.exists(audio_file):
            os.remove(audio_file)

        await log("✅ Proceso terminado")


app.mount("/", StaticFiles(directory="static", html=True), name="static")