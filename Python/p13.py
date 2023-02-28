#10
print("Enter elements of list")
l2=[int(b) for b in input().split(',')]
print(l2)

#9
print("Enter city names seperated by comma: ")
l1=[a for a in input().split(',')]
print(l1,type(l1),len(l1))

#8
thislist = ["Java", "SQL","C","Reactjs", "Javascript", "Python"]
print(thislist)
newlist=sorted(thislist)
print(newlist)
print(thislist)
thislist.sort()
print(thislist)

#7
thislist=["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1

#6
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
print(firstlist)
print(secondlist)
firstlist[3:6]=secondlist
print(firstlist)
firstlist.extend(secondlist)
print(firstlist)

#5
mylist=["Java", "SQL", "C", "Reactnative"]
print(mylist)
mylist.append("Python")
print(mylist)

#4
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
print(thislist)
for a in thislist:
    if a=="SQL":
        thislist[1]="NoSQL"
    if a=="Reactnative":
        thislist[3]="Flutter"
print(thislist)

thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
print(thislist)
i=0
while i<len(thislist):
    if thislist[i]=="SQL":
        thislist[i]="NoSQL"
    if thislist[i]=="Reactnative":
        thislist[i]="Flutter"
    i+=1
print(thislist)


#3
mylist = ["Java", "C", "Python"]
print(mylist[2],mylist[-1])


#2
l2=[1,"Python",2.5,3+4j]
print(l2,type(l2))


#1
l1=["Java","Python","SQL","C"]
print(l1,type(l1))
