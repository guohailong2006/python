a=[1,2,3]
b=[3,4,5]
list=[]
for i in a:
  if i not in b:
    list.append(i)
for x in b:
  if x not in a:
    list.append(x)
print list
