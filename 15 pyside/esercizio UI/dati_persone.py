import pandas as pd

# Creiamo un DataFrame con 10 righe e alcune colonne fittizie
data = {
    'Nome': ['Anna', 'Luca', 'Giulia', 'Marco', 'Paolo', 'Sara', 'Francesca', 'Alessandro', 'Giorgia', 'Matteo'],
    'Età': [28, 34, 29, 45, 38, 23, 32, 40, 26, 36],
    'Salario': [3000, 4500, 3200, 5000, 4700, 2900, 4100, 5300, 3100, 4600]
}

# Creiamo il DataFrame
df = pd.DataFrame(data)

# Salviamo il DataFrame come file CSV
csv_file_path = '/mnt/data/dati_persone.csv'
df.to_csv(csv_file_path, index=False)

csv_file_path
