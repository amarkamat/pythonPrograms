#10
x=5
y=5
z=x is y
print(id(x),id(y),z)

#9
n=input("Enter a letter from string-program")
o="program"
p = n not in o
print("Is entered data present: ",p)


#8
k=input("Enter a letter from string-python")
l="python"
m = k in l
print("Is entered data present: ",m)

#7
j=input("Enter a number ")
print("Last digit of the number is ", j[2])

#6
i=input("Enter a number ")
print("Middle digit of the number is ", i[1])


#5
h=int(input("Enter a number "))
print("First digit of the number is ", h//100)


#4
f=float(input("Enter a number "))
g=float(input("Enter a power number "))
print(f," Power ",g," is ",f**g)


#3
c=12.3#10#"hi"
d=13.2#20#"hello"
print(c,d)
e=c
c=d
d=e
print(c,d)

#2
b=int(input("Enter a number "))
print("Last digit of the number is ", b%10)

#1
a=int(input("Enter a number "))
print("Number without last digit is ", a//10)