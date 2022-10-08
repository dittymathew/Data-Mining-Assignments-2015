import os,sys
from apriori import Apriori
from time import time
from fp_growth import find_frequent_itemsets
import matplotlib.pyplot as plt

transdata =open(sys.argv[1]).readlines()
n=len(transdata)
T= [[int(itm) for itm in t.strip().split(' ')] for t in transdata]

x=[]
y1=[]
y2=[]
for s in range (1,50):
  x.append(s)
  minsup = (float(s)/float(100))*n
  print 'APRIORI'
  ap =Apriori(minsup,T)
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
plt.title('Performance of Apriori based on support threshold')
plt.xlabel("Support (%)")
plt.ylabel("Time (s)")
plt.savefig("results/supportComp-apriori.png")
plt.show()
plt.figure()
plt.plot(x,y2,'b-')
plt.title('Performance of Fp-growth based on support threshold')
plt.xlabel("Support (%)")
plt.ylabel("Time (ms)")
plt.savefig("results/supportComp-FPgrowth.png")
plt.show()

