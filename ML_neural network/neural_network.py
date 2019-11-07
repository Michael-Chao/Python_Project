import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.io import loadmat
import scipy.optimize as opt
from sklearn.metrics import classification_report#这个包是评价报告

def load_data(path, transepose = True):
    data = loadmat(path)
    y = data.get("y")#得到的数组，既不是行向量，也不是列向量y：[5000:1]，算是列向量
    y = y.reshape(y.shape[0])#让y变成行向量

    X = data.get("X")

    if transepose:
        #需要对图像进行转置，没有这一步的话图像是歪的
        X = np.array([im.reshape((20, 20)).T for im in X])
        X = np.array([it.reshape(400) for it in X])

    return X, y

def plot_100_image(X):
    """ sample 100 image and show them
    assume the image is square

    X : (5000, 400)
    """
    size = int(np.sqrt(X.shape[1]))

    # sample 100 image, reshape, reorg it
    sample_idx = np.random.choice(np.arange(X.shape[0]), 100)  # 100*400
    sample_images = X[sample_idx, :]

    fig, ax_array = plt.subplots(nrows=10, ncols=10, sharey=True, sharex=True, figsize=(8, 8))#
                                #nrows，ncols ：子图网格的行数/列数
                                #sharex，sharey ：True or 'all': x- or y-axis will be shared among all subplots.
    for r in range(10):
        for c in range(10):
            ax_array[r, c].matshow(sample_images[10 * r + c].reshape((size, size)),
                                   cmap=matplotlib.cm.binary)
            plt.xticks(np.array([]))#获取或设置x轴的当前标记位置和标签。
            plt.yticks(np.array([]))
            #绘图函数，画100张图片

def plot_an_image(image):
    """画一个图"""
    fig, ax = plt.subplots(figsize=(1, 1))
    ax.matshow(image.reshape((20, 20)), cmap=matplotlib.cm.binary)
    plt.xticks()
    plt.yticks()

#train 1D model
def sigmoid(z):
    """定义一个S形函数"""
    return 1 / (1 + np.exp(-z))

def cost(theta, X, y):
    """未加正则化项的代价函数"""
    return np.mean(-y * np.log(sigmoid(X @ theta)) - (1 - y) * np.log(1 - sigmoid(X @ theta)))

def regularized_cost(theta, X, y ,l = 1):
    """构造一个正则化代价函数"""
    theta_j1_n = theta[1 : ]
    regularized_term = (1 / (2 * len(X))) * np.power(theta_j1_n, 2).sum()

    return cost(theta, X, y) + regularized_term

def regularized_gradient(theta, X, y, l = 1):
    theta_j1_n = theta[1:]
    regularized_theta = (1 / len(X)) *theta_j1_n

    regularized_term = np.concatenate([np.array([0]), regularized_theta])#concatenate功能：数组拼接
    #这么做是为了使theta没有偏移

    return gradient(theta, X, y) + regularized_term

def gradient(theta, X, y):
    return (1 / len(X)) * X.T @ (sigmoid( X @ theta) - y)

def logistic_regression(X, y, l = 1):
    """generalized logistic regression
    args:
        X: feature matrix, (m, n+1) # with incercept x0=1
        y: target vector, (m, )
        l: lambda constant for regularization

    return：
        trained parameter
        """
    #初始化theta（init theta）
    theta = np.zeros(X.shape[1])

    #train it
    res = opt.minimize(fun=regularized_cost,
                       x0=theta,
                       args=(X, y, l),
                       method="TNC",
                       jac=regularized_gradient,
                       options={"disp": True})

    final_theta = res.x

    return final_theta

def predict(X, theta):
    prob = sigmoid(X @ theta)
    return (prob >= 0.5).astype(int)

#train k model(训练K维模型）
    """所用的函数都是1维模型里面的"""

#神经网络模型
def load_weight(path):
    data = loadmat(path)
    return data["Theta1"], data["Theta2"]

if __name__ == "__main__":
    path = "ex3data1.mat"
    X, y = load_data(path)

    pick_one = np.random.randint(0, 5000)#random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
    plot_an_image(X[pick_one, :])
    print('this should be {}'.format(y[pick_one]))

    #画2500张图片
    plot_100_image(X)
    #plt.show()

    raw_X, raw_y = load_data(path)
    print(raw_X.shape)
    print(raw_y.shape)

    #准备数据
    X = np.insert(raw_X, 0, values=np.ones(X.shape[0]), axis=1)#插入第一列（全为1）
    #value为插入的值；arr为目标向量；obj为目标位置；axis为插入的维度
    # 如果axis=0，则沿着纵轴进行操作；axis=1，则沿着横轴进行操作。
    print(X.shape)

    y_matrix = []
    for k in range(1, 11):
        y_matrix.append((raw_y == k).astype(int))#ndarray.satype():数组的副本，强制转换为指定的类型,在png图片中有此部分解释

    y_matrix = [y_matrix[-1]] + y_matrix[ : -1]
    y = np.array(y_matrix)#将y_matrix整为整体的数组形式
    print(y)
    #将y由5000*1扩展到5000*10

    #训练一维模型
    t0 = logistic_regression(X, y[0])
    print(t0.shape)
    y_pred = predict(X, t0)
    print("Accuracy = {}".format(np.mean(y[0] == y_pred)))

    #训练K维模型
    k_theta = np.array([logistic_regression(X, y[k]) for k in range(10)])
    print(k_theta.shape)

    prob_matrix = sigmoid(X @ k_theta.T)#（5000，10）对于1个观测应有10个sigmoid()结果，选择其中最大的作为这一观测的预测类别
    np.set_printoptions(suppress=True)#设置打印选项  supress；如果为真，则始终使用定点表示法打印浮点数，在这种情况下，当前精度为零的数字将打印为零。
    print(prob_matrix)

    y_pred = np.argmax(prob_matrix, axis=1)#返回沿轴的最大值的索引，axis=1代表行，索引即代表数字
    print(y_pred)

    y_answer = raw_y.copy()
    y_answer[y_answer == 10] = 0#复制y，并把有y[10,...,10,1,...,1,...,9,...,9]变为[0，...0...9]
    print(classification_report(y_answer, y_pred))#构建显示主要分类指标的文本报告

    #神经网络
    theta1, theta2 = load_weight("ex3weights.mat")
    print(theta1.shape, theta2.shape)

    #预先处理数据
    X, y = load_data("ex3data1.mat", transepose=False)
    X = np.insert(X, 0, values=np.zeros(X.shape[0]), axis=1)
    print(X.shape, y.shape)

    #前馈预测
    a1 = X
    z2 = a1 @ theta1.T
    print(z2.shape)#(5000,25)

    z2 = np.insert(z2, 0, values=np.zeros(z2.shape[0]), axis=1)

    a2 = sigmoid(z2)
    print(a2.shape)#（5000,26）

    z3 = a2 @ theta2.T
    print(z3.shape)

    a3 = sigmoid(z3)
    print(a3)

    y_pred1 = np.argmax(a3, axis=1) + 1
    print(y_pred1)

    print(classification_report(y, y_pred1))