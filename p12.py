#4
a,b=int(input("Enter range: "))
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


