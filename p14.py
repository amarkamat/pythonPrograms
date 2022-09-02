#10
l13=[1,2,3,2,2,1,3,1,2,1,3,3,2,2]
l14=sorted(l13)
print(l13)
l13.sort()
print(l13)
print(l14)

#9
l12=[1,2,3,2,2,1,3,1,2,1,3,3,2,2]
#l12.count()
print(l12)
for e in l12:
    print("Element: ",e,"Index: ",l12.index(e))


#8
#l9=[1,2,3,2,2,1,3,1,2,1,3,3,2,2]
print("Enter elements: ")
l9=[e for e in input().split(',')]
print("list: ",l9)
l10=[]
l11=[]
l9.sort()
print("sorted list: ",l9,len(l9),len(l10))
i=0
j=0
l10.append(l9[i])
k=0
while i<len(l9):
    if l10[j]!=l9[i]:
        j+=1
        l10.append(l9[i])
        l11.append(k)
        k=1
    else:
        k+=1
    i+=1
l11.append(k)
print("distinct list: ",l10)
print("frequency: ",l11)


#7
l7=[1,2.5,5,"hi",6,3+4j]
print("list: ",l7)
l8=[]
for e in l7:
    if type(e)==int:
        l8.append(e)
print("new list: ",l8)
"""
l9=[1,2.5,5,"hi",6,3+4j]
print("list: ",l9)
l10=[e if type(e)==int else  for e in l9]
print("new list: ",l10)
"""

#6
l6=[3,2,6,1,9]
print("list: ",l6)
print("sum: ",sum(l6))

#5
l5=[2,4,1,5,6]
print("list: ",l5)
print("smallest: ",min(l5))

#4
l4=[2,6,1,9,3]
print("list: ",l4)
print("greatest: ",max(l4))

#3
l3=[e for e in range(2,int(input("Enter number: "))*2+1,2)]
print("list: ",l3)

#2
l2=[e for e in range(1,int(input("Enter number: "))*2,2)]
print("list: ",l2)

#1
l1=[e for e in range(1,int(input("Enter number: "))+1)]
print("list: ",l1)

