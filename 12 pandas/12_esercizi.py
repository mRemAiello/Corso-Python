# Importazione CSV semplice
#
#     Carica il file vendite.csv (colonne: data, prodotto, quantità, prezzo_unitario). Mostra:
#
#         il numero totale di righe,
#
#         i tipi di dato (dtypes) di ciascuna colonna.
#
# Filtraggio righe con condizione
#
#     Dal DataFrame delle vendite, estrai tutte le righe in cui quantità≥10 e prezzo_unitario<20€.
#
# Selezione colonne e rinominazione
#
#     Crea un nuovo DataFrame con sole colonne data e prodotto, poi rinomina prodotto in item.
#
# Ordinamento
#
#     Ordina il DataFrame originale delle vendite in ordine decrescente di prezzo_unitario, a parità di prezzo ordina per quantità crescente.
#
# Indicizzazione su colonna data
#
#     Converte la colonna data in datetime e impostala come indice. Resetta poi l’indice riportando la colonna al suo posto originario.
#
# Operazione aritmetica vettoriale
#
#     Aggiungi una colonna ricavo calcolata come quantità×prezzo_unitario.
#
# Raggruppamento e aggregazione
#
#     Raggruppa per prodotto e calcola:
#
#         somma di quantità,
#
#         ricavo medio (ricavo).
#
# Gestione dei valori nulli
#
#     Nel DataFrame clienti con colonne nome, città, email, sostituisci i valori
#     mancanti di email con la stringa "non_disponibile".
#
# Join tra DataFrame
#
#     Disponi di due DataFrame:
#
#         ordini (ordine_id, cliente_id, totale)
#
#         clienti (cliente_id, nome, città)
#
#     Esegui un inner join su cliente_id per ottenere nome e città associati a ciascun ordine.
#
# Pivot elementare
#
#     Dal DataFrame delle vendite crea una tabella pivot che mostri,
#     per ogni prodotto, la somma di quantità per mese (data→mese).
#
# Esportazione in Excel
#
#     Salva il DataFrame con i ricavi in un file report_vendite.xlsx, foglio chiamato Riepilogo, senza includere l’indice.
#
# Filtrare righe con pattern di stringa
#
#     Nel DataFrame log_web con colonna url, seleziona le righe in cui l’URL contiene la stringa "/checkout".
#
# Operazioni su serie temporali
#
#     Crea una serie con indice date range giornaliero (1mese) e valori casuali.
#     Calcola la media mobile a 7 giorni.
#
# Conteggio valori univoci
#
#     Nel DataFrame utenti con colonna paese, conta quanti utenti provengono
#     da ciascun paese e ordina il risultato in senso discendente.