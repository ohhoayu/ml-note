def seleceJrand(i,m):
    j=i
    while(j==i):
        j = int(random.uniform(0,m))
    return j

def clipAlpha(aj,H,L):
    if aj>H:
        aj = H
    if L>aj:
        aj = L
    return aj

def smoSimple(dataMatIn,classLabels,C,toler,maxIter):
    dataMatrix = mat(dataMatin);
    labelMat = mat(classLabels).transpose
    b=0;
    m,n=shape(dataMatrix)
    alphas = mat(zeros(m,1))
    iter = 0
    while (iter<maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXj = float(multiply(alphas,labelMat).T*\
                        (dataMatrix*dataMatrix[i,:].T))+b
            #预测变量 y=alphaj*yj*xj*xi+b
            Ej=fXj - float(labelMat[j])#预测分类和实际分类之差
            alphaIold = alpha[i].copy();
            alphaJold = alpha[j].copy();
            if (labelMat[i]!=labelMat[j]):
                L = max(0,alphas[j]-alpha[i])
                H = min(C,C+alpha[j] - alpha[i])
            else:
                L=max(0,alpha[j]+alpha[i]-C)
                H=min(C,alpha[j]+alpha[i])
            if L==H:print("L=H");continue
            eta = 2.0*dataMatrix[i,:]*dataMatrix[j,:].T-\
                  dataMatrix[i,:]*dataMatrix[i,:].T-\
                  dataMatrix[j,:]*dataMatrix[j,:].T
            if eta >= 0 :print"eta>=0";continue#eta是啥呀
            alphas[j]-= labelMat[j]*(Ei - Ej)/eta
            alpha[i]+=labelMat[j]*labelMat[i]*(alphaJold - alpha[j])
            #使用梯度下降法优化
            #解出b

def kernelTrans(X,A,KTup):
    m,n = shape(X)
    K= mat(zeros((m,1)))
    if KTup[0] == 'lin':K=X*A.T
    elif KTup[0]=='rbf':
        for j in range(m):
            deltaRow = X[j,:]-A
            K[j] = deltaRow*deltaRow.T
        K = exp(K /(-1*KTup[1]**2))
    return K

# https://www.jianshu.com/p/55458caf0814
# https://www.cnblogs.com/xxrxxr/p/7536131.html
    
            
