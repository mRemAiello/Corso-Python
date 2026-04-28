from openai import OpenAI

client = OpenAI()

# Simulare una conversazione multi-turno
# GPT non ha memoria: bisogna inviare tutta la cronologia ogni volta

messaggi = [
    {"role": "system", "content": "Sei un assistente esperto di cucina italiana."}
]

print("Chat con GPT (scrivi 'esci' per uscire)\n")

while True:
    testo = input("Tu: ")
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

    #
    file = open("risposte_conversazione.txt", "w")
    for elemento in messaggi:
        ruolo = elemento["role"]
        messaggio = elemento["content"]
        file.write(f"Role: {ruolo}\n")
        file.write(f"{messaggio}\n\n")
    file.close()
