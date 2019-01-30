
from numpy import *
import sys

def loadDataSet():
    postingList=[['my','dog','has','flea','problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    ##分别表示标签
    return postingList,classVec ##返回输入数据和标签向量

def createVocabList(dataSet):
    vocabSet = set([]);
    for document in dataSet:
        vocabSet = vocabSet | set (document)#所有文本共有的词汇
    return list(vocabSet)#将元组转化为列表


def setOfwords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:print ("the word: %s is not in it" % word)
    return returnVec

def trainNBO(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)#训练数据总数
    numWords = len(trainMatrix[0])#总词汇数
    pAbusive = sum(trainCategory)/float(numTrainDocs)#p(c)
    p0Num = zeros(numWords);
    p1Num = zeros(numWords);
    p0Denom = 0.0;
    p1Denom = 0.0;
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])

    p1Vect=p1Num/p1Denom
    p0Vect=p0Num/p0Denom
    return p0Vect, p1Vect, numTrainDocs
            
        
    
