from openai_setup import get_client

client = get_client()

# Simulare una conversazione multi-turno
# GPT non ha memoria: bisogna inviare tutta la cronologia ogni volta

system = "Sei un assistente esperto di cucina italiana.\n"
system += "Rispondi in maniera sintetica e diretta, non superare le 100 parole.\n"
system += "Qualora ti venga posta una domanda NON relativa alla cucina, rispondi che non hai conoscenze in merito"

messaggi = [
    {"role": "system", "content": system}
]

print("Chat con GPT (scrivi 'esci' per uscire)\n")

while True:
    testo = input("La tua richiesta: ")
    if testo.lower() == "esci":
        break

    # Aggiungere il messaggio dell'utente alla cronologia
    messaggi.append({"role": "user", "content": testo})

    risposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messaggi
    )

    contenuto = risposta.choices[0].message.content

    # Aggiungere la risposta dell'assistente alla cronologia
    messaggi.append({"role": "assistant", "content": contenuto})

    print(f"\nAssistente: {contenuto}\n")

    print(f"\nToken usati - Prompt: {risposta.usage.prompt_tokens}, "
          f"Risposta: {risposta.usage.completion_tokens}, "
          f"Totale: {risposta.usage.total_tokens}")

    #
    file = open("risposte_conversazione.txt", "w")
    for elemento in messaggi:
        ruolo = elemento["role"]
        messaggio = elemento["content"]
        file.write(f"Role: {ruolo}\n")
        file.write(f"{messaggio}\n\n")
    file.close()
