import pandas as pd

df = pd.read_csv('dataset.csv')
X = df.drop(['Survived', 'Cabin'], axis=1)
y = df['Survived']

# X => Tizio, 20 anni, Uomo, 3 classe
# Y => Sopravvissuto SI

print(X.head(5))
print()
print(y.head(5))