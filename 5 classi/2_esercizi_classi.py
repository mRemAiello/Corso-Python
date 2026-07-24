# Esercizi sulle classi
#
# Regola generale: per ogni esercizio crea una funzione main() che istanzi gli
# oggetti, prova anche casi limite e stampa risultati leggibili. Evita valori
# "magici": salva i dati in variabili con nomi chiari.

# ============================================================================
# LIVELLO 1 - Classi, attributi, metodi e condizioni
# ============================================================================

# 1. Persona
# Crea una classe Persona con gli attributi nome, eta e sesso.
# - Implementa __init__ e il metodo presentati().
# - presentati() deve costruire e stampare una frase come:
#   "Ciao, mi chiamo Marco e ho 32 anni".
# - Nel main crea almeno tre persone, salvale in una lista e usa un ciclo for
#   per presentarle tutte.

# 2. Animale
# Crea una classe Animale con nome e specie.
# - Implementa emetti_suono() usando if / elif / else: gatto -> "Miao!",
#   cane -> "Bau!", mucca -> "Muu!". Per una specie sconosciuta stampa un
#   messaggio adeguato.
# - Crea una lista di animali e usa un ciclo per far emettere il suono a tutti.

# 3. Automobile
# Crea una classe Automobile con marca, modello e anno.
# - Aggiungi descrivi(), che restituisce una descrizione dell'auto.
# - Aggiungi e_storica(): restituisce True se l'auto ha almeno 30 anni,
#   altrimenti False.
# - Nel main stampa le auto storiche di una lista usando un ciclo e una
#   condizione.

# ============================================================================
# LIVELLO 2 - Costruttori, funzioni e validazione dei dati
# ============================================================================

# 4. PersonalComputer
# Crea la classe PersonalComputer con marca, modello, processore, ram_gb,
# memoria_hd_gb e scheda_video.
# - Implementa una funzione esterna stampa_configurazione(pc) che riceve un
#   oggetto PersonalComputer e ne stampa i dati in modo ordinato.
# - Aggiungi il metodo adatto_ai_giochi(): restituisce True solo se RAM e spazio
#   disco rispettano soglie che scegli e documenti con variabili locali.
# - Crea almeno tre PC in una lista e usa un ciclo per stamparli e distinguerli
#   con una condizione.

# 5. Calcolatrice
# Crea una classe Calcolatrice con i metodi somma, sottrazione,
# moltiplicazione, divisione, divisione_resto e potenza.
# - Ogni metodo riceve due numeri e restituisce il risultato, senza stamparlo.
# - divisione() e divisione_resto() devono gestire il divisore uguale a zero
#   con una condizione, senza far terminare il programma con un errore.
# - Crea una funzione mostra_risultato(nome_operazione, risultato) e usala nel
#   main per mostrare almeno un esempio per ciascuna operazione.

# 6. Studente e Insegnante
# Crea le classi Studente e Insegnante, entrambe con nome ed eta.
# - Studente implementa vado_in_classe(), che stampa "Sto andando in classe".
# - Insegnante implementa insegna(), che stampa "Sto insegnando".
# - Entrambe implementano imposta_eta(nuova_eta) e mostra_eta(). Valida che
#   l'eta sia un intero positivo prima di modificarla.
# - Salva oggetti delle due classi in due liste distinte e scorri ciascuna lista.

# 7. Impiegato
# Crea una classe Impiegato con nome, cognome, matricola e stipendio.
# - Implementa aumenta_stipendio(percentuale=10), con un valore predefinito.
# - Accetta soltanto percentuali positive e stipendio non negativo.
# - Implementa stampa_dettagli() e crea una funzione esterna che calcoli lo
#   stipendio totale di una lista di impiegati usando un ciclo.

# ============================================================================
# LIVELLO 3 - Liste, dizionari e oggetti che collaborano
# ============================================================================

# 8. Magazzino di prodotti
# Crea una classe Prodotto con nome, prezzo e scorta. Crea GestoreMagazzino con:
# - un dizionario prodotti che associ il nome del prodotto al relativo oggetto;
# - costo_magazzinaggio, cioe' il costo mensile per ogni unita' in scorta.
#
# Implementa aggiungi_prodotto(), rimuovi_prodotto(nome), cerca_prodotto(nome)
# e calcola_costi_magazzinaggio(). Il costo totale deve essere calcolato con un
# ciclo sui prodotti e tenere conto della scorta. Gestisci con if i prodotti non
# presenti e impedisci scorte o prezzi negativi.
#
# Scrivi inoltre aggiungi_prodotti(lista_prodotti): riceve una lista di oggetti
# Prodotto e li aggiunge uno alla volta. Nel main prova aggiunte, rimozioni e
# ricerche sia riuscite sia non riuscite.

# 9. Docente e Universita
# Crea Docente con nome, cognome, codice ed eta, piu' i metodi get_codice(),
# get_cognome() e get_eta(). Crea Universita con una lista di docenti.
# - Implementa get_eta_minima() e trova_giovane().
# - Se la lista e' vuota, i metodi devono restituire None oppure un messaggio
#   coerente: scegli una soluzione e applicala in entrambi.
# - Usa un ciclo esplicito per cercare l'eta minima, senza min().
# - Nel main verifica il comportamento con una universita popolata e una vuota.

# 10. Libreria
# Crea Libro con titolo, autore e prezzo, con i metodi get_titolo(),
# get_autore() e get_prezzo(). Crea Libreria con una lista di libri.
# - Implementa trova(autore, prezzo_minimo): restituisce quanti libri dello
#   stesso autore costano piu' di prezzo_minimo.
# - Implementa titoli_per_autore(autore): restituisce una lista di titoli.
# - Aggiungi un metodo libri_sotto_prezzo(limite) che restituisca una lista.
# - Nel main usa cicli e condizioni per stampare i risultati, compreso il caso
#   di un autore assente.

# ============================================================================
# LIVELLO 4 - Menu, cicli while e rappresentazione degli oggetti
# ============================================================================

# 11. Conversione dei voti
# Crea una classe Grade con un attributo lettera e il metodo get_numeric_grade().
# Le lettere A, B, C, D e F valgono rispettivamente 4, 3, 2, 1 e 0. Un suffisso
# + o - modifica il voto di 0.3; A+ vale comunque 4.0 e F+ / F- non sono validi.
# - Usa condizioni per validare l'input e un dizionario per i valori base.
# - Nel main chiedi voti in un ciclo while finche' l'utente scrive "Esci".
# - Per ogni input valido stampa il valore numerico; per ogni input non valido
#   mostra un messaggio e continua il ciclo.

# 12. Studente e Corso
# Crea Corso con nome e codice. Crea Studente con nome, cognome, matricola e una
# struttura dati per memorizzare corsi e voti.
# - aggiungi_corso(corso, voto) deve controllare che il voto sia tra 18 e 30.
# - media_voti() restituisce la media, oppure None se lo studente non ha voti.
# - elenco_corsi() stampa ogni corso con il relativo voto usando un ciclo.
# - Crea due studenti e tre corsi; assegna corsi diversi e confronta le medie
#   con if / elif / else.

# 13. Paziente e VisitaMedica
# Crea Paziente con nome, cognome, data_nascita, codice_fiscale e una lista di
# visite. Crea VisitaMedica con data, medico e diagnosi.
# - Personalizza __str__ in VisitaMedica per ottenere una riga leggibile.
# - Paziente implementa aggiungi_visita(visita) ed elenca_visite().
# - Aggiungi ha_visite(): restituisce True o False in base alla lista.
# - Nel main crea almeno due pazienti, di cui uno senza visite, e gestisci i due
#   casi con una condizione.

# ============================================================================
# LIVELLO 5 - Sfida finale: classi correlate e ricerca
# ============================================================================

# 14. Gestione chiavi
# Crea una classe base Chiave con descrizione e peso. Crea poi:
# - ChiaveMeccanica: aggiunge lunghezza e numero_dentelli;
# - ChiaveMagnetica: aggiunge lunghezza e ampiezza;
# - ChiaveMicrochip: aggiunge codice_seriale e il metodo aggiorna_codice().
#
# Ogni classe deve avere il proprio costruttore e un metodo informazioni() che
# stampi tutti i dati ordinatamente. Crea una lista con chiavi di tipi diversi,
# scorri la lista per stamparle e scrivi una funzione chiave_piu_leggera(chiavi)
# che restituisca l'oggetto piu' leggero. Gestisci anche la lista vuota.
#
# Bonus: chiedi all'utente un tipo di chiave e, con un ciclo e condizioni,
# stampa solo le chiavi del tipo richiesto.

# 15. Biblioteca con prestiti
# Crea le classi Libro, Utente e Biblioteca.
# - Libro contiene titolo, autore, codice e disponibile (True / False).
# - Utente contiene nome, tessera e una lista dei libri presi in prestito.
# - Biblioteca contiene due dizionari: libri, indicizzati per codice, e utenti,
#   indicizzati per numero di tessera.
#
# Implementa registra_libro(), registra_utente(), presta_libro(codice, tessera),
# restituisci_libro(codice, tessera) ed elenco_libri_disponibili(). Un libro non
# puo' essere prestato se non esiste, se e' gia' in prestito oppure se l'utente
# non e' registrato. Usa condizioni per ogni controllo e cicli per creare gli
# elenchi. Nel main prova un prestito valido e almeno tre casi non validi.
#
# Bonus: crea un menu nel main con while che permetta di scegliere prestito,
# restituzione, elenco libri e uscita.

# 16. Parcheggio
# Crea la classe Veicolo con targa, marca e ore_sosta. Crea Parcheggio con una
# lista di veicoli e una tariffa_oraria.
# - aggiungi_veicolo(veicolo) non deve accettare due veicoli con la stessa targa.
# - rimuovi_veicolo(targa) rimuove e restituisce il veicolo trovato; se non lo
#   trova restituisce None oppure un valore coerente scelto da te.
# - calcola_costo(targa) calcola il prezzo della sosta moltiplicando ore_sosta e
#   tariffa_oraria. Le ore devono essere maggiori di zero.
# - incasso_totale() usa un ciclo per sommare il costo di tutti i veicoli.
#
# Nel main crea una lista iniziale di veicoli, prova l'inserimento di una targa
# duplicata e stampa il veicolo che ha pagato di piu'. Per la ricerca non usare
# funzioni avanzate: scorri esplicitamente la lista con un ciclo.

# 17. Rubrica telefonica interattiva
# Crea Contatto con nome, cognome, telefono e categoria (per esempio "famiglia",
# "lavoro" o "altro"). Crea Rubrica con un dizionario di contatti, usando il
# numero di telefono come chiave.
# - Implementa aggiungi_contatto(), elimina_contatto(telefono),
#   cerca_per_nome(testo) e contatti_per_categoria(categoria).
# - Le ricerche devono restituire liste di oggetti Contatto, anche quando la
#   lista e' vuota.
# - Aggiungi __str__ a Contatto per stamparne i dati in una sola riga.
# - Impedisci l'aggiunta di numeri vuoti o gia' presenti e mostra messaggi chiari.
#
# Nel main realizza un menu con while: aggiungi, elimina, cerca per nome, filtra
# per categoria, mostra tutti i contatti ed esci. Dividi le operazioni del menu
# in piccole funzioni esterne e usa if / elif / else per gestire la scelta.