from openai import OpenAI

client = OpenAI()

# Streaming: ricevere la risposta token per token in tempo reale
# Utile per interfacce utente reattive (come ChatGPT)

print("Risposta in streaming:\n")

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Parlami di Numpy."}
    ],
    stream=True  # Abilita lo streaming
)

# Iterare sui chunk della risposta
testo_completo = ""
for chunk in stream:
    # Ogni chunk contiene un delta (frammento) della risposta
    delta = chunk.choices[0].delta

    if delta.content is not None:
        print(delta.content, end="", flush=True)
        testo_completo += delta.content

print("\n\n--- Fine dello streaming ---")
print(f"Lunghezza risposta: {len(testo_completo)} caratteri")
