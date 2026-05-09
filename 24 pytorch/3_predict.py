"""
Predizione: il gatto in foto e' Marte o un gatto generico?

Carica il modello addestrato (cnn_othercat.pth), classifica
un'immagine fornita dall'utente e salva le feature map dei tre
strati convoluzionali in:
    feature_maps/<nome_immagine>/layer_1_conv32.png
    feature_maps/<nome_immagine>/layer_2_conv64.png
    feature_maps/<nome_immagine>/layer_3_conv128.png

Esecuzione:
- python 3_predict.py
"""

import math
from pathlib import Path

import matplotlib.pyplot as plt
import torch
from PIL import Image
from torch import nn
from torchvision import transforms


# ── Stessa architettura usata in 1_cnn_othercat.py ──────────────────────────

class SimpleCNN(nn.Module):
    def __init__(self, num_classes: int) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=5, padding=2),   # 0
            nn.ReLU(),                                      # 1
            nn.MaxPool2d(kernel_size=2),                   # 2
            nn.Conv2d(32, 64, kernel_size=5, padding=2),   # 3
            nn.ReLU(),                                      # 4
            nn.MaxPool2d(kernel_size=2),                   # 5
            nn.Conv2d(64, 128, kernel_size=5, padding=2),  # 6
            nn.ReLU(),                                      # 7
            nn.MaxPool2d(kernel_size=2),                   # 8
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

# Indici dei layer ReLU (output dopo ogni blocco conv+relu) in features
FEATURE_LAYERS = {
    "layer_1_conv32":  1,   # dopo Conv2d(3,32)  + ReLU
    "layer_2_conv64":  4,   # dopo Conv2d(32,64) + ReLU
    "layer_3_conv128": 7,   # dopo Conv2d(64,128)+ ReLU
}


def load_model(model_path: Path, device: torch.device) -> SimpleCNN:
    model = SimpleCNN(num_classes=2).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    return model


def save_feature_maps(
    activations: dict[str, torch.Tensor],
    output_dir: Path,
) -> None:
    """Salva ogni mappa di feature come griglia di immagini PNG."""
    output_dir.mkdir(parents=True, exist_ok=True)

    for layer_name, fmap in activations.items():
        # fmap: [1, C, H, W] -> [C, H, W]
        fmap = fmap.squeeze(0).cpu()
        num_channels = fmap.shape[0]

        cols = math.ceil(math.sqrt(num_channels))
        rows = math.ceil(num_channels / cols)

        fig, axes = plt.subplots(rows, cols, figsize=(cols * 1.5, rows * 1.5))
        fig.suptitle(layer_name, fontsize=10)

        # Normalizzazione globale per rendere visibili le attivazioni
        vmin, vmax = fmap.min().item(), fmap.max().item()

        for idx in range(rows * cols):
            ax = axes.flat[idx] if rows * cols > 1 else axes
            if idx < num_channels:
                ax.imshow(fmap[idx], cmap="viridis", vmin=vmin, vmax=vmax)
            ax.axis("off")

        plt.tight_layout()
        save_path = output_dir / f"{layer_name}.png"
        fig.savefig(save_path, dpi=90, bbox_inches="tight")
        plt.close(fig)
        print(f"  Feature map salvata: {save_path}")


def predict_with_maps(
    model: SimpleCNN,
    image_path: Path,
    device: torch.device,
    maps_root: Path,
) -> tuple[str, float]:
    image = Image.open(image_path).convert("RGB")
    tensor = transform(image).unsqueeze(0).to(device)  # [1, 3, 128, 128]

    # ── Hook per catturare le attivazioni ────────────────────────────────────
    activations: dict[str, torch.Tensor] = {}
    hooks = []

    for layer_name, layer_idx in FEATURE_LAYERS.items():
        layer = model.features[layer_idx]

        def make_hook(name: str):
            def hook(_module, _input, output):
                activations[name] = output.detach()
            return hook

        hooks.append(layer.register_forward_hook(make_hook(layer_name)))

    with torch.no_grad():
        logits = model(tensor)
        probs = torch.softmax(logits, dim=1)[0]

    for h in hooks:
        h.remove()

    # ── Salva feature map ────────────────────────────────────────────────────
    output_dir = maps_root / image_path.stem
    save_feature_maps(activations, output_dir)

    class_idx = probs.argmax().item()
    confidence = probs[class_idx].item()
    return CLASS_NAMES[class_idx], confidence


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    model_path = base_dir / "cnn_othercat.pth"
    maps_root = base_dir / "feature_maps"

    if not model_path.exists():
        print(f"[ERRORE] Modello non trovato: {model_path}")
        print("Esegui prima '1_cnn_othercat.py' per addestrare e salvare il modello.")
        return

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = load_model(model_path, device)

    print("=== Classificatore gatti: Marte vs Other cat ===")
    print(f"Modello caricato da: {model_path}")
    print(f"Feature map salvate in: {maps_root}/<nome_immagine>/")
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

        label, confidence = predict_with_maps(model, image_path, device, maps_root)
        print(f"\n  Risultato  : {label}")
        print(f"  Confidenza : {confidence * 100:.1f}%\n")


main()