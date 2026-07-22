import json
from openai_setup import get_client

client = get_client()


# Structured Output: forzare GPT a rispondere in formato JSON strutturato
# Utile per integrare le risposte in applicazioni

# classe Utente -> nome, cognome, eta
# {
#     "utente_1":
#     {
#      "nome": "Mirko", "cognome": "Aiello", "eta" : "35"
#     }
# }

# --- Metodo 1: response_format con json_object ---
risposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Rispondi sempre in formato JSON valido."
        },
        {
            "role": "user",
            "content": "Dammi 10 capitali mondiali con il loro paese, popolazione approssimativa "
                       "e il continente di cui fanno parte."
        }
    ],
    response_format={"type": "json_object"}
)

dati = json.loads(risposta.choices[0].message.content)
print("Risposta JSON:")
print(json.dumps(dati, indent=2, ensure_ascii=False))

# --- Metodo 2: Structured Output con Pydantic (raccomandato) ---
from pydantic import BaseModel


class Capitale(BaseModel):
    capitale: str
    paese: str
    popolazione: int
    continente: str


class ListaCapitali(BaseModel):
    capitali: list[Capitale]


risposta_strutturata = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Rispondi con i dati richiesti."
        },
        {
            "role": "user",
            "content": "Dammi 10 capitali mondiali con il loro paese, popolazione approssimativa "
                       "e il continente di cui fanno parte."
        }
    ],
    response_format=ListaCapitali
)

risultato = risposta_strutturata.choices[0].message.parsed
print("\nRisposta strutturata con Pydantic:")
for cap in risultato.capitali:
    print(f"  {cap.capitale} ({cap.paese}) - {cap.popolazione:,} abitanti, continente: {cap.continente}")
