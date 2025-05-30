import pandas as pd

df = pd.read_csv('dataset.csv')
X = df.drop('Survived', axis=1)
y = df['Survived']

# X => Tizio, 20 anni, Uomo, 3 classe
# Y => Sopravvissuto SI