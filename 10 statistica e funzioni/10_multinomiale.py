# Distribuzione Multinomiale
# Generalizzazione della binomiale a più di 2 esiti possibili.
# Esempio: lancio di un dado (6 esiti) ripetuto n volte.

import numpy as np
import matplotlib.pyplot as plt

# Parametri
n = 100     # numero di prove
# Probabilità per ciascun esito (devono sommare a 1)
pvals = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]  # dado equo
categorie = ['1', '2', '3', '4', '5', '6']

# Genera un singolo esperimento multinomiale
risultato = np.random.multinomial(n, pvals)
print(f"Risultato di {n} lanci di dado: {risultato}")

# Genera più esperimenti
num_esperimenti = 1000
esperimenti = np.random.multinomial(n, pvals, size=num_esperimenti)

# Media dei conteggi per ogni categoria
medie = esperimenti.mean(axis=0)

# Grafico del singolo esperimento
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(categorie, risultato, color='steelblue', edgecolor='black', alpha=0.7)
ax1.axhline(y=n/6, color='red', linestyle='--', label=f'Valore atteso ({n/6:.1f})')
ax1.set_title(f'Singolo esperimento ({n} lanci)')
ax1.set_xlabel('Faccia del dado')
ax1.set_ylabel('Conteggio')
ax1.legend()

# Grafico delle medie su molti esperimenti
ax2.bar(categorie, medie, color='coral', edgecolor='black', alpha=0.7)
ax2.axhline(y=n/6, color='red', linestyle='--', label=f'Valore atteso ({n/6:.1f})')
ax2.set_title(f'Media su {num_esperimenti} esperimenti')
ax2.set_xlabel('Faccia del dado')
ax2.set_ylabel('Conteggio medio')
ax2.legend()

plt.tight_layout()
plt.show()

# Dado truccato
pvals_truccato = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]  # il 6 esce più spesso
esperimenti_truccato = np.random.multinomial(n, pvals_truccato, size=num_esperimenti)
medie_truccato = esperimenti_truccato.mean(axis=0)

plt.figure(figsize=(8, 5))
larghezza = 0.35
x_pos = np.arange(len(categorie))
plt.bar(x_pos - larghezza/2, medie, larghezza, label='Dado equo', color='steelblue', alpha=0.7)
plt.bar(x_pos + larghezza/2, medie_truccato, larghezza, label='Dado truccato', color='coral', alpha=0.7)
plt.xticks(x_pos, categorie)
plt.title('Confronto: dado equo vs dado truccato')
plt.xlabel('Faccia del dado')
plt.ylabel('Conteggio medio')
plt.legend()
plt.grid(True, axis='y')
plt.show()
