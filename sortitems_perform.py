import os,sys
from apriori import Apriori
from time import time
from fp_growth import find_frequent_itemsets
import matplotlib.pyplot as plt
import operator


def findItemsCount():
  itemcount={}
  for itemset in T:
    for item in itemset:
      if item not in itemcount:
        itemcount[item]=0
      itemcount[item] +=1
  return itemcount

def sortItems(items):
  sorted_items=sorted(items.iteritems(),key=operator.itemgetter(1),reverse=True)
  return sorted_items

def getNPerItems(items,n1):
  N=len(items)
  n1 = int((float(n1)/float(100))*N)
  nitems=[]
  for i in range(0,n1):
    nitems.append(items[i][0])
  return nitems

def getTrans(n1):
  itemcount =findItemsCount()
  sorted_items =sortItems(itemcount)
  nitems =getNPerItems(sorted_items,n1)
  trans=[]
  for t in T:
    t1=[itm for itm in t if itm in nitems ]
    trans.append(t1)
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
  
  print 'APRIORI'
  trans =getTrans(ln)
  ap =Apriori(minsup,trans)
  start = time()
  ap.apriori()
  exe_time =time() -start
  print 's=',ln,' Execution time :',exe_time
  y1.append(exe_time)
  print 'FP TREE'
  start = time()
  find_frequent_itemsets(T, minsup)
  exe_time =time() -start
  y2.append(exe_time*1000)
  print 's=',ln,' Execution time :',exe_time
plt.figure()
plt.plot(x,y1,'b-')
plt.title('Performance od Apriori based on sorted items')
plt.xlabel("No of items (%)")
plt.ylabel("Time (s)")
plt.savefig("results/sortitems-apriori.png")
plt.show()
plt.figure()
plt.plot(x,y2,'b-')
plt.title('Performance of Fp-growth based on sorted items')
plt.xlabel("No of items (%)")
plt.ylabel("Time (ms)")
plt.savefig("results/sortitems-fpgrowth.png")
plt.show()


