"""
Esempio avanzato: chatbot RAG (Retrieval-Augmented Generation)
che risponde a domande basandosi su documenti forniti.
"""

from openai import OpenAI

client = OpenAI()


# --- 1. Base di conoscenza simulata ---
documenti = [
    {
        "titolo": "Python - Variabili",
        "contenuto": "In Python le variabili non hanno bisogno di dichiarazione di tipo. "
                     "Si assegna un valore con l'operatore =. Esempio: x = 10, nome = 'Mario'."
    },
    {
        "titolo": "Python - Liste",
        "contenuto": "Le liste in Python sono collezioni ordinate e mutabili. "
                     "Si creano con le parentesi quadre: lista = [1, 2, 3]. "
                     "Supportano append(), remove(), sort() e slicing."
    },
    {
        "titolo": "Python - Dizionari",
        "contenuto": "I dizionari sono collezioni chiave-valore. "
                     "Si creano con le parentesi graffe: d = {'nome': 'Mario', 'età': 30}. "
                     "Accesso: d['nome']. Metodi: keys(), values(), items()."
    },
    {
        "titolo": "Python - Classi",
        "contenuto": "Le classi in Python si definiscono con la keyword class. "
                     "Il metodo __init__ è il costruttore. self è il riferimento all'istanza. "
                     "Supportano ereditarietà: class Figlio(Padre)."
    },
    {
        "titolo": "Python - File",
        "contenuto": "Per leggere un file: open('file.txt', 'r'). Per scrivere: open('file.txt', 'w'). "
                     "È buona pratica usare il context manager with. "
                     "Esempio: with open('file.txt') as f: contenuto = f.read()"
    },
]


# --- 2. Creare embeddings per i documenti ---
def crea_indice(docs):
    """Crea un indice di embeddings per i documenti."""
    testi = [f"{d['titolo']}: {d['contenuto']}" for d in docs]

    risposta = client.embeddings.create(
        model="text-embedding-3-small",
        input=testi
    )

    for i, item in enumerate(risposta.data):
        docs[i]["embedding"] = item.embedding

    return docs


def similarita_coseno(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x ** 2 for x in a) ** 0.5
    norm_b = sum(x ** 2 for x in b) ** 0.5
    return dot / (norm_a * norm_b)


# --- 3. Recuperare documenti rilevanti ---
def recupera_contesto(domanda, docs_indicizzati, top_k=2):
    """Trova i documenti più rilevanti per la domanda."""
    emb_domanda = client.embeddings.create(
        model="text-embedding-3-small",
        input=[domanda]
    ).data[0].embedding

    risultati = []
    for doc in docs_indicizzati:
        sim = similarita_coseno(emb_domanda, doc["embedding"])
        risultati.append((doc, sim))

    risultati.sort(key=lambda x: x[1], reverse=True)
    return risultati[:top_k]


# --- 4. Generare risposta con contesto ---
def rispondi_con_rag(domanda, docs_indicizzati):
    """Genera una risposta usando RAG."""
    # Recuperare contesto
    contesto_docs = recupera_contesto(domanda, docs_indicizzati)
    contesto = "\n\n".join([
        f"[{doc['titolo']}]\n{doc['contenuto']}"
        for doc, score in contesto_docs
    ])

    print(f"Documenti recuperati:")
    for doc, score in contesto_docs:
        print(f"  - {doc['titolo']} (similarità: {score:.4f})")

    # Generare risposta
    risposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"Sei un assistente che risponde SOLO basandosi sul contesto fornito. "
                           f"Se l'informazione non è nel contesto, dì che non lo sai.\n\n"
                           f"CONTESTO:\n{contesto}"
            },
            {"role": "user", "content": domanda}
        ],
        temperature=0.3
    )

    return risposta.choices[0].message.content


# --- 5. Esecuzione ---
print("Indicizzazione documenti...")
docs_indicizzati = crea_indice(documenti)
print(f"Indicizzati {len(docs_indicizzati)} documenti.\n")

# Test con domande
domande = [
    "Come si crea una lista in Python?",
    "Come funziona l'ereditarietà nelle classi?",
    "Come si legge un file in Python?",
]

for domanda in domande:
    print(f"\nDomanda: {domanda}")
    risposta = rispondi_con_rag(domanda, docs_indicizzati)
    print(f"Risposta: {risposta}\n")
    print("-" * 60)
