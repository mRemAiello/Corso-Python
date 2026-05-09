"""
Esercizio 2: CNN CatClassifier (architettura da screenshot).

Obiettivo:
- Usare la CNN con:
  Conv2d(3->16) -> ReLU -> MaxPool
  Conv2d(16->8) -> ReLU -> MaxPool
  Flatten -> Linear(8*56*56 -> 32) -> ReLU -> Linear(32 -> 2)
- Addestrare sul dataset locale in dataset/00_othercat e dataset/01_marte

Prerequisiti:
- pip install torch torchvision

Esecuzione:
- python 2_esercizio_catclassifier.py
"""

from pathlib import Path

import torch
import torch.nn.functional as F
from torch import nn
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms


class CatClassifier(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=5, padding=2)
        self.conv2 = nn.Conv2d(16, 8, kernel_size=5, padding=2)
        self.pool = nn.MaxPool2d(2)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(8 * 56 * 56, 32)
        self.fc2 = nn.Linear(32, 2)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out = self.pool(F.relu(self.conv1(x)))
        out = self.pool(F.relu(self.conv2(out)))
        out = self.flatten(out)
        out = self.fc2(F.relu(self.fc1(out)))
        return out


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    criterion: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
) -> tuple[float, float]:
    model.train()
    total_loss = 0.0
    correct = 0
    total = 0

    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        logits = model(images)
        loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item() * images.size(0)
        preds = logits.argmax(dim=1)
        correct += (preds == labels).sum().item()
        total += labels.size(0)

    return total_loss / total, correct / total


def evaluate(
    model: nn.Module,
    loader: DataLoader,
    criterion: nn.Module,
    device: torch.device,
) -> tuple[float, float]:
    model.eval()
    total_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            logits = model(images)
            loss = criterion(logits, labels)

            total_loss += loss.item() * images.size(0)
            preds = logits.argmax(dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

    return total_loss / total, correct / total


def main() -> None:
    torch.manual_seed(42)

    base_dir = Path(__file__).resolve().parent
    dataset_root = base_dir / "dataset"

    if not dataset_root.exists():
        raise FileNotFoundError(f"Dataset non trovato: {dataset_root}")

    transform = transforms.Compose(
        [
            transforms.Resize((224, 224)),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
        ]
    )

    dataset = datasets.ImageFolder(root=dataset_root, transform=transform)

    if len(dataset.classes) != 2:
        raise ValueError(
            "Questo esercizio usa fc2 con 2 classi fisse. "
            f"Classi trovate: {len(dataset.classes)} ({dataset.classes})"
        )

    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = CatClassifier().to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    epochs = 8
    print(f"Device: {device}")
    print(f"Classi: {dataset.classes}")
    print(f"Immagini totali: {len(dataset)}")

    for epoch in range(1, epochs + 1):
        train_loss, train_acc = train_one_epoch(
            model, train_loader, criterion, optimizer, device
        )
        val_loss, val_acc = evaluate(model, val_loader, criterion, device)

        print(
            f"Epoch {epoch:02d}/{epochs} | "
            f"train_loss: {train_loss:.4f} train_acc: {train_acc:.4f} | "
            f"val_loss: {val_loss:.4f} val_acc: {val_acc:.4f}"
        )

    model_path = base_dir / "cat_classifier.pth"
    torch.save(model.state_dict(), model_path)
    print(f"Modello salvato in: {model_path}")


if __name__ == "__main__":
    main()
