from openai import OpenAI

client = OpenAI()

# Gestione errori e best practice per applicazioni robuste

# --- 1. Gestione errori ---
from openai import (
    APIConnectionError,
    RateLimitError,
    APIStatusError,
)
import time


def richiesta_con_retry(messaggi, max_tentativi=3):
    """Esegue una richiesta con gestione errori e retry automatico."""
    for tentativo in range(max_tentativi):
        try:
            risposta = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messaggi,
                timeout=30  # timeout in secondi
            )
            return risposta.choices[0].message.content

        except APIConnectionError:
            print(f"Tentativo {tentativo + 1}: errore di connessione, riprovo...")
            time.sleep(2 ** tentativo)  # backoff esponenziale

        except RateLimitError:
            print(f"Tentativo {tentativo + 1}: rate limit raggiunto, attendo...")
            time.sleep(2 ** tentativo * 5)

        except APIStatusError as e:
            print(f"Errore API: {e.status_code} - {e.message}")
            if e.status_code >= 500:
                time.sleep(2 ** tentativo)
                continue
            raise  # errori 4xx non ritentabili

    raise Exception("Numero massimo di tentativi raggiunto")


# Test
risultato = richiesta_con_retry([
    {"role": "user", "content": "Ciao!"}
])
print(f"Risposta: {risultato}")


# --- 2. Contare i token prima dell'invio ---
# pip install tiktoken
import tiktoken


def conta_token(messaggi, modello="gpt-4o-mini"):
    """Stima il numero di token nei messaggi."""
    try:
        encoding = tiktoken.encoding_for_model(modello)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")

    num_token = 0
    for messaggio in messaggi:
        num_token += 4  # overhead per messaggio
        for chiave, valore in messaggio.items():
            num_token += len(encoding.encode(valore))
    num_token += 2  # overhead finale
    return num_token


messaggi_test = [
    {"role": "system", "content": "Sei un assistente utile."},
    {"role": "user", "content": "Spiegami la ricorsione in Python con un esempio."}
]

token_stimati = conta_token(messaggi_test)
print(f"\nToken stimati nel prompt: {token_stimati}")


# --- 3. Troncare la cronologia per rispettare il limite token ---
def tronca_cronologia(messaggi, max_token=4000):
    """Rimuove i messaggi più vecchi se si supera il limite di token."""
    while conta_token(messaggi) > max_token and len(messaggi) > 2:
        # Mantieni sempre il system message (primo) e l'ultimo messaggio
        messaggi.pop(1)
    return messaggi
