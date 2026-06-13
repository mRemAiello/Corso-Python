#!/usr/bin/env python3
"""Anonymize sensitive content in PDF files.

Features:
- Replaces PII references with consistent placeholders across the whole PDF.
- Applies a strong blur over embedded images.

Usage:
    python pdf_anonymizer.py input.pdf output.pdf
"""

from __future__ import annotations

import argparse
import io
import logging
import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

import fitz  # PyMuPDF
from PIL import Image, ImageFilter

try:
    import spacy
except ImportError:  # pragma: no cover
    spacy = None


LOGGER = logging.getLogger("pdf_anonymizer")


@dataclass(frozen=True)
class Entity:
    text: str
    kind: str


@dataclass
class EntityBucket:
    kind: str
    forms: Set[str]


@dataclass(frozen=True)
class TextStyle:
    fontname: str
    fontsize: float
    color: Tuple[float, float, float]


# Patterns for common sensitive information.
REGEX_PATTERNS: Sequence[Tuple[str, str]] = (
    ("EMAIL", r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    (
        "PHONE",
        r"\b(?:\+?\d{1,3}[\s.-]?)?(?:\(?\d{2,4}\)?[\s.-]?)?\d{3,4}[\s.-]?\d{3,4}\b",
    ),
    ("CODICE_FISCALE", r"\b[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]\b"),
    ("PARTITA_IVA", r"\b(?:IT)?\d{11}\b"),
    (
        "IBAN",
        r"\bIT\d{2}[A-Z]\d{10}[A-Z0-9]{12}\b",
    ),
    (
        "STREET",
        r"\b(?:via|viale|piazza|corso|strada|largo|vicolo)\s+[A-Z][\w'.-]*(?:\s+[A-Z][\w'.-]*)*\b",
    ),
    ("DATE", r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b"),
)


NER_LABEL_MAP = {
    "PER": "PERSON",
    "PERSON": "PERSON",
    "ORG": "COMPANY",
    "LOC": "CITY",
    "GPE": "CITY",
}


PLACEHOLDER_PREFIX = {
    "PERSON": "Persona",
    "COMPANY": "Azienda",
    "CITY": "Citta",
    "STREET": "Via",
    "EMAIL": "Email",
    "PHONE": "Telefono",
    "CODICE_FISCALE": "CodiceFiscale",
    "PARTITA_IVA": "PartitaIVA",
    "IBAN": "IBAN",
    "DATE": "Data",
    "SENSITIVE": "DatoSensibile",
}


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).lower()


def load_ner_model() -> Optional[object]:
    """Load the best available spaCy NER model."""
    if spacy is None:
        LOGGER.warning("spaCy not installed: running with regex-only detection.")
        return None

    model_candidates = [
        "it_core_news_lg",
        "it_core_news_md",
        "it_core_news_sm",
        "xx_ent_wiki_sm",
    ]
    for model_name in model_candidates:
        try:
            nlp = spacy.load(model_name)
            LOGGER.info("Loaded NER model: %s", model_name)
            return nlp
        except Exception:
            continue

    LOGGER.warning(
        "No spaCy NER model available. Install one with: python -m spacy download it_core_news_sm"
    )
    return None


def detect_regex_entities(text: str) -> List[Entity]:
    results: List[Entity] = []
    for kind, pattern in REGEX_PATTERNS:
        flags = re.IGNORECASE if kind in {"EMAIL", "PHONE", "STREET"} else 0
        for match in re.finditer(pattern, text, flags):
            matched = match.group(0).strip()
            if len(matched) < 2:
                continue
            results.append(Entity(matched, kind))
    return results


def detect_ner_entities(text: str, nlp: Optional[object]) -> List[Entity]:
    if nlp is None:
        return []

    doc = nlp(text)
    results: List[Entity] = []
    for ent in doc.ents:
        mapped = NER_LABEL_MAP.get(ent.label_)
        if not mapped:
            continue

        candidate = ent.text.strip()
        if len(candidate) < 2:
            continue

        # Skip all-uppercase short acronyms often found in tables.
        if candidate.isupper() and len(candidate) <= 3:
            continue

        results.append(Entity(candidate, mapped))
    return results


def collect_entities_from_pdf(doc: fitz.Document, nlp: Optional[object]) -> Dict[str, EntityBucket]:
    """Return normalized_text -> entity bucket (kind + observed forms)."""
    discovered: Dict[str, EntityBucket] = {}

    for page in doc:
        page_text = page.get_text("text")
        entities = detect_regex_entities(page_text)
        entities.extend(detect_ner_entities(page_text, nlp))

        for entity in entities:
            key = normalize_text(entity.text)
            if not key:
                continue

            existing = discovered.get(key)
            if existing is None:
                discovered[key] = EntityBucket(kind=entity.kind, forms={entity.text.strip()})
            else:
                # Keep the more specific STREET kind if present.
                if existing.kind == "CITY" and entity.kind == "STREET":
                    existing.kind = "STREET"
                existing.forms.add(entity.text.strip())

    return discovered


def build_placeholder_map(entity_buckets: Dict[str, EntityBucket]) -> Dict[str, str]:
    counters: Dict[str, int] = {}
    placeholder_map: Dict[str, str] = {}

    for key, bucket in sorted(entity_buckets.items(), key=lambda item: (-len(item[0]), item[0])):
        kind = bucket.kind
        normalized_kind = kind if kind in PLACEHOLDER_PREFIX else "SENSITIVE"
        counters[normalized_kind] = counters.get(normalized_kind, 0) + 1
        prefix = PLACEHOLDER_PREFIX[normalized_kind]
        placeholder_map[key] = f"{prefix} {counters[normalized_kind]}"

    return placeholder_map


def build_search_replacements(
    entity_buckets: Dict[str, EntityBucket], placeholder_map: Dict[str, str]
) -> List[Tuple[str, str]]:
    replacements: Dict[str, str] = {}

    for normalized, bucket in entity_buckets.items():
        replacement = placeholder_map.get(normalized)
        if replacement is None:
            continue

        variants = set(bucket.forms)
        variants.add(normalized)
        variants.add(normalized.title())
        variants.add(normalized.upper())

        for variant in variants:
            cleaned = variant.strip()
            if len(cleaned) < 2:
                continue
            replacements[cleaned] = replacement

    return sorted(replacements.items(), key=lambda item: len(item[0]), reverse=True)


def intersects_any(rect: fitz.Rect, existing_rects: Iterable[fitz.Rect]) -> bool:
    for existing in existing_rects:
        if rect.intersects(existing):
            return True
    return False


def int_color_to_rgb(color_value: int) -> Tuple[float, float, float]:
    r = ((color_value >> 16) & 255) / 255.0
    g = ((color_value >> 8) & 255) / 255.0
    b = (color_value & 255) / 255.0
    return (r, g, b)


def get_best_text_style_for_rect(page: fitz.Page, target_rect: fitz.Rect) -> Optional[TextStyle]:
    page_dict = page.get_text("dict")
    best_style: Optional[TextStyle] = None
    best_overlap = 0.0

    for block in page_dict.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                bbox = span.get("bbox")
                if not bbox:
                    continue

                span_rect = fitz.Rect(bbox)
                if not span_rect.intersects(target_rect):
                    continue

                overlap = (span_rect & target_rect).get_area()
                if overlap <= best_overlap:
                    continue

                color_value = int(span.get("color", 0))
                best_style = TextStyle(
                    fontname=str(span.get("font", "helv")),
                    fontsize=float(span.get("size", 8.0)),
                    color=int_color_to_rgb(color_value),
                )
                best_overlap = overlap

    return best_style


def apply_text_redactions(doc: fitz.Document, replacements: List[Tuple[str, str]]) -> int:
    total_redactions = 0

    for page in doc:
        redaction_regions: List[fitz.Rect] = []
        pending_insertions: List[Tuple[fitz.Rect, str, Optional[TextStyle]]] = []

        for original_text, replacement in replacements:
            if not original_text:
                continue

            for found in page.search_for(original_text, quads=True):
                rect = found.rect
                if intersects_any(rect, redaction_regions):
                    continue

                detected_style = get_best_text_style_for_rect(page, rect)

                page.add_redact_annot(
                    rect,
                    text="",
                    fill=None,
                )
                redaction_regions.append(rect)
                pending_insertions.append((rect, replacement, detected_style))
                total_redactions += 1

        if redaction_regions:
            page.apply_redactions()

            for rect, replacement, style in pending_insertions:
                fontname = "helv"
                fontsize = 8.0
                color = (0.0, 0.0, 0.0)

                if style is not None:
                    fontname = style.fontname
                    fontsize = max(6.0, style.fontsize)
                    color = style.color

                # Try to keep original style; fallback to Helvetica if embedded font is not reusable.
                try:
                    written = page.insert_textbox(
                        rect,
                        replacement,
                        fontname=fontname,
                        fontsize=fontsize,
                        color=color,
                        align=fitz.TEXT_ALIGN_LEFT,
                    )
                except Exception:
                    written = page.insert_textbox(
                        rect,
                        replacement,
                        fontname="helv",
                        fontsize=fontsize,
                        color=color,
                        align=fitz.TEXT_ALIGN_LEFT,
                    )

                if written < 0:
                    page.insert_textbox(
                        rect,
                        replacement,
                        fontname="helv",
                        fontsize=max(6.0, fontsize - 1.0),
                        color=color,
                        align=fitz.TEXT_ALIGN_LEFT,
                    )

    return total_redactions


def blur_image_bytes(image_bytes: bytes, blur_radius: float) -> bytes:
    with Image.open(io.BytesIO(image_bytes)) as img:
        blurred = img.convert("RGB").filter(ImageFilter.GaussianBlur(radius=blur_radius))
        output = io.BytesIO()
        blurred.save(output, format="PNG")
        return output.getvalue()


def apply_image_blur(doc: fitz.Document, blur_radius: float) -> int:
    """Overlay blurred versions of image blocks; returns number of blurred image occurrences."""
    blurred_count = 0

    for page in doc:
        page_dict = page.get_text("dict")
        for block in page_dict.get("blocks", []):
            if block.get("type") != 1:
                continue

            image_bytes = block.get("image")
            bbox = block.get("bbox")
            if not image_bytes or not bbox:
                continue

            try:
                blurred_bytes = blur_image_bytes(image_bytes, blur_radius=blur_radius)
                page.insert_image(fitz.Rect(bbox), stream=blurred_bytes, overlay=True)
                blurred_count += 1
            except Exception as exc:
                LOGGER.warning("Could not blur one image block: %s", exc)

    return blurred_count


def anonymize_pdf(
    input_path: str,
    output_path: str,
    blur_radius: float = 18.0,
    blur_images: bool = True,
) -> None:
    nlp = load_ner_model()

    with fitz.open(input_path) as doc:
        entity_buckets = collect_entities_from_pdf(doc, nlp)
        placeholder_map = build_placeholder_map(entity_buckets)
        replacements = build_search_replacements(entity_buckets, placeholder_map)

        redactions = apply_text_redactions(doc, replacements)
        blurred = apply_image_blur(doc, blur_radius=blur_radius) if blur_images else 0

        doc.save(output_path, garbage=4, deflate=True, clean=True)

    LOGGER.info("Detected unique sensitive entities: %d", len(placeholder_map))
    LOGGER.info("Applied text redactions: %d", redactions)
    LOGGER.info("Blurred image occurrences: %d", blurred)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Anonymize sensitive data in a PDF file.")
    parser.add_argument("input_pdf", help="Path to input PDF")
    parser.add_argument("output_pdf", help="Path to output anonymized PDF")
    parser.add_argument(
        "--blur-radius",
        type=float,
        default=18.0,
        help="Gaussian blur radius for images (default: 18.0)",
    )
    parser.add_argument(
        "--no-image-blur",
        action="store_true",
        help="Do not blur images in the output PDF",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    anonymize_pdf(
        args.input_pdf,
        args.output_pdf,
        blur_radius=args.blur_radius,
        blur_images=not args.no_image_blur,
    )


if __name__ == "__main__":
    main()
