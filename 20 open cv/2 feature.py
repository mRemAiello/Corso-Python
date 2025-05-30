import cv2

# Carica l'immagine
img = cv2.imread('example.jpg')

if img is None:
    print("Errore: immagine non trovata.")
    exit()

# Converti in scala di grigi
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Crea l'oggetto ORB (puoi settare il numero di feature da rilevare)
orb = cv2.ORB_create(nfeatures=1000)

# Rileva i keypoints e calcola i descrittori
keypoints, descriptors = orb.detectAndCompute(gray, None)

# Disegna i keypoints sull'immagine
img_keypoints = cv2.drawKeypoints(
    img, keypoints, None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# Mostra il risultato
cv2.imshow("Originale", img)
cv2.imshow("Scala di grigi", gray)
cv2.imshow("Feature rilevate (ORB)", img_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()