from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.pipeline import Pipeline


# Iris
data = load_iris()
X = data.data
y = data.target
print(data.feature_names)
print(data.target_names)


# Divisione del dataset: train e test
# test_size è la grandezza del dataset destinata al test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train[0:5])
print(y_train[0:5])
print()

# Normalizzazione
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(X_scaled[0:5])
print()


# Encoding
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)


# Costruzione di pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    # ('encoder', OneHotEncoder()),  # se necessario
    # ('model', LogisticRegression())  # nella prossima lezione
])
X_transformed = pipeline.fit_transform(X)

#
print(X_transformed[0:5])