#10 Write a python script to calculate HCF of two numbers
#9 Write a python script to calculate LCM of two numbers
import math
def factor(t):
    i=2
    l=[]
    while i<=t:
        if t%i==0:
            l.append(i)
            t=t//i
            i=2
        else:
            i+=1
    return l
n1,n2=28,12
l1=factor(n1)
l2=factor(n2)
print("Factors of ",n1," : ",l1)
print("Factors of ",n2," : ",l2)
l3,l4=[],[]
for e in l1:
    for i in l2:
        if e==i:
            l2.remove(i)
            l3.append(e)
            break
    else:
        l4.append(e)
l4=l4+l3+l2
print("HCF is: ",math.prod(l3))
print("LCM is: ",math.prod(l4))

#8
a=int(input("Enter number: "))
l=[0,1]
i=2
while i<a:
    l.append(l[-1]+l[-2])
    i+=1
print("Fibonacci series",l)


#7
a=int(input("Enter first number: "))
z=int(input("Enter second number: "))
b=False
i=2
while i<(a if a>z else z):
    if a%i==0 and z%i==0:
        break
    i+=1
else:
    b=True
print("Is ({},{}) Co-Prime numbers : {}".format(a,z,b))


#6
n=int(input("Enter count: "))
l=[]
k=0
m=2
while m:
    b=False
    i=2
    while i<m:
        if m%i==0:
            break
        i+=1
    else:
        k+=1
        l.append(m)
        b=True
        if k>=n:
            break
    m+=1
print("Count: {} \nPrime numbers: {}".format(n,l))



#5
a=int(input("Enter number: "))
c=0
m=a+1
while m:
    b=False
    i=2
    while i<m:
        if m%i==0:
            break
        i+=1
    else:
        c=m
        b=True
        break
    m+=1
print("Next Prime number after {} is {}".format(a,c))


#4
a=int(input("Enter start: "))
z=int(input("Enter end: "))
l=[]
m=a
while m<=z:
    b=False
    i=2
    while i<m:
        if m%i==0:
            break
        i+=1
    else:
        l.append(m)
        b=True
    m+=1
print("Prime numbers ({}-{}): {}".format(a,z,l))


#3
l=[]
m=2
while m<=100:
    b=False
    i=2
    while i<m:
        if m%i==0:
            break
        i+=1
    else:
        l.append(m)
        b=True
    m+=1
print("Prime numbers (1-100): {}".format(l))


#2
n=int(input("Enter number: "))
b=False
i=2
while i<n:
    if n%i==0:
        break
    i+=1
else:
    b=True
print("Is {} Prime number?: {}".format(n,b))


#1
n=input("Enter number: ")
print("Reverse of {}: {}".format(n,n[::-1]))


