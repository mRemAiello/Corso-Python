import json
from openai_setup import get_client

client = get_client()


# Function Calling: GPT può "chiamare" funzioni Python
# GPT non esegue il codice, ma indica quale funzione chiamare e con quali parametri

# 1. Definire le funzioni disponibili
def get_meteo(citta: str, unita: str = "celsius") -> str:
    """Funzione simulata che restituisce il meteo."""
    meteo_finto = {
        "roma": {"temperatura": 22, "condizioni": "soleggiato"},
        "milano": {"temperatura": 18, "condizioni": "nuvoloso"},
        "napoli": {"temperatura": 25, "condizioni": "soleggiato"},
    }
    dati = meteo_finto.get(citta.lower(), {"temperatura": 20, "condizioni": "variabile"})
    return json.dumps({"citta": citta, **dati, "unita": unita})


# 2. Descrivere le funzioni per GPT
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_meteo",
            "description": "Ottieni le condizioni meteo attuali per una città",
            "parameters": {
                "type": "object",
                "properties": {
                    "citta": {
                        "type": "string",
                        "description": "Il nome della città, es. 'Roma'"
                    },
                    "unita": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Unità di misura della temperatura"
                    }
                },
                "required": ["citta"]
            }
        }
    }
]

# 3. Inviare la richiesta con le funzioni disponibili
messaggi = [
    {"role": "user", "content": "Che tempo fa a Palermo oggi?"}
]

risposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messaggi,
    tools=tools,
    tool_choice="auto"  # GPT decide se usare una funzione
)

messaggio = risposta.choices[0].message

# 4. Controllare se GPT vuole chiamare una funzione
if messaggio.tool_calls:
    for tool_call in messaggio.tool_calls:
        nome_funzione = tool_call.function.name
        argomenti = json.loads(tool_call.function.arguments)

        print(f"GPT vuole chiamare: {nome_funzione}({argomenti})")

        # 5. Eseguire la funzione
        if nome_funzione == "get_meteo":
            risultato = get_meteo(**argomenti)

        # 6. Inviare il risultato a GPT
        messaggi.append(messaggio)
        messaggi.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": risultato
        })

    # 7. Ottenere la risposta finale
    risposta_finale = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messaggi,
        tools=tools
    )

    print(f"Messaggi inviati all'IA: {messaggi}")
    print(f"\nRisposta: {risposta_finale.choices[0].message.content}")
else:
    print(risposta.choices[0].message.content)
