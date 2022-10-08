import numpy as np
from numpy import linalg
#from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import math

def euclideandist(x,y):
  d=len(x)
  i=0
  eu_dist=0
  while i<d:
    eu_dist += (x[i]-y[i])*(x[i]-y[i])
    i +=1
  eu_dist =math.sqrt(eu_dist)
  return eu_dist

data =np.loadtxt(open("data/cluster_data.txt","rb"), delimiter=" ")
#km =kmeans(data,2)
#cent=km[0]
#cdist(X, cent, 'euclidean')
#print km
plt.figure()
plt.plot(data[:,0],data[:,1],'*')
plt.show()
x=[]
y1=[]
y2=[]
#k=1
#while k<100:
for k in range(2,11):
  km = KMeans(init='k-means++', n_clusters=k)
  km.fit(data)
  intra_dist=0
  inter_dist=0
  i=0
  while i<k:
    mu =km.cluster_centers_[i]
    cl_dist=0
    np=0
    for l in range(0,len(km.labels_)):
      if km.labels_[l]==i:
#        cl_dist +=euclideandist(data[l][:],mu)
        cl_dist += linalg.norm(mu-data[l][:])
        np +=1
    intra_dist += float(cl_dist)/float(np)
    i+=1
  n=0
  icl_dist=0
  for i in range(0,k-1):
    for j in range(1,k):
      inter_dist += linalg.norm(km.cluster_centers_[i]-km.cluster_centers_[j])
#      if icl_dist>inter_dist:
#        inter_dist =icl_dist
      n +=1
  #    inter_dist += euclideandist(km.cluster_centers_[i],km.cluster_centers_[j])
#  if n>0:

  #  inter_dist =float(icl_dist)/float(n)
  print inter_dist,intra_dist,float(intra_dist)/float(inter_dist),k
  x.append(k)
  y1.append(float(inter_dist)/float(intra_dist))
  y2.append(float(intra_dist)/float(inter_dist))
plt.figure()
plt.plot(x,y2,'b-')
plt.title('Finding No of clusters using knee/elbow')
plt.xlabel("No of Clusters")
plt.ylabel("Intra/inter cluster distance")
plt.savefig("results/findK.png")
plt.show()
#kmeans.fit(data)

