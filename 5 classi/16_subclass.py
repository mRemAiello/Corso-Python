# Superclasse
class Persona:

    # Proprietà
    nome = 'Luca'
    cognome = 'Rossi'
    eta = 20
    codice_fiscale = ""
    luogo_di_nascita = ""

    # Costruttore
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.codice_fiscale = ""

    def imposta_luogo_di_nascita(self, luogo):
        self.luogo_di_nascita = luogo

    # Metodo della classe
    def saluta(self):
        print("Saluta di Persona")

    def __str__(self):
        stringa = f"Nome: {self.nome}, Cognome: {self.cognome}, Età: {self.eta}"
        return stringa


# Sottoclasse
class Studente(Persona):

    matricola = ""
    materie = []

    # Costruttore
    def __init__(self, nome, cognome, eta, matricola):
        super().__init__(nome, cognome, eta)
        self.matricola = matricola

    def vai_a_lezione(self):
        print("Lo studente va a lezione")

    def saluta(self):
        print("Saluta di Studente")

    def __str__(self):
        stringa = super().__str__()
        stringa += f", Matricola: {self.matricola}"
        return stringa


class Dipendente(Persona):

    id_azienda = ""

    def __init__(self, nome, cognome, eta, id_azienda):
        super().__init__(nome, cognome, eta)
        self.id_azienda = id_azienda

    def __str__(self):
        stringa = super().__str__()
        stringa += f", ID: {self.id_azienda}"
        return stringa


#
persona = Persona('Luca', 'Rossi', 20)
persona.saluta()
print(persona)
print()

#
studente = Studente('Antonio', 'Rossi', 25, "01")
studente.saluta()
studente.vai_a_lezione()
print(studente)
print()

#
dipendente = Dipendente("Luca", "Verdi", 30, "m0111")
dipendente.saluta()
print(dipendente)


# Creare una classe Scatola con gli opportuni attributi e metodi, per ogni scatola bisognerà memorizzare la dimensione dei lati e il suo peso,
# si potrà poi avere a disposizione le caratteristiche della scatola, ovvero le dimensioni dei lati, l’area della base, il volume, il peso, la densità media.
# Creare la classe GiocoInScatola in cui andranno memorizzate, oltre alle informazioni della scatola, anche il numero di giocatori e il nome del gioco.
# Si crei inoltre per entrambe le classi un metodo __str__ che permette di stampare a schermo i valori degli attributi dell’istanza sul quale è richiamato.
# Testare le classi con un opportuno main.
# Tra le prove, far inserire le informazioni di due giochi da tastiera e poi dire quali tra i due ha il rapporto volume/numero di giocatori maggiore.



# Si vuole creare un programma per gestire i prodotti alimentari di un supermercato. Ogni prodotto alimentare ha un nome,
# un prezzo e una data di scadenza. I prodotti freschi inoltre hanno un campo per indicare la temperatura di conservazione ideale.
# Si richiede di definire una classe Product che contenga i campi comuni a tutti i prodotti alimentari (nome, prezzo, data di scadenza)
# e un metodo per controllare se il prodotto è scaduto. Inoltre, si devono definire due sottoclassi di Product: FreshProduct e NonFreshProduct.
# La prima rappresenta i prodotti freschi e deve contenere un campo per indicare la temperatura di conservazione ideale,
# oltre a un metodo per controllare se il prodotto è ancora fresco (ovvero se la data di scadenza non è ancora passata e la temperatura di conservazione è corretta).
# La seconda rappresenta i prodotti non freschi e non ha bisogno di campi o metodi aggiuntivi.
# Infine, si deve creare una classe Main che istanzia alcuni oggetti di tipo FreshProduct e NonFreshProduct e li aggiunge ad un array.
# In un secondo momento, la classe Main deve scorrere l'array e stampare il nome e il prezzo di ogni prodotto, indicando anche se il prodotto
# è scaduto (nel caso di un NonFreshProduct il controllo è sempre negativo).



# Si vuole creare un programma per gestire una flotta di veicoli. Ogni veicolo ha una marca, un modello, un anno
# di produzione e un prezzo di listino. Inoltre, esistono diverse tipologie di veicoli: auto, moto, furgoni e biciclette.
# Tutti i veicoli hanno in comune i campi sopracitati, ma ogni tipo di veicolo ha anche dei campi specifici:
# le auto hanno il numero di porte e la cilindrata del motore;
# le moto hanno il tipo di motore (endotermico o elettrico) e la cilindrata del motore;
# i furgoni hanno il volume di carico e la portata massima;
# le biciclette hanno il tipo di telaio (da corsa o da passeggio) e il tipo di cambio (a scatto fisso o a cambi).
# Si richiede di definire una classe Vehicle che contenga i campi comuni a tutti i veicoli (marca, modello, anno di produzione, prezzo di listino) e
# un metodo per calcolare il prezzo scontato del veicolo (scontato del 10% se l'anno di produzione è precedente al 2010, del 5% altrimenti).
# Inoltre, si devono definire quattro sottoclassi di Vehicle: Car, Motorcycle, Van e Bicycle, ognuna con i campi specifici e
# un metodo per calcolare il prezzo scontato del veicolo che tenga conto anche delle caratteristiche specifiche del tipo di veicolo.
# Infine, si deve creare una classe Main che istanzia alcuni oggetti di tipo Vehicle e li aggiunge ad un array.
# In un secondo momento, la classe Main deve scorrere l'array e stampare le caratteristiche di ogni veicolo,
# insieme al prezzo di listino e al prezzo scontato.



# Si vuole creare un programma per gestire un insieme di animali domestici. Ogni animale ha un nome, un'età e un peso.
# Inoltre, esistono diverse tipologie di animali domestici: cani, gatti, uccelli e gatti persiani. Tutti gli animali domestici
# hanno in comune i campi sopracitati, ma ogni tipo di animale ha anche dei campi specifici:
# i cani hanno la razza e il livello di addestramento;
# i gatti hanno la lunghezza del pelo e il livello di affettuosità;
# gli uccelli hanno l'apertura alare e il tipo di piumaggio;
# i gatti persiani hanno la lunghezza del pelo, il colore e il livello di affettuosità.
# Si richiede di definire una classe Animale che contenga i campi comuni a tutti gli animali (nome, età, peso) e un metodo emettiVerso()
# che emette un verso generico per l'animale. Inoltre, si devono definire quattro sottoclassi di Animale: Cane, Gatto, Uccello e GattoPersiano,
# ognuna con i campi specifici e un metodo emettiVerso() che emetta un verso appropriato per il tipo di animale.
# Infine, si deve creare una classe Zoo che raccoglie e gestisce alcuni oggetti di tipo Animale e li aggiunge ad un array.
# In un secondo momento, creare uno Zoo dentro la classe Main e stampare le caratteristiche di ogni animale, insieme al verso emesso.



#     Creare una classe chiamata Persona con le seguenti proprietà:
#         nome (string): il nome della persona.
#         cognome (string): il cognome della persona.
#         eta (int): l'età della persona.
#         email (string): l'indirizzo email della persona.
#
#     Creare una classe chiamata Studente che erediti dalla classe Persona e abbia le seguenti proprietà aggiuntive:
#         matricola (string): il numero di matricola dello studente.
#         anno_corso (int): l'anno di corso dello studente.
#
#     Creare due sottoclassi di Studente chiamate StudenteTriennale e StudenteMagistrale,
#     che abbiano proprietà specifiche come il corso di laurea e il voto di laurea (applicabile solo per studenti magistrali).
#
#     Creare una classe chiamata Docente con le seguenti proprietà:
#         id_docente (string): un identificatore unico per il docente.
#         materia_insegnata (string): la materia insegnata dal docente.
#
#     Creare una classe chiamata Inserviente con le seguenti proprietà:
#         id_inserviente (string): un identificatore unico per l'inserviente.
#         ruolo (string): il ruolo dell'inserviente (ad esempio, "custode", "segretaria", "tecnico").
#
# Creare una classe chiamata Segreteria con le seguenti funzioni:
#   registra_studente(studente): registra uno studente nel sistema universitario.
#   registra_docente(docente): registra un docente nel sistema universitario.
#   registra_inserviente(inserviente): registra un inserviente nel sistema universitario.
#   trova_persona(email): restituisce una persona (studente, docente o inserviente) in base all'indirizzo email fornito.
#   elenco_studenti(): stampa l'elenco di tutti gli studenti registrati.
#   elenco_docenti(): stampa l'elenco di tutti i docenti registrati.
#   elenco_inservienti(): stampa l'elenco di tutti gli inservienti registrati.



# Un Elemento Multimediale è una Immagine, un Filmato o una registrazione Audio identificato da un titolo (una stringa non vuota).
# Un elemento è riproducibile se ha una durata (un valore positivo di tipo int) e un metodo play().
# Una registrazione Audio è riproducibile e ha associato anche un volume (un valore positivo di tipo int) e i metodi weaker() e louder() per regolarlo.
# Se riprodotta, ripete per un numero di volte pari alla durata la stampa del titolo concatenato a una sequenza di punti esclamativi di lunghezza
# pari al volume (una stampa per riga).
# Un Filmato è riproducibile e ha associato un volume regolabile analogo a quello delle registrazioni audio e
# anche una luminosità (un valore positivo di tipo int) e i metodi brighter() e darker() per regolarla.
# Se riprodotta, ripete per un numero di volte pari alla durata la stampa del titolo concatenato a una sequenza
# di punti esclamativi di lunghezza pari al volume e poi a una sequenza di asterischi di lunghezza pari alla luminosità (una stampa per riga).
# Una Immagine non è riproducibile, ma ha una luminosità regolabile analoga a quella dei filmati e un metodo show()
# che stampa il titolo concatenato a una sequenza di asterischi di lunghezza pari alla luminosità
# Eseguire un oggetto multimediale significa invocarne il metodo show() se è un'immagine o il metodo play() se è riproducibile.
# Organizzare opportunamente il codice di un lettore multimediale
# che memorizza 5 elementi (creati con valori letti da tastiera) in un array e poi chiede ripetutamente
# all'utente quale oggetto eseguire (leggendo un intero da 1 a 5 oppure 0 per finire) e dopo ogni
# esecuzione fornisce la possibilità di regolarne eventuali parametri (volume / luminosità).