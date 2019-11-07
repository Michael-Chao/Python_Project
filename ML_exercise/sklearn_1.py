from sklearn import linear_model
import numpy as np

path = ""
data = pd.read_csv(path, header = None, names = [])
model = linear_model.LinearRegression()
model.fit(X, y)

x = np.arange(X[:, 1].A1)
y = model.predict(X).flatten()

Draw Picture as linear_regression.py