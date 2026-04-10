# pip install openai

from openai import OpenAI

# Creare un client OpenAI
# La chiave API viene letta automaticamente dalla variabile d'ambiente OPENAI_API_KEY
# oppure puoi passarla direttamente: OpenAI(api_key="sk-...")
client = OpenAI()

# Richiesta base: una singola domanda
risposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Ciao! Spiegami cos'è Python in 2 frasi."}
    ]
)

# Stampare la risposta
print(risposta.choices[0].message.content)

# Informazioni sull'utilizzo dei token
print(f"\nToken usati - Prompt: {risposta.usage.prompt_tokens}, "
      f"Risposta: {risposta.usage.completion_tokens}, "
      f"Totale: {risposta.usage.total_tokens}")
