import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from openai import OpenAI

# Creare un client OpenAI
# La chiave API viene letta automaticamente dalla variabile d'ambiente OPENAI_API_KEY
# oppure puoi passarla direttamente: OpenAI(api_key="sk-...")
client = OpenAI()


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def extract_urls_from_sitemap(sitemap_url):
    try:
        response = requests.get(sitemap_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Errore nel recupero della sitemap: {e}")
        return []

    results = []

    try:
        # Analizza il contenuto XML della sitemap
        root = ET.fromstring(response.content)

        # Cerca gli elementi <url> e <loc> che contengono gli URL delle pagine
        for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
            results.append({"url": loc})

    except ET.ParseError as e:
        print(f"Errore nel parsing XML: {e}")

    return results


def extract_content(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Errore richiesta: {e}")
        return None

    # SOUP
    soup = BeautifulSoup(response.content, 'html.parser')

    # Estrazione del <title>
    title_tag = soup.title.string.strip() if soup.title and soup.title.string else ""

    # Estrazione del <meta name="description">
    description_tag = soup.find('meta', attrs = {'name': 'description'})
    description = description_tag.get('content', '').strip() if description_tag else ""

    # H1 e H2
    h1_tags = [h1.get_text(strip = True) for h1 in soup.find_all('h1')]
    h2_tags = [h2.get_text(strip = True) for h2 in soup.find_all('h2')]

    # List to string
    h1_tags = '\n'.join(h1_tags)
    h2_tags = '\n'.join(h2_tags)

    #
    return {'title': title_tag, 'description': description, 'h1': h1_tags, 'h2': h2_tags}


def call_gpt(question):
    # Richiesta base: una singola domanda
    risposta = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "user", "content": question}
        ]
    )
    return risposta.choices[0].message.content



# URL sito web
sitemap_url = "https://www.gedemy.it/gedemy-documentation-sitemap.xml"
urls = extract_urls_from_sitemap(sitemap_url)
for url in urls:
    try:
        # Leggo contenuto url (title, description)
        content = extract_content(url["url"])
        title = content["title"]
        description = content["description"]
        url = url["url"]
        question = f"Agisci come un esperto Articolista, dimmi come migliorare questo articolo chiamato '{title}'"
        question += f", con descrizione '{description}' e url '{url}'"
        answer = call_gpt(question)
        print(answer)

    except :
        print("Errore: ")

    break