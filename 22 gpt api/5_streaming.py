from openai_setup import get_client

client = get_client()

print("Risposta in streaming:\n")

domanda = input("Scrivi la domanda da porre all'IA: ")

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": (
                "Rispondi come un esperto di programmazione. "
                "Rispondi in maniera diretta senza ripetere concetti."
            ),
        },
        {"role": "user", "content": domanda},
    ],
    stream=True,
    stream_options={"include_usage": True},
)

testo_completo = ""
usage = None

for chunk in stream:
    # L'ultimo chunk contiene l'usage
    if chunk.usage is not None:
        usage = chunk.usage

    if chunk.choices:
        delta = chunk.choices[0].delta
        if delta.content is not None:
            print(delta.content, end="", flush=True)
            testo_completo += delta.content

print("\n\n--- Fine dello streaming ---")
print(f"Lunghezza risposta: {len(testo_completo)} caratteri")

if usage:
    print(
        f"\nToken usati - "
        f"Prompt: {usage.prompt_tokens}, "
        f"Risposta: {usage.completion_tokens}, "
        f"Totale: {usage.total_tokens}"
    )
else:
    print("\nUsage non disponibile.")