# pip install openai

from openai import OpenAI

# Creare un client OpenAI
# La chiave API viene letta automaticamente dalla variabile d'ambiente OPENAI_API_KEY
# oppure puoi passarla direttamente: OpenAI(api_key="sk-...")
client = OpenAI()

question = input("Scrivi la domanda da fare a gpt")
question += "\nFornisci la risposta in JSON"

# Richiesta base: una singola domanda
risposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": question}
    ]
)

# I messaggi sono liste di dizionari
# 0 -> Role: user, content: Parlami di Numpy
# 1 -> Role: agent, content: Risposta di gpt
# 2 ->

# Stampare la risposta
print(risposta.choices[0].message.role)

stringa = risposta.choices[0].message.content
file = open("risposte.txt", "a", encoding="utf-8")
file.write(stringa)
file.close()

# Informazioni sull'utilizzo dei token
print(f"\nToken usati - Prompt: {risposta.usage.prompt_tokens}, "
      f"Risposta: {risposta.usage.completion_tokens}, "
      f"Totale: {risposta.usage.total_tokens}")
