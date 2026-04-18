# ==========================================================
# Clustering con KMeans - Apprendimento non supervisionato
# ==========================================================
# Finora abbiamo sempre usato dati ETICHETTATI (supervisionato):
# sapevamo a quale classe apparteneva ogni campione.
#
# Il CLUSTERING è un metodo NON supervisionato:
#   - NON ha etichette (nessun "target" y)
#   - Cerca di raggruppare i dati in cluster (gruppi) simili
#   - Trova pattern nascosti nei dati
#
# Applicazioni pratiche:
#   - Segmentazione clienti (clienti simili nello stesso gruppo)
#   - Raggruppamento di documenti per argomento
#   - Compressione immagini (raggruppamento colori)
#   - Rilevamento anomalie
#
# KMeans è l'algoritmo di clustering più famoso.
# Come funziona:
#   1. Sceglie K punti casuali come "centroidi"
#   2. Assegna ogni campione al centroide più vicino
#   3. Ricalcola i centroidi come media dei punti assegnati
#   4. Ripete i passi 2-3 fino a convergenza

from sklearn.datasets import load_iris, make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import numpy as np

# ==========================================================
# 1. Esempio base: clustering su dati generati
# ==========================================================
# make_blobs() crea dati sintetici con cluster ben separati.
# Perfetto per capire come funziona KMeans.
X_blobs, y_blobs = make_blobs(
    n_samples=300,       # 300 campioni
    centers=4,           # 4 cluster "veri"
    cluster_std=0.6,     # Dispersione dei punti
    random_state=42
)

print("Esempio con dati sintetici (4 cluster):")
print(f"  Shape: {X_blobs.shape}")

# ==========================================================
# 2. Applicazione di KMeans
# ==========================================================
# n_clusters=4: chiediamo a KMeans di trovare 4 gruppi.
# NOTA: dobbiamo specificare NOI quanti cluster cercare!
# KMeans non sa quanti cluster ci sono realmente.
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

# fit_predict() addestra il modello E restituisce le etichette dei cluster.
# Ogni campione riceve un numero (0, 1, 2, 3) che indica il suo cluster.
etichette = kmeans.fit_predict(X_blobs)

print(f"  Etichette assegnate: {np.unique(etichette)}")
print(f"  Campioni per cluster: {np.bincount(etichette)}")

# I centroidi sono i "punti centrali" di ogni cluster.
print(f"  Centroidi:\n{kmeans.cluster_centers_}")

# ==========================================================
# 3. Silhouette Score: quanto sono buoni i cluster?
# ==========================================================
# Il Silhouette Score misura la qualità del clustering.
# Valore tra -1 e 1:
#   +1 = cluster perfettamente separati
#    0 = cluster sovrapposti
#   -1 = campioni assegnati al cluster sbagliato
#
# In pratica, per ogni campione:
#   - a = distanza media dai punti del proprio cluster
#   - b = distanza media dai punti del cluster più vicino
#   - silhouette = (b - a) / max(a, b)
sil_score = silhouette_score(X_blobs, etichette)
print(f"\n  Silhouette Score: {sil_score:.4f}")

# ==========================================================
# 4. Trovare il numero ottimale di cluster (Elbow Method)
# ==========================================================
# Se non sappiamo quanti cluster ci sono, come scegliamo K?
# Il metodo del "gomito" (Elbow Method):
#   - Proviamo K da 2 a 10
#   - Per ogni K calcoliamo l'inertia (somma delle distanze intra-cluster)
#   - Cerchiamo il punto dove l'inertia smette di diminuire velocemente
#
# L'inertia è la somma delle distanze al quadrato di ogni punto
# dal centroide del proprio cluster. Più bassa = cluster più compatti.
print("\n\nElbow Method (dati sintetici):")
print("-" * 45)

for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_blobs)
    sil = silhouette_score(X_blobs, km.labels_)
    barra = "█" * int(km.inertia_ / 20)
    print(f"  K={k:2d}  Inertia={km.inertia_:8.1f}  Silhouette={sil:.3f}  {barra}")

# Il "gomito" dovrebbe essere a K=4 (i 4 cluster reali)!

# ==========================================================
# 5. Clustering sul dataset Iris (senza usare le etichette)
# ==========================================================
# Proviamo KMeans su Iris, facendo FINTA di non conoscere le specie.
# Poi confrontiamo i cluster trovati con le specie reali.
print("\n\nClustering su dataset Iris:")
print("=" * 50)

data = load_iris()
X = data.data
y_reale = data.target  # Lo usiamo solo per confronto!

# Normalizziamo le feature (KMeans usa le distanze)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Applichiamo KMeans con 3 cluster (sappiamo che le specie sono 3)
kmeans_iris = KMeans(n_clusters=3, random_state=42, n_init=10)
cluster_labels = kmeans_iris.fit_predict(X_scaled)

# ==========================================================
# 6. Confronto cluster vs specie reali
# ==========================================================
# ATTENZIONE: i numeri dei cluster (0, 1, 2) NON corrispondono
# necessariamente alle specie (0=setosa, 1=versicolor, 2=virginica).
# KMeans assegna i numeri in modo arbitrario.
print("\nConfrontiamo cluster trovati vs specie reali:")
print("-" * 50)

for cluster_id in range(3):
    # Per ogni cluster, vediamo quante specie reali contiene
    maschera = cluster_labels == cluster_id
    specie_nel_cluster = y_reale[maschera]
    conteggio = np.bincount(specie_nel_cluster, minlength=3)
    print(f"\n  Cluster {cluster_id}: {conteggio.sum()} campioni")
    for specie_id, nome in enumerate(data.target_names):
        print(f"    {nome:12s}: {conteggio[specie_id]:3d}")

sil_iris = silhouette_score(X_scaled, cluster_labels)
print(f"\n  Silhouette Score Iris: {sil_iris:.4f}")
