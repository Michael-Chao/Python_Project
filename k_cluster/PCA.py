from numpy import *

def loadDataSet(fileName, delim = '\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [list(map(float, line)) for line in stringArr]
    return mat(datArr)

def pca(dataMat, topNfeat = 9999999):
    meanVals = mean(dataMat, axis=0)#求取均值
    meanRemoved = dataMat - meanVals#减去均值
    covMat = cov(meanRemoved, rowvar=0)#求取协方差矩阵
    eigVals, eigVects = linalg.eig(mat(covMat))
    eigValInd = argsort(eigVals)
    eigValInd = eigValInd[: -(topNfeat + 1): -1]
    redEigvects = eigVects[:, eigValInd]
    lowDDataMat = meanRemoved * redEigvects
    reconMat = (lowDDataMat * redEigvects.T) + meanVals
    return lowDDataMat, reconMat

#测试
import pandas as pd
dataMat = loadDataSet('test.txt')
lowDMat, reconMat = pca(dataMat, 3)
print(shape(lowDMat))

#show
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:,0].flatten().A[0], dataMat[:,1].flatten().A[0], marker='^',  s= 90)
ax.scatter(reconMat[:,0].flatten().A[0], reconMat[:,1].flatten().A[0], marker='o', s= 50, c ='red')
