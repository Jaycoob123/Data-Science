import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_circles
from sklearn.svm import SVC  #clasifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('data/heart.csv', comment='#')


X, y = make_circles(n_samples=526, factor=0.5, random_state=0, noise=0.2)
print(X)
print(y)
plt.scatter(X[:, 0], X[:, 1], c=y) # X oznacza weź wszystkie listy w tej liście. Dwokropek oznacza wejdź w każdy z tych punktówy
# Każdą z par współrzędnych. Weż 0, czyli pierwszy element (tutaj: pierwszą współrzędną). Potem weż 1, czyli drugi element (tutaj: drugą współrzędną)
plt.show()

print('\nDescribe:')
print(df.describe().T.round(2).to_string())


X = df.iloc( : , :-1)
Y = df.target

(X_train, y_train)
print( X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

model = LogisticRegression()
model.fidel.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('\nKNN')
model = KNeighborsClassifier()
model.fit# # print('\nRegresja logistyczna')(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('\nDrzewo decyzyjne')
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('\nSVN')
model = SVC()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))