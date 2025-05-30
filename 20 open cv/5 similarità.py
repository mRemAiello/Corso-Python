import cv2

# Carica le immagini
img1 = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)

# SIFT + keypoints
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# FLANN matcher
index_params = dict(algorithm=1, trees=5)  # FLANN con KD-Tree
search_params = dict(checks=400)
flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

# Applica il filtro di Lowe (rimuove i falsi positivi)
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# VALUTAZIONE SIMILITUDINE
print(f"Numero di good matches: {len(good_matches)}")

if len(good_matches) > 40:  # soglia empirica
    print("Le immagini sono SIMILI")
else:
    print("Le immagini sono DIVERSE")