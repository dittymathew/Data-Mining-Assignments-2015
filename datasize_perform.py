import os,sys
from apriori import Apriori
from time import time
from fp_growth import find_frequent_itemsets
import matplotlib.pyplot as plt
import random

def getRandom(n):
  trans=[]
  for i in range(0,n):
    t=random.choice(T)
    while t in trans:
      t=random.choice(T)
    trans.append(t)
  return trans

transdata =open(sys.argv[1]).readlines()
n=len(transdata)
T= [[int(itm) for itm in t.strip().split(' ')] for t in transdata]

x=[]
y1=[]
y2=[]
s=10
for ln in [10,25,50,100]:
  x.append(ln)
  minsup = (float(s)/float(100))*n
  l = int((float(ln)/float(100))*n)
  
  print 'APRIORI'
  if ln ==100:
    trans =T
  else:
    trans =getRandom(l)
  ap =Apriori(minsup,trans)
  start = time()
  ap.apriori()
  exe_time =time() -start
  print 's=',s,' Execution time :',exe_time
  y1.append(exe_time)
  print 'FP TREE'
  start = time()
  find_frequent_itemsets(T, minsup)
  exe_time =time() -start
  y2.append(exe_time*1000)
  print 's=',s,' Execution time :',exe_time
plt.figure()
plt.plot(x,y1,'b-')
plt.title('Performance od Apriori based on dataset size')
plt.xlabel("Data size (%)")
plt.ylabel("Time (s)")
plt.savefig("results/datasize-apriori.png")
plt.show()
plt.figure()
plt.plot(x,y2,'b-')
plt.title('Performance of Fp-growth based on dataset size')
plt.xlabel("Data size (%)")
plt.ylabel("Time (ms)")
plt.savefig("results/datasize-fpgrowth.png")
plt.show()


