import pandas as pd
import numpy as np

# --- Importazione CSV semplice ---
vendite = pd.read_csv('vendite.csv')

# Numero totale di righe
num_righe = len(vendite)

# Tipi di dato
tipi_colonne = vendite.dtypes

# --- Filtraggio righe con condizione ---
filtro = vendite[(vendite['quantità'] >= 10) & (vendite['prezzo_unitario'] < 20)]

# --- Selezione colonne e rinominazione ---
df_item = vendite[['data', 'prodotto']].rename(columns={'prodotto': 'item'})

# --- Ordinamento ---
ordinato = vendite.sort_values(by=['prezzo_unitario', 'quantità'], ascending=[False, True])

# --- Indicizzazione su colonna data ---
vendite['data'] = pd.to_datetime(vendite['data'])
vendite_indicizzato = vendite.set_index('data')
vendite_reset = vendite_indicizzato.reset_index()

# --- Operazione aritmetica vettoriale ---
vendite['ricavo'] = vendite['quantità'] * vendite['prezzo_unitario']

# --- Raggruppamento e aggregazione ---
riepilogo = vendite.groupby('prodotto').agg({
    'quantità': 'sum',
    'ricavo': 'mean'
}).reset_index()

# --- Gestione dei valori nulli ---
clienti = pd.DataFrame({
    'nome': ['Mario', 'Luca', 'Anna'],
    'città': ['Roma', 'Milano', 'Torino'],
    'email': ['mario@mail.com', None, '']
})
clienti['email'] = clienti['email'].replace('', np.nan).fillna('non_disponibile')

# --- Join tra DataFrame ---
ordini = pd.DataFrame({
    'ordine_id': [1, 2, 3],
    'cliente_id': [101, 102, 103],
    'totale': [50, 75, 100]
})
clienti = pd.DataFrame({
    'cliente_id': [101, 102, 103],
    'nome': ['Mario', 'Luca', 'Anna'],
    'città': ['Roma', 'Milano', 'Torino']
})
join_df = pd.merge(ordini, clienti, on='cliente_id', how='inner')

# --- Pivot elementare ---
vendite['mese'] = vendite['data'].dt.to_period('M')
pivot = vendite.pivot_table(index='prodotto', columns='mese', values='quantità', aggfunc='sum')

# --- Esportazione in Excel ---
vendite.to_excel('report_vendite.xlsx', sheet_name='Riepilogo', index=False)

# --- Filtrare righe con pattern di stringa ---
log_web = pd.DataFrame({
    'url': [
        '/home',
        '/checkout/payment',
        '/products',
        '/checkout/confirm'
    ]
})
checkout_urls = log_web[log_web['url'].str.contains('/checkout')]

# --- Operazioni su serie temporali ---
serie = pd.Series(
    np.random.rand(31),
    index=pd.date_range(start='2025-01-01', periods=31, freq='D')
)
media_mobile = serie.rolling(window=7).mean()

# --- Conteggio valori univoci ---
utenti = pd.DataFrame({
    'paese': ['Italia', 'Italia', 'Francia', 'Germania', 'Francia', 'Italia']
})
conteggio_paesi = utenti['paese'].value_counts().sort_values(ascending=False)
