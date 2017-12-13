import random
s1=(1,2,3)
s2=(3,4,5)
s1_1=set(s1)
s2_2=set(s2)
t=list()
for i in s1_1:
  if i not in s2_2:
    t.append(i)
print t
