from numpy import * #-> numpy : 과학용 계산 패키지
import operator #-> operator : 정렬 기능 제공하는 라이브러리

 
def createDataSet():
    group = array([1,4,10,12,100])
    labels = ['1','2','5','10','20']
    return group, labels
 
 
group, labels = createDataSet()
#print group
#print labels
zz=group.argsort()
print(zz) 

#-> inX : 분류를 위한 입력 벡터
#-> dataSet : 훈련을 위한 예제의 전체 행렬
#-> labels : 분류 항목을 표시한 벡터
#-> k : 투표에서 사용하게 될 최근접 이웃 수
#-> 21행 ~ 26행 : 거리 계산

def classify(inX, dataSet, labels, k):
    #-> dataSet.shape[0] : returns the dimension of the array
    dataSetSize = dataSet.shape[0] 
    #-> tile(A, reps) : A가 reps번 반복된 결과를 하나의 행렬로 만들어 줌
    #- A : 반복하고자 하는 값/행렬, reps : 값/행렬(A)를 반복할 횟수
    diffMat = tile(inX, (dataSetSize,1)) - dataSet 
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()     
    classCount={}
          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
 
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

group, labels = createDataSet()
result = classify([0.0], group, labels, 3)
print result


import matplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
plt.title("The number of Iterations according to the change of 'K' value")
ax.plot(labels[0:10],group[0:10],'rs--')
ax.set_xlabel("K-Means clustering")
ax.set_ylabel("Iterations")
plt.show()