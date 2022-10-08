import sys
from itertools import combinations,chain

class Apriori:
  def __init__(self,minsup,Trans):
    self.minsup =minsup
    self.T= Trans

  def getCandidateGen(self,Fk_items):
    can=[]
    f1f2 =combinations(Fk_items,2)
    for comb in f1f2:
      flag=0 
      k=len(comb[0])
      for i in range(0,k-1):
        if comb[0][i] != comb[1][i] :
          flag=1
      if flag ==0 and int(comb[0][k-1])<int(comb[1][k-1]):
        c=[comb[0][i] for i in range(0,k)]
        c.append(comb[1][k-1])
        add_c=1
      
        for s in self.subsets(c,k):
          if s not in Fk_items:
            add_c=0
            break
        if add_c ==1:
          can.append(c)
    return can        

  def subsets(self,S,k):
    subS= [[s1 for s1 in s if s1 !=''] for s in chain(*[combinations(S, i + 1) for i, a in enumerate(S)]) if len(s)==k]
    return subS

  def findFrequentItemset(self):
    itemcount={}
    freq_items=[]
    for itemset in self.T:
      for item in itemset:
        if item not in itemcount:
          itemcount[item]=0
        itemcount[item] +=1
    for item in itemcount:
      sup =itemcount[item]
      if sup>=self.minsup:
        freq_items.append([item])
    freq_items.sort()
    return [freq_items,itemcount]

  def apriori(self):
    no=0
    freq_items ={}
    [freq_items[1],itemCount]=self.findFrequentItemset()
    k=2
    fk=freq_items[1]
    for i in range(0,len(fk)):
      for j in range(0,len(fk[i])):
        print str(fk[i][j])+' ',
      no +=1
      print 
    while freq_items[k-1] !=[]:
      can =self.getCandidateGen(freq_items[k-1])
      can_dict ={can.index(c):c for c in can}
      can_count={}
      for t in self.T:
        for c_idx in can_dict:
          c=can_dict[c_idx]
          c_present=1
          for ci in c:
            if ci  not in t:
              c_present=0
              break
          if c_present==1:
            if c_idx not in can_count:
              can_count[c_idx]=0
        
            can_count[c_idx] +=1
      fk=[]
      for c_idx in can_count:
        if can_count[c_idx]>=self.minsup:
          fk.append(can_dict[c_idx])
      fk.sort()
      freq_items[k]=fk
      for i in range(0,len(fk)):
        for j in range(0,len(fk[i])):
          print str(fk[i][j])+' ',
        no +=1
        print
      k +=1
    print no


if __name__ == '__main__':

  transdata =open(sys.argv[1]).readlines()
  n=len(transdata)
  minsup = (float(sys.argv[2])/float(100))*n
  T= [[int(itm) for itm in t.strip().split(' ')] for t in transdata]
  ap =Apriori(minsup,T)
  ap.apriori()
