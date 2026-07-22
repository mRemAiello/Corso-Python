import asyncio
from openai_setup import get_async_client

# Client asincrono per richieste parallele
client = get_async_client()

# Sincrono
# funzione1 -> funzione2 -> funzione3

# Asincrono
# funzione1 -> 10:30
# funzione2 -> 10:01
# funzione3 -> 10:05


async def richiesta_singola(domanda: str, indice: int) -> str:
    """Esegue una singola richiesta asincrona."""
    print(f"[{indice}] Invio richiesta: {domanda[:50]}...")

    risposta = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": domanda}],
        max_tokens=100
    )

    testo = risposta.choices[0].message.content
    print(f"[{indice}] Risposta ricevuta!")
    return testo


async def streaming_asincrono():
    """Streaming con il client asincrono."""
    print("--- Streaming asincrono ---\n")

    stream = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Elenca 5 linguaggi di programmazione popolari."}
        ],
        stream=True
    )

    async for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

    print("\n")


async def richieste_parallele():
    """Esegue più richieste in parallelo per risparmiare tempo."""
    print("--- Richieste parallele ---\n")

    domande = [
        "Cos'è una lista in Python?",
        "Cos'è un dizionario in Python?",
        "Cos'è una tupla in Python?",
        "Cos'è un set in Python?",
    ]

    # Eseguire tutte le richieste in parallelo con asyncio.gather
    tasks = [richiesta_singola(d, i) for i, d in enumerate(domande)]
    risposte = await asyncio.gather(*tasks)

    print("\n--- Tutte le risposte ---\n")
    for domanda, risposta in zip(domande, risposte):
        print(f"D: {domanda}")
        print(f"R: {risposta[:100]}...\n")


async def main():
    # await streaming_asincrono()
    await richieste_parallele()


if __name__ == "__main__":
    asyncio.run(main())
