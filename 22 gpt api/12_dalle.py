from openai_setup import get_client

client = get_client()

# Generazione e analisi di immagini con DALL-E

# --- 1. Generare un'immagine ---
risposta = client.images.generate(
    model="dall-e-3",
    prompt="Un gatto arancione seduto su una pila di libri di programmazione, "
           "stile illustrazione digitale, colori vivaci",
    size="1024x1024",
    quality="standard",  # "standard" o "hd"
    n=1
)

url_immagine = risposta.data[0].url
prompt_rivisto = risposta.data[0].revised_prompt

print(f"URL immagine: {url_immagine}")
print(f"Prompt rivisto da DALL-E: {prompt_rivisto}")

# --- 2. Variazioni di stile ---
stili = [
    "fotorealistico",
    "acquerello",
    "pixel art",
]

for stile in stili:
    print(f"\nGenerazione stile: {stile}...")
    r = client.images.generate(
        model="dall-e-3",
        prompt=f"Un paesaggio di montagna con un lago, stile {stile}",
        size="1024x1024",
        n=1
    )
    print(f"  URL: {r.data[0].url}")

# --- 3. Scaricare e salvare l'immagine ---
import urllib.request

# Scaricare la prima immagine generata (decommentare per usare)
# urllib.request.urlretrieve(url_immagine, "immagine_generata.png")
# print("\nImmagine salvata come 'immagine_generata.png'")
