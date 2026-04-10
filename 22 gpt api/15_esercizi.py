"""
Esercizi sulle API di GPT
"""

# --- ESERCIZIO 1 (Base) ---
# Crea un programma che chiede all'utente un argomento
# e genera un riassunto di 3 frasi su quell'argomento.
# Usa temperature=0.3 per risposte precise.


# --- ESERCIZIO 2 (Base) ---
# Crea un traduttore che accetta una frase e una lingua di destinazione,
# e restituisce la traduzione usando GPT.
# Esempio: "Ciao mondo" -> spagnolo -> "Hola mundo"


# --- ESERCIZIO 3 (Intermedio) ---
# Crea un chatbot a tema che:
# - All'avvio chiede all'utente di scegliere un personaggio (es. pirata, scienziato, chef)
# - Imposta il system message in base alla scelta
# - Mantiene la conversazione con cronologia dei messaggi


# --- ESERCIZIO 4 (Intermedio) ---
# Crea un programma che legge un file .py dal disco e chiede a GPT di:
# 1. Analizzare il codice
# 2. Trovare possibili bug
# 3. Suggerire miglioramenti
# Usa response_format=json_object per strutturare l'output.


# --- ESERCIZIO 5 (Intermedio) ---
# Implementa un sistema di streaming che:
# - Mostra la risposta token per token
# - Conta i caratteri ricevuti in tempo reale
# - Alla fine mostra statistiche (tempo totale, caratteri/secondo)
# Suggerimento: usa il modulo time per misurare i tempi.


# --- ESERCIZIO 6 (Avanzato) ---
# Crea un assistente con function calling che può:
# - Calcolare operazioni matematiche (somma, media, fattoriale)
# - Generare numeri casuali in un range
# - Convertire temperature (Celsius <-> Fahrenheit)
# L'utente interagisce in linguaggio naturale.


# --- ESERCIZIO 7 (Avanzato) ---
# Costruisci un mini sistema RAG:
# - Leggi tutti i file .py da una cartella del corso
# - Crea embeddings per ogni file
# - Permetti all'utente di fare domande sul codice
# - Recupera i file più rilevanti e genera una risposta contestualizzata
