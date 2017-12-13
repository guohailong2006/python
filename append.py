import os
list=[]
f=open('1.txt','rw+')
for x  in f:
   #print x 
  #line=line.strip('\n')
   a=x.strip('\n')
   list.append(a)
print list

