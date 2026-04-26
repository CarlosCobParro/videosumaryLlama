import ollama

def summarize_chunk(text):

    prompt = f"""
    Resume en español este fragmento de un video de YouTube.
    En el caso de que sea una lista, representame la lista.
    Extrae las ideas principales en puntos.

    TEXTO:
    {text}
    """

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

def final_summary(chunk_summaries):

    combined = "\n".join(chunk_summaries)

    prompt = f"""
    A partir de estos resúmenes parciales,
    crea un resumen final claro del video.

    {combined}
    """

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]