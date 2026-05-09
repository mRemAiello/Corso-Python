from openai_setup import get_client

client = get_client()

# Text-to-Speech (TTS) e Speech-to-Text (STT)

# --- 1. Text-to-Speech: generare audio da testo ---
risposta_audio = client.audio.speech.create(
    model="tts-1",  # "tts-1" (veloce) o "tts-1-hd" (alta qualità)
    voice="nova",  # voci: alloy, echo, fable, onyx, nova, shimmer
    input="Hello, this is an example of vocal synthesis with the API of OpenAI. Python is a fantastic language for artificial intelligence."
)

# Salvare il file audio
risposta_audio.stream_to_file("output_audio.mp3")
print("Audio generato: output_audio.mp3")


# --- 2. Speech-to-Text: trascrivere audio ---
# (richiede un file audio esistente)
def trascrivi_audio(percorso_file: str) -> str:
    """Trascrive un file audio in testo."""
    with open(percorso_file, "rb") as file_audio:
        trascrizione = client.audio.transcriptions.create(
            model="whisper-1",
            file=file_audio,
            language="it"  # opzionale: specificare la lingua
        )
    return trascrizione.text


# Trascrivere l'audio appena generato
testo = trascrivi_audio("output_audio.mp3")
print(f"\nTrascrizione: {testo}")


# --- 3. Traduzione audio (qualsiasi lingua -> inglese) ---
def traduci_audio(percorso_file: str) -> str:
    """Traduce un file audio in inglese."""
    with open(percorso_file, "rb") as file_audio:
        traduzione = client.audio.translations.create(
            model="whisper-1",
            file=file_audio
        )
    return traduzione.text


traduzione = traduci_audio("output_audio.mp3")
print(f"Traduzione in inglese: {traduzione}")
