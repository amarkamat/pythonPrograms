#12
o=complex(input("Enter complex number: "))
print(o)
if o.real>o.imag:
    print("Real is greater")
elif o.imag>o.real:
    print("Imag is greater")
else:
    print("Both are equal")

#11
n=int(input("Enter Month in numeric format"))
if n==1:
    print("31 days")
elif n==2:
    print("28 days")
elif n==3:
    print("31 days")
elif n==4:
    print("30 days")
elif n==5:
    print("31 days")
elif n==6:
    print("30 days")
elif n==7:
    print("31 days")
elif n==8:
    print("31 days")
elif n==9:
    print("30 days")
elif n==10:
    print("31 days")
elif n==11:
    print("30 days")
elif n==12:
    print("31 days")
else:
    print("Invalid")


#10
k=int(input("Enter first number: "))
l=int(input("Enter second number: "))
m=int(input("Enter third number: "))
if k>l and k>m:
    print("First number is greater")
elif l>m and l>k:
    print("Second number is greater")
elif m>k and m>l:
    print("Third number is greater")
else:
    if k==m and k==l:
        print("All are equal")
    if k==m and l>k:
        print("Second number is greater")
    if l==m and k>m:
        print("First number is greater")
    if l==k and m>l:
        print("First number is greater")


#9
j=int(input("Enter a year: "))
if j%4!=0:
    print("Common year")
elif j%100!=0:
    print("Leap year")
elif j%400!=0:
    print("Common year")
else:
    print("Leap year")

#8

#7
i=int(input("Enter a number"))
if i>0:
    print("Positive number")
elif i<0:
    print("Negetive number")
else:
    print("Zero number")

#6
h=int(input("Enter a number: "))
if h>99 and h<1000:
    print("3 digit number")
else:
    print("Not a 3 digit number")

#5
f=input("Enter first word: ")
g=input("Enter second word: ")
print("Words in dictionary order")
if f>g:
    print(g,f)
elif g>f:
    print(f,g)
else:
    print(f,g)

#4
d=int(input("Enter first number"))
e=int(input("Enter second number"))
if d>e:
    print("first number is greater")
elif e>d:
    print("second number is greater")
else:
    print("Numbers are equal")

#3
c=int(input("Enter a number"))
if c%2==0:
    print("Number is even")
else:
    print("Number is odd")

#2
b=int(input("Enter a number"))
if b%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

#1
a=int(input("Enter a number"))
if a>0:
    print("Positive Number")
else:
    print("Non positive number")


