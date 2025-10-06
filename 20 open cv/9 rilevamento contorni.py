"""Esempio di rilevamento contorni e bounding box con OpenCV.

Lo script esegue i seguenti passaggi:
1. Converte l'immagine in scala di grigi e applica una sfocatura per ridurre il rumore.
2. Applica l'algoritmo di Canny per ottenere i bordi principali.
3. Trova i contorni e disegna un rettangolo attorno a quelli più grandi.
"""

import cv2

immagine = cv2.imread('example.jpg')
if immagine is None:
    raise SystemExit("Errore: immagine non trovata.")

scala_grigi = cv2.cvtColor(immagine, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(scala_grigi, (5, 5), 0)
bordi = cv2.Canny(blur, 50, 150)

contorni, _ = cv2.findContours(bordi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
immagine_contorni = immagine.copy()

# Disegna i contorni più grandi (filtrati per area)
for cnt in contorni:
    area = cv2.contourArea(cnt)
    if area < 500:
        continue
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(immagine_contorni, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Originale', immagine)
cv2.imshow('Bordi (Canny)', bordi)
cv2.imshow('Contorni principali', immagine_contorni)
cv2.waitKey(0)
cv2.destroyAllWindows()
