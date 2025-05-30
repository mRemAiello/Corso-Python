import cv2

# Carica le due immagini
img1 = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)

if img1 is None or img2 is None:
    print("Errore nel caricamento delle immagini.")
    exit()

# Crea il rilevatore SIFT
sift = cv2.SIFT_create()

# Rileva i keypoints e i descrittori per entrambe le immagini
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Crea il matcher BF (Brute Force)
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# Trova le corrispondenze tra descrittori
matches = bf.match(des1, des2)

# Ordina le corrispondenze per distanza (più bassa = migliore)
matches = sorted(matches, key=lambda x: x.distance)

# Disegna le prime 50 corrispondenze
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=2)

# Mostra il risultato
cv2.namedWindow("Matching SIFT", cv2.WINDOW_NORMAL)  # consente il resize
cv2.resizeWindow("Matching SIFT", 1200, 800)          # imposta dimensioni fisse
cv2.imshow("Matching SIFT", img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()