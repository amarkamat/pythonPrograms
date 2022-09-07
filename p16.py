#10
t1=(11,[22,33],44,55)
print(t1)
t1[1][0]=222
print(t1)

#9
t1=("Python",[10,20,30],(2,4,16))
print(t1)
print(t1[1][1])


#8
t1=(('a',21),('b',37),('c',11),('d',29))
print(t1)
print(sorted(t1,key=lambda x:x[1]))


#7
t1=(1,2,3,4,5,6)
t2=t1[3:5:1]
print("t1= ",t1,"t2= ",t2)


#6
t1=(100,200,300,400)
a,b,c,d=t1
print("t1= ",t1)
print("a=",a,"b=",b,"c=",c,"d=",d)


#5
print("Enter tuple elements: ")
t=tuple(e for e in input().split(','))
print(t)
for e in t:
    if e != t[0]:
        print("All tuple elements are not same")
        break
else:
    print("All tuple elements are same")


#4
t1=(1,2,3)
t2=('a','s','d')
print("t1= ",t1)
print("t2= ",t2)
t=t1
t1=t2
t2=t
print("t1= ",t1)
print("t2= ",t2)


#3
print("Enter tuple elements: ")
t=tuple(e for e in input().split(','))
print(t,type(t))
print(t[-1::-1])


#2
s=input("Enter number: ")
t=(s,)
print(t,type(t))


#1
t=("Java","Python","SQL","C")
print(t)


