t1=tuple('1234')
t2=tuple('23345')
print t1
print t2
s1 = set (t1)
s2 = set (t2)
print  s1
print s2
d12=s1.difference(s2)
d21=s2.difference(s1)
print d12,d21
for x in d21:
    d12.add(x)
print d12
