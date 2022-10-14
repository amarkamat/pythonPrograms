#10 Write a recursive python function to find the Nth term of the Fibonacci series.
def fib(n,a=0,b=1):
#    a,b=0,1
    if n>2:
        a,b=b,a+b
        b=fib(n-1,a,b)
    return b
print(fib(10))

#9 Write a recursive python function to print octal of a given decimal number
def octal(n):
    l=[]
    if n//8!=0:
        l = octal(n//8)
        l.append(str(n%8))
    else:
        l.append(str(n%8))
    return l
print(octal(100))

#8 Write a recursive python function to print binary of a given decimal number.
def binary(n):
    l=[]
    if n//2!=0:
        l = binary(n//2)
        l.append(str(n%2))
    else:
        l.append(str(n%2))
    return l
print(binary(100))

#7 Write a recursive python function to calculate sum of the digits of a given number
def sumdig(n):
    s=0
    if n//10!=0:
        s = n%10 + sumdig(n//10)
    else:
        s+=n
    return s
print(sumdig(1202))

#6 Write a recursive python function to calculate the factorial of a number.
def fact(n):
    s=1
    if n>0:
        s=n*fact(n-1)
    return s
print(fact(10))

#5 Write a recursive python function to calculate sum of cubes of first N natural numbers
def sumcubnums(n):
    s=0
    if n>0:
        s=n**3+sumcubnums(n-1)
    return s
print(sumcubnums(10))

#4 Write a recursive python function to calculate sum of squares of first N natural numbers
def sumsqnums(n):
    s=0
    if n>0:
        s=n*n+sumsqnums(n-1)
    return s
print(sumsqnums(10))

#3 Write a recursive python function to calculate sum of first N even natural numbers
def sumevennums(n):
    s=0
    if n>0:
        s=(n*2)+sumevennums(n-1)
    return s
print(sumevennums(10))

#2 Write a recursive python function to calculate sum of first N odd natural numbers
def sumoddnums(n):
    s=0
    if n>0:
        s=(n*2-1)+sumoddnums(n-1)
    return s
print(sumoddnums(10))


#1 Write a recursive python function to calculate sum of first N natural numbers
def sumnums(n):
    s=0
    if n>0:
        s=n+sumnums(n-1)
    return s
print(sumnums(10))
