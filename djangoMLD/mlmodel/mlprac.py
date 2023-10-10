from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()

x_data = pd.DataFrame(data.data, columns=data.feature_names)
y_data = pd.Series(data=data.target, name="Targets")

print(x_data.head())
print(y_data.shape)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

#print(accuracy_score(y_test, y_pred))

from joblib import dump

dump(model, './../savedmodel/model.joblib')