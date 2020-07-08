import random
import math

#2개의 차원 점의 유클리디안 거리
def eucldist(p0,p1):
    dist = 0.0
    for i in range(0,len(p0)):
        dist += (p0[i] - p1[i])**2
    return math.sqrt(dist)


    
#K-Means Algorithm
def kmeans(k,datapoints):

    # d - datapoints의 차원
    d = len(datapoints[0]) 
    
    Max_Iterations = 1000
    i = 0
    
    cluster = [0] * len(datapoints)
    prev_cluster = [-1] * len(datapoints)
    
    #무작위로 클러스터의 중심(센트로이드) 선택
    cluster_centers = []
    for i in range(0,k):
        new_cluster = []
        cluster_centers += [random.choice(datapoints)]
        force_recalculation = False
    
    while (cluster != prev_cluster) or (i > Max_Iterations) or (force_recalculation) :
        
        prev_cluster = list(cluster)
        force_recalculation = False
        i += 1
    
        for p in range(0,len(datapoints)):
            min_dist = float("inf")
            
            #모든 센트로이드에 대해 최소 거리 확인
            for c in range(0,len(cluster_centers)):
                
                dist = eucldist(datapoints[p],cluster_centers[c])
                
                if (dist < min_dist):
                    min_dist = dist  
                    cluster[p] = c   # 새로운 클러스터에 점 재 할당
        
        
        #Update Cluster's Position
        for k in range(0,len(cluster_centers)):
            new_center = [0] * d
            members = 0
            for p in range(0,len(datapoints)):
                if (cluster[p] == k): #이 점이 클러스터에 속하면
                    for j in range(0,d):
                        new_center[j] += datapoints[p][j]
                    members += 1
            
            for j in range(0,d):
                if members != 0:
                    new_center[j] = new_center[j] / float(members) 
                
                #초기 무작위 할당이 잘못 선택되었음을 의미
                else: 
                    new_center = random.choice(datapoints)
                    force_recalculation = True
                    print "Forced Recalculation..."
                    
            
            cluster_centers[k] = new_center
    
        
    print "======== Results ========"
    print "Clusters", cluster_centers
    print "Iterations",i
    print "Assignments", cluster
    
    
#프로그램 테스트#
if __name__ == "__main__":
    datapoints = [(3,2),(2,2),(1,2),(0,1),(1,0),(1,1),(5,6),(7,7),(9,10),(11,13),(12,12),(12,13),(13,13)]

    k = 1 # K - 클러스터 수
      
    kmeans(k,datapoints) 