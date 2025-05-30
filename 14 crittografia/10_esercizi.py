# Esercizio 1: Crittografia Simmetrica con Fernet
#
# Obiettivo: Utilizzare la crittografia simmetrica per cifrare e
# decifrare un messaggio con l'algoritmo Fernet della libreria cryptography.
#
#     Scrivi un programma che:
#         Generi una chiave segreta utilizzando l'algoritmo Fernet.
#         Prenda un messaggio dall'utente, lo cifri utilizzando la chiave generata e visualizzi il messaggio cifrato.
#         Decifri il messaggio cifrato e mostri il risultato originale.
#
# Domande di riflessione:
#
#     Cosa accade se provi a decifrare il messaggio con una chiave diversa?
#     Come potresti salvare e recuperare la chiave per uso futuro?



# Esercizio 2: Crittografia Simmetrica con AES
#
# Obiettivo: Implementare la crittografia simmetrica utilizzando l'algoritmo AES (Advanced Encryption Standard).
#
#     Genera una chiave simmetrica AES di 128 bit.
#     Usa la modalità CFB per cifrare un messaggio fornito dall'utente.
#     Decifra il messaggio cifrato e visualizza il risultato.
#     Modifica l'esercizio per utilizzare la modalità GCM, che offre sia riservatezza che integrità dei dati.
#
# Domande di riflessione:
#
#     Qual è la differenza tra le modalità CFB e GCM?
#     Perché l'integrità dei dati è importante?



# Esercizio 3: Crittografia Asimmetrica con RSA
#
# Obiettivo: Applicare la crittografia asimmetrica per cifrare e decifrare messaggi utilizzando RSA.
#
# Istruzioni:
#
#     Genera una coppia di chiavi RSA (una chiave pubblica e una chiave privata).
#     Cifra un messaggio utilizzando la chiave pubblica e visualizza il risultato.
#     Decifra il messaggio cifrato utilizzando la chiave privata e visualizza il messaggio originale.
#     Salva le chiavi in formato PEM su file e recuperale per utilizzarle in sessioni future.
#
# Domande di riflessione:
#
#     Cosa succede se provi a decifrare un messaggio con la chiave pubblica?
#     Quali sono i vantaggi della crittografia asimmetrica rispetto a quella simmetrica?



# Esercizio 4: Hashing con SHA256
#
# Obiettivo: Comprendere il funzionamento delle funzioni di hashing utilizzando SHA256.
#
# Istruzioni:
#
#     Scrivi un programma che:
#         Chieda all'utente di inserire una stringa.
#         Generi l'hash della stringa utilizzando l'algoritmo SHA256.
#         Mostri l'hash generato all'utente.
#
#     Aggiungi una funzione che permetta all'utente di confrontare l'hash di un nuovo messaggio con quello
#     originale per verificare se i due messaggi sono uguali.
#
# Domande di riflessione:
#
#     Qual è la differenza tra crittografia e hashing?
#     Perché non è possibile recuperare il messaggio originale da un hash?



# Esercizio 5: Firma Digitale con RSA
#
# Obiettivo: Creare e verificare una firma digitale utilizzando la crittografia asimmetrica.
#
# Istruzioni:
#
#     Genera una coppia di chiavi RSA.
#     Scrivi un programma che:
#         Crea una firma digitale di un messaggio utilizzando la chiave privata.
#         Verifica la firma utilizzando la chiave pubblica.
#     Modifica il programma per includere un hash (ad es. SHA256) come parte del processo di firma.
#
# Domande di riflessione:
#
#     Perché si usa una firma digitale in combinazione con un algoritmo di hashing?
#     Quali sono le applicazioni pratiche delle firme digitali?



# Esercizio 6: Utilizzo di IV (Initialization Vector) con AES
#
# Obiettivo: Capire l'importanza del vettore di inizializzazione (IV) nella crittografia simmetrica.
#
# Istruzioni:
#
#     Scrivi un programma che:
#         Generi una chiave AES e un IV.
#         Cifri un messaggio con la modalità CFB usando l'IV generato.
#         Decifri il messaggio usando la stessa chiave e IV.
#     Ripeti il processo usando un IV diverso per la decifratura e osserva cosa succede.
#
# Domande di riflessione:
#
#     Perché l'IV è importante nella crittografia?
#     Cosa succede se l'IV viene riutilizzato o condiviso in modo errato?