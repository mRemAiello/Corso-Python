# 1. Caricamento dei dati

from sklearn.datasets import load_iris


data = load_iris()
X = data.data
y = data.target
print(data)
print(data.feature_names)
print(data.target_names)