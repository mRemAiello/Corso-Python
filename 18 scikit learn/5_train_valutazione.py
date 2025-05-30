from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Caricamento dataset
data = load_iris()
X = data.data
y = data.target

# Suddivisione in train e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Pipeline con scaler e modello di classificazione
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(max_iter=200))
])

# Addestramento del modello
# Fitting -> X_train -> y_train
pipeline.fit(X_train, y_train)

# Predizione sul test set
# Predice su X_test => y_pred
# Controlla y_pred con y_test
y_pred = pipeline.predict(X_test)

# Calcolo dell'accuratezza
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza sul test set: {accuracy * 100:.2f}%")
