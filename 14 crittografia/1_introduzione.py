# Crittografia è una tecnica per proteggere le informazioni attraverso la trasformazione dei dati,
# rendendoli incomprensibili per chiunque non possieda una chiave per decifrarli.


# Gli scopi principali della crittografia sono:

# Riservatezza: Garantire che solo i destinatari autorizzati possano accedere ai dati.
# Attraverso la crittografia, i dati sono cifrati e quindi leggibili solo da chi possiede la chiave corretta.

# Integrità: Assicurare che i dati non siano stati alterati durante il trasferimento
# o l'archiviazione. Un meccanismo di controllo, spesso basato su hash,
# può essere utilizzato per rilevare modifiche non autorizzate ai dati.

# Autenticità: Verificare l'identità del mittente o del destinatario dei dati.
# La crittografia permette di firmare digitalmente i messaggi, garantendo che provengano da una fonte affidabile.

# Non ripudio: Garantire che il mittente non possa negare di aver inviato un messaggio.
# Le firme digitali creano una traccia che dimostra la partecipazione del mittente nella comunicazione.



# 1. Crittografia Simmetrica

# Nella crittografia simmetrica, la stessa chiave viene utilizzata sia per cifrare che per decifrare i dati.
# Questa chiave deve essere mantenuta segreta e condivisa tra le parti coinvolte nella comunicazione.

# Vantaggi: È veloce e richiede meno risorse computazionali rispetto alla crittografia asimmetrica.
# Svantaggi: La gestione delle chiavi è complessa, poiché la chiave deve essere trasmessa in modo sicuro ai destinatari.

# Algoritmi comuni di crittografia simmetrica:

# AES (Advanced Encryption Standard): Uno degli algoritmi più sicuri e ampiamente utilizzati.
# Supporta chiavi di 128, 192 o 256 bit.

# DES (Data Encryption Standard): Algoritmo più vecchio, ora considerato insicuro
# a causa delle dimensioni ridotte della chiave (56 bit).

# ChaCha20: Algoritmo moderno molto veloce, utilizzato per ambienti con risorse limitate.



# 2. Crittografia Asimmetrica

# Esempio:
# stringa -> chiave pubblica -> 1xmdjkqwowi2weiwe2ko2kio
# chiave + stringa criptata -> banca -> chiave privata -> stringa

# Nella crittografia asimmetrica, si utilizzano due chiavi diverse: una chiave pubblica per cifrare i dati
# e una chiave privata per decifrarli.
# La chiave pubblica può essere condivisa liberamente, mentre la chiave privata deve essere mantenuta segreta.

# Vantaggi: Non c'è bisogno di trasmettere in modo sicuro una chiave segreta, poiché solo la chiave pubblica è distribuita.
# Svantaggi: È più lenta rispetto alla crittografia simmetrica e richiede più risorse computazionali.

# Algoritmi comuni di crittografia asimmetrica:

# RSA (Rivest–Shamir–Adleman): Uno degli algoritmi più popolari, basato sulla fattorizzazione di grandi numeri primi.

# ECC (Elliptic Curve Cryptography): Utilizza le curve ellittiche per creare chiavi più piccole ma altrettanto sicure,
# rispetto a RSA. È più efficiente in termini di risorse computazionali, ideale per dispositivi mobili e IoT.


# 3. Hashing

# zip -> 299dlwe92kls92903i

# Sito web -> registrazione -> password "ciao" -> hashing -> 1200xow9029sl
# Login -> "ciao2" -> hashing -> 1200xow9129sl -> controlla password criptata nel db con quella inserita da te


# Le funzioni di hashing trasformano i dati in una stringa di lunghezza fissa (chiamata digest o hash),
# indipendentemente dalla dimensione del messaggio originale. Gli algoritmi di hashing sono progettati
# per essere a senso unico, cioè è praticamente impossibile ricostruire i dati originali a partire dal digest.

# Scopi dell'hashing: L'hashing è usato per verificare l'integrità dei dati (ad esempio nei checksum),
# per la gestione delle password e nelle firme digitali.


# Algoritmi comuni di hashing:

# SHA (Secure Hash Algorithm): Famiglia di algoritmi di hashing sicuri,
# tra cui SHA-256 e SHA-512, ampiamente utilizzati.

# MD5 (Message Digest Algorithm 5): Un tempo molto utilizzato,
# ora considerato insicuro a causa delle vulnerabilità alle collisioni (due input diversi producono lo stesso hash).