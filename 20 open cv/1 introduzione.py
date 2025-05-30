import cv2

# Carica l'immagine da file
# 800 x 600
# (100, 10, 0, 1) (30, 100, 10, 1)
immagine = cv2.imread('example.jpg')

# Verifica se l'immagine è stata caricata correttamente
if immagine is None:
    print("Errore: immagine non trovata.")
    exit()

# Converti in scala di grigi
grigia = cv2.cvtColor(immagine, cv2.COLOR_BGR2GRAY)

# Applica il filtro di Canny per rilevare i bordi
bordi = cv2.Canny(grigia, 100, 200)

# Mostra l'immagine originale, quella in scala di grigi e i bordi
cv2.imshow('Originale', immagine)
cv2.imshow('Scala di Grigi', grigia)
cv2.imshow('Bordi', bordi)

# Attendi la pressione di un tasto, poi chiudi le finestre
cv2.waitKey(0)
cv2.destroyAllWindows()