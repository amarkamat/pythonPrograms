#4
def f4(**kwargs):
    print(kwargs)

f4(xy='ab',mn='cd')

#3
def f3(*t):
    print(t)

f3(1,2,3,4,5,"string",[1,2,3],{1,2,3},(1,2,3),range(10))

#2
def f2(a,b):
    print(a,b)

f2(10,20)

#1
def f1():
    print("MySirG")

f1()
