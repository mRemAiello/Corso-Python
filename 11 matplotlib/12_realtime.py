import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Inizializza i dati
x_data = []
y_data = []

# Crea la figura e l'asse
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')  # Linea rossa

# Imposta i limiti del grafico
ax.set_xlim(0, 100)
ax.set_ylim(0, 10)


# Funzione di inizializzazione: imposta i dati di base (vuoti)
def init():
    line.set_data([], [])
    return line,


# Funzione di aggiornamento dei dati, chiamata ad ogni intervallo
def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame * 0.1) + np.random.normal(0, 0.1))  # Esempio di dati dinamici
    line.set_data(x_data, y_data)

    # Espande i limiti dell'asse man mano che i dati crescono
    ax.set_xlim(0, frame + 1)
    return line,


# Animazione: aggiorna il grafico ogni 100 ms
ani = FuncAnimation(fig, update, frames = np.arange(0, 100), init_func = init, blit = True, interval = 100)

# Mostra il grafico
plt.grid()
plt.show()