# PDF Anonymizer

Script Python per anonimizzare PDF in modo coerente su tutto il file:
- sostituisce nomi, aziende, vie, citta e altri dati sensibili con placeholder (es. `Persona 1`, `Citta 1`);
- mantiene la coerenza: la stessa entita viene sempre sostituita con lo stesso placeholder;
- applica un blur forte alle immagini presenti nel PDF.

## Requisiti

```bash
pip install -r requirements.txt
python -m spacy download it_core_news_sm
```

Nota: se non e disponibile un modello spaCy, lo script funziona comunque in modalita regex-only (meno accurata su nomi/aziende/citta).

## Uso

```bash
python pdf_anonymizer.py input.pdf output_anon.pdf --verbose
```

## Interfaccia grafica

```bash
python pdf_anonymizer_gui.py
```

Funzioni GUI:
- selezione file input/output
- toggle blur immagini
- configurazione raggio blur
- avvio anonimizzazione con finestra di stato

Opzioni:
- `--blur-radius`: intensita blur immagini (default `18.0`)
- `--no-image-blur`: disattiva il blur delle immagini
- `--verbose`: log dettagliati

## Entita gestite

- PERSON -> `Persona N`
- COMPANY -> `Azienda N`
- CITY -> `Citta N`
- STREET -> `Via N`
- EMAIL -> `Email N`
- PHONE -> `Telefono N`
- CODICE_FISCALE -> `CodiceFiscale N`
- PARTITA_IVA -> `PartitaIVA N`
- IBAN -> `IBAN N`
- DATE -> `Data N`

## Limiti pratici

- PDF con testo rasterizzato (scansioni) richiedono OCR prima dell'anonimizzazione testuale.
- Il blur immagini viene applicato in overlay sui riquadri immagine rilevati nella pagina.
