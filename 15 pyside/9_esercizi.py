# Creazione di una Finestra Base
#
#     Crea una finestra vuota utilizzando PySide6. La finestra deve avere
#     un titolo personalizzato e dimensioni di 400x300 pixel.


# Aggiunta di un Pulsante
#
#     Aggiungi un pulsante al centro della finestra. Quando il pulsante viene cliccato,
#     deve stampare un messaggio di testo nella console.


# Interfaccia con Più Widget
#
#     Crea un'interfaccia che contenga due etichette (label), un campo di testo e due pulsanti:
#     "Conferma" e "Annulla". Quando si clicca su "Conferma", il testo inserito deve
#     essere mostrato in una seconda etichetta sotto i pulsanti. Quando clicchi "Annulla"
#     cancella il contenuto della seconda etichetta.


# Layout Orizzontale e Verticale
#
#     Crea una finestra che utilizzi un layout orizzontale e verticale.
#     In un layout orizzontale in alto, posiziona tre pulsanti allineati a sinistra, centro e destra.
#     Sotto, aggiungi un'area di testo in un layout verticale che occupi il resto dello spazio disponibile.


# Finestra con QMainWindow
#
#     Implementa una finestra utilizzando QMainWindow. Aggiungi una barra dei menu con le voci "File" e "Modifica".
#     Sotto la barra dei menu, crea una toolbar con icone per "Apri", "Salva" e "Chiudi".


# Dialog Personalizzata
#
#     Crea una finestra di dialogo personalizzata che permetta all'utente di inserire nome e cognome.
#     Dopo aver premuto "OK", la finestra di dialogo si chiude e i dati inseriti vengono mostrati in una finestra principale.


# Uso dei Segnali e Slot
#
#     Crea una finestra con due pulsanti. Il primo pulsante deve inviare un segnale
#     personalizzato che aggiorni un'etichetta con un testo predefinito.
#     Il secondo pulsante deve ripristinare il testo dell'etichetta allo stato originale.


# Threading con QThread
#
#     Implementa una finestra che avvii un thread secondario quando viene cliccato un pulsante.
#     Il thread deve simulare un'operazione lunga di 5 secondi, durante la quale la finestra principale
#     rimane reattiva. Alla fine del thread, aggiorna un'etichetta con un messaggio di completamento.


# Applicazione Multi-Finestra
#
#     Crea un'applicazione che utilizzi due finestre separate. La prima finestra deve avere
#     un pulsante che apre una seconda finestra di dialogo.
#     Quando si inserisce un testo nella seconda finestra e si preme "OK", il testo deve apparire nella prima finestra.


# Gestione di File con QFileDialog
#
#     Implementa un'applicazione con una barra dei menu che contiene l'opzione "Apri File".
#     Quando viene selezionata questa opzione, deve aprirsi una finestra di dialogo per
#     la selezione di file. Il percorso del file selezionato deve essere mostrato in
#     un'etichetta all'interno della finestra principale.