import argparse
import os
import re
from typing import Dict, Tuple

import pandas as pd


# Patterns usati per riconoscere automaticamente il tipo di colonna.
COLUMN_RULES: Tuple[Tuple[str, str], ...] = (
    (r"nome|name|cognome|surname|persona|utente|user|cliente", "Persona"),
    (r"mail|email|e-mail|posta", "Email"),
    (r"citta|città|city|localita|località|comune|provincia|regione|indirizzo|address", "Città"),
    (r"telefono|phone|cellulare|mobile|tel", "Telefono"),
    (r"azienda|company|societa|società", "Azienda"),
)


def infer_label_from_column(column_name: str) -> str:
    """Ritorna l'etichetta anonima in base al nome colonna."""
    normalized = str(column_name).strip().lower()
    for pattern, label in COLUMN_RULES:
        if re.search(pattern, normalized):
            return label
    return "Valore"


def anonymize_series(series: pd.Series, label: str) -> pd.Series:
    """Anonimizza una serie mantenendo valori uguali -> stessa etichetta."""
    mapping: Dict[str, str] = {}
    counter = 1

    def _replace(value):
        nonlocal counter
        if pd.isna(value):
            return value

        original = str(value).strip()
        if original == "":
            return value

        if original not in mapping:
            mapping[original] = f"{label} {counter}"
            counter += 1
        return mapping[original]

    return series.apply(_replace)


def anonymize_csv(input_path: str, output_path: str) -> None:
    """Legge un CSV, anonimizza tutte le colonne e salva il risultato."""
    df = pd.read_csv(input_path, encoding="utf-8-sig")
    anonymized = df.copy()

    for column in anonymized.columns:
        # Pandas puo usare dtype "object" oppure "string" per colonne testuali.
        if not (
            pd.api.types.is_object_dtype(anonymized[column])
            or pd.api.types.is_string_dtype(anonymized[column])
        ):
            continue
        label = infer_label_from_column(column)
        anonymized[column] = anonymize_series(anonymized[column], label)

    anonymized.to_csv(output_path, index=False, encoding="utf-8-sig")


def build_default_output_path(input_path: str) -> str:
    base, ext = os.path.splitext(input_path)
    ext = ext or ".csv"
    return f"{base}_anonimo{ext}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Anonimizza il contenuto di un CSV con etichette progressive usando Pandas."
    )
    parser.add_argument("input_csv", help="Percorso del file CSV da anonimizzare")
    parser.add_argument(
        "-o",
        "--output",
        help="Percorso del CSV anonimizzato (default: <input>_anonimo.csv)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_path = args.output or build_default_output_path(args.input_csv)
    anonymize_csv(args.input_csv, output_path)
    print(f"CSV anonimizzato creato in: {output_path}")


if __name__ == "__main__":
    main()