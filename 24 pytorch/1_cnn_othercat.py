"""
Esercizio PyTorch: classificazione immagini con CNN.

Obiettivo:
- Creare una CNN semplice
- Addestrarla sul dataset locale in dataset/00_othercat e dataset/01_marte

Prerequisiti:
- pip install torch torchvision

Esecuzione:
- python 1_cnn_othercat.py
"""

from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms

# RBG n * m -> R, G, B

class SimpleCNN(nn.Module):
    def __init__(self, num_classes: int) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=5, padding=2),  # Estrae feature locali: da 3 canali RGB a 32 mappe.
            # Inserisce un padding di 1 per mantenere le dimensioni spaziali (128x128) ed evitare perdita sulle feature maps.
            nn.ReLU(),  # Introduce non linearita, azzerando i valori negativi. f(x) = max(0, x)
            nn.MaxPool2d(kernel_size=2),  # Riduce altezza/larghezza di 2x mantenendo le feature piu rilevanti.
            nn.Conv2d(32, 64, kernel_size=5, padding=2),  # Aumenta la profondita: da 32 a 64 mappe di feature.
            nn.ReLU(),  # Nuova non linearita dopo la seconda convoluzione.
            nn.MaxPool2d(kernel_size=2),  # Nuovo downsampling spaziale (dimensioni ancora dimezzate).
            nn.Conv2d(64, 128, kernel_size=5, padding=2),  # Livello piu profondo: apprende pattern piu complessi.
            nn.ReLU(),  # Applica la funzione di attivazione anche su queste feature avanzate.
            nn.MaxPool2d(kernel_size=2),  # Ultima riduzione spaziale prima del classificatore fully-connected.
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),  # Trasforma il tensore [C, H, W] in un vettore 1D per i layer lineari.
            nn.Linear(128 * 16 * 16, 256),  # Proietta le feature in 256 neuroni densi.
            nn.ReLU(),  # Non linearita nel classificatore.
            nn.Dropout(0.3),  # Spegne casualmente il 30% dei neuroni durante il training per ridurre overfitting.
            nn.Linear(256, num_classes),  # Produce i logits finali, uno per ciascuna classe.
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        return self.classifier(x)


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    criterion: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
) -> tuple[float, float]:
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        logits = model(images)
        loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)
        preds = logits.argmax(dim=1)
        correct += (preds == labels).sum().item()
        total += labels.size(0)

    return running_loss / total, correct / total


def evaluate(
    model: nn.Module,
    loader: DataLoader,
    criterion: nn.Module,
    device: torch.device,
) -> tuple[float, float]:
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            logits = model(images)
            loss = criterion(logits, labels)

            running_loss += loss.item() * images.size(0)
            preds = logits.argmax(dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

    return running_loss / total, correct / total


def main() -> None:
    torch.manual_seed(42)

    base_dir = Path(__file__).resolve().parent
    dataset_root = base_dir / "dataset"

    if not dataset_root.exists():
        raise FileNotFoundError(f"Dataset non trovato: {dataset_root}")

    transform = transforms.Compose(
        [
            transforms.Resize((128, 128)),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
        ]
    )

    dataset = datasets.ImageFolder(root=dataset_root, transform=transform)
    num_classes = len(dataset.classes)

    if num_classes < 2:
        raise ValueError(
            "Servono almeno due classi in dataset/. "
            "Esempio: dataset/00_othercat e dataset/01_marte"
        )

    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SimpleCNN(num_classes=num_classes).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    epochs = 8
    print(f"Device: {device}")
    print(f"Classi trovate: {dataset.classes}")
    print(f"Immagini totali: {len(dataset)}")

    for epoch in range(1, epochs + 1):
        train_loss, train_acc = train_one_epoch(model, train_loader, criterion, optimizer, device)
        val_loss, val_acc = evaluate(model, val_loader, criterion, device)

        print(
            f"Epoch {epoch:02d}/{epochs} | "
            f"train_loss: {train_loss:.4f} train_acc: {train_acc:.4f} | "
            f"val_loss: {val_loss:.4f} val_acc: {val_acc:.4f}"
        )

    model_path = base_dir / "cnn_othercat.pth"
    torch.save(model.state_dict(), model_path)
    print(f"Modello salvato in: {model_path}")


main()