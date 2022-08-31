#10
n=int(input("Enter N: "))
for m in range(1, 10+1, 1):
    print(m*n,end=' ') 
print("")


#9
for l in range(1, int(input("Enter N: "))+1, 1):
    print(l**3,end=' ') 
print("")


#8
for k in range(1, int(input("Enter N: "))+1, 1):
    print(k**2,end=' ') 
print("")


#7
for j in range(int(input("Enter N: "))*2, 0, -2):
    print(j,end=' ') 
print("")


#6
for i in range(2, int(input("Enter N: "))*2+1, 2):
    print(i,end=' ') 
print("")


#5
for h in range(int(input("Enter N: "))*2-1, 0, -2):
    print(h,end=' ') 
print("")


#4
for g in range(1, int(input("Enter N: "))*2, 2):
    print(g,end=' ') 
print("")


#3
for f in range(int(input("Enter N: ")), 0, -1):
    print(f,end=' ') 
print("")


#2
for e in range(1,int(input("Enter N: "))+1,1):
    print(e,end=' ') 
print("")


#1
a=int(input("How many times to print string: "))
c=1
while c<=a:
    for b in "MySirG":
        print(b,end='')
    print("",end='  ')
    c+=1
print("")




