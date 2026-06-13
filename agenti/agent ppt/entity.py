import json
import re
from pathlib import Path
from collections import defaultdict

import spacy


class EntityDetector:
    def __init__(self, language_model: str = "en_core_web_lg"):
        try:
            self.nlp = spacy.load(language_model)
        except OSError:
            raise RuntimeError(
                f"Modello spaCy non trovato: {language_model}\n"
                f"Installa con:\n"
                f"python -m spacy download {language_model}"
            )

        self.patterns = {
            "EMAIL": re.compile(
                r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
            ),
            "PHONE": re.compile(
                r"(?:(?:\+|00)\d{1,3}[\s.-]?)?"
                r"(?:\(?\d{2,4}\)?[\s.-]?)?"
                r"\d{3,4}[\s.-]?\d{3,4}\b"
            ),
            "URL": re.compile(
                r"\b(?:https?://|www\.)[^\s<>()]+",
                re.IGNORECASE
            ),
            "DOMAIN": re.compile(
                r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"
            ),
            "VAT_OR_TAX_CODE": re.compile(
                r"\b(?:P\.?\s?IVA|VAT|CF|Cod\.?\s?Fisc\.?)"
                r"[:\s]*[A-Z0-9]{8,16}\b",
                re.IGNORECASE
            ),
            "PROJECT_CODE": re.compile(
                r"\b[A-Z]{2,6}[-_]\d{2,6}\b"
            ),
        }

        self.company_suffixes = [
            "srl", "s.r.l.", "spa", "s.p.a.", "sas", "s.a.s.",
            "snc", "s.n.c.", "ltd", "limited", "inc", "corp",
            "corporation", "gmbh", "llc", "group", "holding"
        ]

    def detect_from_text(self, text: str):
        entities = []

        if not text or not text.strip():
            return entities

        # Regex detection
        for entity_type, pattern in self.patterns.items():
            for match in pattern.finditer(text):
                entities.append({
                    "text": match.group().strip(),
                    "type": entity_type,
                    "start": match.start(),
                    "end": match.end(),
                    "method": "regex"
                })

        # spaCy NER
        doc = self.nlp(text)

        for ent in doc.ents:
            mapped_type = self.map_spacy_label(ent.label_)

            if mapped_type:
                entities.append({
                    "text": ent.text.strip(),
                    "type": mapped_type,
                    "start": ent.start_char,
                    "end": ent.end_char,
                    "method": "spacy",
                    "original_label": ent.label_
                })

        # Company heuristic
        entities.extend(self.detect_company_names(text))

        return self.deduplicate_entities(entities)

    def map_spacy_label(self, label: str):
        mapping = {
            "PER": "PERSON",
            "PERSON": "PERSON",
            "ORG": "COMPANY",
            "GPE": "LOCATION",
            "LOC": "LOCATION",
            "PRODUCT": "PRODUCT",
            "MISC": "MISC"
        }

        return mapping.get(label)

    def detect_company_names(self, text: str):
        entities = []

        for suffix in self.company_suffixes:
            pattern = re.compile(
                rf"\b[A-ZÀ-Ú][A-Za-zÀ-ÿ0-9&.'’\-\s]{{1,60}}\s+{re.escape(suffix)}\b",
                re.IGNORECASE
            )

            for match in pattern.finditer(text):
                entities.append({
                    "text": match.group().strip(),
                    "type": "COMPANY",
                    "start": match.start(),
                    "end": match.end(),
                    "method": "company_suffix_heuristic"
                })

        return entities

    def should_keep_entity(self, entity):
        text = entity["text"].strip()
        entity_type = entity["type"]

        if entity_type in {"LOCATION", "COMPANY", "PERSON"} and len(text) <= 2:
            return False

        blacklist = {
            "us", "it", "ai", "hr", "ui", "ux", "ok", "no",
            "as", "to", "in", "on", "of", "by"
        }

        if text.lower() in blacklist:
            return False

        return True

    def deduplicate_entities(self, entities):
        seen = set()
        clean = []

        for entity in entities:
            if not self.should_keep_entity(entity):
                continue

            key = (
                entity["text"].lower(),
                entity["type"],
                entity["start"],
                entity["end"]
            )

            if key not in seen:
                seen.add(key)
                clean.append(entity)

        return clean


def collect_text_blocks(parsed_pptx_json: dict):
    blocks = []

    for slide in parsed_pptx_json.get("slides", []):
        slide_number = slide.get("slide_number")

        for text in slide.get("texts", []):
            blocks.append({
                "source": "slide_text",
                "slide_number": slide_number,
                "text": text
            })

        for table_index, table in enumerate(slide.get("tables", []), start=1):
            for row_index, row in enumerate(table, start=1):
                for col_index, cell_text in enumerate(row, start=1):
                    if cell_text:
                        blocks.append({
                            "source": "table_cell",
                            "slide_number": slide_number,
                            "table_index": table_index,
                            "row_index": row_index,
                            "col_index": col_index,
                            "text": cell_text
                        })

        for note in slide.get("notes", []):
            blocks.append({
                "source": "speaker_notes",
                "slide_number": slide_number,
                "text": note
            })

    for metadata_name, metadata_text in parsed_pptx_json.get("metadata", {}).items():
        blocks.append({
            "source": "metadata",
            "metadata_file": metadata_name,
            "text": metadata_text
        })

    for link in parsed_pptx_json.get("links", []):
        blocks.append({
            "source": "embedded_link",
            "source_file": link.get("source_file"),
            "text": link.get("target", "")
        })

    return blocks


def generate_anonymization_map(all_entities):
    counters = defaultdict(int)
    anonymization_map = {}

    priority_labels = {
        "PERSON": "Persona",
        "COMPANY": "Azienda",
        "EMAIL": "email",
        "PHONE": "telefono",
        "URL": "url",
        "DOMAIN": "dominio",
        "LOCATION": "Luogo",
        "PRODUCT": "Prodotto",
        "PROJECT_CODE": "Progetto",
        "VAT_OR_TAX_CODE": "Codice fiscale/P.IVA",
        "MISC": "Entità"
    }

    sorted_entities = sorted(
        all_entities,
        key=lambda e: len(e["text"]),
        reverse=True
    )

    for entity in sorted_entities:
        original = entity["text"].strip()
        entity_type = entity["type"]

        if not original:
            continue

        normalized_key = original.lower()

        if normalized_key in anonymization_map:
            continue

        counters[entity_type] += 1
        label = priority_labels.get(entity_type, "Entità")

        if entity_type == "EMAIL":
            replacement = f"email_{counters[entity_type]}@example.com"
        elif entity_type == "PHONE":
            replacement = f"+39 000 000 000{counters[entity_type]}"
        elif entity_type == "URL":
            replacement = f"https://example{counters[entity_type]}.com"
        elif entity_type == "DOMAIN":
            replacement = f"example{counters[entity_type]}.com"
        else:
            replacement = f"{label} {counters[entity_type]}"

        anonymization_map[normalized_key] = {
            "original": original,
            "replacement": replacement,
            "type": entity_type
        }

    return anonymization_map


def detect_sensitive_entities(
    input_json_path: str,
    output_dir: str = "pptx_detection",
    language_model: str = "it_core_news_lg"
):
    input_json_path = Path(input_json_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(input_json_path, "r", encoding="utf-8") as f:
        parsed_pptx = json.load(f)

    detector = EntityDetector(language_model=language_model)
    text_blocks = collect_text_blocks(parsed_pptx)

    all_entities = []
    detections_by_block = []

    for block_index, block in enumerate(text_blocks, start=1):
        text = block.get("text", "")
        entities = detector.detect_from_text(text)

        if entities:
            detections_by_block.append({
                "block_index": block_index,
                "location": {
                    k: v for k, v in block.items() if k != "text"
                },
                "text": text,
                "entities": entities
            })

            for entity in entities:
                enriched_entity = dict(entity)
                enriched_entity["block_index"] = block_index
                enriched_entity["location"] = {
                    k: v for k, v in block.items() if k != "text"
                }
                all_entities.append(enriched_entity)

    anonymization_map = generate_anonymization_map(all_entities)

    result = {
        "source_file": parsed_pptx.get("file_name"),
        "total_blocks_scanned": len(text_blocks),
        "total_entities_found": len(all_entities),
        "detections": detections_by_block,
        "anonymization_map": anonymization_map
    }

    output_path = output_dir / "sensitive_entities.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    map_path = output_dir / "anonymization_map.json"

    with open(map_path, "w", encoding="utf-8") as f:
        json.dump(anonymization_map, f, indent=2, ensure_ascii=False)

    return result