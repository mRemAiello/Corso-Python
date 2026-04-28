from openai_setup import get_client

client = get_client()

# Embeddings: rappresentazioni numeriche del testo
# Utili per: ricerca semantica, clustering, raccomandazioni

# --- Creare embeddings ---
testi = [
    "Il gatto dorme sul divano",
    "Il cane gioca nel parco",
    "Python è un linguaggio di programmazione",
    "Il felino riposa sul sofà",  # simile al primo!
]

risposta = client.embeddings.create(
    model="text-embedding-3-small",
    input=testi
)

embeddings = [item.embedding for item in risposta.data]
print(f"Dimensione di ogni embedding: {len(embeddings[0])}")


# --- Calcolare la similarità tra testi ---
def similarita_coseno(vec_a, vec_b):
    """Calcola la similarità del coseno tra due vettori."""
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = sum(a ** 2 for a in vec_a) ** 0.5
    norm_b = sum(b ** 2 for b in vec_b) ** 0.5
    return dot / (norm_a * norm_b)


print("\nSimilarità tra le frasi:")
for i in range(len(testi)):
    for j in range(i + 1, len(testi)):
        sim = similarita_coseno(embeddings[i], embeddings[j])
        print(f'  "{testi[i]}" <-> "{testi[j]}"')
        print(f"  Similarità: {sim:.4f}\n")


# --- Ricerca semantica ---
def ricerca_semantica(query: str, documenti: list[str], top_k: int = 2) -> list[tuple]:
    """Cerca i documenti più simili alla query."""
    # Creare embedding per query e documenti insieme
    tutti = [query] + documenti
    risposta = client.embeddings.create(
        model="text-embedding-3-small",
        input=tutti
    )
    emb = [item.embedding for item in risposta.data]
    emb_query = emb[0]
    emb_docs = emb[1:]

    # Calcolare similarità
    risultati = []
    for i, emb_doc in enumerate(emb_docs):
        sim = similarita_coseno(emb_query, emb_doc)
        risultati.append((documenti[i], sim))

    risultati.sort(key=lambda x: x[1], reverse=True)
    return risultati[:top_k]


documenti = [
    "La pizza margherita è nata a Napoli",
    "Python supporta la programmazione orientata agli oggetti",
    "Il Colosseo è a Roma",
    "Le liste in Python sono strutture dati mutabili",
    "La pasta alla carbonara è un piatto romano",
]

query = "linguaggio di programmazione"
risultati = ricerca_semantica(query, documenti)

print(f'\nRicerca per: "{query}"')
for doc, score in risultati:
    print(f"  [{score:.4f}] {doc}")