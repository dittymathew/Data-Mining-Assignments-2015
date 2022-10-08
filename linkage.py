from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import numpy as np
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

y =[[0.4,0.53], [0.22,0.39], [0.35,0.32], [0.26,0.19], [0.08,0.41], [0.45,0.30]]
Y = linkage(y, method='single')
Z1 = dendrogram(Y, orientation='top',labels=["1", "2", "3", "4","5","6"])
print Z1
idx1 = Z1['leaves']

for i in range(0,6):
  print i+1,
  for j in range(0,6):
    print ' & ',round(euclideandist(y[i],y[j]),4),
  print '\\\\'

plt.plot(idx1)
plt.show()

