from sklearn import linear_model
import numpy as np
import pandas as pd

def data_process(data):
    cols = data.shape[1]
    X = data.iloc[:, :cols - 1]
    y = data.iloc[:, cols - 1 : cols]
    return X, y

def logistic(X, y):
    model = linear_model.LinearRegression()
    model.fit(X, y)
    return model.score(X, y)

def regularized_logistic(X, y):
    model = linear_model.LogisticRegression()
    model.fit(X, y)
    return  model.score(X, y)

if __name__ == "__main__":
    path1 = "ex2data1.txt"
    data1 = pd.read_csv(path1, header=None, names=["Test1", "Test2", "Admitted"])
    print(data1.head())

    X, y = data_process(data1)
    print(logistic(X, y))

    #正则化逻辑回归
    path2 = "ex2data2.txt"
    data2 = pd.read_csv(path1, header=None, names=["Test1", "Test2", "Admitted"])
    print(data2.head())

    X2, y2 = data_process(data2)
    print((regularized_logistic(X2, y2)))