#10
def decorgethcf(fun):
    def check_coprime(a,b):
        print("Checking coprime number")
        fun(a,b)
    return check_coprime

@decorgethcf
def gethcf(a,b):
    print("HCF of two numbers")

gethcf(1,2)

#9
def decor_perimeter(perimeter):
    def check_perimeter(a,b,c):
        if a>0 and b>0 and c>0:
            perimeter(a,b,c)
        else:
            print("Invalid arguments")
    return check_perimeter

@decor_perimeter
def perimeter(a,b,c):
    print("Perimeter is: ",a+b+c)

perimeter(-1,2,3)


#8
def endlessprime():
    i=2
    while i:
        k=2
        while k<i:
            if i%k==0:
                break
            k+=1
        else:
            yield k
        i+=1
it=endlessprime()
for e in range(10):
    print(next(it),end=' ')
print()

#7
def endlessfib():
    i,j,k=0,1,1
    while j:
        yield i
        i,k=k,i+k
        j+=1
it=endlessfib()
for e in range(10):
    print(next(it),end=' ')
print()

#6
def prime(n):
    i=2
    j=0
    while i:
        k=2
        while k<i:
            if i%k==0:
                break
            k+=1
        else:
            j+=1
            yield k
        i+=1
        if j>=n:
            break
it=prime(10)
for e in range(10):
    print(next(it),end=' ')
print()

#5
def fib(n):
    i=0
    j=1
    k=1
    while j<=n:
        yield i
        i,k=k,i+k
        j+=1
it=fib(5)
for e in range(5):
    print(next(it),end=' ')
print()

#4
def sqnum(n):
    i=1
    while i<=n:
        yield i*i
        i+=1
it=sqnum(5)
for e in range(5):
    print(next(it),end=' ')
print()

#3
def evennum(n):
    i=1
    while i<=n:
        yield i*2
        i+=1
it=evennum(5)
for e in range(5):
    print(next(it),end=' ')
print()

#2
def oddnum(n):
    i=1
    while i<=n:
        yield i*2-1
        i+=1
it=oddnum(5)
for e in range(5):
    print(next(it),end=' ')
print()

#1
l1=[1,3,2,5,3,6,4]
it=iter(l1)
i=0
while i<len(l1):
    print(next(it),end=' ')
    i+=1
print()

