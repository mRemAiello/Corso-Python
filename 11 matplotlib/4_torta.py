from matplotlib import pyplot as plt

slices = [35, 100, 150, 200]
labels = ["si", "no", "forse", "non so"]
colors = ["green", "orange", "blue", "r"]
explode = [0, 0.1, 0, 0]

# Labels inserisce delle etichette
# Colors inserisce dei colori
# Wedge props utilizza un dizionario, ad ogni chiave è associata un'opzione (il valore è il setting di tale opzione)
# Start angle cambia l'angolo di inizio della pie
# Explode "sposta" una o più fette
plt.pie(slices, labels=labels, colors=colors, wedgeprops={"edgecolor": "black"}, startangle=40, explode=explode, autopct="%1.5f%%")

plt.title("Grafico a torta")
plt.show()