import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def DataPre(data):
    """数据预处理"""
    data.insert(0, "Ones", 1)
    #print(data.head())
    cols = data.shape[1]
    X = data.iloc[:, :cols - 1]
    y = data.iloc[:, cols - 1: cols]
    X = np.matrix(X.values)
    y = np.matrix(y.values)
    theta = np.matrix(np.zeros(X.shape[1]))
    return X, y, theta

def costFunction(X, y, theta):
    """计算代价函数"""
    cost = np.power((X * theta.T) - y, 2)
    return np.sum(cost) / (2*len(X))

def gradientDescent(X, y, theta, alpha, iters):
    """批量梯度下降"""
    temp = np.matrix(np.zeros(theta.shape[1]))
    cost = np.zeros(iters)
    for i in range(iters):
        inner = (X * theta.T) - y
        for j in range(theta.shape[1]):
            term = np.multiply(inner, X[:, j])
            temp[0, j] = theta[0, j] - (alpha/len(X)) * np.sum(term)

        theta = temp
        cost[i] = costFunction(X, y, theta)
    return theta, cost



def scatterFunction():
    """画散点图"""
    data.plot(kind="scatter", x="Population", y="Profit", figsize=(16,6))
    plt.show()

def subplot():
    """线性回归图"""
    x = np.array(X[:, 1].A1)
    y = g[0, 0] + g[0, 1] * x

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(x, y, 'r', label="Prediction")
    ax.scatter(data.Population, data.Profit, label="Training Data")
    ax.legend(loc=2)
    ax.set_xlabel("Population")
    ax.set_ylabel("Profit")
    ax.set_title("Predicted Profit vs. Population Size")

def pltcost():
    """绘制梯度下降函数"""
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.plot(np.arange(iters), cost, "r")
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Cost')
    ax.set_title('Error vs. Training Epoch')

if __name__ == '__main__':
    """scatter plot"""
    path = "E:\\my AI\\Coursera-ML-AndrewNg-Notes-master\\code\\ex1-linear regression\\ex1data1.txt"
    data = pd.read_csv(path, header=None, names=["Population", "Profit"])
    # print(data.head())
    # print(data.describe())
    #scatterFunction()

    #Gradient Decent
    X, y, theta = DataPre(data)
    #print(X.shape, y.shape, theta.shape)
    #print(costFunction(X, y, theta))
    alpha = 0.01
    iters = 1000
    g, cost = gradientDescent(X, y, theta, alpha, iters)
    print(g)
    costFunction(X, y, theta)
    subplot()
    pltcost()
    plt.show()

