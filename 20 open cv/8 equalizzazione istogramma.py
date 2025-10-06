"""Esempio di equalizzazione dell'istogramma con OpenCV.

Questo script mostra due tecniche per migliorare il contrasto:
1. Equalizzazione standard su un'immagine in scala di grigi.
2. CLAHE (Contrast Limited Adaptive Histogram Equalization) che lavora su piccole
   regioni dell'immagine per preservare i dettagli e limitare l'amplificazione del rumore.
"""

import cv2

# Carica l'immagine a colori e verifica che sia stata trovata
immagine_color = cv2.imread('example.jpg')
if immagine_color is None:
    raise SystemExit("Errore: immagine non trovata.")

# Converte in scala di grigi per applicare l'equalizzazione classica
immagine_grigio = cv2.cvtColor(immagine_color, cv2.COLOR_BGR2GRAY)

equalizzata = cv2.equalizeHist(immagine_grigio)

# Applica CLAHE per un contrasto locale più controllato
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_output = clahe.apply(immagine_grigio)

cv2.imshow('Originale (grigio)', immagine_grigio)
cv2.imshow('Equalizzazione istogramma', equalizzata)
cv2.imshow('CLAHE', clahe_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
