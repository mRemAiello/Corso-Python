import cv2
import numpy as np

# Carica l'immagine in scala di grigi
immagine = cv2.imread('example.jpg')
if immagine is None:
    raise SystemExit("Errore: immagine non trovata.")

grigi = cv2.cvtColor(immagine, cv2.COLOR_BGR2GRAY)

# Applica una sfocatura gaussiana per ridurre il rumore
sfocata = cv2.GaussianBlur(grigi, (5, 5), 0)

# Applica una sogliatura binaria
_, soglia = cv2.threshold(sfocata, 120, 255, cv2.THRESH_BINARY)

# Esegue un'operazione morfologica di apertura per eliminare piccoli artefatti
kernel = np.ones((3, 3), np.uint8)
apertura = cv2.morphologyEx(soglia, cv2.MORPH_OPEN, kernel, iterations=2)

# Mostra i risultati
cv2.imshow('Originale', immagine)
cv2.imshow('Scala di grigi', grigi)
cv2.imshow('Sfocata', sfocata)
cv2.imshow('Soglia binaria', soglia)
cv2.imshow('Apertura morfologica', apertura)

cv2.waitKey(0)
cv2.destroyAllWindows()
