from openai import OpenAI

client = OpenAI()

# I messaggi hanno 3 ruoli principali:
# - "system": istruzioni per il comportamento dell'assistente
# - "user": messaggi dell'utente
# - "assistant": risposte precedenti dell'assistente (per contesto)

risposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Sei un insegnante di informatica italiano. "
                       "Rispondi in modo semplice e con esempi pratici."
        },
        {
            "role": "user",
            "content": "Cosa sono le variabili in programmazione?"
        }
    ]
)

print(risposta.choices[0].message.content)
