li1=[1,3,5,6]
li2=[2,3,6,9,10]
#l= li1 + li2
list=[]
li2_2=set(li2)
li1_1=set(li1)
li12=li2_2.difference(li1_1)
for x in li12:
    x=list.append(x)
    print x
    
print li1
print li2
print li12
#ls
#s=set(1)
#ll=list(lss)
#print ll
