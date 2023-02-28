#10
n=int(input("Enter number: "))
m=n
o=0
l=[]
if n>=0 and n<=7:
    l.append(str(n))
else:
    while m//8!=0:
        o=m%8
        m=m//8
        l.append(str(o))
        if m>=0 and m<=7:
            l.append(str(m))

l.append(str('o'))
l.append(str('0'))
l.reverse()

print("Octal of {}: {}".format(n,''.join(l)))
print("Octal is : ",oct(n))


#9
n=int(input("Enter number: "))
m=n
b=0
l=[]
if n!=0 and n!=1:
    while m//2!=0:
        b=m%2
        m=m//2
        l.append(str(b))
        if m==1:
            l.append(str(m))
else:
    l.append(str(n))

l.append(str('b'))
l.append(str('0'))
l.reverse()

print("Binary of {}: {}".format(n,''.join(l)))
print("Bin is : ",bin(n))


#8
n=int(input("Enter number: "))
i=0
sum=0
m=n
while m!=0:
    sum=sum+(m%10)
    m=m//10
    i+=1
print("Digit Sum of {}: {}".format(n,sum))


#7
n=int(input("Enter number: "))
i=0
m=n
while m!=0:
    m=m//10
    i+=1
print("Digit count of {}: {}".format(n,i))


#6
n=int(input("Enter number: "))
i=1
mul=1
if n>0:
    while i<=n:
        mul=mul*i
        i+=1
print("Factorial of {}: {}".format(n,mul))


#5
n=int(input("Enter number: "))
i=2
sum=0
while i<=n*2:
    sum=sum+i
    i+=2
print("Sum of N even numbers",sum)


#4
n=int(input("Enter number: "))
i=1
sum=0
while i<=n*2:
    sum=sum+i
    i+=2
print("Sum of N odd numbers",sum)


#3
n=int(input("Enter number: "))
i=1
sum=0
while i<=n:
    sum=sum+(i**3)
    i+=1
print("Sum of cubes of N numbers",sum)


#2
n=int(input("Enter number: "))
i=1
sum=0
while i<=n:
    sum=sum+(i**2)
    i+=1
print("Sum of squares of N numbers",sum)


#1
n=int(input("Enter number: "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print("Sum of N numbers",sum)


