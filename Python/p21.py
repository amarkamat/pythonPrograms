#10
def numrev(n):
    print(n%10,end='')
    if n//10!=0:
        numrev(n//10)
numrev(987654321)
print()

#9
def multiple(n,m):
    if m>0:
        multiple(n,m-1)
        print(n*m,end=' ')
multiple(5,10)
print()

#8
def printcubnum(n):
    if n>0:
        printcubnum(n-1)
        print(n**3,end=' ')
printcubnum(5)
print()

#7
def printsqnum(n):
    if n>0:
        printsqnum(n-1)
        print(n*n,end=' ')
printsqnum(5)
print()

#6
def printevennumrev(n):
    if n>0:
        print(n*2,end=' ')
        printevennumrev(n-1)
printevennumrev(5)
print()

#5
def printevennum(n):
    if n>0:
        printevennum(n-1)
        print(n*2,end=' ')
printevennum(5)
print()

#4
def printnumoddrev(n):
    if n>0:
        print(n*2-1,end=' ')
        printnumoddrev(n-1)
printnumoddrev(5)
print()

#3
def printnumodd(n):
    if n>0:
        printnumodd(n-1)
        print(n*2-1,end=' ')
printnumodd(5)
print()

#2
def printnumrev(n):
    if n>0:
        print(n,end=' ')
        printnumrev(n-1)
printnumrev(5)
print()

#1
def printnum(n):
    if n>0:
        printnum(n-1)
        print(n,end=' ')
printnum(5)
print()
