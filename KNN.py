

 #-*-coding:utf-8-*-
from numpy import *
import operator
 
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels;


def classify0(inX, dataSet, labels ,k):
    #shape[0]：第二维个数
    dataSetSize=dataSet.shape[0];
    #tile:重复inX 多少次
    diffMat=tile(inX,(dataSetSize,1))-dataSet;
    sqdiffMat=diffMat**2;
    sqDistances=sqdiffMat.sum(axis=1);
    distances=sqDistances**0.5;

    sortDistIndices=distances.argsort();
    classCount={]
  
    for i in range(k):
        voteIlabel = labels[sortedDistIndices(i)]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1

    sortedClassCount=sorted(classCount.iteritems(),key=operator.itmgetter(1),reverse=True)
    return sortedClassCount[0][0]
    
    
    
