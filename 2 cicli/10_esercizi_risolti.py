#  Far inserire una serie numerica di interi fermandosi
#  quando viene inserito due volte consecutive lo stesso numero.

penultimo_numero = int(input("Scrivi un numero: "))
ultimo_numero = int(input("Scrivi un numero: "))

while not ultimo_numero == penultimo_numero:
    numero = int(input("Scrivi un numero: "))

    penultimo_numero = ultimo_numero
    ultimo_numero = numero