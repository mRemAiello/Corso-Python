# 1. Caricamento dei dati

from sklearn.datasets import load_iris


# Data
# 'sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'target'
# [5.1, 3.5, 1.4, 0.2, 'setosa']

data = load_iris()
X = data.data
y = data.target
print(data)
print(data.feature_names)
print(data.target_names)