import base64
from openai import OpenAI

client = OpenAI()

# GPT-4o può analizzare immagini (Vision)

# --- Metodo 1: immagine da URL ---
risposta_url = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Descrivi cosa vedi in questa immagine."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg"
                    }
                }
            ]
        }
    ],
    max_tokens=300
)

print("Analisi da URL:")
print(risposta_url.choices[0].message.content)


# --- Metodo 2: immagine locale (base64) ---
def analizza_immagine_locale(percorso_immagine: str, domanda: str) -> str:
    """Analizza un'immagine locale con GPT Vision."""
    with open(percorso_immagine, "rb") as f:
        immagine_base64 = base64.b64encode(f.read()).decode("utf-8")

    risposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": domanda},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{immagine_base64}"
                        }
                    }
                ]
            }
        ],
        max_tokens=500
    )
    return risposta.choices[0].message.content


# Esempio (decommentare con un percorso immagine valido):
# risultato = analizza_immagine_locale("foto.jpg", "Cosa c'è in questa foto?")
# print(risultato)
