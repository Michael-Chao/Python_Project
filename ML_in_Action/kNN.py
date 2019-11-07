from numpy import *
import operator

def creatDataset():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ["A", "A", "B", "B"]
    return group, labels

def classify0(inX, dataSet, labels, k):#labels:标签向量
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    Distances = sqDistances ** 0.5
    sortedDistance = Distances.argsort()
    classCount = {}#这是一个字典，用于计数，即用于存储不同标签（labels）出现的次数
    for i in range(k):
        voteIlabel = labels[sortedDistance[i]]# 从前面已经排好序的矩阵中选择距离最小的k个点并获得这k个点所对应的标签，也就是前k个点，k是你在使用时具体输入的，书上k是3，所以就提炼出了前3个训练数据集的标签
        # sortedDistIndicies[i]是索引值，正好与label的值的索引是对应的
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1  # classCount[voteIlabel]是个变量名，别多想，然后voteIlabel是前k个，也就是距离最小的k个训练数据集所对应的标签（labels），现在利用dict.get(key, default=None)函数来统计这k个的标签出现的次数，key就是dict中的键voteIlabel，如果不存在则返回一个0并存入dict（这里的dict就是classCount），如果存在则读取（get）当前值（标签），并在classCount中加1
        # 最后得到的classCount{}应该是类似这种样子的：classCount{'A':3,'B':0}

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def file2mateix(filename):
    fr = open(filename)
    arrayOlines = fr.readlines()
    print(arrayOlines)
    numberOflines = len(arrayOlines)
    returnMat = zeros((numberOflines, 3))#3列可调
    classLabelVector = []
    index = 0
    for i in arrayOlines:
        line = line.strip()
        listFrome

if __name__ == "__main__":
    group, labels= creatDataset()
    print(classify0([0,0], group, labels, 3))