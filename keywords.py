l1=[7,3,2,5,10,20,10,225,3,2,0,22,]
print(l1)
#slice
print (l1[3:8])
#count
print(l1.count(10))
#index
print(l1.index (225))
#index for repited items like 10
print(l1.index (10,5))
#insert
l1.insert(2,66)
print (l1)
# pop -deleat
l1.pop(3,)
print (l1) #2 is deleted
#extend - Add the element in the list
l2 =['a','b','c','d']
print(l2)
print (type(l2))
l1.extend(l2)
print (l1)
#copy all
#l3=l1.copy/ l3=l1[:]/l3=l1
l3=l1
print (l3)
#copy sum element
l4=l1[0:4]
print(l4)
#sort
l5=[12,20,15,36,6,7,92,4,565,98,102,132,332,55,]
l5.sort()
print(l5)
#sort in desinding order
#l5.sort(reverse=true)
#print(l5) #not exacuated
#reverce
l5.reverse()
print(l5)
# nested list
#list inside list
#list compriensing
lc=['ankush','anakit','prasad','sagar','navin','dinu']
a=[word for word in lc if word.startswith("a")]
print(a)
P=[word for word in lc if word.startswith("p")]
print(P)
#list unpacking(n1,n2 should be defined for each element)
l6=[12,15,20,]
n1,n2,n3=l6
print(n1)
print(n2)
print(n3)