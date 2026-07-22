from openai_setup import get_client

client = get_client()

# I messaggi hanno 3 ruoli principali:
# - "system": istruzioni per il comportamento dell'assistente
# - "user": messaggi dell'utente
# - "assistant": risposte precedenti dell'assistente (per contesto)

# messages = [....]
# singolo elemento -> { "role": "system", "content": "contenuto" }

risposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Sei un insegnante di informatica italiano, esperto in programmazione. "
                       "Rispondi in modo semplice e con esempi pratici."
                       "Rispondi in maniera sintetica, massimo 100 parole."
        },
        {
            "role": "user",
            "content": "Cosa sono le variabili in programmazione?"
        }
    ]
)

print(risposta.choices[0].message.content)