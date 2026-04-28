from openai_setup import get_client

client = get_client()

# Parametri principali per controllare la generazione del testo

risposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Sei esperto in matematica."},
        {"role": "user", "content": "Parlami della congettura Yau-Tian-Donaldson"}
    ],

    # temperature: controlla la creatività (0.0 = deterministico, 2.0 = molto creativo)
    temperature=1.0,

    # max_tokens: limite massimo di token nella risposta
    max_tokens=500,

    # top_p: campionamento nucleus (alternativa a temperature)
    # top_p=0.9,

    # frequency_penalty: penalizza parole già usate (-2.0 a 2.0)
    frequency_penalty=0.5,

    # presence_penalty: incoraggia argomenti nuovi (-2.0 a 2.0)
    presence_penalty=0.3,
)

print(risposta.choices[0].message.content)

# --- Esempio: risposta deterministica (temperature=0) ---
print("\n--- Risposta deterministica ---\n")

risposta_det = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Sei esperto in matematica."},
        {"role": "user", "content": "Parlami della congettura Yau-Tian-Donaldson"}
    ],
    temperature=0,
)

print(risposta_det.choices[0].message.content)
