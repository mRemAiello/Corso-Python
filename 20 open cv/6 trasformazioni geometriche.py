import cv2
import numpy as np

# Carica l'immagine di esempio
immagine = cv2.imread('example.jpg')
if immagine is None:
    raise SystemExit("Errore: immagine non trovata.")

# Ridimensiona l'immagine mantenendo le proporzioni
ridimensionata = cv2.resize(immagine, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Ruota l'immagine di 45 gradi intorno al suo centro
altezza, larghezza = immagine.shape[:2]
centro = (larghezza // 2, altezza // 2)
matrice_rotazione = cv2.getRotationMatrix2D(centro, 45, 1.0)
ruotata = cv2.warpAffine(immagine, matrice_rotazione, (larghezza, altezza))

# Specchia l'immagine orizzontalmente
specchiata = cv2.flip(immagine, 1)

# Mostra tutte le trasformazioni
cv2.imshow('Originale', immagine)
cv2.imshow('Ridimensionata 50%', ridimensionata)
cv2.imshow('Ruotata 45 gradi', ruotata)
cv2.imshow('Specchiata', specchiata)

cv2.waitKey(0)
cv2.destroyAllWindows()
