"""
Predizione: il gatto in foto e' Marte o un gatto generico?

Carica il modello addestrato (cnn_othercat.pth) e classifica
un'immagine fornita dall'utente.

Esecuzione:
- python 3_predict.py
"""

from pathlib import Path

import torch
from PIL import Image
from torch import nn
from torchvision import transforms


# ── Stessa architettura usata in 1_cnn_othercat.py ──────────────────────────

class SimpleCNN(nn.Module):
    def __init__(self, num_classes: int) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 16 * 16, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        return self.classifier(x)


# ── Trasformazioni (identiche al training, senza augmentation) ───────────────

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
])

# ImageFolder ordina le cartelle alfabeticamente:
#   00_othercat -> indice 0
#   01_marte    -> indice 1
CLASS_NAMES = ["Gatto generico (other cat)", "Marte"]


def load_model(model_path: Path, device: torch.device) -> SimpleCNN:
    model = SimpleCNN(num_classes=2).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    return model


def predict(model: SimpleCNN, image_path: Path, device: torch.device) -> tuple[str, float]:
    image = Image.open(image_path).convert("RGB")
    tensor = transform(image).unsqueeze(0).to(device)   # [1, 3, 128, 128]

    with torch.no_grad():
        logits = model(tensor)
        probs = torch.softmax(logits, dim=1)[0]

    class_idx = probs.argmax().item()
    confidence = probs[class_idx].item()
    return CLASS_NAMES[class_idx], confidence


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    model_path = base_dir / "cnn_othercat.pth"

    if not model_path.exists():
        print(f"[ERRORE] Modello non trovato: {model_path}")
        print("Esegui prima '1_cnn_othercat.py' per addestrare e salvare il modello.")
        return

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = load_model(model_path, device)

    print("=== Classificatore gatti: Marte vs Other cat ===")
    print(f"Modello caricato da: {model_path}")
    print(f"Device: {device}\n")

    while True:
        raw = input("Inserisci il percorso dell'immagine (o 'q' per uscire): ").strip()
        if raw.lower() in ("q", "quit", "exit"):
            print("Uscita.")
            break

        image_path = Path(raw)
        if not image_path.exists():
            print(f"  [ERRORE] File non trovato: {image_path}\n")
            continue
        if image_path.suffix.lower() not in (".jpg", ".jpeg", ".png", ".bmp", ".webp"):
            print("  [ERRORE] Formato non supportato. Usa jpg, png, bmp o webp.\n")
            continue

        label, confidence = predict(model, image_path, device)
        print(f"\n  Risultato  : {label}")
        print(f"  Confidenza : {confidence * 100:.1f}%\n")


# Avvio del programma
def main() -> None:
    base_dir = Path(__file__).resolve().parent
    model_path = base_dir / "cnn_othercat.pth"

    if not model_path.exists():
        print(f"[ERRORE] Modello non trovato: {model_path}")
        print("Esegui prima '1_cnn_othercat.py' per addestrare e salvare il modello.")
        return

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = load_model(model_path, device)

    print("=== Classificatore gatti: Marte vs Other cat ===")
    print(f"Modello caricato da: {model_path}")
    print(f"Device: {device}\n")

    while True:
        raw = input("Inserisci il percorso dell'immagine (o 'q' per uscire): ").strip()
        if raw.lower() in ("q", "quit", "exit"):
            print("Uscita.")
            break

        image_path = Path(raw)
        if not image_path.exists():
            print(f"  [ERRORE] File non trovato: {image_path}\n")
            continue
        if image_path.suffix.lower() not in (".jpg", ".jpeg", ".png", ".bmp", ".webp"):
            print("  [ERRORE] Formato non supportato. Usa jpg, png, bmp o webp.\n")
            continue

        label, confidence = predict(model, image_path, device)
        print(f"\n  Risultato  : {label}")
        print(f"  Confidenza : {confidence * 100:.1f}%\n")
        

#        
main()