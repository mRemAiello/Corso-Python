import os
from pathlib import Path

from dotenv import load_dotenv
from openai import AsyncOpenAI, OpenAI

# Carica il file .env dalla root del progetto, indipendentemente dalla cartella di avvio.
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")


def _get_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY non trovata. Imposta la chiave nel file .env alla root del progetto."
        )
    return api_key


def get_client() -> OpenAI:
    return OpenAI(api_key=_get_api_key())


def get_async_client() -> AsyncOpenAI:
    return AsyncOpenAI(api_key=_get_api_key())
