import cv2

# Carica l'immagine
img = cv2.imread('example.jpg')

if img is None:
    print("Errore: immagine non trovata.")
    exit()

# Converte in scala di grigi
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Crea il rilevatore SIFT
sift = cv2.SIFT_create()

# Rileva keypoints e descrittori
keypoints, descriptors = sift.detectAndCompute(gray, None)

# Disegna i keypoints (con scala e orientamento)
img_sift = cv2.drawKeypoints(
    img, keypoints, None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# Mostra l'immagine con i keypoints
cv2.imshow("Feature Rilevate con SIFT", img_sift)
cv2.waitKey(0)
cv2.destroyAllWindows()
